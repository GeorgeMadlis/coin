"""Step 2 — chunk ingested documents and persist them for retrieval."""

from __future__ import annotations

import json
from pathlib import Path

from coin.config import settings
from coin.store.database import get_db


ARTIFACTS_DIR = Path(settings.artifacts_dir)
DOCUMENTS_DIR = ARTIFACTS_DIR / "documents"


async def run() -> int:
    """Chunk all ingested documents that do not yet have stored chunks."""

    async with get_db() as db:
        existing_rows = await db.execute_fetchall("SELECT DISTINCT doc_id FROM chunks")
        embedded_doc_ids = {int(row["doc_id"]) for row in existing_rows}
        inserted = 0

        for path in sorted(DOCUMENTS_DIR.glob("*.json")):
            doc = json.loads(path.read_text(encoding="utf-8"))
            doc_id = int(doc["doc_id"])
            if doc_id in embedded_doc_ids:
                continue

            for index, chunk in enumerate(_chunk_text(doc.get("content", ""))):
                await db.execute(
                    "INSERT OR REPLACE INTO chunks (doc_id, chunk_index, text) VALUES (?, ?, ?)",
                    (doc_id, index, chunk),
                )
                inserted += 1

        await db.commit()
        return inserted


def _chunk_text(text: str) -> list[str]:
    words = text.split()
    if not words:
        return []

    size = max(settings.chunk_size, 1)
    overlap = min(settings.chunk_overlap, size - 1) if size > 1 else 0
    chunks: list[str] = []
    start = 0

    while start < len(words):
        end = min(start + size, len(words))
        chunks.append(" ".join(words[start:end]))
        if end >= len(words):
            break
        start = max(end - overlap, start + 1)

    return chunks
