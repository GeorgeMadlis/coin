# COIN — ConnectedInformation · Repo Structure

> Paste this file at the start of any Claude.ai or ChatGPT session to give the
> model full context of the codebase before asking it to help with a step.

---

## What COIN is

COIN (ConnectedInformation) is an LLM-compiled knowledge base and common
research/provenance layer for ConnectedNature and ConnectedInfo. ConnectedNature
publishes broad and systemic public inquiries; ConnectedInfo publishes focused
claim-by-claim public fact-checks. COIN can support either output mode, and not
every COIN inquiry needs to be published. It ingests raw sources (URLs, PDFs,
audio, social posts) and compiles them into an interconnected wiki with
citations, a knowledge graph, Q&A with auto-research, contradiction linting, and
watch-mode auto-updates.

Inspired by Andrej Karpathy's idea: feed raw data into an LLM → compile a
structured, auto-linked knowledge base.

---

## Two operating modes

### Manual mode (web UI)
Each pipeline step is executed by pasting a prompt from `coin/prompts/` into
Claude.ai or ChatGPT. The human copies the LLM output back into the relevant
file on disk. No API keys required. Ideal during development and curation.

### Agent mode (automated)
The same pipeline steps run programmatically via `coin run --mode agent`.
The LLM is called via API (Anthropic, OpenAI, or local Ollama). Runs
unattended on a schedule. Requires API keys.

The pipeline steps and their output artifacts are **identical in both modes**.
The only difference is who executes each step.

---

## Pipeline steps

Each step lives in `coin/pipeline/stepN_name.py` and produces a persistent
artifact (a file or DB row). Steps can be run independently.

```
Step 1  ingest      Raw source → RawDocument (doc_id, title, content) → artifacts/documents/
Step 2  embed       RawDocument chunks → stored chunks                 → store/chunks (DB)
Step 3  group       Document summaries → topic clusters               → artifacts/groups.json
Step 4  compile     Topic group + chunks → wiki article (.md)          → wiki/*.md
Step 5  link        All wiki/*.md → resolve [[wikilinks]], backlinks   → store/backlinks (DB)
Step 6  lint        All articles → contradictions, gaps, stale flags   → store/lint_findings (DB)
Step 7  qa          Question + relevant chunks → cited answer          → (returned to caller)
```

---

## Directory structure

```
coin/                          ← Python package
│
├── pipeline/                  ← One file per pipeline step
│   ├── step1_ingest.py        Fetch + normalise a raw source
│   ├── step2_embed.py         Chunk text + generate embeddings
│   ├── step3_group.py         Cluster chunks into topic groups
│   ├── step4_compile.py       Write/update a wiki article per topic
│   ├── step5_link.py          Resolve [[wikilinks]] across all articles
│   ├── step6_lint.py          Detect contradictions, gaps, stale content
│   └── step7_qa.py            Answer a question with citations
│
├── prompts/                   ← Web UI prompts (Manual mode)
│   ├── 01_ingest.md           Prompt: extract and normalise a source
│   ├── 02_group.md            Prompt: cluster document summaries into topics
│   ├── 03_compile.md          Prompt: write a wiki article for a topic
│   ├── 04_lint.md             Prompt: find contradictions and gaps
│   └── 05_qa.md               Prompt: answer a question from the KB
│
├── agent/
│   ├── orchestrator.py        Runs the full pipeline in agent mode
│   └── watcher.py             APScheduler watch-mode daemon
│
├── ingestion/                 ← Source adapters (used by step1)
│   ├── url_ingestor.py        Web pages, RSS
│   ├── pdf_ingestor.py        PDFs, EPUB, DOCX
│   ├── audio_ingestor.py      MP3/MP4/YouTube → Whisper transcript
│   ├── subtitle_ingestor.py   YouTube caption track (fast; no audio download)
│   ├── social_ingestor.py     Twitter/X, Reddit, HN
│   └── browser_clip.py        Receives clips from Chrome extension
│
├── memory/
│   └── ultramemory.py         Embedding store + semantic search (sqlite-vss)
│
├── store/
│   └── database.py            SQLite schema + async connection helper
│
├── export/
│   ├── html_exporter.py       Wiki → self-contained HTML report
│   ├── pdf_exporter.py        HTML → PDF (WeasyPrint)
│   └── snapshot.py            Full-KB JSON snapshot
│
├── web/
│   ├── app.py                 FastAPI app (wiki reader, graph, Q&A UI)
│   └── routes/
│       ├── articles.py        GET/POST /api/articles
│       ├── graph.py           GET /api/graph (D3-compatible JSON)
│       └── qa.py              POST /api/qa (SSE streaming)
│
├── llm.py                     LLM provider abstraction (Anthropic/OpenAI/Ollama)
├── config.py                  Pydantic settings (reads .env)
└── cli.py                     Typer CLI — all commands

wiki/                          ← Compiled Markdown articles (git-tracked)
research/                      ← Curated research trails, recorded inquiries, claim ledgers, and source-check bundles
artifacts/                     ← Intermediate pipeline artifacts (groups.json etc.)
chrome-extension/              ← Manifest V3 browser clip extension
tests/
docs/
```

