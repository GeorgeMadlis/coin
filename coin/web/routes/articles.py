"""Article routes for listing and saving wiki content."""

from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter
from pydantic import BaseModel

from coin.config import settings


router = APIRouter()
WIKI_DIR = Path(settings.wiki_dir)


class ArticlePayload(BaseModel):
    slug: str
    content: str


@router.get("")
async def list_articles() -> list[dict[str, str]]:
    """Return all compiled wiki articles."""

    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    return [
        {"slug": path.stem, "content": path.read_text(encoding="utf-8")}
        for path in sorted(WIKI_DIR.glob("*.md"))
    ]


@router.post("")
async def save_article(payload: ArticlePayload) -> dict[str, str]:
    """Create or overwrite a wiki article."""

    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    path = WIKI_DIR / f"{payload.slug}.md"
    path.write_text(payload.content, encoding="utf-8")
    return {"slug": payload.slug, "path": path.as_posix()}
