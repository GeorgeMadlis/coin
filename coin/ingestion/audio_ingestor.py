"""Audio and video transcription adapter."""

from __future__ import annotations

from pathlib import Path


async def ingest_audio(source: str) -> dict[str, str]:
    """Return a placeholder transcript for the supplied media source."""

    name = Path(source).name or source
    return {
        "source_url": source,
        "title": name,
        "content": (
            f"Transcript placeholder for {name}. "
            "Wire Whisper or another speech-to-text backend here for full support."
        ),
    }
