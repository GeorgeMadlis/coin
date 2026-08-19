---
type: Round
fc-level: 3
fc-axis: INQUIRY
fc-round: 6
fc-move: fix
fc-stage: consolidation
fc-party: codex
fc-status: human_review_required
fc-touches:
  - index.md
  - reproduction/lineage.md
  - EUDR_WOOD_LIBERIA_FMC_AREA_K_BUNDLE_READING_GUIDE.md
  - log.md
  - inquiry/index.md
gsp-aoi: "liberia_fmc_area_k_contract_boundary"
---
# Round 0006 - Snapshot portability link fix

## Move

Fix source links that rendered as relative paths escaping the published task snapshot.

## Evidence Added

- Prompt C relative-link crawl of the published round-5 snapshot found three escaping Markdown
  links: the root `index.md` parent-bundle link and two `reproduction/lineage.md` links to parent
  `eudr-gee` rounds 30-31.
- The snapshot is intended to be portable and self-contained; parent lineage can be cited as a
  repository path without turning it into a broken local snapshot link.

## Effect On State

No evidence value, report artifact, hash, verdict, provenance class or remaining evidence gap
changes. The current state remains `human_review_required` / `pinned-not-reproduced`.

Parent method references are retained as non-clickable repository paths:
`bundles/eudr-gee`, `bundles/eudr-gee/inquiry/round-0030.md`, and
`bundles/eudr-gee/inquiry/round-0031.md`.

## Resulting Revisions

- `reproduction/lineage.md` supersedes `reproduction/lineage.md@round-0001`.
- Root `index.md` and the bundle-root reading guide are updated as portability/navigation guides;
  they carry no frontmatter in this bundle.

## Classification Rationale

**fc-stage: consolidation** - this round consolidates existing lineage/navigation content into the
portable publication contract. It does not add evidence or alter method semantics.
