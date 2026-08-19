---
type: Event
title: "Round 9: metadata repair for round 8"
description: "Metadata repair: quoted round-0008 description frontmatter so YAML parsing preserves its fc-round and snapshot/catalog generation sees bundle round 8."
fc-axis: INQUIRY
fc-round: 9
fc-move: evidence
fc-stage: enrichment
fc-party: codex
fc-touches: [inquiry/round-0008.md]
fc-status: open
timestamp: 2026-07-20
---

# Move

The first round-scope policy commit left `inquiry/round-0008.md` with an unquoted colon in the YAML frontmatter description. YAML parsing therefore treated the frontmatter as invalid, so `okf-fc publish` could not see `fc-round: 8` and incorrectly proposed another `r0007` snapshot.

# Evidence added

The `description` value in `inquiry/round-0008.md` is now quoted, preserving the existing prose while making the frontmatter valid YAML.

# Effect on state

Context window: added the failed publish attempt as evidence that malformed round metadata can hide an otherwise present bundle round from generated manifests and catalogs.

Frame: unchanged. The two-counter model from round 8 remains adopted.

# Resulting revisions

- `inquiry/round-0008.md` — metadata repair only: quoted the `description` scalar so `fc-round`, `fc-stage`, and related fields parse correctly.
- `tools/tests/test_render.py` — adds a regression check that all committed `framework-self` inquiry round files parse with integer `fc-round` metadata.

# Classification rationale

This is an enrichment-stage evidence round: it adds a mechanical metadata repair and a regression check, with no live counter-position. `fc-type-at-round` is intentionally omitted.
