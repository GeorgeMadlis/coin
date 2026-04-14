"""Minimal LLM abstraction with a safe offline fallback."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass
class OfflineLLM:
    """Offline fallback used when no external provider is wired in."""

    async def complete(self, system: str, user: str) -> str:
        if '"groups"' in system:
            return self._group_documents(user)
        return user

    def _group_documents(self, user: str) -> str:
        groups: dict[str, list[int]] = {}
        for match in re.finditer(r"\[doc (\d+)\] ([^\n]+)", user):
            doc_id = int(match.group(1))
            source = match.group(2).strip()
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
