---
type: Method
title: "Decision rules"
fc-level: 2
fc-axis: S
fc-round: 6
fc-supersedes: "s/modeling.md@round-0001"
---
# Decision rules

The counterpart report marks the AOI `human_review_required` when post-2020 baseline-forest loss is
detected with commodity-relevant evidence. For this formation round, the OKF verdict class is
`possible_relevant_deforestation` because:

- JRC-baseline post-2020 loss is 23.85 ha.
- Current configured coffee evidence covers 355.86 ha after preserving baseline-year coffee.
- Current coffee and post-2020 baseline loss overlap by 1.08 ha.
- New post-baseline coffee and post-2020 baseline loss overlap by 0.27 ha.

The temporal commodity-mask rule for this round is:

- baseline coffee = coffee plantations in 2020;
- current coffee = latest observed coffee (2024 for this bundle) OR baseline coffee, unless an
  explicit clearing/removal evidence layer proves baseline coffee was cleared;
- new coffee since baseline = latest observed coffee (2024) AND NOT baseline coffee.

The two-source evidence is not collapsed into a single undifferentiated commodity mask:

| evidentiary strength | new coffee area | post-2020 loss/new coffee overlap |
|---|---:|---:|
| FDP new coffee | 137.88 ha | 0.27 ha |
| FDP-only new coffee | 137.43 ha | 0.27 ha, as source-specific conversion |
| MapBiomas new coffee | 1.08 ha | 0.0 ha |
| MapBiomas-only new coffee | 0.63 ha | 0.0 ha |
| FDP and MapBiomas agreement | 0.45 ha | 0.0 ha |

This distinction is why the verdict is a human-review screening flag rather than a stronger
source-agreement conversion claim.
