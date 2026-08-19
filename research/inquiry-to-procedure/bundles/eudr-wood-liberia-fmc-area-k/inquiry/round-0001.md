---
type: Event
title: "Round 1: form Liberia wood FMC Area K task bundle"
fc-axis: INQUIRY
fc-round: 1
fc-move: formation
fc-stage: formation
fc-party: codex
fc-status: underdetermined
fc-touches: "bundle.json, agent-contract.md, index.md, answer.md, pf/*, s/*, r/*, reproduction/*, inquiry/index.md, log.md"
gsp-aoi: "liberia_fmc_area_k_contract_boundary"
gsp-engine: gee
---
# Move

Form a new task-specific bundle for EUDR wood/timber evidence collection and screening in Liberia,
beginning with FMC Area K.

Earlier Liberia/wood work was initially recorded inside the broader `eudr-gee` method-family frame.
Those rounds remain immutable historical evidence. This formation round makes the task boundary
explicit: FMC Area K is concession-level screening and legal-provenance context, not a resolved
production plot and not a shipment/log chain-of-custody task.

# Evidence added

- Scope gate reading completed for `AGENTS.md`, `CLAUDE.md`, framework/spec docs, root and parent
  logs, `eudr-gee` rounds 30-31, Liberia input assessment/registry, and sibling task-bundle logs.
- Git history inspection found the Liberia parent records now resolved as rounds 30-31 and the two Liberia input files introduced in
  framework commit `cc729797d737a9ae9f3cb6f97123fc6fc0c25fc1`.
- Counterpart inspection found `GeorgeMadlis/eudr-dmi-gil@ac783345db5df54fb5656059fb70ab02a948e4ca`
  with a committed Liberia source-screening runner and Area K GeoJSON.
- Counterpart source-inventory handoff:
  `/Users/server/projects/eudr-dmi-gil/out/okf_handoffs/eudr-wood-liberia-fmc-area-k.json`,
  SHA-256 `ac4b29157a25fb8aff2414c54d995b8ad1f012d1d3fb442174c7c1b54fbd8985`.
- Counterpart manifest SHA-256:
  `7cb778d42d14ddfe18770d27367238dbffb257a55e95890ced9a51eeeaafb45b`.

# Effect on state

This bundle begins at round 1 because the observer deliberately selected a clearer task frame.
Legacy parent rounds are cited through `reproduction/lineage.md`; they are not moved, renumbered or
rewritten.

No AOI-level deforestation, degradation or source-of-origin determination is created. The current
state remains `underdetermined` / `UNVERIFIED` for a task-level screening conclusion.

# Resulting revisions

- Created `bundles/eudr-wood-liberia-fmc-area-k/`.
- Created `s/task-scope.md` with the Frame Declaration and scope-change protocol.
- Created `reproduction/lineage.md` mapping `eudr-gee` rounds 30-31.
- Created a bundle-root reading guide and a contact-sheet status guide.
- Recorded the absence of a contact-sheet PDF because no pinned report PDF exists in the clean
  handoff.

# Classification rationale

**fc-stage: formation** - this round forms the task frame itself. It records a scope/taxonomy
correction, not a software bug and not an evidence verdict.
