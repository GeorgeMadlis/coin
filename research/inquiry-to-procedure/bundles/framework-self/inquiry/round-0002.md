---
type: Event
title: "Round 2: HTML inspection renderer"
description: Added a static HTML rendering path for manual inspection of the bundle.
fc-axis: INQUIRY
fc-round: 2
fc-move: evidence
fc-party: codex
fc-type-at-round: resolved
fc-touches: [_site/ (generated), bundles/README.md]
fc-status: open
timestamp: 2026-07-16
---

# Move

HTML rendering added for visual inspection.

# Evidence added

The repository now includes a static renderer at `tools/src/okf_fc/render.py` and a CLI entry point exposed as `okf-fc render`.

# Effect on state

The framework-self bundle can be inspected offline through the generated `_site/` directory without changing source Markdown content.

# Resulting revisions

None to content files.

# Classification rationale

This is an evidence move about inspection infrastructure. It does not revise bundle claims or adjudicate a disagreement.
