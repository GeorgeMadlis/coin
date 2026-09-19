---
type: InquiryRound
title: "Round 10 - provenance audit of the morphology trigger"
fc-level: 3
fc-axis: INQUIRY
fc-round: 10
fc-move: contestation
fc-stage: contestation
fc-party: codex
fc-status: open
date: 2026-09-19
gsp-aoi: fazenda_sucuri_screening_aoi
gsp-verdict-class: possible_relevant_deforestation
gsp-provenance: pinned-not-reproduced
fc-touches: "answer.md, pf/full-context.md, s/modeling.md, r/overview.md, r/results.md, log.md, inquiry/index.md"
---
# Round 10 - provenance audit of the morphology trigger

## Move

Contest the origin claim embedded in round 8's motivation without rewriting round 8. Separate the
verified target execution from the underdetermined origin of the task-forming visual observation.

## Evidence added

### AOI identity

The rectangle `[-46.775, -19.26, -46.745, -19.23]` is not Fazenda Sucuri. The August 12 snapshot
`eudr-coffee-brazil-minas-gerais-eudr-compliant/2026-08-12-r0008-c0ec8b7` preserves that exact
polygon in `evidence-package/inputs/aoi.geojson` (SHA-256
`78dfab852ee5697ed150ca53da044c9b93b1bcd0de57d46fd61d868254d1982d`). Its inspected 12-page
contact sheet has SHA-256
`4ba01fdb1c4dcb01b89aa34a09b99b4d75e469045506721f8d041a54d1584992`. The later formal
`coffee_brazil_ibia_patrocinio_mg` input has byte-different metadata but exactly the same coordinate
array and identifies the region as Ibiá / Patrocínio border, municipality Serra do Salitre, Minas
Gerais. Fazenda Sucuri is a different Coromandel screening polygon around
`(-46.8977, -18.5178)`.

### Retrospective image inspection

On 2026-09-19, direct inspection found narrow, branching JRC-forest structures and broader
agricultural units in the earlier Minas Gerais / Ibiá–Patrocínio imagery. This is retrospective
visual compatibility, not evidence that the historical observer used those images to form the
September task.

The artifact roles also matter:

- The named August 12 compliant snapshot's page 6 and method page identify its commodity layer as
  `Coffee plantations (2023)` from MapBiomas, not FDP. Its relevant hashes are
  `02_jrc_forest_2020.png = c5473b03ac85f1c8f9332d772e15ac95fbd0b63730be669913aa0a94839fd74e`
  and
  `04_commodity_layer.png = d636bbfd38ac29cff14089000ba7ce97619ef4e669d8019b3522562c029891fb`.
- A separate August 11 Ibiá / Patrocínio inspection snapshot over the identical geometry identifies
  its commodity layer as FDP Coffee Probability model 2025b at threshold 0.25. Its relevant hashes
  are
  `02_jrc_forest_2020.png = 011eb81f8e0af6a39b93321e4e1e2cc311c3e21bf0e50439aaa28f7b474096c0`
  and
  `04_commodity_layer.png = efc3b9fc3db0978f0dc4767777a504c337c2f57f14b9cbfc3082f402e426ad2b`.

The distinction prevents the visually similar MapBiomas snapshot from being retroactively described
as an FDP observation.

### Surviving chronology

| time | surviving event | provenance implication |
|---|---|---|
| 2026-08-11/12 | Ibiá / Patrocínio and compliant-Minas imagery exists over the identical rectangle | Earlier compatible artifacts exist; no task-transfer link is recorded. |
| 2026-09-10 17:28 +03:00 | `geospatial-evidence-framework@8a6992c` records a JRC/Hansen `treecover2000 >=10%` diagnostic | This is a different JRC/Hansen conditioning question, not an FDP morphology trigger. |
| 2026-09-11 15:54 +03:00 | Retained implementation prompt, SHA-256 `a2fd7f375480a4aad081851307a3d651e6089f592c0466bdce4664cb9f3a0156`, first carries the exact corridor-versus-broad-unit wording and attributes it to Sucuri | This proves recorded attribution at task formation, not the underlying observation event. |
| 2026-09-11 16:08 +03:00 | `eudr-dmi-gil@d68e7eb` commits the FDP/JRC diagnostic implementation | P1 target execution is established. |
| 2026-09-11 16:30 +03:00 | Retained framework-recording prompt, SHA-256 `a4c156004c10ea2eab0402f9464dc8363e114bc49e4f3db2faf22e59feea4625`, repeats the Sucuri attribution | The assertion is propagated into the bundle instruction. |
| 2026-09-11 16:45 +03:00 | `geospatial-evidence-framework@898a192` records Sucuri round 8 | Round 8 accurately records the instructed attribution and the executed result. |

Targeted search found no earlier retained occurrence of the exact corridor/broad-unit wording and no
historical `VIS_THRESHOLD` variable or instruction. `VIS_THRESHOLD` first appears in the 2026-09-19
audit request. Therefore it cannot be used to bridge the August images to the September task.
The two prompt files are locally retained audit inputs identified by checksum; they are not copied
into this public source bundle. Their content supports this local reconstruction but is not upgraded
to a publicly packaged primary artifact.

## Proposition findings

- **P1: the diagnostic was executed on Sucuri — verified.** The implementation commit, clean
  handoff, evidence package, threshold table, morphology metrics, and round-8 record agree.
- **P2: the observation originated on Sucuri — underdetermined.** The retained task instruction
  asserts Sucuri, while older Ibiá / Patrocínio imagery is compatible with the observation. Neither
  is a retained record of the originating inspection, and no artifact establishes transfer.

The audit therefore does **not** confirm that the observation originated on Minas Gerais / Ibiá–
Patrocínio, and it does **not** confirm that it originated on Sucuri. Chronological precedence plus
visual similarity is insufficient to choose between those accounts.

## Effect on state

Round 8 remains immutable. Its numerical diagnostic and conclusion remain valid for the Sucuri
target. Its phrase "Visual inspection showed..." must now be cited as a recorded motivation
attribution, not as verified provenance of where the observation was first made.

No retrospective Ibiá / Patrocínio round is added because doing so would convert a plausible origin
into an unsupported historical claim. No metric, report artifact, evidence hash, provenance class,
screening verdict, or legal interpretation changes. Current state remains
`possible_relevant_deforestation` / `pinned-not-reproduced`, with human review required.

## Resulting revisions

- `answer.md` states the P1/P2 distinction at L0.
- `pf/full-context.md` corrects current explanatory wording while retaining round 8 as history.
- `s/modeling.md` separates execution provenance from task-formation provenance.
- `r/overview.md` and `r/results.md` record the underdetermined origin finding and its no-metric-
  change boundary.
- The bundle and repository ledgers append this contestation round.

Supersedes ledger for current concept files:

- `answer.md@round-0008`
- `pf/full-context.md@round-0008`
- `s/modeling.md@round-0008`
- `r/overview.md@round-0008`
- `r/results.md@round-0008`

## Classification rationale

**fc-stage: contestation.** The round challenges a provenance attribution in an earlier round,
preserves the earlier record, evaluates discriminating evidence, and retains the origin question as
underdetermined rather than manufacturing a supersession that the evidence cannot support.
