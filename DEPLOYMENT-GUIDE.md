# Deployment Guide: Document Intelligence PoC

This guide gives the core team a step-by-step process to implement, run, validate, and demo the Document Intelligence proof of concept.

## What This PoC Implements

The PoC has one automated pipeline:

1. Convert a Word `.docx` file to DITA-XML.
2. Apply brand terminology changes from a JSON rules file.
3. Validate the final DITA output against basic quality checks.
4. Expose the same workflow as a Claude Code plugin command.

## Quick Start: Two Ways to Run the Pipeline

### Option 1: Claude Code Plugin (Recommended for Demo)

**Prerequisites:**
- Claude Code with this repo open
- Python 3.10 or 3.11 with dependencies installed

**Run the pipeline:**
```bash
/pipeline sample-data/input/Gmail_Installation_Guide.docx
```

This executes all three steps automatically and preserves the input filename in outputs:
- `Gmail_Installation_Guide-output.dita` (converted)
- `Gmail_Installation_Guide-rebranded.dita` (with branding applied)

---

### Option 2: Manual Commands (for Debugging)

Run from the repo root:

```bash
# Step 1: Convert
python prototype/converter.py --input sample-data/input/Gmail_Installation_Guide.docx --output sample-data/output/Gmail_Installation_Guide-output.dita

# Step 2: Rebrand
python prototype/rebranding-engine.py --input sample-data/output/Gmail_Installation_Guide-output.dita --rules prototype/rebranding-rules.json --output sample-data/output/Gmail_Installation_Guide-rebranded.dita

# Step 3: Validate
bash prototype/validation-script.sh sample-data/output/Gmail_Installation_Guide-rebranded.dita
```

---

## Repository Layout

