#!/usr/bin/env python3
"""Expose local metadata sidecars for committed inquiry bundle snapshots."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
from pathlib import Path
from typing import Any


BUNDLE_ROOT = Path("research/inquiry-to-procedure/bundles")
DEFAULT_BUNDLES = (
    "eudr-coffee-brazil-fazenda-sucuri",
    "framework-self",
)
SCHEMA = "coin-bundle-local-metadata/v1"
UNAVAILABLE = "NOT AVAILABLE in this committed COIN copy"
HTML_HREF_RE = re.compile(r"href=[\"']([^\"']+)[\"']")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+(?:\s+\"[^\"]+\")?)\)")
SOURCE_COMMIT_RE = re.compile(r'<meta name="source_commit" content="([^"]+)">')
FOOTER_FIELD_RE = re.compile(r"<span>([^:<]+):\s*<code>(.*?)</code></span>")
DEV_PATH_RE = re.compile(r"(?:file://|/Users/server|[A-Za-z]:\\)")
MARKER_RE = re.compile(
    r"\n?<!-- coin-local-metadata:start -->.*?<!-- coin-local-metadata:end -->\n?",
    re.DOTALL,
)
CSS_MARKER_RE = re.compile(
    r"\n?/\* coin-local-metadata:start \*/.*?/\* coin-local-metadata:end \*/\n?",
    re.DOTALL,
)
LEGACY_CSS_RE = re.compile(
    r"\n?\.coin-local-metadata \{\n  background: #ffffff;.*?"
    r"\.coin-local-metadata p \{\n  margin: 0;\n  overflow-wrap: anywhere;\n\}\n?",
    re.DOTALL,
)


class BundleError(RuntimeError):
    """Raised when a bundle cannot be rendered or validated."""


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def bundle_path(name: str) -> Path:
    path = repo_root() / BUNDLE_ROOT / name
    if not path.is_dir():
        raise BundleError(f"bundle not found: {name}")
    return path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def split_frontmatter(text: str) -> tuple[dict[str, Any], str, str]:
    if not text.startswith("---\n"):
        return {}, text, ""
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text, ""
    raw = text[4:end]
    return parse_frontmatter(raw), text[end + 5 :], raw


def parse_frontmatter(raw: str) -> dict[str, Any]:
    parsed: dict[str, Any] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        parsed[key.strip()] = parse_scalar(value.strip())
    return parsed


def parse_scalar(value: str) -> Any:
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        return [parse_scalar(part.strip()) for part in split_csv_like(inner)] if inner else []
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    return value


def split_csv_like(value: str) -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    quote: str | None = None
    for char in value:
        if char in {"'", '"'}:
            quote = None if quote == char else char if quote is None else quote
        if char == "," and quote is None:
            parts.append("".join(current))
            current = []
        else:
            current.append(char)
    parts.append("".join(current))
    return parts


def markdown_files(bundle: Path) -> list[Path]:
    return sorted(path for path in bundle.rglob("*.md") if "metadata" not in path.parts)


def html_files(bundle: Path) -> list[Path]:
    return sorted(path for path in bundle.rglob("*.html") if "metadata" not in path.parts)


def source_for_html(bundle: Path, html_path: Path) -> Path | None:
    rel = html_path.relative_to(bundle)
    source = bundle / rel.with_suffix(".md")
    if source.exists():
        return source
    return None


def html_for_source(bundle: Path, source_path: Path) -> Path:
    return bundle / source_path.relative_to(bundle).with_suffix(".html")


def load_published_manifest(bundle: Path) -> dict[str, Any]:
    manifest = bundle / "manifest.json"
    if manifest.exists():
        return json.loads(manifest.read_text(encoding="utf-8"))
    return {}


def manifest_page_record(manifest: dict[str, Any], html_rel: str) -> dict[str, Any]:
    pages = manifest.get("pages", [])
    if isinstance(pages, list):
        for page in pages:
            if page == html_rel:
                return {"path": html_rel}
            if isinstance(page, dict) and page.get("path") == html_rel:
                return page
    return {}


def manifest_concept_record(manifest: dict[str, Any], source_rel: str) -> dict[str, Any]:
    concepts = manifest.get("concepts", [])
    if isinstance(concepts, list):
        for concept in concepts:
            if isinstance(concept, dict) and concept.get("path") == source_rel:
                return concept
    return {}


def manifest_file_record(manifest: dict[str, Any], source_rel: str) -> dict[str, Any]:
    files = manifest.get("files", [])
    if isinstance(files, list):
        for file_record in files:
            if isinstance(file_record, dict) and file_record.get("path") == source_rel:
                return file_record
    return {}


def render_missing_html(bundle: Path) -> None:
    ensure_fallback_stylesheet(bundle)
    for source in markdown_files(bundle):
        target = html_for_source(bundle, source)
        if target.exists():
            continue
        frontmatter, body, _raw = split_frontmatter(source.read_text(encoding="utf-8"))
        title = str(frontmatter.get("title") or first_heading(body) or source.relative_to(bundle))
        target.write_text(
            fallback_html(
                title,
                render_markdown(body),
                source.relative_to(bundle),
                frontmatter,
            ),
            encoding="utf-8",
        )


def ensure_fallback_stylesheet(bundle: Path) -> None:
    stylesheet = bundle / "style.css"
    if stylesheet.exists():
        return
    stylesheet.write_text(
        """
