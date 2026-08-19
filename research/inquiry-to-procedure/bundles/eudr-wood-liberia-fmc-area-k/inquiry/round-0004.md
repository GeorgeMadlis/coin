---
type: Round
fc-level: 3
fc-axis: INQUIRY
fc-round: 4
fc-move: enrichment
fc-stage: enrichment
fc-party: codex
fc-status: human_review_required
fc-touches:
  - answer.md
  - bundle.json
  - index.md
  - s/index.md
  - s/task-scope.md
  - s/overview.md
  - s/data-sources.md
  - s/gsp-mapping.md
  - s/modeling.md
  - s/specification.md
  - s/report-structure.md
  - r/index.md
  - r/overview.md
  - r/results.md
  - r/artifact-inventory.md
  - r/report-page-audit.md
  - reproduction/index.md
  - reproduction/code.md
  - reproduction/data.md
  - reproduction/environment.md
  - reproduction/gee-auth.md
  - reproduction/source-evidence.json
  - reproduction/contact-sheet-status.md
  - reproduction/liberia_fmc_area_k_contact_sheet.pdf
  - reproduction/liberia_fmc_area_k_contact_sheet.pdf.metadata.json
  - EUDR_WOOD_LIBERIA_FMC_AREA_K_BUNDLE_READING_GUIDE.md
  - liberia_fmc_area_k_contact_sheet_guide.html
  - log.md
  - inquiry/index.md
gsp-aoi: "liberia_fmc_area_k_contract_boundary"
---
# Round 0004 - Verified multi-source report integration

## Move

Integrate the verified Prompt-A multi-source report package `area-k-real-004` as the current
Liberia FMC Area K evidence state, add the missing report-structure and report-page-audit concepts,
regenerate the contact sheet from the new canonical PDF, and refresh local inspection guides.

## Evidence Added

- Counterpart HEAD and handoff commit:
  `single-earth/eudr-dmi-gil@696ca85e4fce3c09211653845dced273b8e9e511`.
- Counterpart tracked tree: clean; untracked derived outputs remain non-canonical.
- Handoff:
  `/Users/server/projects/eudr-dmi-gil/out/okf_handoffs/eudr-wood-liberia-fmc-area-k.json`,
  SHA-256 `9a1ee6880ae917fe88461647af1ebc69f15bbda581809612ebbda04c6798a58f`.
- Evidence bundle: `area-k-real-004`.
- Root evidence manifest SHA-256:
  `7ed8576b22eb006eeda91311a332085220ce74c63a9626b8feaa333a0274f0c3`.
- Report JSON/HTML/PDF SHA-256:
  `bdabbec99b63e014ad15b429586842ab80338f6403d12e66036d4b4224b21a2b`,
  `a9c10dafadce5e28e1106ae549d5a14cbab58baa9f4c4a0d858f0f3cd44f1de3`,
  `cb83898664221ffb851a2193403fbe0cd2069faeb3ab21327796ea2ebd1f81d5`.
- Metrics CSV SHA-256:
  `0128a66e65523bc103077c10a6d6345717173488350cfc690a5dc38d9664b4c5`.
- Report page count: `12`; all 52 manifest-declared artifacts were hash-verified by the
  framework handoff verifier using the counterpart virtualenv.
- Canonical AOI hash:
  `db386f478d9b461418155cb5db4ed9bd70d26d0b554786d61e76aad6280a210b`.
- Dataset/source pins include JRC GFC2020 V3, Hansen GFC v1.13 through 2025, JRC TMF v1_2025,
  RADD `projects/radar-wur/raddalert/v1` frozen at `2026-08-15T09:12:17Z`, and Sentinel-2 L2A
  visual-context rasters.
- Report HTML references resolve locally; mapped artifacts are present for JRC forest 2020,
  Hansen/JRC loss, TMF deforestation, TMF degradation, RADD confirmed alerts and RADD
  low-confidence alerts.
