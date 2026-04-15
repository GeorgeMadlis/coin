"""Export wiki articles as a self-contained HTML page."""

from __future__ import annotations

from html import escape
from pathlib import Path

from coin.config import settings


class HtmlExporter:
    """Render wiki markdown files into a simple HTML bundle."""

    def _collect_wiki_paths(self) -> list[Path]:
        """Return all wiki .md files from wiki_dir and research/*/wiki/ directories."""
        seen: set[Path] = set()
        paths: list[Path] = []

        def _add(p: Path) -> None:
            resolved = p.resolve()
            if resolved not in seen:
                seen.add(resolved)
                paths.append(p)

        wiki_dir = Path(settings.wiki_dir)
        if wiki_dir.is_dir():
            for p in sorted(wiki_dir.glob("*.md")):
                _add(p)

        research_root = Path(__file__).parent.parent.parent / "research"
        if research_root.is_dir():
            for p in sorted(research_root.glob("*/wiki/*.md")):
                _add(p)

        return paths

    async def export(self, out_dir: Path) -> Path:
        out_dir.mkdir(parents=True, exist_ok=True)
        body_parts = []
        for path in self._collect_wiki_paths():
            markdown_text = path.read_text(encoding="utf-8")
            body_parts.append(f"<section><h2>{escape(path.stem)}</h2><pre>{escape(markdown_text)}</pre></section>")

        html = (
            "<!doctype html><html><head><meta charset='utf-8'>"
            "<title>COIN Export</title>"
            "<style>body{font-family:system-ui;margin:2rem;}pre{white-space:pre-wrap;}"
            "section{margin-bottom:2rem;}</style></head><body>"
            "<h1>COIN Knowledge Base</h1>"
            + "".join(body_parts)
            + "</body></html>"
        )
        out_path = out_dir / "index.html"
        out_path.write_text(html, encoding="utf-8")
        return out_path
