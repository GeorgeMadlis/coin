---
type: Method
title: "Decision rules"
fc-level: 2
fc-axis: S
fc-round: 10
fc-supersedes: "s/modeling.md@round-0008"
---
# Decision rules

The counterpart report marks the AOI `human_review_required` when post-2020 baseline-forest loss is
detected with commodity-relevant evidence. For the current round, the OKF verdict class is
`possible_relevant_deforestation` because:

- JRC-baseline post-2020 loss is 23.77 ha.
- Current configured coffee evidence covers 482.28 ha.
- Current coffee and post-2020 baseline loss overlap by 5.14 ha.
- New post-baseline coffee and post-2020 baseline loss overlap by 1.17 ha.

The temporal commodity-mask rule for this round is:

- baseline coffee = coffee plantations in 2020;
- current coffee = latest observed coffee (2024 for this bundle) OR baseline coffee, unless an
  explicit clearing/removal evidence layer proves baseline coffee was cleared;
- new coffee since baseline = latest observed coffee (2024) AND NOT baseline coffee.

The two-source evidence is not collapsed into a single undifferentiated commodity mask:

| evidentiary strength | new coffee area | post-2020 loss/new coffee overlap |
|---|---:|---:|
| FDP new coffee | 225.29 ha | 1.17 ha |
| FDP-only new coffee | 224.86 ha | 1.17 ha, as source-specific conversion |
| MapBiomas new coffee | 1.04 ha | 0.0 ha |
| MapBiomas-only new coffee | 0.61 ha | 0.0 ha |
| FDP and MapBiomas agreement | 0.43 ha | 0.0 ha |

This distinction is why the verdict is a human-review screening flag rather than a stronger
source-agreement conversion claim.

Round 8 adds a task-specific FDP/JRC diagnostic distinction that is not globalized to the parent
method:

- `JRC2020 AND FDP2024` is spatial co-location between the JRC 2020 forest mask and the current FDP
  coffee-probability mask.
- `JRC2020 AND (FDP2024 minus FDP2020)` is spatial co-location between JRC 2020 forest and pixels
  newly admitted by FDP since the 2020 baseline year at the same probability threshold.

Simple `JRC2020 AND FDP2024` co-location is insufficient to infer post-2020 conversion because it
does not distinguish persistent/baseline coffee, threshold artifacts, boundary/corridor effects, or
post-2020 establishment. The threshold sensitivity views use 0.025, 0.05, 0.10, 0.20, and 0.25;
0.025 is a permissive 2.5% model-probability diagnostic threshold, not verified parcel ground
truth. The morphology evidence is interpretive screening evidence and cannot independently
establish EUDR non-compliance or causation.

## Execution provenance versus task-formation provenance

The numerical and morphology rules above describe the diagnostic actually executed on Fazenda
Sucuri. They do not establish where the observation that prompted the diagnostic was first made.
Round 10 classifies those claims separately:

- **P1 — executed target:** verified. The pinned Sucuri handoff contains the threshold and morphology
  outputs produced by `single-earth/eudr-dmi-gil@d68e7eb`.
- **P2 — observation origin:** underdetermined. The first retained instruction with the exact
  corridor-versus-broad-unit wording calls it a Sucuri observation, but it contains no source-image
  reference. Older Ibiá / Patrocínio images are compatible with the wording but are not a retained
  causal link.

Accordingly, the diagnostic can support interpretation of Sucuri evidence, but its round-8
motivation sentence is recorded provenance rather than independently verified discovery provenance.
