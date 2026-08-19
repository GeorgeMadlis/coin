---
type: Round
fc-level: 3
fc-axis: INQUIRY
fc-round: 5
fc-move: fix
fc-stage: consolidation
fc-party: codex
fc-status: human_review_required
fc-touches:
  - pf/full-context.md
  - log.md
  - inquiry/index.md
gsp-aoi: "liberia_fmc_area_k_contract_boundary"
---
# Round 0005 - Observer terminology audit fix

## Move

Fix one remaining static-artifact observer wording found during the final publication audit.

## Evidence Added

- Prompt C observer/process terminology audit found that `pf/full-context.md` still described the
  Forest Atlas polygon as an "allocation observer".
- Parent method round 34 and this task's round 3 require static polygons and queried boundary files
  to be described as observation artifacts unless the relevant producing process/procedure is named.

## Effect On State

No evidence value, report artifact, hash, verdict, provenance class or production/source-linkage
gap changes. The current state remains `human_review_required` / `pinned-not-reproduced`.

The Forest Atlas FMC polygon is now described as an allocation-boundary observation artifact emitted
by an administrative publication/query process, preserving the process/artifact distinction.

## Resulting Revisions

- `pf/full-context.md` supersedes `pf/full-context.md@round-0001`.

## Classification Rationale

**fc-stage: consolidation** - this round consolidates the already-adopted observer/process ontology
into one missed current PF sentence. It does not add new AOI evidence or change the report package.
