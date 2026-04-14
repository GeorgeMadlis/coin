"""Step 1 — ingest a source into the artifacts store and database."""

from __future__ import annotations

import json
from pathlib import Path

from coin.config import settings
from coin.ingestion.audio_ingestor import ingest_audio, is_transcript_path, looks_like_youtube_source
from coin.ingestion.pdf_ingestor import ingest_document
from coin.ingestion.social_ingestor import ingest_social_post
from coin.ingestion.url_ingestor import ingest_url
from coin.store.database import get_db


ARTIFACTS_DIR = Path(settings.artifacts_dir)
DOCUMENTS_DIR = ARTIFACTS_DIR / "documents"


async def run(source: str, media_type_hint: str | None = None) -> int:
    """Ingest a source and persist it as a document artifact."""

    payload = await _select_ingestor(source, media_type_hint)
    doc_id = _next_doc_id()

    data = {
        "doc_id": doc_id,
        "source_url": payload["source_url"],
        "title": payload["title"],
        "content": payload["content"],
    }

    DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
    artifact_path = DOCUMENTS_DIR / f"{doc_id:04d}_{_slugify(data['title'])}.json"
    artifact_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    async with get_db() as db:
        await db.execute(
            """
            INSERT OR REPLACE INTO documents (doc_id, source_url, title, content)
            VALUES (?, ?, ?, ?)
            """,
            (doc_id, data["source_url"], data["title"], data["content"]),
        )
        await db.commit()

    return doc_id


async def _select_ingestor(source: str, media_type_hint: str | None) -> dict[str, str]:
    if media_type_hint == "tweet":
        return await ingest_social_post(source)
    if media_type_hint == "audio":
        return await ingest_audio(source)
    if looks_like_youtube_source(source) or is_transcript_path(source):
        return await ingest_audio(source)

    suffix = Path(source).suffix.lower()
    if suffix in {".pdf", ".epub", ".docx"}:
        return await ingest_document(source)
    if suffix in {".mp3", ".mp4", ".m4a", ".wav"}:
        return await ingest_audio(source)
    return await ingest_url(source)


def _next_doc_id() -> int:
    if not DOCUMENTS_DIR.exists():
        return 1
    existing = [int(path.name.split("_", 1)[0]) for path in DOCUMENTS_DIR.glob("*.json")]
    return max(existing, default=0) + 1


def _slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")
    return "-".join(part for part in cleaned.split("-") if part) or "document"
