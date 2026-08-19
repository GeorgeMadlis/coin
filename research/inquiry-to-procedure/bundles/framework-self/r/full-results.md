---
type: Finding
title: Framework-self measurements and retrospective classifications
description: Reproducible Step 5 measurements, Step 6 observations, Step 7 pilot classifications, and Step 8 limitations boundary.
fc-level: 3
fc-axis: R
fc-status: open
fc-round: 17
fc-supersedes: r/full-results.md@r16
timestamp: 2026-07-21
---

# Measurement Target

The Step 5 pilot measurement covers `bundles/framework-self` bundle rounds
1-13 at source commit `0c3346b7f4ebc92260cfecc1c6ee63e676d46ce8`, the HEAD of
`main` when Step 5 started.

Round 14 records this measurement and is intentionally excluded from the target
values, so the result does not measure itself.

The machine-readable table is
[metrics-rounds-0001-0013.csv](metrics-rounds-0001-0013.csv).

The Step 7 framework-self-only retrospective classification table is
[retrospective-round-classification.csv](retrospective-round-classification.csv).
It covers rounds 1-15 and intentionally excludes round 16, so the
classification artifact does not classify itself.

The Step 8 limitations registry is recorded in
[docs/limitations.md](../../../docs/limitations.md). It is not a measurement
artifact. It specifies operational failure conditions for P1-P5, P4', the
three disagreement types, the five stages, and the claim that explicit
recording reduces re-litigation.

# Count Rules

- Stage sequence: read from `inquiry/index.md`, because rounds 1-3 predate
  `fc-stage` frontmatter. Values for rounds 1-3 are therefore retrospective
  classifications recorded in the index, not original round frontmatter.
- Move, party, type, touches, and stage-frontmatter coverage: read from
  `inquiry/round-NNNN.md` frontmatter.
- Type-trajectory metrics: computed only over contestation-stage rounds.
- Evidence added per round: counted as share of rounds whose `fc-move` is
  `evidence`; individual evidence items are not normalized in the historical
  record.
- Post-consolidation supersession rate: after the first consolidation round,
  count rounds that establish at least one current concept file with
  `fc-supersedes`; this uses current-file metadata only and does not expand
  superseded successors from Git history.
- Description-length asymmetry: count words in round bodies after frontmatter,
  group by `fc-party`, and report Claude/Codex mean and median ratios. This is
  a representation-dependent demonstration only.

# Reproduction

From the repository root, run the following Python snippet. It recomputes the
values from recorded files and metadata without using cached HTML:

```python
from pathlib import Path
from collections import Counter, defaultdict
import re
import statistics

bundle = Path("bundles/framework-self")
target_rounds = range(1, 14)

stage_from_index = {}
index_text = (bundle / "inquiry/index.md").read_text()
for line in index_text.splitlines():
    if line.startswith("| ") and "[round-" in line:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells and cells[0].isdigit() and int(cells[0]) in target_rounds:
            stage_from_index[int(cells[0])] = cells[4]

rounds = []
for path in sorted((bundle / "inquiry").glob("round-*.md")):
    text = path.read_text()
    frontmatter = {}
    body = text
    if text.startswith("---"):
        _, raw, body = text.split("---", 2)
        for raw_line in raw.splitlines():
            if ":" in raw_line:
                key, value = raw_line.split(":", 1)
                frontmatter[key.strip()] = value.strip()
    number = int(frontmatter["fc-round"])
    if number not in target_rounds:
        continue
    words = len(re.findall(r"[A-Za-z0-9_'-]+", body))
    rounds.append(
        {
            "round": number,
            "party": frontmatter.get("fc-party"),
            "move": frontmatter.get("fc-move"),
            "stage_frontmatter": frontmatter.get("fc-stage"),
            "stage": stage_from_index.get(number),
            "type": frontmatter.get("fc-type-at-round"),
            "words": words,
        }
    )

n = len(rounds)
stage_transitions = sum(
    1 for left, right in zip(rounds, rounds[1:]) if left["stage"] != right["stage"]
)
handoffs = sum(
    1 for left, right in zip(rounds, rounds[1:]) if left["party"] != right["party"]
)
stage_counts = Counter(row["stage"] for row in rounds)
move_counts = Counter(row["move"] for row in rounds)
stage_frontmatter_count = sum(1 for row in rounds if row["stage_frontmatter"])

by_party = defaultdict(list)
for row in rounds:
    by_party[row["party"]].append(row["words"])

supersession_rounds = Counter()
for path in bundle.rglob("*.md"):
    if path.name in {"index.md", "log.md"} or "_site" in path.parts:
        continue
    text = path.read_text()
    if not text.startswith("---"):
        continue
    raw = text.split("---", 2)[1]
    data = {}
    for raw_line in raw.splitlines():
        if ":" in raw_line:
            key, value = raw_line.split(":", 1)
            data[key.strip()] = value.strip()
    if "fc-supersedes" in data:
        supersession_rounds[int(data["fc-round"])] += 1

first_consolidation = min(
    row["round"] for row in rounds if row["stage"] == "consolidation"
)
post_consolidation_rounds = [row["round"] for row in rounds if row["round"] > first_consolidation]
post_consolidation_supersession_rounds = [
    number for number in post_consolidation_rounds if supersession_rounds[number] > 0
]

print("rounds", n)
print("stage_counts", dict(stage_counts))
print("stage_transition_rate", stage_transitions / (n - 1))
print("time_to_first_contestation_rounds", 3 - 1)
print("contestation_round_count", stage_counts["contestation"])
print("time_to_first_consolidation_from_formation_rounds", first_consolidation - 1)
print("post_consolidation_supersession_round_rate", len(post_consolidation_supersession_rounds) / len(post_consolidation_rounds))
print("evidence_move_share", move_counts["evidence"] / n)
print("frame_change_frequency", move_counts["frame-change"] / n)
print("observer_handoff_frequency", handoffs / (n - 1))
print("stage_frontmatter_completeness", stage_frontmatter_count / n)
print("stage_availability_including_index", len(stage_from_index) / n)
print("description_length_mean_ratio_claude_over_codex", (sum(by_party["claude"]) / len(by_party["claude"])) / (sum(by_party["codex"]) / len(by_party["codex"])))
print("description_length_median_ratio_claude_over_codex", statistics.median(by_party["claude"]) / statistics.median(by_party["codex"]))
```

