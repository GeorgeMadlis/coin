---
type: Round
fc-level: 3
fc-axis: INQUIRY
fc-round: 9
fc-move: fix
fc-stage: consolidation
fc-party: codex
fc-status: open
fc-touches:
  - index.md
  - log.md
  - inquiry/index.md
gsp-aoi: "fazenda_sucuri_screening_aoi"
---
# Round 0009 - Snapshot portability link fix

## Move

Fix parent-bundle links that rendered as relative paths escaping the published task snapshot.

## Evidence Added

- Acceptance audit of the published round-8 snapshot found two identical broken local links in
  root `index.html`: `../eudr-gee/index.md` resolved inside the portable published tree to a path
  that is not shipped with the Fazenda Sucuri snapshot.
- The snapshot is intended to be portable and self-contained. Parent-method lineage can be cited as
  a repository path without turning it into a broken local snapshot link.

## Effect On State

No evidence value, report artifact, hash, verdict, provenance class, contact-sheet layout, or
diagnostic semantics changes. The current state remains `possible_relevant_deforestation` /
`pinned-not-reproduced`, with report status `human_review_required`.

Parent method references are retained as non-clickable repository paths: `bundles/eudr-gee`.

## Resulting Revisions

- Root `index.md` is updated as a portability/navigation guide. It has no frontmatter in this
  bundle and carries no evidentiary claim beyond navigation/provenance context.

## Classification Rationale

**fc-stage: consolidation** - this round consolidates existing navigation content into the portable
publication contract. It does not add evidence or alter method semantics.