---

## Key data models

```python
# Step 1 artifact — artifacts/documents/NNNN_slug.json
RawDocument(doc_id, source_url, title, content)

# Intermediate
Chunk(doc_id, text, position)
TopicGroup(label, doc_ids)

# Output artifacts
WikiArticle  → wiki/{slug}.md  (Markdown with [[wikilinks]] and [^citations])
BackLink     → store: (source_slug, target_slug)
LintFinding  → store: (kind, article_slug, detail)
Answer(text, confidence, citations, web_searched)
```

---

## SQLite schema (summary)

```
documents      id, source_url, content, media_type, metadata, ingested_at
chunks         id, doc_id, text, position
chunks_vss     virtual table (sqlite-vss) — embedding(1536)
entities       id, doc_id, label, text, start, end
fact_triples   id, doc_id, subject, predicate, object, confidence
articles       id, slug, title, path, compiled_at
backlinks      id, from_slug, to_slug
watched_topics id, topic, cron, last_run_at, enabled
lint_findings  id, kind, article_slug, detail, resolved, created_at
```

---

## CLI commands

```bash
coin ingest <source>                    # Step 1 — ingest a URL, file path, or social post
  --audio                               #   Download audio → Whisper transcript
  --audio-subtitles                     #   Fetch YouTube caption track (fast, no model needed)
  --tweet                               #   Treat source as a social post

coin embed                              # Step 2 — chunk + store all new documents
coin group                              # Step 3 — cluster into topic groups
coin compile [--topic <name>]           # Step 4 — write/update wiki articles
coin link                               # Step 5 — resolve wikilinks
coin lint                               # Step 6 — find issues
coin ask "<question>"                   # Step 7 — Q&A
coin run                                # Run steps 2–6 end-to-end (agent mode)
coin watch add <topic>                  # Add a topic to watch mode
coin watch run                          # Run all scheduled topics now
coin export html|pdf|snapshot           # Export the KB
coin serve                              # Start the web UI (localhost:7860)
```

---

## Configuration (.env keys)

```
COIN_MODE                  manual | agent
COIN_LLM_PROVIDER          anthropic | openai | ollama
ANTHROPIC_API_KEY
OPENAI_API_KEY
COIN_OLLAMA_MODEL
COIN_EMBED_PROVIDER        openai | ollama
COIN_EMBED_MODEL
COIN_DB_PATH               ./coin.db
COIN_WIKI_DIR              ./wiki
COIN_ARTIFACTS_DIR         ./artifacts
COIN_PORT                  7860
```

---

## How to use this file with a web UI

**Claude.ai or ChatGPT workflow:**

1. Start a new conversation.
2. Paste the contents of this file as your first message.
3. Then paste the relevant prompt from `coin/prompts/` for the step you are working on.
4. Copy the LLM output back into the appropriate file on disk.

Each prompt in `coin/prompts/` is self-contained — it tells the model exactly
what inputs to expect, what to produce, and in what format.

Transcript inputs:
- Local `.txt`, `.md`, `.srt`, and `.vtt` files are valid ingest sources.
- YouTube URLs can be ingested directly when a transcript is available.

---

## Architecture governance

**This file is the single source of truth for repo structure.**

The rules below exist to prevent the codebase and its documentation from
drifting apart — a failure mode that is especially costly when LLMs are used
as development assistants, because stale structural documentation leads to
compounding hallucinations across sessions.

### What requires a STRUCTURE.md update

Any change to the following **must** be reflected in this file in the same
commit or PR, before the code change is merged:

- Adding, removing, or renaming a pipeline step (`stepN_*.py`)
- Adding, removing, or renaming an ingestion adapter in `coin/ingestion/`
- Adding, removing, or renaming a top-level directory
- Changing where a pipeline step writes its output artifact
- Adding a new CLI command or flag
- Adding a new database table or column
- Adding a new key data model

### What does NOT require a STRUCTURE.md update

- Refactoring internals of an existing file without changing its interface
- Bug fixes that do not change artifact locations or CLI surface
- Adding tests

### Rule of thumb

If you would describe the change as "I added a new X" or "I moved X to Y",
update STRUCTURE.md. If you would describe it as "I fixed X" or
"I improved X", you probably do not need to.

### Enforcement

There is no automated check yet. Until one exists, reviewers should treat a
structural code change without a matching STRUCTURE.md update as a blocking
issue. When working with an LLM assistant: paste the current STRUCTURE.md at
the start of each session, and ask the model to propose STRUCTURE.md changes
alongside any structural code changes.
