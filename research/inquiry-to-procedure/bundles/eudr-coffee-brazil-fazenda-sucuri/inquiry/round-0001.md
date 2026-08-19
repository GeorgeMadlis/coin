---
type: Event
title: "Round 1: form Fazenda Sucuri task bundle"
fc-axis: INQUIRY
fc-round: 1
fc-move: formation
fc-stage: formation
fc-party: codex
fc-status: open
fc-touches: "bundle.json, answer.md, pf/*, s/*, r/*, reproduction/*, index.md, log.md, inquiry/index.md"
gsp-engine: gee
gsp-counterpart: single-earth/eudr-dmi-gil@b48bcbcbbf198d5eb7ff33ed3dfe3ebc7a06328e
---
# Move

Form `bundles/eudr-coffee-brazil-fazenda-sucuri/` as a task-specific child under `eudr-gee` for
AOI `fazenda_sucuri_screening_aoi`.

# Evidence added

- Counterpart evidence handoff:
  `/Users/server/projects/eudr-dmi-gil/out/okf_handoffs/eudr-coffee-brazil-fazenda-sucuri.json`.
- Counterpart commit:
  `single-earth/eudr-dmi-gil@b48bcbcbbf198d5eb7ff33ed3dfe3ebc7a06328e`, clean.
- Evidence bundle:
  `fazenda_sucuri_screening_aoi_evidence_freeze_20260811T094600Z`.
- Root manifest hash:
  `2ba7dc9786c6d85e8c42e32839367faca03cc6a8532c5ba94c074903607e2510`.
- Report PDF hash:
  `b5584c2e97edb92b598c3c70ad4ff699e49b35c902016eeacab8933dbd693f16`, 12 pages.
- Derived contact sheet:
  `reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf`.

# Result

The bundle records `possible_relevant_deforestation` / `pinned-not-reproduced`. The counterpart
report's status is `human_review_required`: post-2020 JRC-baseline loss is 23.85 ha, latest coffee
evidence is 242.46 ha, latest coffee/loss overlap is 0.45 ha, and new post-baseline coffee/loss
overlap is 0.27 ha. The new-conversion overlap is FDP-specific; MapBiomas and both-source-agreement
conversion overlap are both 0.0 ha.

# Classification rationale

**fc-stage: formation** - this round creates the task bundle, records its first pinned evidence
state, and applies existing sibling-history conventions without changing the parent method itself.