body {
  margin: 0;
  color: #22262f;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.58;
}
main {
  max-width: 70ch;
  margin: 0 auto;
  padding: 2.5rem 1.25rem 4rem;
}
a { color: #2458a6; }
pre, code {
  background: #eceff5;
  border-radius: 4px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}
pre { overflow-x: auto; padding: 0.9rem; }
code { padding: 0.08rem 0.22rem; }
pre code { padding: 0; }
""".strip()
        + "\n",
        encoding="utf-8",
    )


def first_heading(body: str) -> str | None:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def render_markdown(body: str) -> str:
    blocks: list[str] = []
    paragraph: list[str] = []
    in_code = False
    code: list[str] = []

    def flush() -> None:
        if paragraph:
            blocks.append(f"<p>{render_inline(' '.join(paragraph))}</p>")
            paragraph.clear()

    for line in body.splitlines():
        if line.startswith("```"):
            flush()
            if in_code:
                blocks.append(f"<pre><code>{html.escape(chr(10).join(code))}</code></pre>")
                code.clear()
            in_code = not in_code
            continue
        if in_code:
            code.append(line)
            continue
        if not line.strip():
            flush()
            continue
        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            flush()
            level = len(heading.group(1))
            blocks.append(f"<h{level}>{render_inline(heading.group(2))}</h{level}>")
            continue
        bullet = re.match(r"^\s*[-*]\s+(.*)$", line)
        if bullet:
            flush()
            blocks.append(f"<ul><li>{render_inline(bullet.group(1))}</li></ul>")
            continue
        paragraph.append(line.strip())
    flush()
    if code:
        blocks.append(f"<pre><code>{html.escape(chr(10).join(code))}</code></pre>")
    return "\n".join(blocks)


def render_inline(text: str) -> str:
    escaped = html.escape(text)

    def replace(match: re.Match[str]) -> str:
        label = match.group(1)
        href = match.group(2).split()[0]
        if href.endswith(".md"):
            href = href[:-3] + ".html"
        return f'<a href="{html.escape(href, quote=True)}">{label}</a>'

    return MARKDOWN_LINK_RE.sub(replace, escaped)


def fallback_html(
    title: str,
    body: str,
    source_rel: Path,
    frontmatter: dict[str, Any],
) -> str:
    stylesheet = relative_href(source_rel.with_suffix(".html"), Path("style.css"))
    source_commit = frontmatter.get("source_commit", "")
    source_meta = (
        f'  <meta name="source_commit" content="{html.escape(str(source_commit), quote=True)}">\n'
        if source_commit
        else ""
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
{source_meta}  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{html.escape(stylesheet, quote=True)}">
</head>
<body>
<main>
<article>
{body}
</article>
</main>
</body>
</html>
"""


def relative_href(from_rel: Path, to_rel: Path) -> str:
    return Path(os.path.relpath(to_rel, start=from_rel.parent)).as_posix()


def infer_axis(rel_path: Path, frontmatter: dict[str, Any], concept: dict[str, Any]) -> str:
    if frontmatter.get("fc-axis"):
        return str(frontmatter["fc-axis"])
    if concept.get("axis"):
        return str(concept["axis"])
    if rel_path.parts and rel_path.parts[0] in {"pf", "s", "r", "reproduction", "inquiry"}:
        return rel_path.parts[0].upper()
    if rel_path.name == "answer.html":
        return "L0"
    if rel_path.name == "index.html":
        return "INDEX"
    return UNAVAILABLE


def artifact_type(rel_path: Path, frontmatter: dict[str, Any], concept: dict[str, Any]) -> str:
    if frontmatter.get("type"):
        return str(frontmatter["type"])
    if concept.get("type"):
        return str(concept["type"])
    if rel_path.name == "index.html":
        return "Index"
    if rel_path.name == "log.html":
        return "Ledger"
    if rel_path.parts and rel_path.parts[0] == "inquiry":
        return "InquiryRound" if rel_path.name.startswith("round-") else "InquiryIndex"
    if rel_path.parts and rel_path.parts[0] == "reproduction":
        return "Runbook"
    return "HTMLArtifact"


def source_concept_kind(rel_path: Path) -> str:
    if rel_path.parts and rel_path.parts[0] == "inquiry":
        return "inquiry-round" if rel_path.name.startswith("round-") else "inquiry-index"
    if rel_path.parts and rel_path.parts[0] == "reproduction":
        return "reproduction"
    if rel_path.parts and rel_path.parts[0] == "r":
        return "result"
    if rel_path.parts and rel_path.parts[0] == "s":
        return "method"
    if rel_path.parts and rel_path.parts[0] == "pf":
        return "problem-framing"
    if rel_path.name == "index.html":
        return "bundle-index"
    return "artifact"


def parse_html_metadata(html_text: str) -> dict[str, Any]:
    meta: dict[str, Any] = {}
    commit = SOURCE_COMMIT_RE.search(html_text)
    if commit:
        meta["source_commit"] = commit.group(1)
    for key, value in FOOTER_FIELD_RE.findall(html_text):
        meta[key.strip().replace(" ", "_")] = html.unescape(value)
    return meta


def page_metadata(bundle: Path, html_path: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    html_rel_path = html_path.relative_to(bundle)
    html_rel = html_rel_path.as_posix()
    source = source_for_html(bundle, html_path)
    frontmatter: dict[str, Any] = {}
    raw_frontmatter = ""
    source_rel = html_rel_path.with_suffix(".md").as_posix()
    source_available = False
    source_sha = UNAVAILABLE
    if source:
        source_available = True
        frontmatter, _body, raw_frontmatter = split_frontmatter(source.read_text(encoding="utf-8"))
        source_rel = source.relative_to(bundle).as_posix()
        source_sha = sha256(source)

    concept = manifest_concept_record(manifest, source_rel)
    file_record = manifest_file_record(manifest, source_rel)
    page_record = manifest_page_record(manifest, html_rel)
    html_meta = parse_html_metadata(html_path.read_text(encoding="utf-8"))
    metadata_path = metadata_path_for(bundle, html_path)
    return {
        "schema": SCHEMA,
        "bundle": {
            "id": manifest.get("bundle_id", manifest.get("bundle", bundle.name)),
            "profile": manifest.get("profile", bundle_profile(bundle.name)),
            "status": manifest.get("fc_status", frontmatter.get("fc-status", UNAVAILABLE)),
            "bundle_round": manifest.get("bundle_round", frontmatter.get("fc-round", UNAVAILABLE)),
            "source_repository_round": manifest.get(
                "source_repository_round", manifest.get("source_repo_round", UNAVAILABLE)
            ),
            "source_commit": manifest.get(
                "source_commit", html_meta.get("source_commit", UNAVAILABLE)
            ),
            "source_dirty": manifest.get("source_dirty", UNAVAILABLE),
        },
        "represented_artifact": {
            "html_path": html_rel,
            "metadata_path": metadata_path.relative_to(bundle).as_posix(),
            "source_path": source_rel if source_available else UNAVAILABLE,
            "source_available_in_coin_copy": source_available,
            "source_concept_kind": source_concept_kind(html_rel_path),
            "artifact_type": artifact_type(html_rel_path, frontmatter, concept),
            "title": frontmatter.get("title", concept.get("title", page_record.get("title", html_rel))),
            "description": frontmatter.get("description", concept.get("description", UNAVAILABLE)),
        },
        "progressive_disclosure": {
            "axis": infer_axis(html_rel_path, frontmatter, concept),
            "level": frontmatter.get("fc-level", concept.get("level", UNAVAILABLE)),
        },
        "inquiry": {
            "bundle_round_for_page": frontmatter.get(
                "fc-round", concept.get("round", page_round_from_path(html_rel_path) or UNAVAILABLE)
            ),
            "party": frontmatter.get("fc-party", frontmatter.get("party", UNAVAILABLE)),
            "move": frontmatter.get("fc-move", frontmatter.get("move", UNAVAILABLE)),
            "stage": frontmatter.get("fc-stage", UNAVAILABLE),
            "timestamp_or_date": frontmatter.get(
                "timestamp", frontmatter.get("date", frontmatter.get("fc-date", UNAVAILABLE))
            ),
        },
        "supersession": {"supersedes": frontmatter.get("fc-supersedes", concept.get("supersedes", UNAVAILABLE))},
        "provenance": {
            "published_manifest": "manifest.json" if (bundle / "manifest.json").exists() else UNAVAILABLE,
            "local_metadata_manifest": "metadata/local-metadata-manifest.json",
            "bundle_json": "bundle.json" if (bundle / "bundle.json").exists() else UNAVAILABLE,
            "source_checksum_sha256": source_sha,
            "published_manifest_source_checksum_sha256": file_record.get("sha256", UNAVAILABLE),
            "html_checksum_sha256": sha256(html_path),
            "rendered_at": manifest.get("rendered_at", UNAVAILABLE),
            "published_path": manifest.get("published_path", UNAVAILABLE),
            "external_evidence_note": (
                "External citations and remote datasets are referenced by metadata; they are not "
                "all bundled for offline use."
            ),
        },
        "snapshot_manifest_record": page_record,
        "concept_manifest_record": concept,
        "frontmatter": frontmatter,
        "frontmatter_raw": raw_frontmatter or UNAVAILABLE,
    }


def page_round_from_path(rel_path: Path) -> int | None:
    match = re.search(r"round-(\d{4})\.html$", rel_path.as_posix())
    return int(match.group(1)) if match else None


def bundle_profile(name: str) -> str:
    if name == "framework-self":
        return "okf-fc"
    if name == "eudr-coffee-brazil-fazenda-sucuri":
        return "okf-gsp"
    return UNAVAILABLE


def metadata_path_for(bundle: Path, html_path: Path) -> Path:
    return bundle / "metadata" / html_path.relative_to(bundle).with_suffix(".metadata.json")


def inject_metadata_panel(bundle: Path, html_path: Path, metadata_path: Path) -> None:
    text = html_path.read_text(encoding="utf-8")
    text = MARKER_RE.sub("\n", text)
    text = CSS_MARKER_RE.sub("\n", text)
    text = LEGACY_CSS_RE.sub("\n", text)
    rel_html = html_path.relative_to(bundle)
    metadata_href = relative_href(rel_html, metadata_path.relative_to(bundle))
    local_manifest_href = relative_href(rel_html, Path("metadata/local-metadata-manifest.json"))
    published_manifest_href = relative_href(rel_html, Path("manifest.json"))
    panel = f"""
<!-- coin-local-metadata:start -->
<section class="coin-local-metadata" aria-label="Local metadata links">
  <h2>Metadata</h2>
  <p>
    <a href="{html.escape(metadata_href, quote=True)}">Page metadata JSON</a>
    <span aria-hidden="true"> | </span>
    <a href="{html.escape(published_manifest_href, quote=True)}">Published bundle manifest</a>
    <span aria-hidden="true"> | </span>
    <a href="{html.escape(local_manifest_href, quote=True)}">Local metadata manifest</a>
  </p>
</section>
<!-- coin-local-metadata:end -->
"""
    if "</article>" in text:
        text = text.replace("</article>", panel + "\n</article>", 1)
    elif "</main>" in text:
        text = text.replace("</main>", panel + "\n</main>", 1)
    else:
        text = text.replace("</body>", panel + "\n</body>", 1)
    if "</style>" in text:
        text = text.replace("</style>", metadata_css() + "\n</style>", 1)
    html_path.write_text(text, encoding="utf-8")


def metadata_css() -> str:
    return """
/* coin-local-metadata:start */
.coin-local-metadata {
  background: #ffffff;
  border: 1px solid #dfe3ec;
  border-radius: 8px;
  margin: 1.25rem 0;
  padding: 1rem;
}
.coin-local-metadata h2 {
  font-size: 1rem;
  margin: 0 0 0.55rem;
}
.coin-local-metadata p {
  margin: 0;
  overflow-wrap: anywhere;
}
/* coin-local-metadata:end */
"""


def build_bundle(bundle: Path) -> dict[str, Any]:
    render_missing_html(bundle)
    manifest = load_published_manifest(bundle)
    metadata_dir = bundle / "metadata"
    metadata_dir.mkdir(exist_ok=True)
    pages = []
    for html_path in html_files(bundle):
        metadata_path = metadata_path_for(bundle, html_path)
        metadata_path.parent.mkdir(parents=True, exist_ok=True)
        metadata = page_metadata(bundle, html_path, manifest)
        metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        inject_metadata_panel(bundle, html_path, metadata_path)
        metadata["provenance"]["html_checksum_sha256"] = sha256(html_path)
        metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        pages.append(
            {
                "html_path": html_path.relative_to(bundle).as_posix(),
                "metadata_path": metadata_path.relative_to(bundle).as_posix(),
                "source_path": metadata["represented_artifact"]["source_path"],
                "source_available_in_coin_copy": metadata["represented_artifact"][
                    "source_available_in_coin_copy"
                ],
                "artifact_type": metadata["represented_artifact"]["artifact_type"],
                "axis": metadata["progressive_disclosure"]["axis"],
                "level": metadata["progressive_disclosure"]["level"],
                "html_sha256": sha256(html_path),
                "metadata_sha256": sha256(metadata_path),
            }
        )
    local_manifest = {
        "schema": SCHEMA,
        "bundle": {
            "id": manifest.get("bundle_id", manifest.get("bundle", bundle.name)),
            "profile": manifest.get("profile", bundle_profile(bundle.name)),
            "bundle_round": manifest.get("bundle_round", UNAVAILABLE),
            "source_repository_round": manifest.get(
                "source_repository_round", manifest.get("source_repo_round", UNAVAILABLE)
            ),
            "source_commit": manifest.get("source_commit", UNAVAILABLE),
        },
        "metadata_convention": {
            "page_sidecars": "metadata/<html-path-with-.metadata.json-suffix>",
            "published_manifest": "manifest.json",
            "local_entry_point": "index.html",
            "relative_links_only": True,
            "checksum_algorithm": "sha256",
        },
        "pages": pages,
        "inventory": {
            "html_pages": [page["html_path"] for page in pages],
            "source_markdown_files": [
                path.relative_to(bundle).as_posix() for path in markdown_files(bundle)
            ],
            "inquiry_round_html_pages": [
                page["html_path"]
                for page in pages
                if page["html_path"].startswith("inquiry/round-")
            ],
            "manifest_or_provenance_files": [
                path.relative_to(bundle).as_posix()
                for path in sorted(bundle.rglob("*.json"))
                if "metadata" not in path.parts
            ],
        },
    }
    local_manifest_path = metadata_dir / "local-metadata-manifest.json"
    local_manifest_path.write_text(
        json.dumps(local_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return local_manifest


def validate_bundle(bundle: Path) -> list[str]:
    errors: list[str] = []
    local_manifest_path = bundle / "metadata" / "local-metadata-manifest.json"
    if not local_manifest_path.exists():
        return [f"{bundle.name}: missing metadata/local-metadata-manifest.json"]
    local_manifest = json.loads(local_manifest_path.read_text(encoding="utf-8"))
    if (bundle / "index.html").exists():
        index_text = (bundle / "index.html").read_text(encoding="utf-8")
        if "metadata/local-metadata-manifest.json" not in index_text:
            errors.append(f"{bundle.name}: index.html does not link to local metadata manifest")
        if "manifest.json" not in index_text:
            errors.append(f"{bundle.name}: index.html does not link to published manifest")
    for page in local_manifest.get("pages", []):
        html_path = bundle / page["html_path"]
        metadata_path = bundle / page["metadata_path"]
        if not html_path.exists():
            errors.append(f"{bundle.name}: missing HTML page {page['html_path']}")
            continue
        if not metadata_path.exists():
            errors.append(f"{bundle.name}: missing metadata sidecar {page['metadata_path']}")
            continue
        html_text = html_path.read_text(encoding="utf-8")
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        hrefs = HTML_HREF_RE.findall(html_text)
        metadata_links = [href for href in hrefs if href.endswith(".metadata.json")]
        if not metadata_links:
            errors.append(f"{bundle.name}: no metadata link in {page['html_path']}")
        for href in metadata_links:
            target = (html_path.parent / href).resolve()
            if not str(target).startswith(str(bundle.resolve())):
                errors.append(f"{bundle.name}: metadata link escapes bundle: {href}")
            if not target.exists():
                errors.append(f"{bundle.name}: broken metadata link {href}")
        for href in hrefs:
            if href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if href.endswith((".metadata.json", "manifest.json", "bundle.json")):
                target = (html_path.parent / href).resolve()
                if not str(target).startswith(str(bundle.resolve())):
                    errors.append(f"{bundle.name}: metadata/provenance link escapes bundle: {href}")
                if not target.exists():
                    errors.append(f"{bundle.name}: broken metadata/provenance link {href}")
        generated_paths = [
            page["metadata_path"],
            metadata["represented_artifact"]["metadata_path"],
            metadata["provenance"]["published_manifest"],
            metadata["provenance"]["local_metadata_manifest"],
            metadata["provenance"]["bundle_json"],
        ]
        for generated_path in generated_paths:
            if isinstance(generated_path, str) and DEV_PATH_RE.search(generated_path):
                errors.append(
                    f"{bundle.name}: generated metadata/provenance path is absolute: {generated_path}"
                )
        if metadata["represented_artifact"]["html_path"] != page["html_path"]:
            errors.append(f"{bundle.name}: HTML cross-reference mismatch for {page['html_path']}")
        if metadata["represented_artifact"]["metadata_path"] != page["metadata_path"]:
            errors.append(f"{bundle.name}: metadata cross-reference mismatch for {page['html_path']}")
        source_path_value = metadata["represented_artifact"]["source_path"]
        if source_path_value != UNAVAILABLE:
            source_path = bundle / source_path_value
            if not source_path.exists():
                errors.append(f"{bundle.name}: metadata source path missing {source_path_value}")
            else:
                frontmatter, _body, _raw = split_frontmatter(source_path.read_text(encoding="utf-8"))
                missing = set(frontmatter) - set(metadata.get("frontmatter", {}))
                if missing:
                    errors.append(
                        f"{bundle.name}: dropped frontmatter keys for {source_path_value}: "
                        + ", ".join(sorted(missing))
                    )
                if metadata["provenance"]["source_checksum_sha256"] != sha256(source_path):
                    errors.append(f"{bundle.name}: stale source checksum for {source_path_value}")
        if page["html_sha256"] != sha256(html_path):
            errors.append(f"{bundle.name}: stale HTML checksum for {page['html_path']}")
        if page["metadata_sha256"] != sha256(metadata_path):
            errors.append(f"{bundle.name}: stale metadata checksum for {page['metadata_path']}")
    errors.extend(validate_inquiry_sequence(bundle))
    return errors


def validate_inquiry_sequence(bundle: Path) -> list[str]:
    errors: list[str] = []
    rounds: list[int] = []
    for path in sorted((bundle / "inquiry").glob("round-*.md")):
        frontmatter, _body, _raw = split_frontmatter(path.read_text(encoding="utf-8"))
        value = frontmatter.get("fc-round")
        if isinstance(value, int):
            rounds.append(value)
    if rounds and rounds != list(range(1, max(rounds) + 1)):
        errors.append(f"{bundle.name}: Markdown inquiry rounds are not contiguous: {rounds}")
    html_round_numbers = sorted(
        round_value
        for round_value in (page_round_from_path(path.relative_to(bundle)) for path in html_files(bundle))
        if round_value is not None
    )
    if html_round_numbers and html_round_numbers != list(range(1, max(html_round_numbers) + 1)):
        errors.append(f"{bundle.name}: HTML inquiry rounds are not contiguous: {html_round_numbers}")
    return errors


def render_command(names: list[str]) -> int:
    for name in names or list(DEFAULT_BUNDLES):
        manifest = build_bundle(bundle_path(name))
        print(f"rendered {name}: {len(manifest['pages'])} HTML pages")
    return 0


def validate_command(names: list[str]) -> int:
    errors: list[str] = []
    for name in names or list(DEFAULT_BUNDLES):
        bundle_errors = validate_bundle(bundle_path(name))
        if bundle_errors:
            errors.extend(bundle_errors)
        else:
            print(f"validated {name}: ok")
    if errors:
        for error in errors:
            print(error)
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    render_parser = subparsers.add_parser("render", help="render missing HTML and metadata sidecars")
    render_parser.add_argument("bundles", nargs="*")
    validate_parser = subparsers.add_parser("validate", help="validate local metadata links")
    validate_parser.add_argument("bundles", nargs="*")
    args = parser.parse_args()
    if args.command == "render":
        return render_command(args.bundles)
    if args.command == "validate":
        return validate_command(args.bundles)
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
