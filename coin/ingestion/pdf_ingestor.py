"""Ingest PDF, EPUB, and DOCX-style files."""

from __future__ import annotations

from pathlib import Path


async def ingest_document(source: str) -> dict[str, str]:
    """Return a best-effort text representation of a document file."""

    path = Path(source)
    if path.suffix.lower() in {".md", ".txt"}:
        content = path.read_text(encoding="utf-8")
    else:
        content = (
            f"Document placeholder for {path.name}. "
            "Add a richer extractor here when you wire in PDF/EPUB/DOCX parsing."
        )

    return {
        "source_url": path.resolve().as_posix(),
        "title": path.stem,
        "content": content,
    }
