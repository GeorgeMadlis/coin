---
type: Claim
title: "Formal claim"
fc-level: 2
fc-axis: PF
fc-round: 6
fc-supersedes: "pf/formal.md@round-0001"
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

The round-1 claim is:

| condition | pinned value | implication |
|---|---:|---|
| JRC 2020 forest baseline | 220.14 ha | baseline forest exists inside AOI |
| post-2020 loss on JRC baseline | 23.85 ha | disturbance exists after the cutoff |
| all configured current coffee evidence | 355.86 ha | baseline-year coffee is preserved in the current mask |
| post-2020 loss and any current coffee overlap | 1.08 ha | relevant screening overlap exists |
| post-2020 loss and new coffee overlap | 0.27 ha | source-specific new-conversion candidate |

The verdict is `possible_relevant_deforestation` / `pinned-not-reproduced`.
