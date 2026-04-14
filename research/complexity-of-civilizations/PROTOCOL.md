# Research Protocol — Complexity of Civilizations

**Slug**: complexity-of-civilizations  
**Started**: 2026-04-14  
**Status**: active  
**Source**: https://www.youtube.com/watch?v=hQLEu3ZIrYU

---

## Stage 1 — Author & claim extraction

**Input**: `raw/transcript.md`  
**Output**: `authors.md`, `claims.md`

Read `raw/transcript.md` in full. Then:

1. Extract every named person (author, researcher, historian, scientist) mentioned,
   whether quoted, cited, or implied.
2. For each person, note: name, discipline (if stated), and the specific claim or
   idea attributed to them in the text.
3. List any unnamed claims asserted as fact (e.g. "studies show…", "evidence
   suggests…") — flag these as *unsourced assertions* for Stage 2 follow-up.
4. Write results to `authors.md` using this structure per entry:

   ```
   ## Firstname Lastname
   - **Discipline**: …
   - **Claim in source**: …
   - **Works to investigate**: (leave blank — filled by Stage 2)
   - **URLs**: (leave blank — filled by Stage 2)
   ```

5. Write all major factual claims (including unsourced ones) to `claims.md`,
   one claim per line, prefixed with the author name or `[unsourced]`.

Ignore music/sound cues, filler phrases, and formatting artifacts in the
transcript (e.g. `>> [music] >>`, `[^1]` footnote markers).

---

## Stage 2 — Works discovery

**Input**: `authors.md`  
**Output**: `authors.md` (updated in-place)

For each author in `authors.md`:

1. Web-search: `{Firstname Lastname} major works {discipline}`
2. Web-search: `{Firstname Lastname} publications complexity collapse` (adjust
   keywords to complexity of civilizations)
3. For each work found that is relevant to Complexity of Civilizations, record:
   - Title, year, publisher
   - URL (direct link preferred; Google Scholar, JSTOR, publisher page, or
     author's homepage as fallback)
   - Access status: `open` / `paywalled` / `archive.org` / `unknown`
4. Update the `authors.md` entry in-place.

For unsourced assertions in `claims.md`, web-search the claim text to find
the likely source. Add any identified author/work to `authors.md`.

---

## Stage 3 — Source reading

**Input**: `authors.md` (URLs column)  
**Output**: `sources/{author-slug}.md` per source

For each URL with access status `open` or `archive.org`:

1. Fetch the URL.
2. Extract the core argument in ≤500 words.
3. List 3–5 key claims or findings, as direct paraphrases.
4. Note the methodology used (empirical, comparative, theoretical, etc.).
5. Save to `sources/{firstname-lastname}.md`.

For paywalled or inaccessible sources:
- Note access status at top of the file.
- Use the abstract or any freely available excerpt only.
- Flag explicitly: `[Full text not retrieved — abstract only]`

Do not fabricate content for sources you cannot access. Mark gaps honestly.

---

## Stage 3.5 — Human review checkpoint  *(manual step)*

Before running Stage 4, review `sources/` and flag:

- Which sources were fully retrieved vs. abstract-only.
- Any source that seems central but was missed entirely.
- Whether the source coverage is sufficient to evaluate the claims in
  `claims.md` fairly.

Add a `## Coverage notes` section to `claims.md` summarising gaps.

---

## Stage 4 — Critical overview

**Input**: `raw/transcript.md`, `claims.md`, `authors.md`, `sources/*.md`  
**Output**: `critical-overview.md`

Write a structured critical analysis with these sections:

### 4.1 Source text summary
2–3 paragraphs summarising the overall argument of `raw/transcript.md`.

### 4.2 Claim-by-claim evaluation
For each claim in `claims.md`:
- State the claim.
- Evaluate against retrieved sources: **well-supported / oversimplified /
  contested / unverified**.
- Cite the specific source(s) that support or challenge it.
- Note if the claim could not be evaluated due to missing sources.

### 4.3 Broader context
What does the literature suggest that the source text *omits* or
*underweights*? What are the significant counterarguments?

### 4.4 Confidence rating
Overall: how well does the source text represent the scholarly literature?
Scale: `high / moderate / low / mixed`. Justify briefly.

### 4.5 Recommended reading
3–5 sources from `authors.md` a reader should prioritise, with one-sentence
rationale per item.

---

## Invocation guide (Claude Code)

Run stages individually by pasting one of these prompts into Claude Code:

```
Execute Stage 1 of research/complexity-of-civilizations/PROTOCOL.md
Execute Stage 2 of research/complexity-of-civilizations/PROTOCOL.md
Execute Stage 3 of research/complexity-of-civilizations/PROTOCOL.md
Execute Stage 4 of research/complexity-of-civilizations/PROTOCOL.md
```

After each stage, commit the outputs before proceeding:
`git add research/complexity-of-civilizations/ && git commit -m "stage-N: complexity-of-civilizations"`
