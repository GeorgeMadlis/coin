---
type: Finding
title: The project in plain language
description: A short explanation of the observer-disagreement-framework project.
fc-level: 0
fc-axis: R
fc-status: open
fc-round: 20
fc-supersedes: answer.md@r4
timestamp: 2026-08-16
---

A statement — a claim, a verdict, an answer — is rarely settled the moment it is first said. It gets added to, questioned, sometimes disputed, and eventually treated as settled. This project builds a theory of that whole life cycle, which it calls a **statement trajectory**.

Disagreement is the part of that life cycle this project started from, and it is still the central case: people can look at the same facts and still disagree, and the same can happen to one person over time, or to two AI agents asked to study the same problem. But disagreement — the project's own name for it is the **contestation** stage — is only one of five stages a statement can pass through. A statement can also be enriched with new evidence, or critiqued by a probing question, with no live disagreement in the picture at all; and it can be consolidated, meaning a verdict, convention, or "no further answer is recoverable" is formally adopted.

The basic idea underneath all five stages is that every observer process is a limited summarizer. We never hold the whole world in view. We use partial information, habits of interpretation, and surviving records. What an observer process emits is an observation: a statement, verdict, answer, classification, or other reduced representation. Within the contestation stage specifically, disagreement appears when comparable observations are maintained as rival positions: sometimes because information is missing from one context, sometimes because the same information is sorted differently, and sometimes because the needed information was never recorded, so no later observer can recover it.

The project also proposes a filing format for statements under this kind of scrutiny. It records the question, the answer, the evidence, the method, and every later revision, including which stage each revision belongs to. That way, a statement's whole history — not just its disagreements — is not lost when people or agents keep digging. The committed `HEAD` of `main` is the current, authoritative projection of the record at any moment; earlier concept bodies are recovered through Git history and pinned snapshots, and anything rendered or exported is a snapshot pinned to whichever version it was taken from.

Dig deeper: [problem](pf/overview.md), [framework](s/overview.md), [status](r/overview.md).
