# COIN · Manual prompt — Ingest and normalize a source

## Instructions for the LLM (paste everything below this line into Claude.ai or ChatGPT)

---

You are helping build a knowledge base called COIN (ConnectedInformation) for the ConnectedNature website.

I will give you one raw source. Your job is to normalize it into a clean JSON document that COIN can store and process.

**Rules:**
- Preserve the core meaning of the source. Do not invent facts.
- Extract a short, descriptive title.
- Clean obvious boilerplate, navigation, or repeated footer text.
- Keep the full useful body text in `content`.
- Return **only** a JSON object. No prose, no markdown fences.

**Required output format:**
```json
{
  "title": "Source title",
  "source_url": "https://example.com/original-source",
  "content": "Clean normalized text from the source"
}
```

**Raw source:**

{{RAW_SOURCE}}

---

Save the result into `artifacts/documents/NNNN_slug.json`, then continue with `coin/prompts/02_group.md`.
