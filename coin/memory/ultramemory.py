"""Lightweight semantic-ish search over ingested documents and wiki articles."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from coin.config import settings


WORD_RE = re.compile(r"[A-Za-z0-9]+")


@dataclass
class SearchHit:
    source_url: str
    text: str
    score: float
    doc_id: int | None = None
    article_slug: str | None = None


class Ultramemory:
    """Simple overlap scorer that keeps the designed memory module in place."""

    def __init__(self) -> None:
        self._artifacts_dir = Path(settings.artifacts_dir)
        self._wiki_dir = Path(settings.wiki_dir)

    async def search(self, query: str, limit: int = 5) -> list[SearchHit]:
        query_terms = set(_tokenize(query))
        if not query_terms:
            return []

        hits = self._search_documents(query_terms) + self._search_articles(query_terms)
        hits.sort(key=lambda item: item.score, reverse=True)
        return hits[:limit]

    def _search_documents(self, query_terms: set[str]) -> list[SearchHit]:
        docs_dir = self._artifacts_dir / "documents"
        hits: list[SearchHit] = []
        if not docs_dir.exists():
            return hits

        for path in sorted(docs_dir.glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            text = data.get("content", "")
            score = _score_text(text, query_terms)
            if score <= 0:
                continue
            hits.append(
                SearchHit(
                    source_url=data.get("source_url", path.name),
                    text=_excerpt(text, query_terms),
                    score=score,
                    doc_id=data.get("doc_id"),
                )
            )
        return hits

    def _search_articles(self, query_terms: set[str]) -> list[SearchHit]:
        hits: list[SearchHit] = []
        if not self._wiki_dir.exists():
            return hits

        for path in sorted(self._wiki_dir.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            score = _score_text(text, query_terms)
            if score <= 0:
                continue
            hits.append(
                SearchHit(
                    source_url=path.as_posix(),
                    text=_excerpt(text, query_terms),
                    score=score,
                    article_slug=path.stem,
                )
            )
        return hits


def _tokenize(text: str) -> list[str]:
    return [token.lower() for token in WORD_RE.findall(text)]


def _score_text(text: str, query_terms: set[str]) -> float:
    words = set(_tokenize(text))
    if not words:
        return 0.0
    overlap = len(words & query_terms)
    return overlap / max(len(query_terms), 1)


def _excerpt(text: str, query_terms: set[str], width: int = 320) -> str:
    lowered = text.lower()
    index = min((lowered.find(term) for term in query_terms if term in lowered), default=0)
    start = max(index - 80, 0)
    end = min(start + width, len(text))
    return text[start:end].strip()
