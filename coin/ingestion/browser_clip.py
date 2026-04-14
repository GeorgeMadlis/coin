"""Browser clip receiver used by the Chrome extension."""

from __future__ import annotations


async def receive_clip(url: str, content: str) -> dict[str, str]:
    """Normalize a browser clip into the standard ingest payload."""

    return {
        "source_url": url,
        "title": "Browser Clip",
        "content": content.strip(),
    }
