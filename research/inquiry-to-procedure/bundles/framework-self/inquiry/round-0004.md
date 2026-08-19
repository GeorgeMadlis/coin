---
type: Event
title: "Round 4: scope widened from observer disagreement to statement evolution"
description: docs/framework_v3.md supersedes v2; disagreement (contestation) is now one of five stages of a general statement trajectory; sequential multi-observer realization and canonical-state rule formalized.
fc-axis: INQUIRY
fc-round: 4
fc-move: frame-change
fc-stage: consolidation
fc-party: claude
fc-type-at-round: resolved
fc-touches: [answer.md, pf/overview.md, s/overview.md, inquiry/index.md, log.md]
fc-status: open
timestamp: 2026-07-19
---

# Move

The human instruction widened the project's object of study: no longer only the evolution of
observer disagreement, but the evolution of **statements** generally, of which disagreement
(contestation) is one stage among several — formation, enrichment, critique, contestation,
consolidation. Two operational facts from the revised `docs/agent-guide.md` were folded into
the theory: (a) different agents participate sequentially as distinct observers on **one**
interleaved round sequence, not parallel branches (the multi-party regime's realization); (b)
the committed HEAD of `main` is the canonical current bundle state, from which rendered/derived
artifacts are pinned.

# Evidence added

`docs/framework_v3.md` — new document, "Supersedes: v2", produced in this round.

SHA256: `f7fe8e9f98bc0be4331f1dbd1d2cca283ddd063350976a13d91d8d618cdb7d2a`.

`docs/framework_v2.md` is unchanged (SHA256 `c5240cdfcf1f22948f9ece4d1b778195415e64c83c56737e385773bf50102de8`, as recorded in round-0001) and remains the historical record of the prior scope; it is not edited by this round.

# Effect on state

Context window: added the revised `docs/agent-guide.md` (sequential single-agent workflow,
retired dual-agent fusion protocol) as the operational fact motivating the frame change; no new
external evidence about the subject matter.

Frame: f(t) → f(t+1). Old frame f(t): the object of study is observer disagreement, classified
directly by the Type I/II/III taxonomy across all rounds. New frame f(t+1): the object of study
is the **statement trajectory**; each round is first classified by **stage** (formation,
enrichment, critique, contestation, consolidation), and the Type I/II/III taxonomy applies only
to contestation-stage rounds. The bundle-level *type trajectory* of v2 becomes the
contestation-restriction of a more general *stage trajectory*. The sequential multi-observer
regime is now formalized as one round sequence with a party-assignment function `p(t)`, matching
this repository's actual practice, rather than the more general (and here unused)
parallel-branch realization.

# Resulting revisions

- `answer.md` — `fc-supersedes: answer.md@r1`; `fc-round` bumped 1 → 4; text widened from "why
  disagreement persists" to statement evolution with disagreement as the central contested
  regime.
- `pf/overview.md` — `fc-supersedes: pf/overview.md@r1`; `fc-round` bumped 1 → 4; text widened
  from "why people ... still not agree" to the general problem of statement evolution, with
  disagreement (contestation) named as one stage.
- `s/overview.md` — `fc-supersedes: s/overview.md@r1`; `fc-round` bumped 1 → 4; text corrected
  from "classifies those cases as Type I, Type II, Type III... across recorded inquiry rounds"
  (implying the taxonomy covers every round) to the stage-first framing in which Type I/II/III
  classifies contestation-stage rounds specifically.
- `agent-contract.md` and `r/overview.md` were checked and left untouched: neither file's text
  asserts disagreement as the *whole* scope in a way the widened frame contradicts (see
  Classification rationale).
- `inquiry/index.md` — restated as a stage trajectory with the type trajectory embedded; this
  round row added.
- `log.md` (bundle-local) and repo-root `log.md` — one line each appended for this round.

# Classification rationale

This round is a **frame-change** move: `f(t+1)` reclassifies what the framework's object of
study is, without any new fact about the subject matter and without adjudicating a live
counter-position (no party held a rival claim against the v2 framing that this round resolves —
the change was requested directly, as widening the frame rather than continuing an interrupted
contestation). Per §2.2 of the new `docs/framework_v3.md`, a frame-change round is
**contestation** only when it is unilateral and contested, or **consolidation** when it settles
into an adopted frame; here the widened frame is adopted outright as the bundle's current state
(no rival frame stands against it), so this round is classified `fc-stage: consolidation`,
`fc-type-at-round: resolved`.

Files were checked against the "asserts the old scope as the whole scope" test required by the
task: `answer.md` and `pf/overview.md` both open by defining the entire project as an account of
*why disagreement persists* — under v3 this is now a description of one stage (contestation)
presented as if it covered the whole trajectory, so both are contradicted and superseded.
`s/overview.md` states the framework "classifies those cases as Type I, Type II, and Type III,
then tracks how the classification changes across recorded inquiry rounds" — under v3 the
taxonomy classifies contestation rounds only, and the bundle-level record it feeds is the stage
trajectory, not directly the type trajectory — so this is also contradicted and superseded.
`agent-contract.md`'s Participation section describes opening round files and classifying "the
live disagreement type" for *moves*, which remains true without contradiction for contestation
moves specifically; it does not assert that all moves are disagreements, so it is left as-is
(the `fc-stage` field it should additionally record is a Step-3/Step-4 spec-and-tooling matter
per the constraints on this task, not a content contradiction warranting supersession).
`r/overview.md` reports project status ("a v2 framework document exists... nothing in the
framework is yet proven") rather than asserting the scope itself; it is not contradicted by the
widened scope and is left untouched, though it will read as referring to a superseded document
until a future round updates it — noted here rather than silently left inconsistent.
