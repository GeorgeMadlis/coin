"""Audio, subtitle, and YouTube transcript ingestion helpers."""

from __future__ import annotations

import asyncio
import html
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import parse_qs, urlparse


SUBTITLE_SUFFIXES = {".srt", ".vtt"}
TRANSCRIPT_SUFFIXES = SUBTITLE_SUFFIXES | {".md", ".txt"}
AUDIO_SUFFIXES = {".mp3", ".mp4", ".m4a", ".wav"}
YOUTUBE_HOSTS = {
    "youtu.be",
    "m.youtube.com",
    "music.youtube.com",
    "www.youtube.com",
    "youtube.com",
}

_TIMESTAMP_RE = re.compile(
    r"^\d{2}:\d{2}:\d{2}(?:[.,]\d{3})?\s+-->\s+\d{2}:\d{2}:\d{2}(?:[.,]\d{3})?$"
)
_SHORT_TIMESTAMP_RE = re.compile(
    r"^\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d{3})?\s+-->\s+\d{1,2}:\d{2}(?::\d{2})?(?:[.,]\d{3})?$"
)
_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "have",
    "how",
    "in",
    "is",
    "it",
    "no",
    "of",
    "on",
    "or",
    "that",
    "the",
    "their",
    "there",
    "this",
    "to",
    "what",
    "with",
}


async def ingest_audio(source: str) -> dict[str, str]:
    """Return transcript text for a local subtitle/transcript file or YouTube URL."""

    path = Path(source).expanduser()
    if path.exists():
        return await asyncio.to_thread(_ingest_local_source, path)

    video_id = extract_youtube_video_id(source)
    if video_id:
        return await asyncio.to_thread(_ingest_youtube_source, source, video_id)

    name = path.name or source
    return {
        "source_url": source,
        "title": name,
        "content": (
            f"Transcript placeholder for {name}. "
            "Wire Whisper or another speech-to-text backend here for full support."
        ),
    }


def looks_like_youtube_source(source: str) -> bool:
    """Return True when the input looks like a YouTube URL."""

    return extract_youtube_video_id(source) is not None


def is_transcript_path(source: str) -> bool:
    """Return True when the input path points to a subtitle or transcript file."""

    path = Path(source).expanduser()
    return path.exists() and path.suffix.lower() in TRANSCRIPT_SUFFIXES


def label_from_title(title: str) -> str | None:
    """Derive a short topic label from a human title for offline grouping."""

    words = re.findall(r"[A-Za-z][A-Za-z'-]+", title)
    lowered = [word.lower() for word in words]
    if "complexity" in lowered and any(word.startswith("civiliz") for word in lowered):
        return "Complexity of Civilizations"

    keywords = [word for word in words if word.lower() not in _STOPWORDS]
    if not keywords:
        return None

    label_words: list[str] = []
    for word in keywords:
        cleaned = word.strip("-'")
        if not cleaned:
            continue
        normalized = cleaned.title()
        if normalized in label_words:
            continue
        label_words.append(normalized)
        if len(label_words) == 3:
            break

    return " ".join(label_words) if label_words else None


def extract_youtube_video_id(source: str) -> str | None:
    """Extract an 11-character YouTube video id from the supplied URL."""

    parsed = urlparse(source)
    host = parsed.netloc.lower()
    if host not in YOUTUBE_HOSTS:
        return None

    if host == "youtu.be":
        candidate = parsed.path.strip("/").split("/", 1)[0]
        return candidate if _is_video_id(candidate) else None

    if parsed.path == "/watch":
        candidate = parse_qs(parsed.query).get("v", [""])[0]
        return candidate if _is_video_id(candidate) else None

    path_parts = [part for part in parsed.path.split("/") if part]
    if len(path_parts) >= 2 and path_parts[0] in {"embed", "live", "shorts"}:
        candidate = path_parts[1]
        return candidate if _is_video_id(candidate) else None

    return None


def _ingest_local_source(path: Path) -> dict[str, str]:
    suffix = path.suffix.lower()
    if suffix in TRANSCRIPT_SUFFIXES:
        content = _read_transcript_file(path)
        return {
            "source_url": path.resolve().as_posix(),
            "title": _display_title(path.stem),
            "content": content,
        }

    return {
        "source_url": path.resolve().as_posix(),
        "title": path.name,
        "content": (
            f"Transcript placeholder for {path.name}. "
            "Wire Whisper or another speech-to-text backend here for full support."
        ),
    }


def _ingest_youtube_source(source: str, video_id: str) -> dict[str, str]:
    title = _fetch_youtube_title(source) or f"YouTube {video_id}"
    content = _fetch_youtube_transcript(source, video_id)
    return {
        "source_url": source,
        "title": title,
        "content": content,
    }


def _read_transcript_file(path: Path) -> str:
    raw_text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in SUBTITLE_SUFFIXES:
        return _normalise_subtitle_text(raw_text)
    return _normalise_plain_transcript(raw_text)


