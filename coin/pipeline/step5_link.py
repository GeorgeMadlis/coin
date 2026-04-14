"""Step 5 — resolve wikilinks and rebuild backlink data."""

from __future__ import annotations

import json
import re
from pathlib import Path

from coin.config import settings
from coin.store.database import get_db


WIKI_DIR = Path(settings.wiki_dir)
ARTIFACTS_DIR = Path(settings.artifacts_dir)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


async def run() -> int:
    """Scan articles, record backlinks, and save a backlink artifact."""

    title_to_slug = _title_index()
    backlinks: list[dict[str, str]] = []

    async with get_db() as db:
        await db.execute("DELETE FROM backlinks")

        for path in sorted(WIKI_DIR.glob("*.md")):
            source_slug = path.stem
            text = path.read_text(encoding="utf-8")
            for title in WIKILINK_RE.findall(text):
                target_slug = title_to_slug.get(title.strip(), _slugify(title))
                backlinks.append({"source_slug": source_slug, "target_slug": target_slug})
                await db.execute(
                    "INSERT INTO backlinks (source_slug, target_slug) VALUES (?, ?)",
                    (source_slug, target_slug),
                )

        await db.commit()

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    (ARTIFACTS_DIR / "backlinks.json").write_text(
        json.dumps(backlinks, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return len(backlinks)


def _title_index() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in sorted(WIKI_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        title_match = re.search(r"^title:\s*(.+)$", text, re.MULTILINE)
        if title_match:
            mapping[title_match.group(1).strip()] = path.stem
    return mapping


def _slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")
    return "-".join(part for part in cleaned.split("-") if part) or "article"
