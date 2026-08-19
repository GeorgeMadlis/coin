---
type: Finding
title: "Current evidence state"
fc-level: 2
fc-axis: R
fc-round: 8
fc-supersedes: r/results.md@round-0004
fc-status: human_review_required
gsp-provenance: pinned-not-reproduced
gsp-verdict-class: evidence_conflict_human_review_required
gsp-aoi: liberia_fmc_area_k_contract_boundary
---
# Current Evidence State

| field | value |
|---|---|
| Deforestation state | `detected_for_screening` |
| Degradation state | `detected_for_screening` |
| Production geometry role | `concession` |
| Production plot status | `unresolved` |
| Harvest/source linkage | `missing` |
| Legal-provenance context | `present/incomplete` |
| Manual review required | `true` |
| Legal conclusion | `not_evaluated` |
| Evidence bundle | `area-k-real-005` |
| Handoff SHA-256 | `1658fc3fde056d0a154f50dd8b36c78974185323115e863f766951920b50a142` |
| Report JSON SHA-256 | `5e67f0e069d97ebbb1a44c5ff6691df9888bb872dbfe94068cd70f90f2a05922` |
| Report HTML SHA-256 | `db115bf4829b98c6e0703d98e110929d05c6a84edc93859757ecc814f1e95a42` |
| Report PDF SHA-256 | `8a065c495ead890082948e48a0c913dae9c84de9ef02ddf4269d13dbad50ebc1` |
| Metrics CSV SHA-256 | `c890c51427d5c2024f9d0a5a8412791975b3a85852333d2057155b2d8e73c13c` |
| Bundle manifest SHA-256 | `bef58f2d0c372231d76e8b213eb929884f6acd60a8a01de476998fb78f457084` |
| Report page count | `12` |

## Metrics

| process family | metric | value |
|---|---|---:|
| JRC baseline | 2020 forest baseline inside AOI | `261,004.86 ha` |
| Hansen/JRC loss | post-2020 loss on JRC baseline | `10,914.48 ha` |
| Hansen canopy baseline | post-2020 loss on Hansen 10% canopy baseline | `11,216.61 ha` |
| TMF deforestation | 2021-2025 deforestation on JRC baseline | `5,386.32 ha` |
| TMF degradation | 2021-2025 degradation on JRC baseline | `7,088.13 ha` |
| RADD confirmed | confirmed/high-confidence alert area | `13,502.16 ha` |
| RADD low confidence | low-confidence alert area | `4,569.93 ha` |

These measured areas are evidence disagreement and different operational definitions. They are not
automatically contradictions: Hansen/JRC, TMF and RADD detect forest disturbance/change through
different source processes, sensors, spatial supports and class semantics.

## Explicit Gaps

- Area K Annual Operational Plan / Annual Harvesting Certificate geometry is not pinned.
- Harvesting-block geometry is missing.
- Tree/log source geometry is missing.
- Shipment-specific source linkage and chain-of-custody records are missing.
- Public machine-readable LLA parcel/cadastral geometry was not verified.
- No coffee, cocoa, palm, rubber or other non-wood commodity layer is treated as wood attribution.
- The evidence does not establish a particular harvesting block or production plot.
- The evidence does not link a shipment, tree or log to a detected event.

This is not an EUDR compliance or non-compliance finding.
