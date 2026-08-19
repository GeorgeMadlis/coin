---
type: Round
fc-level: 3
fc-axis: INQUIRY
fc-round: 3
fc-move: convention
fc-stage: consolidation
fc-party: codex
fc-touches:
  - agent-contract.md
  - s/task-scope.md
  - s/data-sources.md
  - s/gsp-mapping.md
  - s/modeling.md
  - log.md
  - inquiry/index.md
---
# Round 0003 - Observer/process terminology alignment

## Move

Align the current Liberia task pages with the parent method's round-34 observer/process ontology
audit. The task frame is unchanged; the round corrects current wording so boundary files, queried
polygons, rasters, alerts and Sentinel scenes are not called observers unless the relevant
observation-producing process or confirmation procedure is explicit.

## Evidence Added

- Parent method round: `../eudr-gee/inquiry/round-0034.md`.
- Parent framework pin:
  `observer-disagreement-framework@5670feba043e9fb75302f1a06a3c4e66d0eb90ca`.
- Current registry metadata:
  `../../inputs/liberia-eudr-wood-data-source-registry.json` now carries observation target,
  observer process/family, artifact role, upstream dependencies and independence notes for every
  source record.

## Effect On State

No Area K evidence value changes. The task remains `human_review_required` /
`pinned-not-reproduced`; report hashes, event counts, Tier-2 crops, production/source-linkage gaps
and the page-4 regional-view limitation are unchanged.

The current task contract and S-axis pages now say:

- the proxy agent observes a record of observations, not the Hansen/TMF/RADD/Sentinel/Forest Atlas
  process itself;
- the contract-reconstructed boundary and Forest Atlas FMC query output are boundary observation
  artifacts emitted by reconstruction/query processes;
- `wood_evidence_state.deforestation.observers` and `.degradation.observers` contain process/run
  labels, not static raster artifacts.

## Resulting Revisions

- `s/task-scope.md` supersedes `s/task-scope.md@round-0001`.
- `s/data-sources.md` supersedes `s/data-sources.md@round-0002`.
- `s/gsp-mapping.md` supersedes `s/gsp-mapping.md@round-0001`.
- `s/modeling.md` supersedes `s/modeling.md@round-0001`.
- `agent-contract.md` updated in place; it has no frontmatter round counter.
- `log.md` and `inquiry/index.md` append round 3.

## Classification Rationale

`fc-stage: consolidation` because this round adopts the parent method's corrected terminology as a
task-local convention without adding evidence, changing scope, or altering the verdict.
