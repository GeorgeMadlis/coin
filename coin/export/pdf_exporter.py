"""Export the knowledge base as a PDF."""

from __future__ import annotations

from pathlib import Path

from coin.export.html_exporter import HtmlExporter


class PdfExporter:
    """Generate a PDF when WeasyPrint is available, otherwise write a text fallback."""

    async def export(self, out_path: Path) -> Path:
        html_path = await HtmlExporter().export(out_path.parent / "html")
        html = html_path.read_text(encoding="utf-8")

        try:
            from weasyprint import HTML
        except Exception:
            out_path.write_text(
                "WeasyPrint is not available in this environment.\n\n" + html,
                encoding="utf-8",
            )
            return out_path

        HTML(string=html, base_url=html_path.parent.as_posix()).write_pdf(out_path)
        return out_path
