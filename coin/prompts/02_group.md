# COIN · Step 2 of 5 — Group documents into topics

## Instructions for the LLM (paste everything below this line into Claude.ai or ChatGPT)

---

You are helping build a knowledge base called COIN (ConnectedInformation) for the ConnectedNature website.

I will give you a list of documents that have been ingested. Your job is to group them into coherent topic clusters so that each cluster can become one wiki article.

**Rules:**
- Each group label must be 2–4 words, title-case (e.g. "Soil Carbon Cycling", "Mycorrhizal Networks", "Forest Succession").
- A document can belong to only one group.
- Aim for groups of 2–8 documents. If a document stands clearly alone, give it its own group.
- Do not invent topics that are not represented in the documents.
- Return **only** the JSON object below — no prose, no markdown code fences, no explanation.

**Required output format:**
```
{
  "groups": [
    { "label": "Topic Label", "doc_ids": [1, 4, 7] },
    { "label": "Another Topic", "doc_ids": [2, 3] }
  ]
}
```

**Documents to group:**

{{DOCUMENT_SUMMARIES}}

---

Once you have the JSON, save it to `artifacts/groups.json`, then run:
```bash
coin group --apply artifacts/groups.json
```
to move to the next step, or proceed manually to `coin/prompts/03_compile.md`.