def _normalise_plain_transcript(text: str) -> str:
    lines = [line.strip() for line in text.splitlines()]
    cleaned = [_clean_caption_line(line) for line in lines if line.strip()]
    return "\n".join(line for line in _dedupe_adjacent(cleaned) if line)


def _normalise_subtitle_text(text: str) -> str:
    lines: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line == "WEBVTT" or line.startswith(("Kind:", "Language:", "NOTE")):
            continue
        if line.isdigit() or "-->" in line or _TIMESTAMP_RE.match(line) or _SHORT_TIMESTAMP_RE.match(line):
            continue

        cleaned = _clean_caption_line(line)
        if cleaned:
            lines.append(cleaned)

    return "\n".join(_dedupe_adjacent(lines))


def _clean_caption_line(line: str) -> str:
    text = re.sub(r"<[^>]+>", "", line)
    text = html.unescape(text)
    text = text.replace("\u200b", " ")
    return " ".join(text.split())


def _dedupe_adjacent(lines: list[str]) -> list[str]:
    deduped: list[str] = []
    for line in lines:
        if deduped and deduped[-1] == line:
            continue
        deduped.append(line)
    return deduped


def _fetch_youtube_transcript(source: str, video_id: str) -> str:
    errors: list[str] = []

    try:
        transcript = _fetch_transcript_via_api(video_id)
        if transcript:
            return transcript
    except Exception as exc:  # pragma: no cover - exercised in live validation
        errors.append(f"youtube-transcript-api: {exc}")

    try:
        transcript = _fetch_transcript_via_yt_dlp(source)
        if transcript:
            return transcript
    except Exception as exc:  # pragma: no cover - exercised in live validation
        errors.append(f"yt-dlp: {exc}")

    details = "; ".join(errors) if errors else "no backend succeeded"
    return f"Transcript unavailable for {source}. Attempted backends: {details}."


def _fetch_transcript_via_api(video_id: str) -> str:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError as exc:  # pragma: no cover - depends on local env
        raise RuntimeError("youtube-transcript-api is not installed") from exc

    transcript = YouTubeTranscriptApi().fetch(video_id, languages=["en", "en-US", "en-GB"])
    lines = [_clean_caption_line(_transcript_item_text(item)) for item in transcript]
    return "\n".join(line for line in _dedupe_adjacent(lines) if line)


def _transcript_item_text(item: object) -> str:
    if hasattr(item, "text"):
        return str(getattr(item, "text"))
    if isinstance(item, dict):
        return str(item.get("text", ""))
    return str(item)


def _fetch_transcript_via_yt_dlp(source: str) -> str:
    try:
        from yt_dlp import YoutubeDL
    except ImportError:
        executable = shutil.which("yt-dlp")
        if not executable:  # pragma: no cover - depends on local env
            raise RuntimeError("yt-dlp is not installed")
        with tempfile.TemporaryDirectory(prefix="coin-transcript-") as temp_dir:
            output_template = str(Path(temp_dir) / "subtitle")
            subprocess.run(
                [
                    executable,
                    "--skip-download",
                    "--write-auto-subs",
                    "--sub-langs",
                    "en",
                    "--sub-format",
                    "vtt",
                    "-o",
                    output_template,
                    source,
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            subtitle_paths = sorted(Path(temp_dir).glob("subtitle*.vtt"))
            if not subtitle_paths:
                raise RuntimeError("yt-dlp did not produce a subtitle file")
            return _normalise_subtitle_text(subtitle_paths[0].read_text(encoding="utf-8"))

    options = {
        "quiet": True,
        "skip_download": True,
        "writeautomaticsub": True,
        "writesubtitles": True,
        "subtitleslangs": ["en"],
    }
    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(source, download=False)

    subtitles = info.get("subtitles") or info.get("automatic_captions") or {}
    english_tracks = subtitles.get("en") or subtitles.get("en-US") or subtitles.get("en-GB") or []
    for track in english_tracks:
        track_url = track.get("url")
        if not track_url:
            continue
        try:
            import httpx
        except ImportError as exc:  # pragma: no cover - depends on local env
            raise RuntimeError("httpx is not installed") from exc

        response = httpx.get(track_url, timeout=20)
        response.raise_for_status()
        subtitle_text = response.text
        if subtitle_text:
            return _normalise_subtitle_text(subtitle_text)

    raise RuntimeError("no English subtitles exposed by yt-dlp")


def _fetch_youtube_title(source: str) -> str | None:
    try:
        from yt_dlp import YoutubeDL
    except ImportError:
        executable = shutil.which("yt-dlp")
        if not executable:  # pragma: no cover - depends on local env
            return None
        completed = subprocess.run(
            [executable, "--print", "title", source],
            check=True,
            capture_output=True,
            text=True,
        )
        title = completed.stdout.strip().splitlines()
        return title[-1].strip() if title else None

    with YoutubeDL({"quiet": True, "skip_download": True}) as ydl:
        info = ydl.extract_info(source, download=False)
    title = info.get("title")
    return str(title).strip() if title else None


def _display_title(value: str) -> str:
    return value.replace("_", " ").strip() or "Transcript"


def _is_video_id(value: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9_-]{11}", value))