- Report PDF pages 5-8 and the regenerated contact sheet were rendered and visually inspected.
  Page 6 visibly contains Hansen/JRC, TMF deforestation, TMF degradation and RADD comparison maps.
- Contact sheet:
  `reproduction/liberia_fmc_area_k_contact_sheet.pdf`, SHA-256
  `3135ab23fe592bf13d66600568554f9b145a503cf67fa1efdfebcc307dbc8e53`.

## Effect On State

The current evidence state remains `human_review_required` / `pinned-not-reproduced`, but current
provenance and inspection records now point to the latest verified `area-k-real-004` package rather
than the earlier `area-k-real-003` package.

Canonical metrics from the handoff/report:

| process family | value |
|---|---:|
| JRC forest baseline 2020 | `261,004.86 ha` |
| Hansen/JRC post-2020 loss | `10,914.48 ha` |
| Hansen 10% canopy baseline post-2020 loss | `11,216.61 ha` |
| TMF deforestation 2021-2025 | `5,386.32 ha` |
| TMF degradation 2021-2025 | `7,088.13 ha` |
| RADD confirmed alert area | `13,502.16 ha` |
| RADD low-confidence alert area | `4,569.93 ha` |

These are not treated as contradictions or averaged into one truth value. Hansen/JRC, TMF and RADD
detect forest disturbance/change by different processes with different operational definitions. The
evidence does not establish a harvesting block, production plot, shipment/tree/log source linkage,
chain of custody, or legal compliance/non-compliance determination. No coffee, cocoa, palm, rubber
or other non-wood commodity layer is treated as wood attribution, and missing source linkage is not
converted into a zero.

Compared with the previous Area K evidence package, the headline metrics are unchanged, but the
canonical report package, hashes, counterpart commit/repository field, root manifest hash and
contact-sheet hash are refreshed. The report now has explicit current-page audit and report
structure concepts in the source bundle.

## Resulting Revisions

- `answer.md` supersedes `answer.md@round-0002`.
- `r/overview.md` supersedes `r/overview.md@round-0002`.
- `r/results.md` supersedes `r/results.md@round-0002`.
- `r/artifact-inventory.md` supersedes `r/artifact-inventory.md@round-0002`.
- `r/index.md` supersedes `r/index.md@round-0001`.
- `s/index.md` supersedes `s/index.md@round-0001`.
- `s/task-scope.md` supersedes `s/task-scope.md@round-0003`.
- `s/overview.md` supersedes `s/overview.md@round-0001`.
- `s/data-sources.md` supersedes `s/data-sources.md@round-0003`.
- `s/gsp-mapping.md` supersedes `s/gsp-mapping.md@round-0003`.
- `s/modeling.md` supersedes `s/modeling.md@round-0003`.
- `s/specification.md` supersedes `s/specification.md@round-0001`.
- `reproduction/index.md` supersedes `reproduction/index.md@round-0001`.
- `reproduction/code.md` supersedes `reproduction/code.md@round-0002`.
- `reproduction/data.md` supersedes `reproduction/data.md@round-0002`.
- `reproduction/environment.md` supersedes `reproduction/environment.md@round-0001`.
- `reproduction/gee-auth.md` supersedes `reproduction/gee-auth.md@round-0001`.
- `reproduction/contact-sheet-status.md` supersedes `reproduction/contact-sheet-status.md@round-0002`.
- Created `s/report-structure.md`.
- Created `r/report-page-audit.md`.
- Replaced `reproduction/source-evidence.json` with a compact round-4 provenance record.
- Regenerated `reproduction/liberia_fmc_area_k_contact_sheet.pdf` and metadata.
- Updated the bundle reading guide and local contact-sheet guide.
- Appended `log.md` and `inquiry/index.md`.

## Classification Rationale

`fc-stage: enrichment` because this round adds canonical report integration, inspection concepts and
verified evidence references inside the existing Liberia FMC Area K task frame. It does not change
the task identity, parent method contract or wood evidence-state vocabulary.