```text
doc-intel-platform/
|-- .claude/
|   |-- plugin.json
|   `-- commands/pipeline.md
|-- docs/
|   |-- quality-criteria.md
|   |-- workflow-map.md
|   |-- assumptions.md
|   `-- sample-data-metadata.md
|-- prototype/
|   |-- converter.py
|   |-- rebranding-engine.py
|   |-- rebranding-rules.json
|   |-- validation-script.sh
|   `-- requirements.txt
|-- sample-data/
|   |-- input/Gmail_Installation_Guide.docx
|   `-- expected_output/
|-- results/
|   |-- demo_guide.md
|   `-- validation_summary.md
|-- validation/
|   `-- test-results.md
`-- DEPLOYMENT-GUIDE.md
```

---

## Prerequisites

- **Python 3.10 or 3.11** (required; 3.14 not supported yet)
- **Git** with Git Bash (for Windows)
- **Claude Code** (for `/pipeline` command)
- **libxml2** optional (for stricter XML validation)

---

## Step 1: Clone and Open the Repo

```bash
git clone <repo-url>
cd doc-intel-platform
```

Open the repo in Claude Code or your IDE.

---

## Step 2: Create a Local Python Environment

From the repo root:

```bash
python -m venv .venv
```

On Windows with multiple Python versions:

```bash
py -3.11 -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Git Bash, macOS, or Linux
source .venv/Scripts/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r prototype/requirements.txt
```

Expected result: `python-docx`, `lxml`, and `colorama` install successfully.

---

## Step 4: Test the Pipeline

### Option A: Using Claude Code `/pipeline` Command (Recommended)

1. Open Claude Code with the repo as the workspace.
2. In Claude Code chat, run:

```text
/pipeline sample-data/input/Gmail_Installation_Guide.docx
```

3. Claude Code executes all three steps and reports the result.

**Expected output:**
- `sample-data/output/Gmail_Installation_Guide-output.dita` (converted)
- `sample-data/output/Gmail_Installation_Guide-rebranded.dita` (rebranded)
- Validation status (PASS, WARN, or FAIL)

### Option B: Manual Command-Line Test

Run each step manually for testing or debugging:

```bash
# Step 1: Convert Word to DITA
python prototype/converter.py --input sample-data/input/Gmail_Installation_Guide.docx --output sample-data/output/Gmail_Installation_Guide-output.dita
```

Expected: `sample-data/output/Gmail_Installation_Guide-output.dita` created (17 KB).

```bash
# Step 2: Apply Rebranding
python prototype/rebranding-engine.py --input sample-data/output/Gmail_Installation_Guide-output.dita --rules prototype/rebranding-rules.json --output sample-data/output/Gmail_Installation_Guide-rebranded.dita
```

Expected: `sample-data/output/Gmail_Installation_Guide-rebranded.dita` created with brand terms replaced (e.g., Gmail → NewGmail).

```bash
# Step 3: Validate
bash prototype/validation-script.sh sample-data/output/Gmail_Installation_Guide-rebranded.dita
```

Expected: Validation report printed to terminal. Exit code `0` for PASS or PASS with warnings.

---

## Step 5: Verify Output Quality

Open these files to verify:

1. **Input:** `sample-data/input/Gmail_Installation_Guide.docx`
2. **Converted:** `sample-data/output/Gmail_Installation_Guide-output.dita` (DITA-XML structure)
3. **Rebranded:** `sample-data/output/Gmail_Installation_Guide-rebranded.dita` (brand terms updated)
4. **Quality Reference:** `docs/quality-criteria.md` (what PASS, WARN, FAIL mean)
5. **Expected Output:** `sample-data/expected_output/gmail-guide-expected.dita` (manual reference)

Check:
- DITA root topic, title, body, sections, paragraphs, and tables exist.
- Brand terms were applied correctly.
- No significant content loss.
- Validation status is clear.

---

## Step 6: Record Results (Manual)

Update `validation/test-results.md` after each test run:

```markdown
| Date | Input File | Output | Status | Notes |
|------|-----------|--------|--------|-------|
| 2026-06-25 | Gmail_Installation_Guide.docx | Gmail_Installation_Guide-rebranded.dita | PASS | All checks passed. 77 replacements applied. |
```

---

## How the Pipeline Works

### The Claude Code Plugin Orchestration

File: `.claude/commands/pipeline.md`

The plugin prompt:
1. Extracts the input filename from `$ARGUMENTS`
2. Generates dynamic output filenames (preserving the original name)
3. Runs three steps in order
4. Reports results or failures

**Step 1: Conversion**
- Command: `python prototype/converter.py --input <input-file> --output <basename>-output.dita`
- Converts Word document to DITA-XML format

**Step 2: Rebranding**
- Command: `python prototype/rebranding-engine.py --input <basename>-output.dita --rules prototype/rebranding-rules.json --output <basename>-rebranded.dita`
- Applies brand terminology mappings

**Step 3: Validation**
- Command: `bash prototype/validation-script.sh <basename>-rebranded.dita`
- Validates DITA structure and content

### On Failure

If any step fails, the pipeline:
1. Reports the failed step and the exact command
2. Suggests a practical next action
3. If validation fails, reads `docs/quality-criteria.md` and returns 5 bullet points (PASS, WARN, FAIL)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'docx'` | Run `pip install -r prototype/requirements.txt` |
| `bash: command not found` on Windows | Install Git for Windows; use Git Bash, not PowerShell |
| `lxml==4.9.2` fails to build | Use Python 3.10 or 3.11 (not 3.14) |
| `xmllint not installed` warning | Optional. Install libxml2 for stricter validation, or continue with reduced checks |
| Output folder missing | The converter creates it automatically |
| Rebranding makes no visible changes | Verify input contains matching terms in `prototype/rebranding-rules.json` |
| Validation fails with unclear error | Check `docs/quality-criteria.md` for expected vs. actual behavior |

---

## Practical Improvements Recommended

- After demo approval, add a wrapper script (`prototype/run-pipeline.sh`) for one-command execution.
- Add `sample-data/output/.gitkeep` if you want the output folder visible in fresh checkouts.
- Add automated expected-vs-actual comparison for QA after the PoC.
- Keep Claude command prompts deterministic and small.
- Publish the plugin to a skills marketplace repository after validation.

---

## Definition of Done

The PoC is ready for core-team sign-off when:

✓ Claude Code `/pipeline` command runs end to end  
✓ Manual pipeline commands run end to end (if debugging)  
✓ Output files are generated with preserved input filenames  
✓ Validation results are captured  
✓ Demo has been rehearsed once  
✓ Marketplace packaging steps are documented  

---

## Next Steps

1. **Test the pipeline** using either method above.
2. **Record results** in `validation/test-results.md`.
3. **Review output quality** using `docs/quality-criteria.md`.
4. **Demo to leaders** using `LEADER-DEMO-GUIDE.md`.
5. **Publish to marketplace** using `SKILLS-MARKETPLACE-GUIDE.md` (if approved).
