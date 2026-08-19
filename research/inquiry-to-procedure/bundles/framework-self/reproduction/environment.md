---
type: Runbook
title: Tooling environment
description: Concrete Python package environment for Step 4 generator, append, and validator tooling.
fc-level: 3
fc-axis: REPRO
fc-irreducibility: none
fc-status: open
fc-round: 13
timestamp: 2026-07-21
---

# Environment

Step 4 makes the tooling environment concrete enough to record:

- Python: `>=3.11`.
- Package: `okf-fc 0.1.0` from `tools/pyproject.toml`.
- Runtime dependency: `pyyaml>=6`.
- Render/test extras used by the repository tests: `markdown>=3.5`, `pytest`.
- CLI entry point: `okf-fc = okf_fc.cli:main`.

Install for local development with:

```text
python -m pip install -e "tools[dev,render]"
```

The repository currently includes a local `tools/.venv/` used for validation in
this workspace. That virtual environment is not a portable source artifact; the
portable environment description is the versioned package metadata above.
