# COIN Pipeline Walkthrough

A complete end-to-end example using the YouTube video
**"There Is a Complexity Threshold That No Civilization Has Ever Survived"**
(`https://www.youtube.com/watch?v=hQLEu3ZIrYU`).

Each section shows the command, what it does, and what artifact it produces.

---

## Step 1 — Ingest

Fetch the YouTube caption track and save it as a structured document artifact.

```bash
coin ingest --audio-subtitles 'https://www.youtube.com/watch?v=hQLEu3ZIrYU'
```

**What happens:** yt-dlp pulls the English caption track (manual subtitles
preferred; auto-generated captions as fallback), deduplicates the rolling-line
flicker common in auto-captions, and writes a JSON document to disk.

**Output:** `artifacts/documents/0001_there-is-a-complexity-threshold-that-no-civilization-has-ever-survived.json`

```json
{
  "doc_id": 1,
  "source_url": "https://www.youtube.com/watch?v=hQLEu3ZIrYU",
  "title": "There Is a Complexity Threshold That No Civilization Has Ever Survived",
  "content": "In 1988, an anthropologist in Utah published a book with a graph..."
}
```

> **Alternative:** `--audio` downloads the audio stream and runs Whisper locally.
> Use it when captions are absent or low quality. `--audio-subtitles` is faster
> and requires no local model.

---

## Step 2 — Embed

Chunk the document text and store the chunks in the database, ready for
semantic search and grouping.

```bash
coin embed
```

**What happens:** Each document in `artifacts/documents/` that has not yet been
embedded is split into overlapping text chunks. The chunks are stored in the
`chunks` table in `coin.db`.

**Output:** rows in `store/chunks (DB)`

> Step 2 always runs in agent mode — it calls an embeddings API
> (OpenAI or Ollama, set via `COIN_EMBED_PROVIDER` in `.env`).

---

## Step 3 — Group

Cluster all ingested documents into topic groups that will each become a wiki
article.

```bash
# Agent mode (calls the LLM API automatically)
coin group

# Manual mode — prints a prompt to paste into Claude.ai or ChatGPT
coin group --manual

# Apply a response you got from the web UI
coin group --apply path/to/groups_response.json
```

**What happens:** Document summaries are sent to the LLM, which clusters them
into coherent topic groups.

**Output:** `artifacts/groups.json`

```json
{
  "groups": [
    {
      "label": "Complexity of Civilizations",
      "doc_ids": [2]
    }
  ]
}
```

---

## Step 4 — Compile

Write a wiki article for each topic group.

```bash
# Compile all groups
coin compile

# Compile a single topic by label (use the exact label from artifacts/groups.json)
coin compile --topic "Complexity of Civilizations"

# Manual mode
coin compile --manual

# Apply a manually drafted article
coin compile --apply path/to/my-draft.md
```

**What happens:** The LLM receives the topic label, the relevant chunks, and
instructions to write a Markdown article with `[[wikilinks]]` and
`[^citations]`.

**Output:** `wiki/complexity-of-civilizations.md`

```markdown
# Complexity of Civilizations

Joseph Tainter's 1988 work identified a universal pattern: civilizations
collapse when the marginal return on complexity falls below the cost of
maintaining it... [^1]

## References

[^1]: https://www.youtube.com/watch?v=hQLEu3ZIrYU
```

---

## Step 5 — Link

Resolve all `[[wikilinks]]` across every article and rebuild the backlink index.

```bash
coin link
```

**What happens:** Each `[[wikilink]]` is matched against existing wiki slugs.
Resolved pairs are stored as backlinks in the database so the graph view and
cross-article navigation work correctly.

**Output:** rows in `store/backlinks (DB)`

---

## Step 6 — Lint

Scan all wiki articles for contradictions, gaps, and stale content.

```bash
# Agent mode
coin lint

# Manual mode
coin lint --manual

# Apply findings from a web UI session
coin lint --apply path/to/findings.json
```

**What happens:** Agent mode runs deterministic structural checks over the
compiled wiki articles, such as missing references, very thin articles, and
unresolved `[[wikilinks]]`. Manual mode renders the LLM review prompt in
`coin/prompts/04_lint.md` for broader contradiction and gap review.

**Output:** `store/lint_findings (DB)`, printed as a table:

```
Kind              Article                                        Detail
contradiction     civilizational-collapse-and-complexity...     Claims X in para 2 but Y in para 5
gap               energy-return-on-investment                   Linked from 3 articles but never compiled
```

---

## Step 7 — Q&A

Ask a question against the compiled knowledge base.

```bash
coin ask "What is the complexity threshold Tainter describes?"

# Manual mode — prints the prompt to paste into Claude.ai or ChatGPT
coin ask --manual "What is the complexity threshold Tainter describes?"
```

**What happens:** The question is matched against the stored chunks via semantic
search. The current agent path returns the closest retrieved material with
source URLs. Manual mode renders the LLM prompt in `coin/prompts/05_qa.md` if
you want a synthesized cited answer.

**Example output:**

```
What is the complexity threshold Tainter describes?
───────────────────────────────────────────────────
Here is the closest material currently in the knowledge base:

[1] Tainter's thesis is that every civilization reaches a point where adding
more complexity — more administration, specialisation, or infrastructure —
yields diminishing marginal returns...

Confidence: high

Sources:
  • https://www.youtube.com/watch?v=hQLEu3ZIrYU
```

---

## Running steps 2–6 in one go

```bash
coin run
```

Runs embed → group → compile → link → lint end-to-end in agent mode.

---

## Watch mode

Set the pipeline to re-research a topic on a schedule:

```bash
# Add a topic — default cron is every Monday at 09:00
coin watch add "Civilizational collapse" --cron "0 9 * * 1"

# Run all watched topics immediately
coin watch run
```

---

## Export

```bash
coin export html      # self-contained HTML report  → ./export/
coin export pdf       # PDF                          → ./coin.pdf
coin export snapshot  # full-KB JSON snapshot        → ./coin-snapshot.json
```

---

## Full sequence at a glance

```bash
coin ingest --audio-subtitles 'https://www.youtube.com/watch?v=hQLEu3ZIrYU'
coin embed
coin group
coin compile
coin link
coin lint
coin ask "What is the complexity threshold Tainter describes?"
```
