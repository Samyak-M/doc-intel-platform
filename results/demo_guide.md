# Demo Guide: Local PoC Run

This guide is for a quick local demonstration by the build team. For an executive walkthrough, use `LEADER-DEMO-GUIDE.md`.

## Goal

Show that one Word document can move through the complete pipeline:

1. Word `.docx` input
2. DITA-XML conversion
3. Brand terminology update
4. Validation result

## Setup

Run from the repo root:

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Git Bash, macOS, or Linux
source .venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r prototype/requirements.txt
```

## Run the Demo Pipeline

```bash
python prototype/converter.py --input sample-data/input/Gmail_Installation_Guide.docx --output sample-data/output/out.dita
python prototype/rebranding-engine.py --input sample-data/output/out.dita --rules prototype/rebranding-rules.json --output sample-data/output/out-rebranded.dita
bash prototype/validation-script.sh -f sample-data/output/out-rebranded.dita
```

## What to Show

- Input: `sample-data/input/Gmail_Installation_Guide.docx`
- Converted output: `sample-data/output/out.dita`
- Rebranded output: `sample-data/output/out-rebranded.dita`
- Validation criteria: `docs/quality-criteria.md`
- Expected output reference: `sample-data/expected_output/gmail-guide-expected.dita`

## Talk Track

- "This PoC automates a manual documentation migration workflow."
- "The converter creates DITA-XML from a Word document."
- "The rebranding engine applies controlled terminology changes from JSON rules."
- "The validation script gives the team a repeatable quality gate."
- "The current scope is a PoC, not a production migration platform."

## Demo Exit Criteria

- The final DITA file exists.
- Rebranded terms are visible in the output.
- Validation returns PASS, PASS with warnings, or a clear FAIL.
- Any limitation is explained using `docs/quality-criteria.md`.
