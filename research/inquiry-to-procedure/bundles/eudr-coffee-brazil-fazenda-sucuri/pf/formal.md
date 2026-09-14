---
type: Claim
title: "Formal claim"
fc-level: 2
fc-axis: PF
fc-round: 8
fc-supersedes: "pf/formal.md@round-0006"
gsp-aoi: fazenda_sucuri_screening_aoi
---
# Formal claim

For AOI `fazenda_sucuri_screening_aoi`, compute:

- 2020 forest baseline from JRC GFC2020 V3.
- Post-2020 loss from Hansen lossyear through effective end year 2025.
- Coffee evidence from FDP and MapBiomas baseline/latest observations.
- Source-specific and both-source-agreement post-baseline coffee expansion.
- Current coffee as latest observed coffee plus baseline-year coffee, unless an explicit clearing
  layer proves baseline coffee was removed; this run has no such clearing layer.
- Task-specific FDP/JRC morphology and threshold sensitivity across 0.025, 0.05, 0.10, 0.20, and
  0.25, separating simple current co-location from FDP-new-coffee co-location.

The current claim is:

| condition | pinned value | implication |
|---|---:|---|
| JRC 2020 forest baseline | 219.26 ha | baseline forest exists inside AOI |
| post-2020 loss on JRC baseline | 23.77 ha | disturbance exists after the cutoff |
| all configured current coffee evidence | 482.28 ha | current commodity evidence exists inside AOI |
| post-2020 loss and any current coffee overlap | 5.14 ha | relevant screening overlap exists |
| post-2020 loss and new coffee overlap | 1.17 ha | source-specific new-conversion candidate |
| JRC2020 AND FDP new coffee at 0.025 | 17.25 ha | permissive FDP diagnostic co-location |
| JRC2020 AND FDP new coffee at 0.25 | 5.67 ha | threshold sensitivity remains positive but contracted |

The verdict is `possible_relevant_deforestation` / `pinned-not-reproduced`.