# Result Status

These are actual reproducible repository measurements under the count rules
above. They are not validation of the framework. The target is one
self-referential trajectory, and several observer-distance metrics remain
`NOT_MEASURABLE` because the bundle did not record paired predictions, paired
forced labels, or parallel level-specific observer accounts.

Step 8 strengthens the negative status of this evidence: the framework-self
bundle can demonstrate record discipline, but it cannot test external validity,
causal effects, population-level predictions, or independence of observers. The
framework remains `open`.

# Step 6 Exploratory Prediction Observations

These observations are computed from `bundles/framework-self` rounds 1-14, the
state available before the Step 6 round was appended. They are a worked
calculation only. They do not validate any population-level prediction.

Count rules:

- Stage sequence is read from `inquiry/index.md`.
- Rounds 1-3 use retrospective stage classifications recorded in the index,
  because their round files predate `fc-stage`.
- Supersession rounds are counted from current concept frontmatter only; git
  history is not expanded.

Computed values:

| observation | value |
|---|---:|
| Stage sequence | r1 formation; r2 enrichment; r3 contestation; r4 consolidation; r5-r6 enrichment; r7 critique; r8 consolidation; r9-r14 enrichment |
| Stage counts | formation 1; enrichment 9; critique 1; contestation 1; consolidation 2 |
| Stage-transition rate | 7/13 = 0.5385 |
| First contestation | r3 |
| Contestation rounds | 1 |
| Type-trajectory metrics | NOT MEASURABLE: fewer than two contestation rounds |
| Any critique before first contestation | false |
| Contestation rounds from first contestation to next consolidation | 1 |
| Rounds from first contestation to next consolidation | 1 |
| Post-first-consolidation rounds | 10 |
| Post-first-consolidation supersession rounds | 5/10 = 0.5000 |
| Current superseded concepts after first consolidation | 19 |

Prediction 8 calculation for this bundle:

| variable | value |
|---|---:|
| Formation round `F_b` | r1 |
| First contestation `C_b` | r3 |
| Pre-contestation critique indicator `precrit_b` | 0 |
| Next consolidation `G_b` | r4 |
| Contestation count before `G_b` | 1 |
| Rounds from `C_b` to `G_b` | 1 |
| Post-consolidation supersession rate | 5/10 = 0.5000 |

Limitations:

- The bundle contributes one trajectory only.
- It belongs only to the no-pre-critique group for Prediction 8.
- The first contestation classification is retrospective.
- There is no matched comparison trajectory.
- The calculated values are exploratory observations, not validation.

# Step 7 Retrospective Classification Results

The classification table records 15 prior bundle rounds:

| status | count |
|---|---:|
| rounds with contemporaneous `fc-stage` | 12 |
| rounds with retrospective stage only | 3 |
| usable contestation-type rounds | 1 |
| non-contestation rounds with legacy type metadata excluded from type trajectory | 5 |
| rounds with high stage confidence | 14 |
| rounds with medium type confidence | 1 |

Stage counts over rounds 1-15:

| stage | count | source |
|---|---:|---|
| formation | 1 | retrospective classification of round 1 |
| enrichment | 10 | round 2 plus rounds 5, 6, and 9-15 |
| critique | 1 | round 7 |
| contestation | 1 | round 3 |
| consolidation | 2 | rounds 4 and 8 |

Measured stage returns:

| pattern | value | interpretation |
|---|---:|---|
| consolidation to later enrichment | 2 | consolidation was non-terminal after rounds 4 and 8 |
| longest same-stage run | 7 rounds | enrichment run from rounds 9-15 |
| type stall/reversal/oscillation measurability | NOT_MEASURABLE | only round 3 is contestation-stage |

These results are a case-study pilot only. They show that the
framework-self trajectory is inspectable and classifiable from recorded
rounds, concept metadata, commits, and published manifests. They do not show
that the framework generalizes to external cases.
