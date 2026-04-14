"""Ingest web pages and local text files."""

from __future__ import annotations

from pathlib import Path

import httpx
from bs4 import BeautifulSoup


async def ingest_url(source: str) -> dict[str, str]:
    """Fetch a URL or read a local text-like file."""

    if source.startswith(("http://", "https://")):
        try:
            async with httpx.AsyncClient(follow_redirects=True, timeout=20) as client:
                response = await client.get(source)
                response.raise_for_status()
        except Exception:
            return {
                "source_url": source,
                "title": source,
                "content": f"Unable to fetch {source} in the current environment.",
            }

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else source
        content = soup.get_text("\n", strip=True)
        return {"source_url": source, "title": title, "content": content}

    path = Path(source)
    return {
        "source_url": path.resolve().as_posix(),
        "title": path.stem,
        "content": path.read_text(encoding="utf-8"),
    }
