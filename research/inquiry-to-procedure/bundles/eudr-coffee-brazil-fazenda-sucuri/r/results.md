---
type: Finding
title: "Per-AOI results"
fc-level: 2
fc-axis: R
fc-round: 8
fc-supersedes: "r/results.md@round-0006"
gsp-provenance: pinned-not-reproduced
gsp-verdict-class: possible_relevant_deforestation
---
# Per-AOI results

| metric | value |
|---|---:|
| AOI area | 1722.07 ha |
| JRC 2020 forest baseline | 219.26 ha |
| post-2020 loss on JRC baseline | 23.77 ha |
| current configured coffee evidence | 482.28 ha |
| new coffee since baseline | 225.29 ha |
| current coffee/post-2020 loss overlap | 5.14 ha |
| new coffee/post-2020 loss overlap | 1.17 ha |
| FDP new coffee/post-2020 loss overlap | 1.17 ha |
| MapBiomas new coffee/post-2020 loss overlap | 0.0 ha |
| both-source agreement new coffee/post-2020 loss overlap | 0.0 ha |
| Hansen 10% canopy baseline | 95.48 ha |
| post-2020 loss on Hansen 10% canopy baseline | 5.98 ha |
| Hansen 10% baseline loss/current coffee overlap | 0.70 ha |

## FDP/JRC threshold sensitivity

The threshold values are task-specific diagnostics over the FDP Coffee Probability model 2026a. The
0.025 row is a permissive 2.5% model-probability diagnostic threshold, not verified parcel ground
truth.

| threshold | FDP 2020 coffee | FDP 2024 coffee | FDP new coffee | JRC2020 AND FDP2024 | JRC2020 AND FDP new coffee |
|---:|---:|---:|---:|---:|---:|
| 0.025 | 256.99 ha | 358.74 ha | 225.29 ha | 35.68 ha | 17.25 ha |
| 0.05 | 234.00 ha | 307.80 ha | 198.95 ha | 25.19 ha | 14.66 ha |
| 0.10 | 209.85 ha | 245.38 ha | 162.01 ha | 15.81 ha | 11.06 ha |
| 0.20 | 183.09 ha | 179.28 ha | 117.71 ha | 9.04 ha | 6.97 ha |
| 0.25 | 173.33 ha | 158.60 ha | 104.32 ha | 7.23 ha | 5.67 ha |

Between 0.025 and 0.25, `JRC2020 AND FDP new coffee` contracts from 17.25 ha to 5.67 ha, a 67.1%
decrease. `JRC2020 AND FDP2024` contracts from 35.68 ha to 7.23 ha, a 79.7% decrease.

## FDP/JRC morphology diagnostics

The morphology diagnostic is interpretive screening evidence. It cannot independently establish
post-2020 conversion, causation, illegality, or EUDR non-compliance.

At threshold 0.025:

| mask | total area | components | median component area | max component area | boundary-adjacency fraction | median bbox elongation | median compactness |
|---|---:|---:|---:|---:|---:|---:|---:|
| JRC2020 AND FDP2024 | 35.68 ha | 142 | 0.05 ha | 3.85 ha | 0.440303 | 1.500000 | 0.589049 |
| JRC2020 AND FDP new coffee | 17.25 ha | 150 | 0.03 ha | 2.14 ha | 0.540290 | 1.444444 | 0.669636 |

At threshold 0.25:

| mask | total area | components | median component area | max component area | boundary-adjacency fraction | median bbox elongation | median compactness |
|---|---:|---:|---:|---:|---:|---:|---:|
| JRC2020 AND FDP2024 | 7.23 ha | 71 | 0.04 ha | 1.10 ha | 0.601660 | 1.250000 | 0.620562 |
| JRC2020 AND FDP new coffee | 5.67 ha | 64 | 0.03 ha | 1.09 ha | 0.608466 | 1.291667 | 0.599957 |

The report.html conclusion is: "The morphology is mixed or inconclusive from shape metrics alone."
This records boundary/corridor-like and threshold-sensitive signals requiring human review, not a
confirmed broad/persistent forest-to-coffee transition.

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
