"""Step 6 — detect lightweight structural issues in the wiki."""

from __future__ import annotations

import json
import re
from pathlib import Path

from coin.config import settings
from coin.store.database import get_db


ARTIFACTS_DIR = Path(settings.artifacts_dir)
WIKI_DIR = Path(settings.wiki_dir)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


async def print_manual_prompt() -> str:
    """Build the lint prompt for manual review."""

    template = (Path(__file__).parent.parent / "prompts" / "04_lint.md").read_text(encoding="utf-8")
    article_bundle = "\n\n---\n\n".join(
        f"# {path.stem}\n\n{path.read_text(encoding='utf-8')}" for path in sorted(WIKI_DIR.glob("*.md"))
    ) or "(no wiki articles yet)"
    prompt = template.replace("{{ARTICLES}}", article_bundle)
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    (ARTIFACTS_DIR / "lint_prompt.md").write_text(prompt, encoding="utf-8")
    return prompt


async def apply_manual_findings(response_path: Path) -> list[dict[str, str]]:
    """Save manual lint findings from a JSON file."""

    findings = json.loads(response_path.read_text(encoding="utf-8"))
    await _persist_findings(findings)
    return findings


async def run_agent() -> list[dict[str, str]]:
    """Run deterministic structural checks over compiled wiki articles."""

    valid_slugs = {path.stem for path in WIKI_DIR.glob("*.md")}
    findings: list[dict[str, str]] = []

    for path in sorted(WIKI_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "## References" not in text:
            findings.append(
                {"kind": "missing_references", "article_slug": path.stem, "detail": "Missing references section."}
            )
        if len(text.split()) < 120:
            findings.append(
                {"kind": "thin_article", "article_slug": path.stem, "detail": "Article is still very short."}
            )
        for link in WIKILINK_RE.findall(text):
            target = _slugify(link)
            if target not in valid_slugs:
                findings.append(
                    {
                        "kind": "broken_wikilink",
                        "article_slug": path.stem,
                        "detail": f"Unresolved wikilink: [[{link}]]",
                    }
                )

    await _persist_findings(findings)
    return findings


async def _persist_findings(findings: list[dict[str, str]]) -> None:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    (ARTIFACTS_DIR / "lint_findings.json").write_text(
        json.dumps(findings, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    async with get_db() as db:
        await db.execute("DELETE FROM lint_findings")
        for finding in findings:
            await db.execute(
                "INSERT INTO lint_findings (kind, article_slug, detail) VALUES (?, ?, ?)",
                (finding["kind"], finding.get("article_slug"), finding["detail"]),
            )
        await db.commit()


def _slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")
    return "-".join(part for part in cleaned.split("-") if part) or "article"
