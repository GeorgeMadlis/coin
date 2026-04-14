"""Step 7 — answer a question against the current knowledge base."""

from __future__ import annotations

from pathlib import Path

from coin.memory.ultramemory import Ultramemory


PROMPT_PATH = Path(__file__).parent.parent / "prompts" / "05_qa.md"


async def print_manual_prompt(question: str) -> str:
    """Build the manual Q&A prompt with retrieved excerpts."""

    excerpts = await _render_excerpts(question)
    template = PROMPT_PATH.read_text(encoding="utf-8")
    return template.replace("{{QUESTION}}", question).replace("{{RELEVANT_EXCERPTS}}", excerpts)


async def run_agent(question: str) -> dict[str, object]:
    """Answer using simple local retrieval over documents and wiki pages."""

    hits = await Ultramemory().search(question, limit=5)
    if not hits:
        return {
            "text": "I could not find relevant material in the current knowledge base.",
            "confidence": "Low",
            "citations": [],
            "web_searched": False,
        }

    citations = [{"source_url": hit.source_url} for hit in hits]
    answer_lines = [
        "Here is the closest material currently in the knowledge base:",
        "",
    ]
    answer_lines.extend(f"[{index}] {hit.text}" for index, hit in enumerate(hits, start=1))

    confidence = "High" if len(hits) >= 3 else "Medium"
    return {
        "text": "\n".join(answer_lines),
        "confidence": confidence,
        "citations": citations,
        "web_searched": False,
    }


async def _render_excerpts(question: str) -> str:
    hits = await Ultramemory().search(question, limit=5)
    if not hits:
        return "(no relevant excerpts found)"
    return "\n\n".join(
        f"[{index}] {hit.source_url}\n{hit.text}" for index, hit in enumerate(hits, start=1)
    )
