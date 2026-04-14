"""Step 4 — compile wiki articles from grouped documents."""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

from coin.config import settings


ARTIFACTS_DIR = Path(settings.artifacts_dir)
WIKI_DIR = Path(settings.wiki_dir)
GROUPS_PATH = ARTIFACTS_DIR / "groups.json"


async def print_manual_prompt(topic: str | None = None) -> str:
    """Build a compile prompt for the chosen topic group."""

    group = _select_groups(topic)[0]
    documents = _load_documents(group["doc_ids"])
    slug = _slugify(group["label"])
    existing = _load_existing_article(slug)
    chunks = "\n\n---\n\n".join(
        f"Source: {doc['source_url']}\n\n{doc['content'][:1200].strip()}" for doc in documents
    )

    template = (Path(__file__).parent.parent / "prompts" / "03_compile.md").read_text(
        encoding="utf-8"
    )
    prompt = (
        template.replace("{{TOPIC_LABEL}}", group["label"])
        .replace("{{EXISTING_ARTICLE}}", existing or "(none yet)")
        .replace("{{SOURCE_CHUNKS}}", chunks or "(no source chunks)")
        .replace("{{SLUG}}", slug)
    )

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    (ARTIFACTS_DIR / "compile_prompt.md").write_text(prompt, encoding="utf-8")
    return prompt


async def apply_manual_article(article_path: Path) -> str:
    """Save a manually drafted article into the wiki directory."""

    text = article_path.read_text(encoding="utf-8")
    slug = _slug_from_frontmatter(text) or article_path.stem
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    (WIKI_DIR / f"{slug}.md").write_text(text, encoding="utf-8")
    return slug


async def run_agent(topic: str | None = None) -> list[str]:
    """Compile one or more wiki articles using a deterministic local formatter."""

    titles: list[str] = []
    for group in _select_groups(topic):
        documents = _load_documents(group["doc_ids"])
        if not documents:
            continue

        slug = _slugify(group["label"])
        body = _build_article(group["label"], slug, documents)
        WIKI_DIR.mkdir(parents=True, exist_ok=True)
        (WIKI_DIR / f"{slug}.md").write_text(body, encoding="utf-8")
        titles.append(group["label"])

    return titles


def _select_groups(topic: str | None) -> list[dict[str, object]]:
    data = json.loads(GROUPS_PATH.read_text(encoding="utf-8")) if GROUPS_PATH.exists() else {"groups": []}
    groups = data.get("groups", [])
    if topic is None:
        return list(groups)
    return [group for group in groups if str(group.get("label")) == topic]


def _load_documents(doc_ids: list[int]) -> list[dict[str, object]]:
    docs_dir = ARTIFACTS_DIR / "documents"
    documents: list[dict[str, object]] = []
    for doc_id in doc_ids:
        matches = sorted(docs_dir.glob(f"{int(doc_id):04d}_*.json"))
        if not matches:
            continue
        documents.append(json.loads(matches[0].read_text(encoding="utf-8")))
    return documents


def _load_existing_article(slug: str) -> str:
    path = WIKI_DIR / f"{slug}.md"
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _build_article(title: str, slug: str, documents: list[dict[str, object]]) -> str:
    sources = [str(doc["source_url"]) for doc in documents]
    paragraphs = []
    for index, doc in enumerate(documents, start=1):
        excerpt = str(doc["content"]).strip().replace("\n", " ")
        excerpt = " ".join(excerpt.split())[:700]
        paragraphs.append(f"{excerpt} [^{index}]")

    references = "\n".join(f"[^{index}]: {source}" for index, source in enumerate(sources, start=1))
    return (
        "---\n"
        f"title: {title}\n"
        f"slug: {slug}\n"
        f"compiled_at: {date.today().isoformat()}\n"
        f"sources: {json.dumps(sources, ensure_ascii=False)}\n"
        "---\n\n"
        f"# {title}\n\n"
        + "\n\n".join(paragraphs)
        + "\n\n## References\n\n"
        + references
        + "\n"
    )


def _slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")
    return "-".join(part for part in cleaned.split("-") if part) or "article"


def _slug_from_frontmatter(text: str) -> str | None:
    match = re.search(r"^slug:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else None
