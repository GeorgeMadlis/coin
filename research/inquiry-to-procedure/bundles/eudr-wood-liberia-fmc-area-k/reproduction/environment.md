---
type: Runbook
title: Environment
fc-level: 2
fc-axis: REPRO
fc-round: 8
fc-supersedes: reproduction/environment.md@round-0004
---
# Environment

Round-4 verification ran locally on 2026-08-16 in the shared workspace. Round-8 re-verification
(dataset-registry/provenance fix, no re-analysis) ran locally on 2026-08-17.

- Framework repository: `/Users/server/projects/geospatial-evidence-framework`
- Framework branch: `main` (round 8; round 4 ran on `work/land-use-change-evidence`, since merged)
- Counterpart repository: `/Users/server/projects/eudr-dmi-gil`
- Counterpart branch: `work/tmf-radd-evidence-observers`
- Counterpart HEAD: `61285bd6ac2ef45708dee660620bd9db4181d3c2`
- Counterpart tracked status: clean (`git status --short --untracked-files=no` produced no output)
- Counterpart remotes: `origin` points to `single-earth/eudr-dmi-gil`; `georgemadlis` points to
  `GeorgeMadlis/eudr-dmi-gil`.

The counterpart working tree contains untracked derived output directories. The tracked source tree
is clean and the handoff records `counterpart_dirty: false`, so this source bundle treats the
handoff and commit as the pinned source reference and leaves untracked output non-canonical.
