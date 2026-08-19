---
type: Finding
title: The framework in one paragraph
description: Bounded observers, statement trajectories, stages, disagreement types, and OKF bundles.
fc-level: 1
fc-axis: S
fc-status: open
fc-round: 20
fc-supersedes: s/overview.md@r18
timestamp: 2026-08-16
---

The framework treats each observer process as a bounded summarizer of a
surviving record, using Wolfram observer theory as a formal analogy rather than
as a literal physics claim. The dedicated foundation page
[Wolfram observer theory](foundations/wolfram-observer-theory.md) records what
is directly sourced to Wolfram, what this project translates into `C_i` and
`f_i`, and what this project extends on its own, including the distinction
between an observer process and its emitted observation/output. A statement's
history is then treated as a **trajectory** of recorded rounds. Every round is
first classified by **stage** — formation (the statement's first emission), enrichment
(information added, no rival position), critique (a probe or hard question, no
rival position), contestation (a live disagreement between positions), or
consolidation (a verdict, convention, or bottomed-out status is adopted). Only
within the contestation stage does disagreement arise, because observers use
different accessible records, different ways of compressing the same records,
or records that lost the needed facts before the present inquiry began; only
contestation rounds are classified Type I, Type II, or Type III. The
bundle-level record this produces is a **stage trajectory**; the **type
trajectory** used in earlier work is exactly its contestation-stage restriction.
OKF bundles are the proposed recording function: they store the problem,
method, result, reproduction facts, and the full stage-classified round history
at multiple levels so later humans or agents can re-enter the trajectory
without losing its past. Prior materialized concept bodies normally remain
recoverable through Git history and pinned snapshots; the current bundle tree is
the current projection.
