---
type: Method
title: "Report structure"
fc-axis: S
fc-round: 8
gsp-aoi: liberia_fmc_area_k_contract_boundary
fc-supersedes: s/report-structure.md@round-0004
---
# Report Structure

The pinned canonical report `area-k-real-005` preserves the 12-page inspection contract:

| page | title | Liberia Area K content |
|---:|---|---|
| 1 | Cover | Evidence package identity, commodity `unspecified` in the report UI, Liberia geography and Area K AOI map. |
| 2 | Executive Summary | Evidence-only status, headline JRC/Hansen loss metrics and `Needs review` state. |
| 3 | Assessment Workflow | Deterministic AOI, baseline, Hansen loss, optional commodity, intersection and evidence-package workflow. |
| 4 | Regional Overview | Liberia regional context with county labels and AOI boundary. |
| 5 | Forest Baseline 2020 | JRC Global Forest Cover 2020 baseline map and baseline forest metric. |
| 6 | Forest Change / Disturbance After 2020 | Four-map comparison: Hansen/JRC loss, TMF deforestation, TMF degradation and RADD confirmed/low-confidence alerts. |
| 7 | Satellite Evidence | Sentinel-2 before/after visual context for 2020 and 2026. |
| 8 | Interpretation | Human-review interpretation, source-linkage gap and legal-boundary statement. |
| 9 | Data and Methods | Dataset, processing, spatial-resolution, temporal-scope and configured-data records. |
| 10 | Audit Trail | Report ID, run ID, commit/time records, cutoff and checksum references. |
| 11 | Deterministic Artifacts | Machine-readable report, HTML/PDF report, manifest, metrics and map artifacts. |
| 12 | Appendix | Reference sources, limitations, evidence gaps, assumptions and methodology/version fields. |

The structure is inspectable in both `report.pdf` and `report.html`. Page 6 is the wood-specific
multi-source comparison page: it does not substitute a coffee/cocoa/palm/rubber layer for wood
attribution, and it does not merge TMF degradation or RADD alert areas into a single deforestation
truth value.
