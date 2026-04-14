# Karpathy Pipeline Mapping

This document explains how the PROTOCOL.md stage design corresponds to Karpathy's
view of LLMs as **staged information processors**.

---

## The core idea

Karpathy frames LLMs not as monolithic question-answerers but as transformation
engines that work best when a complex task is decomposed into discrete passes —
each pass taking structured input, performing a well-scoped operation, and writing
durable output that the next pass consumes. No single context window is expected
to carry the whole job.

The PROTOCOL implements this literally: five stages, each a separate Claude Code
invocation, each reading from and writing to files on disk.

---

## Stage-by-stage correspondence

| Karpathy concept | PROTOCOL stage | Input | Output |
|---|---|---|---|
| Raw token stream | Stage 1 — entity extraction | `raw/transcript.md` | `authors.md`, `claims.md` |
| External retrieval / tool use | Stage 2 — works discovery | `authors.md` | `authors.md` (enriched) |
| Context expansion via fetched docs | Stage 3 — source reading | URLs in `authors.md` | `sources/{author}.md` |
| Human-in-the-loop gate | Stage 3.5 — review checkpoint | `sources/` | Coverage notes in `claims.md` |
| Synthesis / generation | Stage 4 — critical overview | All prior outputs | `critical-overview.md` |

---

## Three structural decisions that reflect the pipeline model

### 1. One invocation per stage (context window as RAM)

Each stage runs as a fresh Claude Code call. This keeps the active context
focused — Stage 2 only sees `authors.md`, not the full transcript. Karpathy's
analogy: the context window is RAM, not a hard drive. Filling it with prior-stage
noise degrades the current operation.

### 2. Files as the inter-stage bus

Intermediate artifacts (`authors.md`, `claims.md`, `sources/*.md`) are the only
handoff mechanism between stages. There is no shared in-memory state. This matches
Karpathy's description of tool outputs as the durable, inspectable layer that
decouples pipeline steps and makes each one independently auditable.

### 3. Git commit as checkpoint

The Invocation guide requires `git commit` after every stage. This enforces that
each stage's output is frozen and reviewable before the next stage consumes it —
the same principle Karpathy argues for in multi-step pipelines: human oversight
should be possible at every transition, not just at the end.

---

## The gap: manual orchestration

The current Invocation guide is **manually driven** — the user pastes one prompt
per stage. Karpathy's ideal pipeline would have an orchestration layer manage
stage transitions automatically, with the human review at Stage 3.5 as the only
hard-coded stop. That orchestration layer is not yet implemented; the commit step
is the current substitute.

---

## Ultramemory: the read path

The PROTOCOL stages described above are the **write path** — they transform raw
input into accumulated knowledge. `coin/memory/ultramemory.py` is the **read
path** — it makes that accumulated knowledge queryable.

```text
raw transcript
     │
  Stage 1 ──► claims.md, authors.md
     │
  Stage 2 ──► authors.md (enriched)
     │
  Stage 3 ──► sources/{author}.md
     │
  Stage 4 ──► critical-overview.md  ──► wiki/*.md
                                              │
                                     Ultramemory.search()        ← Step 7 Q&A
                                              │
                                      ranked SearchHits
```

`Ultramemory` indexes two corpora:

- **`_search_documents`** — `artifacts/documents/*.json` (ingested source texts,
  pipeline input side)
- **`_search_articles`** — `wiki/*.md` (pipeline output side — summaries,
  overviews, mapping docs like this one)

In Karpathy's memory taxonomy, it occupies the **external retrieval** slot — the
layer that persists beyond the context window and is queried rather than held
in-weights:

| Karpathy memory type         | coin equivalent                              |
| ---------------------------- | -------------------------------------------- |
| In-weights (slow, permanent) | Base model knowledge                         |
| In-context (fast, ephemeral) | Active stage invocation                      |
| External / retrieval         | `Ultramemory` over `wiki/` + `artifacts/`    |

### How it would be used in this pipeline

After Stage 4 commits `critical-overview.md` to `wiki/`, `Ultramemory` can
immediately serve questions against the full research corpus — without re-running
any stage. For example:

```text
Q: "What did Tainter argue about complexity?"
→ Ultramemory.search("Tainter complexity") 
→ returns excerpts from sources/joseph-tainter.md + critical-overview.md
→ Step 7 assembles an answer with citations
```

This closes the pipeline loop: write path (PROTOCOL) builds the knowledge base,
read path (Ultramemory + Step 7) answers questions against it.

### Current limitation

Scoring is word-overlap (`_score_text`), not semantic similarity. The module
docstring flags this as a placeholder for a proper embedding store (sqlite-vss).
Until that is implemented, queries with synonyms or paraphrased terms will miss
relevant hits — e.g. searching "societal collapse" will not match text that says
"civilizational decline."

---

## Summary

The PROTOCOL is a direct expression of Karpathy's staged-processing model:
raw signal in → entity extraction → retrieval → deep reading → synthesis out,
with files as the bus and commits as checkpoints. The Invocation guide is the
execution contract that enforces one-stage-at-a-time discipline so the pipeline
properties hold in practice. `Ultramemory` completes the picture as the read
layer: once the write path has run, it makes the accumulated knowledge queryable
without re-entering the pipeline.
