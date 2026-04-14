# COIN · Step 4 of 5 — Lint the wiki for contradictions and gaps

## Instructions for the LLM (paste everything below this line into Claude.ai or ChatGPT)

---

You are reviewing the COIN (ConnectedInformation) wiki for structural issues, contradictions, missing context, and stale content.

I will give you the current set of articles. Your job is to return a JSON array of findings.

**Rules:**
- Prefer actionable findings over vague criticism.
- Only report issues that are visible in the provided articles.
- Use these finding kinds when possible: `contradiction`, `gap`, `stale_content`, `broken_wikilink`, `missing_context`.
- Return **only** the JSON array. No prose, no markdown fences.

**Required output format:**
```json
[
  {
    "kind": "gap",
    "article_slug": "soil-carbon",
    "detail": "The article mentions mycorrhizae but never explains their role in carbon storage."
  }
]
```

**Articles:**

{{ARTICLES}}
