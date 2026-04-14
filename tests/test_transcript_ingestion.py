from __future__ import annotations

from pathlib import Path

from coin.ingestion.audio_ingestor import (
    extract_youtube_video_id,
    is_transcript_path,
    label_from_title,
    looks_like_youtube_source,
    _normalise_subtitle_text,
)


def test_extract_youtube_video_id_from_watch_url() -> None:
    assert extract_youtube_video_id("https://www.youtube.com/watch?v=hQLEu3ZIrYU") == "hQLEu3ZIrYU"


def test_detects_youtube_source() -> None:
    assert looks_like_youtube_source("https://youtu.be/hQLEu3ZIrYU")


def test_recognises_transcript_path(tmp_path: Path) -> None:
    path = tmp_path / "sample.vtt"
    path.write_text("WEBVTT\n\n00:00.000 --> 00:01.000\nHello world\n", encoding="utf-8")
    assert is_transcript_path(str(path))


def test_normalise_subtitle_text_removes_timestamps() -> None:
    raw = (
        "WEBVTT\n\n"
        "00:00.000 --> 00:01.000\n"
        "<c.colorE5E5E5>Hello world</c>\n\n"
        "00:01.000 --> 00:02.000\n"
        "Hello world\n"
        "Next line\n"
    )
    assert _normalise_subtitle_text(raw) == "Hello world\nNext line"


def test_label_from_title_handles_civilization_video() -> None:
    title = "There Is a Complexity Threshold That No Civilization Has Ever Survived"
    assert label_from_title(title) == "Complexity of Civilizations"
