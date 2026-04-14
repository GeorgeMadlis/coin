"""Knowledge graph route built from wikilinks."""

from __future__ import annotations

import re
from pathlib import Path

from fastapi import APIRouter

from coin.config import settings


router = APIRouter()
WIKI_DIR = Path(settings.wiki_dir)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


@router.get("")
async def graph() -> dict[str, list[dict[str, str]]]:
    """Return a D3-friendly node and edge structure."""

    nodes = [{"id": path.stem} for path in sorted(WIKI_DIR.glob("*.md"))]
    edges: list[dict[str, str]] = []

    for path in sorted(WIKI_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for title in WIKILINK_RE.findall(text):
            target = _slugify(title)
            edges.append({"source": path.stem, "target": target})

    return {"nodes": nodes, "links": edges}


def _slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")
    return "-".join(part for part in cleaned.split("-") if part) or "article"
