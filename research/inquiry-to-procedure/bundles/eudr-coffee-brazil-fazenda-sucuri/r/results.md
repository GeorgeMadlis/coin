---
type: Finding
title: "Per-AOI results"
fc-level: 2
fc-axis: R
fc-round: 6
fc-supersedes: "r/results.md@round-0001"
gsp-provenance: pinned-not-reproduced
gsp-verdict-class: possible_relevant_deforestation
---
# Per-AOI results

| metric | value |
|---|---:|
| AOI area | 1738.80 ha |
| JRC 2020 forest baseline | 220.14 ha |
| post-2020 loss on JRC baseline | 23.85 ha |
| current configured coffee evidence | 355.86 ha |
| new coffee since baseline | 137.88 ha |
| current coffee/post-2020 loss overlap | 1.08 ha |
| new coffee/post-2020 loss overlap | 0.27 ha |
| FDP new coffee/post-2020 loss overlap | 0.27 ha |
| MapBiomas new coffee/post-2020 loss overlap | 0.0 ha |
| both-source agreement new coffee/post-2020 loss overlap | 0.0 ha |

## Sentinel-2 scene depth

| situation | scene count | least-cloudy date | least-cloudy cloud % | mean valid obs/pixel | min valid obs/pixel |
|---|---:|---|---:|---:|---:|
| 2020 baseline | 30 | 2020-09-11 | 0.000931 | 21.221374 | 14 |
| 2025 recent | 37 | 2025-07-02 | 0.000388 | 26.448841 | 17 |

## Commodity temporal-mask check

The regenerated source masks satisfy the required temporal rule: `baseline_commodity_mask -
current_commodity_mask = 0`, and `current_commodity_mask - baseline_commodity_mask =
new_commodity_since_baseline`. The PDF labels the baseline coffee overlay as `Coffee plantations
(2020)` and the current overlay as `Coffee plantations (2024)`.
