---
type: Claim
title: "Full context"
fc-level: 3
fc-axis: PF
fc-round: 10
fc-supersedes: "pf/full-context.md@round-0008"
gsp-aoi: fazenda_sucuri_screening_aoi
---
# Full context

This bundle is a screening record, not a DDS submission and not a legal finding. It preserves the
counterpart report's human-review posture because the strongest new-conversion signal is FDP-only:
FDP new coffee overlaps post-2020 JRC-baseline loss by 1.17 ha, MapBiomas new coffee overlaps by
0.0 ha, and both-source-agreement new coffee overlaps by 0.0 ha.

Round 8 records a task-specific FDP/JRC morphology and threshold-sensitivity diagnostic. Its
historical motivation sentence attributes the corridor-versus-broad-unit observation to Fazenda
Sucuri. Round 10 leaves that historical record intact but separates two propositions: the diagnostic
was executed on Sucuri, which is verified; the visual observation originated on Sucuri, which the
surviving record cannot establish. Earlier imagery over the identical Minas Gerais / Ibiá–Patrocínio
rectangle is retrospectively compatible with the hypothesis, but coexistence and chronological
precedence do not prove transfer into the Sucuri task. Observation origin is therefore
underdetermined.

The current method distinction remains valid independently of that unresolved origin. It separates
`JRC2020 AND FDP2024` from `JRC2020 AND (FDP2024 minus FDP2020)` and treats
0.025/0.05/0.10/0.20/0.25 as diagnostic thresholds for this AOI, not as global parent-method rules.

PF edge case: the AOI is an approximate screening polygon reconstructed from a published centre and
property-area description, not a cadastral farm boundary. Spatial attribution must therefore be read
as "within this screening polygon" only; the bundle does not assert that any detected loss or coffee
signal is inside a legally surveyed Fazenda Sucuri parcel.

The method-family visual-acceptance history in `../eudr-gee/log.md` rounds 9-20 and 24-26 applies
at formation. The pinned report keeps the AOI extent bounded with a documented buffer, renders
only available legend rows/layers, uses high-contrast commodity colors, preserves no-letterbox
rendering for report surfaces, and records the omitted empty both-source-agreement conversion layer
instead of fabricating an image for it.

The AOI geometry hash is preserved beside report outputs in
`reports/aoi_report_v2/fazenda_sucuri_screening_aoi/aoi_config_hash.json`:
`59f53c1d0ca30b55b3b4a8af5cb9761841cb9a3a2ffafb38b7c4dce2f8879f88`.
