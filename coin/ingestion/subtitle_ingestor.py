"""YouTube subtitle/caption ingestor — faster than Whisper, no audio download."""

from __future__ import annotations


async def ingest_subtitles(source: str) -> dict[str, str]:
    """Fetch auto-generated or manual English captions from a YouTube URL via yt-dlp.

    Prefers manual subtitles over auto-generated ones. Falls back gracefully when
    yt-dlp is absent or the video has no English captions.
    """

    try:
        import yt_dlp  # noqa: PLC0415
    except ImportError:
        return {
            "source_url": source,
            "title": source,
            "content": "yt-dlp is not installed. Run: pip install yt-dlp",
        }

    ydl_opts: dict = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en", "en-US", "en-GB"],
        "subtitlesformat": "json3",
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(source, download=False)

        title: str = info.get("title", source)

        # Manual subtitles take priority over auto-generated captions.
        manual = info.get("subtitles", {})
        auto = info.get("automatic_captions", {})

        sub_entries: list[dict] | None = (
            manual.get("en") or manual.get("en-US") or manual.get("en-GB")
            or auto.get("en") or auto.get("en-US") or auto.get("en-GB")
        )

        if not sub_entries:
            return {
                "source_url": source,
                "title": title,
                "content": f"No English subtitles or captions found for: {source}",
            }

        json3_entry = next((s for s in sub_entries if s.get("ext") == "json3"), None)
        if not json3_entry:
            return {
                "source_url": source,
                "title": title,
                "content": f"json3 caption format not available for: {source}",
            }

        import httpx  # noqa: PLC0415

        async with httpx.AsyncClient(follow_redirects=True, timeout=20) as client:
            resp = await client.get(json3_entry["url"])
            resp.raise_for_status()

        content = _parse_json3(resp.json())
        return {"source_url": source, "title": title, "content": content}

    except Exception as exc:
        return {
            "source_url": source,
            "title": source,
            "content": f"Subtitle fetch failed: {exc}",
        }


def _parse_json3(data: dict) -> str:
    """Extract clean, deduplicated text from a YouTube json3 caption payload."""

    lines: list[str] = []
    for event in data.get("events", []):
        segs = event.get("segs")
        if not segs:
            continue
        text = "".join(s.get("utf8", "") for s in segs).strip()
        if text and text != "\n":
            lines.append(text)

    # Auto-captions repeat the previous line as the next one rolls in — deduplicate.
    deduped: list[str] = []
    prev = ""
    for line in lines:
        if line != prev:
            deduped.append(line)
            prev = line

    return " ".join(deduped)
