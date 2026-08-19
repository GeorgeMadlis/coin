---
type: Runbook
title: "Runtime environment"
fc-axis: REPRO
fc-round: 1
---
# Runtime environment

The canonical report was generated locally from pinned rasters with the counterpart repository's
virtual environment and `eudr_dmi_gil.reports.cli`. The OKF contact sheet was generated from the
pinned `report.pdf` with this repository's `.venv/bin/python` and `tools/pdf_contact_sheet.py`.

Validation used `tools/okf_gsp.py validate` and `okf_gsp.py publish --evidence-handoff`, which
verify counterpart cleanliness, manifest hash, artifact hashes, report PDF hash, and PDF page count.
