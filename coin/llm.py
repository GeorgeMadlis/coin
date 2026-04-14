"""Minimal LLM abstraction with a safe offline fallback."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from urllib.parse import urlparse

from coin.ingestion.audio_ingestor import label_from_title


@dataclass
class OfflineLLM:
    """Offline fallback used when no external provider is wired in."""

    async def complete(self, system: str, user: str) -> str:
        if '"groups"' in system:
            return self._group_documents(user)
        return user

    def _group_documents(self, user: str) -> str:
        groups: dict[str, list[int]] = {}
        for block in user.split("\n---\n"):
            header = re.search(r"\[doc (\d+)\] ([^\n]+)", block)
            if not header:
                continue

            doc_id = int(header.group(1))
            source = header.group(2).strip()
            title_match = re.search(r"^Title:\s*(.+)$", block, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else ""

            label = label_from_title(title)
            if not label:
                parsed = urlparse(source)
                host = parsed.netloc or parsed.path or "Documents"
                label = host.replace("www.", "").split(".")[0].replace("-", " ").title() or "Documents"
            groups.setdefault(label, []).append(doc_id)

        if not groups:
            groups = {"Documents": []}

        payload = {
            "groups": [{"label": label, "doc_ids": doc_ids} for label, doc_ids in sorted(groups.items())]
        }
        return json.dumps(payload, indent=2)


def get_llm() -> OfflineLLM:
    """Return the current LLM client.

    The repo only needs a provider abstraction on disk right now, so we keep the
    default implementation deterministic and local.
    """

    return OfflineLLM()
