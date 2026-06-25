---
description: Execute the Document Intelligence Platform pipeline to convert, rebrand, and validate Word documents. Usage: /doc-intel-platform:pipeline <path-to-docx-file>
---

# Document Intelligence Platform Pipeline

## Input Validation

Check if `$ARGUMENTS` is provided. If it is empty or missing, return immediately with this message:
```
Usage: /doc-intel-platform:pipeline <path-to-docx-file>

Required argument: path to a Word (.docx) document.

Example:
  /doc-intel-platform:pipeline sample-data/input/Gmail_Installation_Guide.docx
```

Then halt execution.

If `$ARGUMENTS` is provided, assign it to `INPUT_FILE` and proceed to filename extraction.

---

## Dynamic Filename Extraction

Extract the base filename from `$ARGUMENTS` without extension and directory path.

**Example:**
- Input: `sample-data/input/Gmail_Installation_Guide.docx`
- Base filename: `Gmail_Installation_Guide`
- Output filenames will be:
  - `sample-data/output/Gmail_Installation_Guide-output.dita`
  - `sample-data/output/Gmail_Installation_Guide-rebranded.dita`

Set these variables:
- `OUTPUT_FILE`: `sample-data/output/{BASE_FILENAME}-output.dita`
- `REBRANDED_FILE`: `sample-data/output/{BASE_FILENAME}-rebranded.dita`

Then proceed to Step 1.

---

## Execution Sequence

Execute the following steps in strict order. Do NOT skip, reorder, or add any steps. Stop immediately if any step fails.

### Step 1: Word-to-DITA Conversion

Run this command exactly as written:
```bash
python prototype/converter.py --input $ARGUMENTS --output $OUTPUT_FILE
```

**On failure:**
- Report: `FAILED: Step 1 - Word-to-DITA conversion`
- Report the exact command that failed
- Suggest next action: "Check input file format and ensure prototype/converter.py is available."
- Stop execution.

**On success:**
- Confirm: "Step 1 passed. DITA output: $OUTPUT_FILE"
- Proceed to Step 2.

---

### Step 2: Rebranding

Run this command exactly as written:
```bash
python prototype/rebranding-engine.py --input $OUTPUT_FILE --rules prototype/rebranding-rules.json --output $REBRANDED_FILE
```

**On failure:**
- Report: `FAILED: Step 2 - Rebranding engine`
- Report the exact command that failed
- Suggest next action: "Verify rebranding rules JSON and check prototype/rebranding-engine.py is available."
- Stop execution.

**On success:**
- Confirm: "Step 2 passed. Rebranded output: $REBRANDED_FILE"
- Proceed to Step 3.

---

### Step 3: Validation

Run this command exactly as written:
```bash
bash prototype/validation-script.sh $REBRANDED_FILE
```

**On success:**
- Report: "SUCCESS: All validation checks passed."
- Report final output paths:
  - `DITA (original):  $OUTPUT_FILE`
  - `DITA (rebranded): $REBRANDED_FILE`
- Halt execution (success state).

**On failure:**
- Report: `FAILED: Step 3 - Validation against quality criteria`
- Report the exact command that failed
- Read the file `docs/quality-criteria.md` immediately
- Based on the content of `docs/quality-criteria.md`, generate and return exactly 5 bullet points summarizing validation status
- Each bullet must begin with exactly one of these words: `PASS`, `WARN`, or `FAIL`
- Format:
  ```
  - PASS: [criterion or validation check that passed]
  - FAIL: [criterion or validation check that failed]
  - WARN: [criterion or validation check with warnings]
  - PASS: [another passing check]
  - FAIL: [another failing check]
  ```
- Stop execution.

---

## Summary

This pipeline is deterministic and must follow the exact sequence above. No deviations, no extra preprocessing, no conditional branches beyond failure handling.

Expected user command:
```
/doc-intel-platform:pipeline sample-data/input/Gmail_Installation_Guide.docx
```

Output will be generated in `sample-data/output/` with filenames preserving the input document name.
