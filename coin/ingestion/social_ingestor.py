"""Normalize social posts into a document-like payload."""

from __future__ import annotations


async def ingest_social_post(source: str) -> dict[str, str]:
    """Wrap a social URL or pasted post into the common ingest shape."""

    return {
        "source_url": source,
        "title": "Social Post",
        "content": f"Social post placeholder captured from: {source}",
    }
