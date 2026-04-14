"""Export a JSON snapshot of the current wiki."""

from __future__ import annotations

import json
from pathlib import Path

from coin.config import settings


async def export_snapshot(out_path: Path) -> Path:
    """Write all wiki articles into a single JSON file."""

    payload = []
    for path in sorted(Path(settings.wiki_dir).glob("*.md")):
        payload.append({"slug": path.stem, "content": path.read_text(encoding="utf-8")})

    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return out_path
