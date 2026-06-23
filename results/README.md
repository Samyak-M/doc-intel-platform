# Results Folder

This folder holds evidence generated during PoC testing and demos.

## Current Files

- `demo_guide.md` - Local demo run instructions for the build team.
- `validation_summary.md` - Summary of validation evidence.

## Generated Demo Artifacts

Pipeline outputs are written to:

```text
sample-data/output/
|-- out.dita
`-- out-rebranded.dita
```

Keep generated outputs out of commits unless the team intentionally captures a demo baseline.

## What To Add After Each Formal Demo

- Date of demo
- Input file used
- Commands or Claude command used
- Validation status
- Screenshots, if required by leadership
- Follow-up actions and owner

For the leader-facing walkthrough, use `LEADER-DEMO-GUIDE.md`.
