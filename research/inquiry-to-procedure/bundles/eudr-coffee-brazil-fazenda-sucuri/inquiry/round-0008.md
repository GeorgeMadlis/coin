---
type: InquiryRound
title: "Round 8 - FDP/JRC morphology and threshold sensitivity"
fc-round: 8
fc-stage: enrichment
date: 2026-09-11
party: codex
move: enrichment
gsp-aoi: fazenda_sucuri_screening_aoi
gsp-verdict-class: possible_relevant_deforestation
gsp-provenance: pinned-not-reproduced
gsp-counterpart: single-earth/eudr-dmi-gil@d68e7ebbcc99fdff75742452538b241a382feb24
fc-touches: "answer.md, index.md, bundle.json, pf/formal.md, pf/full-context.md, s/overview.md, s/data-sources.md, s/modeling.md, s/gsp-mapping.md, s/specification.md, s/report-structure.md, r/overview.md, r/results.md, r/report-page-audit.md, r/artifact-inventory.md, reproduction/code.md, reproduction/data.md, reproduction/index.md, reproduction/source-evidence.json, reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf, reproduction/fazenda_sucuri_screening_aoi_contact_sheet.pdf.metadata.json, EUDR_COFFEE_BRAZIL_FAZENDA_SUCURI_BUNDLE_READING_GUIDE.md, fazenda_sucuri_contact_sheet_guide.html, log.md, inquiry/index.md"
---
# Round 8 - FDP/JRC morphology and threshold sensitivity

Scope classification: task-specific enrichment only. The authoritative counterpart gained reusable
machinery, but this handoff records Fazenda-Sucuri-specific interpretation and threshold
diagnostics. It does not change the parent `eudr-gee` method to require 0.025/0.05/0.10/0.20/0.25
diagnostics, nor does it globalize this AOI's shape interpretation.

Why this analysis was added:

- Visual inspection showed that JRC 2020 forest often forms narrow elongated corridors while FDP
  coffee forms broader agricultural units.
- Simple `JRC2020 AND FDP2024` co-location is insufficient to infer post-2020 conversion because
  it can include persistent/baseline coffee, boundary/corridor effects, and low-probability
  threshold artifacts.
- The diagnostic therefore separates `JRC2020 AND FDP2024` from
  `JRC2020 AND (FDP2024 minus FDP2020)`.

Verified handoff:

- Counterpart repository: `single-earth/eudr-dmi-gil`.
- Counterpart commit: `d68e7ebbcc99fdff75742452538b241a382feb24`.
- `counterpart_dirty: false`.
- Evidence bundle id: `fazenda_sucuri_screening_aoi_evidence_freeze_20260911T130900Z`.
- Root manifest SHA256: `a0cc46dc310751c082f659b3e9682218a45bc4fed92162503207e7a67aa65e6e`.
- Report PDF SHA256: `dc519f6bfb730c79368f03c43a7e07891e6724c5bc1764a081bb0131ec1734e7`.
- Report page count: 12.
- Verified artifact count: 117; required artifact count: 12.
- FDP asset/version: `projects/forestdatapartnership/assets/coffee/model_2026a`, version `2026a`.
- Threshold metrics CSV SHA256: `6c0d1790d09b115ba229c804b6551ef8402d4e339e1778f7ecf9a3b1a911dc39`.
- Morphology diagnostics JSON SHA256:
  `94f8627832221dd95d7779604a67a7b5817ee717669251036df496c0df8260e7`.

The framework's `tools.okf_gsp.verify_evidence_handoff` was run against the handoff and verified
the clean counterpart flag, root manifest hash, every manifest-declared artifact hash/size, report
PDF hash, and 12-page PDF count.

Threshold sensitivity:

| threshold | FDP 2020 coffee | FDP 2024 coffee | FDP new coffee | JRC2020 AND FDP2024 | JRC2020 AND FDP new coffee |
|---:|---:|---:|---:|---:|---:|
| 0.025 | 256.99 ha | 358.74 ha | 225.29 ha | 35.68 ha | 17.25 ha |
| 0.05 | 234.00 ha | 307.80 ha | 198.95 ha | 25.19 ha | 14.66 ha |
| 0.10 | 209.85 ha | 245.38 ha | 162.01 ha | 15.81 ha | 11.06 ha |
| 0.20 | 183.09 ha | 179.28 ha | 117.71 ha | 9.04 ha | 6.97 ha |
| 0.25 | 173.33 ha | 158.60 ha | 104.32 ha | 7.23 ha | 5.67 ha |

The 0.025 threshold is a permissive 2.5% FDP model-probability diagnostic threshold, not verified
parcel ground truth. `JRC2020 AND FDP new coffee` contracts from 17.25 ha at 0.025 to 5.67 ha at
0.25, a 67.1% decrease.

Shape and morphology:

- At 0.025, `JRC2020 AND FDP2024` totals 35.68 ha in 142 components; median component area is
  0.05 ha, max component area is 3.85 ha, boundary-adjacency fraction is 0.440303, and median
  bounding-box elongation is 1.500000.
- At 0.025, `JRC2020 AND FDP new coffee` totals 17.25 ha in 150 components; median component area
  is 0.03 ha, max component area is 2.14 ha, boundary-adjacency fraction is 0.540290, and median
  bounding-box elongation is 1.444444.
- At 0.25, `JRC2020 AND FDP new coffee` totals 5.67 ha in 64 components; median component area is
  0.03 ha, max component area is 1.09 ha, boundary-adjacency fraction is 0.608466, and median
  bounding-box elongation is 1.291667.

The report.html conclusion is: "The morphology is mixed or inconclusive from shape metrics alone."
The recorded interpretation is therefore threshold-sensitive and morphology-inconclusive. It has
some boundary/corridor-like signals, but not enough from shape metrics alone to reclassify the
evidence as a confirmed broad/persistent forest-to-coffee transition.

Verdict effect:

The verdict remains `possible_relevant_deforestation` / `pinned-not-reproduced`. The richer
morphology analysis changes the evidentiary interpretation/detail but not the verdict. Positive
overlap remains candidate/manual-review evidence and is not confirmed deforestation, confirmed
conversion, illegality, EUDR non-compliance, or causation.

Contact-sheet effect:

The canonical report PDF remains 12 pages. The contact sheet was regenerated from the new
`report.pdf` using `tools/pdf_contact_sheet.py` without changing the tool or adding a thirteenth
report page. The metadata records the unchanged structure: 3 columns, 4 rows, 14 pt margin, 4 pt
gutter, and source `page_count: 12`. Contact-sheet PDF SHA256:
`a68592de13ec8879bac692aadad04f153e758c762bf494821b8a205925670f77`.

Source authenticity:

Round 8 preserves the chain
provider observation -> acquired record -> checksum-pinned artifact -> computation ->
interpretation. Hash verification proves the acquired artifacts match the pinned handoff/manifest;
it does not prove that the remote FDP provider record is semantically correct. The metadata records
the FDP asset id and local raster checksum but no separate provider-side task receipt.

Supersedes ledger for current concept files:

- `answer.md@round-0006`
- `pf/formal.md@round-0006`
- `pf/full-context.md@round-0005`
- `s/overview.md@round-0007`
- `s/data-sources.md@round-0001`
- `s/modeling.md@round-0006`
- `s/gsp-mapping.md@round-0007`
- `s/specification.md@round-0007`
- `s/report-structure.md@round-0001`
- `r/overview.md@round-0006`
- `r/results.md@round-0006`
- `r/report-page-audit.md@round-0007`
- `r/artifact-inventory.md@round-0007`
- `reproduction/code.md@round-0007`
- `reproduction/data.md@round-0007`
