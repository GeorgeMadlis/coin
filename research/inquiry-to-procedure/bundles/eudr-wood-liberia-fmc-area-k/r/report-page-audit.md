---
type: Finding
title: "Report page audit"
fc-level: 2
fc-axis: R
fc-round: 4
gsp-provenance: pinned-not-reproduced
gsp-aoi: "liberia_fmc_area_k_contract_boundary"
---
# Report Page Audit

The canonical report PDF hash is
`cb83898664221ffb851a2193403fbe0cd2069faeb3ab21327796ea2ebd1f81d5`; page count is `12`.
The canonical HTML hash is `a9c10dafadce5e28e1106ae549d5a14cbab58baa9f4c4a0d858f0f3cd44f1de3`.

| page | purpose | expected artifact/source | observed content | AOI/map/legend/metrics visible | visual QA status | limitation |
|---:|---|---|---|---|---|---|
| 1 | Report identity and AOI context | `evidence/08_cover_hero.png` and AOI boundary | Cover map with AOI boundary and potential post-2020 disturbance note. | AOI visible; no metric table expected. | accepted | Commodity label in report UI is `unspecified`; bundle frame supplies wood context. |
| 2 | Executive summary | report metrics from `metrics.csv` | Commodity/country/AOI/JRC-2020/post-2020-loss/review-status cards. | Metrics visible; no map expected. | accepted | Screening summary is not a legal conclusion. |
| 3 | Workflow | report model workflow section | AOI, JRC baseline, Hansen loss, optional commodity, intersection and evidence package steps. | No AOI map expected; workflow visible. | accepted | Generic report workflow still contains optional commodity-layer step, but no non-wood layer is used as wood attribution. |
| 4 | Regional overview | `evidence/07_regional_overview.png` | Liberia regional image with county labels and Area K AOI boundary. | AOI and legend visible; regional metrics visible. | accepted | Regional page is context, not production geometry. |
| 5 | Forest baseline 2020 | `evidence/02_jrc_forest_2020.png` | JRC 2020 forest baseline map over satellite context. | AOI, map, legend and `261,004.9 ha` metric visible. | accepted | JRC baseline is an observation artifact, not a legal forest determination. |
| 6 | Forest change/disturbance after 2020 | `evidence/03_forest_loss_2021_2025.png`, `13_tmf_deforestation_2021_2025.png`, `14_tmf_degradation_2021_2025.png`, `17_radd_alerts_confirmed_low_confidence.png` | Four-map comparison for Hansen/JRC loss, TMF deforestation, TMF degradation and RADD alerts. | AOI, maps, legend and headline areas visible. | accepted | Differing areas reflect process semantics and source definitions; they are not averaged. |
| 7 | Satellite visual context | `evidence/06_before_after.png` | Sentinel-2 before/after paired panel for 2020 and 2026. | AOI, map and date/provider table visible. | accepted | Visual context does not itself link a tree/log/shipment to a disturbance event. |
| 8 | Interpretation | report interpretation section | Potential post-2020 disturbance, Hansen/JRC, TMF, RADD, source-linkage gap and legal-boundary notes. | Metrics and review status visible; no map expected. | accepted | The page explicitly leaves compliance status unresolved. |
| 9 | Data and methods | report datasets/methods section | Forest baseline, forest loss, imagery, processing, spatial resolution, temporal scope and configured data. | Method records visible; no map expected. | accepted | Some configured-data records are generic report fields. |
| 10 | Audit trail | report audit fields | Report ID, run ID, generated time, cutoff/end year, CRS, bundle manifest and report version. | Audit table visible. | accepted | Audit trail records deterministic generation, not independent rerun. |
| 11 | Deterministic artifacts | report artifact list | report.json, report.html, report.pdf, metrics.csv, manifest and evidence maps. | Artifact rows visible. | accepted | Full hash inventory is in manifest/source-evidence, not all on the page. |
| 12 | Appendix | references, limitations and evidence gaps | EUDR, JRC, Hansen, Sentinel, TMF, RADD references and limitations/evidence gaps. | References and gaps visible. | accepted | Source authenticity and chain of custody remain unresolved. |

The HTML report was also inspected for local relative references: every map referenced by
`report.html` exists on disk. The embedded report data and map legend include mapped artifacts for
JRC forest 2020, Hansen/JRC loss, TMF deforestation, TMF degradation, RADD confirmed alerts and RADD
low-confidence alerts. These are mapped artifacts, not mere text mentions.
