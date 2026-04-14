# COIN — ConnectedInformation

**An LLM-compiled knowledge base for [ConnectedNature](https://connectednature.com).**

Ingest raw sources (URLs, PDFs, audio, social posts, YouTube transcripts), compile them into an
interconnected wiki with citations and a knowledge graph, answer questions
against your KB, and keep everything current with watch mode.

Inspired by Andrej Karpathy's idea: feed raw data into an LLM → compile a
structured, self-writing knowledge base.

---

## Two operating modes

COIN is designed to work in two modes that share the same pipeline and artifacts:

### Manual mode — web UI (Claude.ai Pro / ChatGPT Plus)
Each pipeline step is driven by pasting a ready-made prompt from `coin/prompts/`
into Claude.ai or ChatGPT. You copy the output back to disk. **No API keys
required.** Ideal for development, curation, and one-off research sessions.

```bash
coin ingest https://example.com/article    # fetch + save raw text to disk
coin ingest https://www.youtube.com/watch?v=hQLEu3ZIrYU
coin ingest /path/to/transcript.vtt
# → open coin/prompts/02_group.md in Claude.ai, paste your document list
# → copy the topic groups back into artifacts/groups.json
# → open coin/prompts/03_compile.md, paste one topic group
# → copy the drafted article into wiki/my-topic.md
```

### Agent mode — automated (Anthropic / OpenAI / Ollama API)
The same steps run programmatically via the CLI. The LLM is called via API.
Runs unattended on a schedule. Requires API keys.

```bash
coin ingest https://example.com/article
coin run                                   # steps 2–6 end-to-end
coin ask "What causes soil carbon loss?"
```

**You can mix both modes freely.** Draft articles manually in Claude.ai,
save them to `wiki/`, and let the agent handle watch mode and Q&A. The
pipeline artifacts are plain files — either mode can read and write them.

---

## Quickstart

```bash
git clone https://github.com/GeorgeMadlis/coin.git
cd coin
pip install -e ".[dev]"
cp .env.example .env
# Edit .env — set COIN_MODE=manual to start without API keys
coin ingest https://en.wikipedia.org/wiki/Mycorrhiza
```

**Manual mode** — no further setup. Open `coin/prompts/02_group.md` in
Claude.ai and follow the instructions inside.

**Agent mode** — add your API key to `.env`, then:
```bash
coin run       # group → compile → link → lint
coin serve     # open http://localhost:7860
```

---

## Project layout

See **[STRUCTURE.md](STRUCTURE.md)** for the full annotated repo map.
Paste `STRUCTURE.md` at the start of any Claude.ai or ChatGPT session to give
the model full codebase context.

```
coin/pipeline/     One script per pipeline step (steps 1–7)
coin/prompts/      Ready-to-paste web UI prompts for each step
coin/agent/        Automated orchestrator and watch-mode daemon
coin/ingestion/    Source adapters (URL, PDF, audio, social, browser)
coin/memory/       Ultramemory — embedding store + semantic search
coin/store/        SQLite schema
coin/web/          FastAPI web UI + REST API
wiki/              Compiled Markdown articles (git-tracked)
artifacts/         Intermediate pipeline artifacts (groups.json, etc.)
STRUCTURE.md       Full repo map — paste into any web UI for context
```

YouTube inputs:
`coin ingest https://www.youtube.com/watch?v=...` fetches the transcript when one
is available. Local `.txt`, `.md`, `.srt`, and `.vtt` transcript files can also
be ingested directly.

---

## Pipeline

```
Raw sources
    ↓ step 1  ingest      → store/documents
    ↓ step 2  embed       → store/chunks_vss
    ↓ step 3  group       → artifacts/groups.json
    ↓ step 4  compile     → wiki/*.md
    ↓ step 5  link        → store/backlinks
    ↓ step 6  lint        → store/lint_findings
    ↓ step 7  qa          → cited answer
```

Each step reads from and writes to files that both modes share.

---

## Contributing

PRs welcome. Run tests with `pytest tests/ -v`.
Code style: `ruff` + `black`. Type hints required on all public functions.

---

## License

MIT
