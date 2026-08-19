---
type: Policy
title: Agent contract
description: Rules for agents consuming or participating in this bundle.
fc-axis: INQUIRY
fc-status: open
fc-round: 20
fc-supersedes: agent-contract.md@r13
timestamp: 2026-08-16
---

## Consumption

An agent should first classify the question by implied level and axis. A broad question asks for L0 or L1; a method question asks for S; a reproduction question asks for REPRO; a question about revisions asks for INQUIRY. The agent should descend only as deep as required, answer from that level, and cite the file path used. It must not answer deeper than the user asked, because that imposes the agent's own framing, and it must not answer shallower than required, because that loses information the user asked for.

The depth rule is a project governance rule motivated by observer-relative
framing and user alignment. It is not a theorem of Wolfram observer theory.

## Participation

When a message is a move in the inquiry, such as an objection, evidence, or a question that extends the inquiry, the agent should open the next `inquiry/round-NNNN.md`. It should classify the stage and, when the stage is contestation, the live disagreement type; record the rationale; apply revisions by supersession using `fc-supersedes`; update the bundle-local and repo-root ledgers; and then answer from the revised state. Agent contributions are moves too: attributable, logged, and supersedable.

Participation is a relation to the evolving record: the agent observes the
current record, emits an observation or move, records/commits that move, and
thereby changes what later observers can inspect. The actor label in
`fc-party` remains authorship metadata; distinct theoretical observer
instances require context such as prompt, tools, retrieved records, model or
version state, and time.

The bundle-local round and repository round are different counters. The root `log.md` row is the repository round; this bundle's `log.md` and `inquiry/round-NNNN.md` are the bundle round. When a repository change updates this bundle, record both and publish the updated bundle to `../okf-bundle-snapshots`. Snapshot names use the bundle round; their manifests and catalog rows record the source repository round separately.
