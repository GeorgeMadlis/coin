"""
coin/pipeline/step3_group.py

Step 3 — Cluster document summaries into topic groups.

This is the first step that requires an LLM call, so it is the clearest
example of the manual/agent split.

Manual mode:
    coin group --manual
    → Prints the prompt to stdout (or a file) ready to paste into Claude.ai.
    → You run the LLM yourself, then paste the JSON response back:
      coin group --apply <response.json>

Agent mode:
    coin group
    → Calls the LLM API automatically and writes artifacts/groups.json.

Output artifact: artifacts/groups.json
"""

from __future__ import annotations

import json
from pathlib import Path

from coin.config import settings


ARTIFACTS_DIR = Path(settings.artifacts_dir)
GROUPS_PATH = ARTIFACTS_DIR / "groups.json"


# ── Manual mode ─────────────────────────────────────────────────────────────────

async def print_manual_prompt() -> str:
    """
    Build the prompt the user should paste into Claude.ai or ChatGPT.
    Also writes it to artifacts/group_prompt.md for convenience.
    """
    summaries = await _load_summaries()
    prompt_template = _load_prompt_template()
    prompt = prompt_template.replace("{{DOCUMENT_SUMMARIES}}", summaries)

    out = ARTIFACTS_DIR / "group_prompt.md"
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    out.write_text(prompt, encoding="utf-8")
    return prompt


async def apply_manual_response(response_path: Path) -> dict:
    """
    Accept the JSON pasted back from the web UI and save it as groups.json.
    The response must be a JSON object: { "groups": [ { "label": "...", "doc_ids": [...] } ] }
    """
    data = json.loads(response_path.read_text(encoding="utf-8"))
    _validate_groups(data)
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    GROUPS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return data


# ── Agent mode ───────────────────────────────────────────────────────────────────

async def run_agent() -> dict:
    """Call the LLM API and write artifacts/groups.json."""
    from coin.llm import get_llm

    summaries = await _load_summaries()
    llm = get_llm()

    response_text = await llm.complete(
        system=(
            "You are a knowledge librarian. Given a list of document summaries, "
            "group them into coherent topics. Return ONLY a JSON object with this "
            "exact shape — no prose, no markdown fences:\n"
            '{ "groups": [ { "label": "<2-4 word topic>", "doc_ids": [1, 2, ...] } ] }'
        ),
        user=summaries,
    )

    clean = response_text.strip().removeprefix("```json").removesuffix("```").strip()
    data = json.loads(clean)
    _validate_groups(data)
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    GROUPS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return data


# ── Shared helpers ───────────────────────────────────────────────────────────────

async def _load_summaries() -> str:
    """Load doc summaries from the artifacts/documents/ directory."""
    docs_dir = ARTIFACTS_DIR / "documents"
    lines: list[str] = []
    if docs_dir.exists():
        for f in sorted(docs_dir.glob("*.json")):
            doc = json.loads(f.read_text(encoding="utf-8"))
            excerpt = doc.get("content", "")[:400].replace("\n", " ")
            lines.append(f"[doc {doc['doc_id']}] {doc['source_url']}\n{excerpt}\n")
    return "\n---\n".join(lines) if lines else "(no documents ingested yet)"


def _load_prompt_template() -> str:
    template_path = Path(__file__).parent.parent / "prompts" / "02_group.md"
    if template_path.exists():
        return template_path.read_text(encoding="utf-8")
    # Inline fallback
    return (
        "Below are summaries of documents in the COIN knowledge base.\n"
        "Group them into coherent topics (2–4 word labels).\n"
        "Return ONLY a JSON object:\n"
        '{ "groups": [ { "label": "Topic Label", "doc_ids": [1, 2] } ] }\n\n'
        "DOCUMENT SUMMARIES:\n{{DOCUMENT_SUMMARIES}}"
    )


def _validate_groups(data: dict) -> None:
    if "groups" not in data or not isinstance(data["groups"], list):
        raise ValueError("Response must be a JSON object with a 'groups' list.")
    for g in data["groups"]:
        if "label" not in g or "doc_ids" not in g:
            raise ValueError(f"Each group must have 'label' and 'doc_ids'. Got: {g}")
