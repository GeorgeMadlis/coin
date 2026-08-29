# COIN · Manual prompt — Compile a wiki article

## Instructions for the LLM (paste everything below this line into Claude.ai or ChatGPT)

---

You are helping build a knowledge base called COIN (ConnectedInformation) for the ConnectedNature website.

I will give you a topic label and the source chunks that belong to it. Your job is to write a wiki article in Markdown.

**Rules:**
- Write in clear, authoritative prose. No bullet-point dumps.
- Use `[[wikilinks]]` for related concepts that deserve their own article (e.g. `[[Mycorrhizal Networks]]`, `[[Soil Carbon]]`). Do not wikilink every noun — only concepts central enough to warrant a dedicated article.
- Add inline citations as `[^1]`, `[^2]`, etc. with a `## References` section at the end listing each source URL.
- If an existing article is provided, **update and expand it** rather than rewriting from scratch. Preserve any `<!-- manual -->...<!-- /manual -->` blocks verbatim.
- Do not invent facts not present in the sources.
- Target length: 400–1200 words depending on the depth of the sources.

**Article front matter:**
```yaml
---
title: <topic label>
slug: <kebab-case version of the title>
compiled_at: <today's date ISO>
sources: [<list of source URLs>]
---
```

**Topic:** {{TOPIC_LABEL}}

**Existing article (if any — update this):**
{{EXISTING_ARTICLE}}

**Source chunks:**
{{SOURCE_CHUNKS}}

---

Once you have the Markdown, save it to `wiki/{{SLUG}}.md`, then either:
- Continue with the next topic using this same prompt, or
- Run `coin link` to resolve all wikilinks automatically.
