from __future__ import annotations

import importlib.util
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TOOL_PATH = REPO_ROOT / "research/inquiry-to-procedure/tools/render_bundle_metadata.py"
BUNDLE_ROOT = REPO_ROOT / "research/inquiry-to-procedure/bundles"
BUNDLES = [
    BUNDLE_ROOT / "eudr-coffee-brazil-fazenda-sucuri",
    BUNDLE_ROOT / "framework-self",
]


def load_tool():
    spec = importlib.util.spec_from_file_location("render_bundle_metadata", TOOL_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_rendered_bundle_metadata_links_validate() -> None:
    tool = load_tool()
    errors = []
    for bundle in BUNDLES:
        errors.extend(tool.validate_bundle(bundle))
    assert errors == []


def test_page_sidecars_preserve_frontmatter_crossrefs_and_checksums() -> None:
    tool = load_tool()
    for bundle in BUNDLES:
        local_manifest = json.loads(
            (bundle / "metadata/local-metadata-manifest.json").read_text(encoding="utf-8")
        )
        assert (bundle / "index.html").exists()
        assert local_manifest["metadata_convention"]["relative_links_only"] is True
        assert local_manifest["metadata_convention"]["published_manifest"] == "manifest.json"

        for page in local_manifest["pages"]:
            assert not Path(page["metadata_path"]).is_absolute()
            assert not Path(page["html_path"]).is_absolute()
            html_path = bundle / page["html_path"]
            metadata_path = bundle / page["metadata_path"]
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))

            assert metadata["represented_artifact"]["html_path"] == page["html_path"]
            assert metadata["represented_artifact"]["metadata_path"] == page["metadata_path"]
            assert page["html_sha256"] == tool.sha256(html_path)
            assert page["metadata_sha256"] == tool.sha256(metadata_path)

            source_path = metadata["represented_artifact"]["source_path"]
            if source_path != tool.UNAVAILABLE:
                source = bundle / source_path
                frontmatter, _body, _raw = tool.split_frontmatter(source.read_text(encoding="utf-8"))
                assert set(frontmatter) <= set(metadata["frontmatter"])
                assert metadata["provenance"]["source_checksum_sha256"] == tool.sha256(source)


def test_fazenda_snapshot_artifacts_and_verdict_metadata_are_restored() -> None:
    bundle = BUNDLE_ROOT / "eudr-coffee-brazil-fazenda-sucuri"
    required_paths = [
        "bundle.json",
        "manifest.json",
        "fazenda_sucuri_contact_sheet_guide.html",
        "reproduction/source-evidence.json",
        "reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf",
        "reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf.metadata.json",
        "evidence-package/inputs/aoi.geojson",
        "evidence-package/reports/aoi_report_v2/fazenda_sucuri_screening_aoi.html",
        "evidence-package/reports/aoi_report_v2/fazenda_sucuri_screening_aoi.json",
    ]
    for rel_path in required_paths:
        assert (bundle / rel_path).exists(), rel_path

    answer_metadata = json.loads((bundle / "metadata/answer.metadata.json").read_text())
    assert answer_metadata["frontmatter"]["gsp-verdict-class"] == "possible_relevant_deforestation"
    assert answer_metadata["frontmatter"]["gsp-provenance"] == "pinned-not-reproduced"

    source_evidence = json.loads((bundle / "reproduction/source-evidence.json").read_text())
    assert source_evidence["counterpart_commit"] == "d68e7ebbcc99fdff75742452538b241a382feb24"
    assert source_evidence["counterpart_dirty"] is False


def test_framework_self_progressive_metadata_and_round_inventory_are_reachable() -> None:
    bundle = BUNDLE_ROOT / "framework-self"
    manifest = json.loads((bundle / "metadata/local-metadata-manifest.json").read_text())
    assert "inquiry/round-0020.html" in manifest["inventory"]["html_pages"]
    assert "r/metrics-rounds-0001-0013.csv" in manifest["inventory"]["source_markdown_files"] or (
        bundle / "r/metrics-rounds-0001-0013.csv"
    ).exists()

    method_metadata = json.loads((bundle / "metadata/s/method.metadata.json").read_text())
    assert method_metadata["progressive_disclosure"]["axis"] == "S"
    assert method_metadata["frontmatter"]["fc-status"] == "open"
    assert method_metadata["supersession"]["supersedes"] != "NOT AVAILABLE in this committed COIN copy"
