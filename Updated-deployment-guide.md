Updated-deployment-guide

## Quick Summary

This guide outlines the immediate next steps required by the Owner to test the Word → DITA converter and the rebranding engine locally before handing off to QA.

---

## Current Repository Structure

Your repository is now organized as follows:


```

doc-intel-platform/
├── charter.md
├── roster.md
├── README.md
├── OWNER-CHECKLIST.md
│
├── /prototype
│   ├── converter.py                 ← Word to DITA-XML converter script
│   ├── rebranding-engine.py         ← Brand terminology mapping script
│   ├── rebranding-rules.json        ← Configuration rules for mapping
│   ├── validation-script.sh         ← DITA output quality validator
│   └── requirements.txt             ← Python dependencies
│
├── /sample-data
│   ├── /input
│   │   ├── Gmail_Installation_Guide.docx
│   │   └── sample-001.md
│   │
│   └── /expected-output
│       ├── sample-001-expected.dita
│       └── gmail-guide-expected.dita
│
├── /docs
│   ├── workflow-map.md
│   ├── quality-criteria.md
│   ├── assumptions.md
│   ├── sample-data-metadata.md
│   └── /meetings
│       └── 2026-06-22-kickoff.md
│
└── /validation
└── test-results.md              ← QA will document findings here

```

---

## Required Testing Environment

To execute the validation workflow, ensure you are using the following tools:
*   **IDE:** Cursor IDE
*   **Terminal:** Git Bash (Required for running the `.sh` validation script)
*   **Python:** Ensure Python 3.x is installed.

---

## Step-by-Step Execution Guide (For the Owner)

Follow these steps exactly within your Cursor IDE to validate the prototype locally.

### Step 1: Initialize the Environment

1.  Open Cursor IDE and load the root folder: `doc-intel-platform`.
2.  Open a new integrated terminal (`Ctrl + \`` or `Cmd + \``).
3.  Ensure your terminal profile is set to **Git Bash**.
4.  Navigate to the prototype directory:
    ```bash
    cd prototype/
    ```

### Step 2: Install Python Dependencies

Install the necessary libraries (like `python-docx`) required by the conversion script.

```bash
pip install -r requirements.txt

```

### Step 3: Execute the End-to-End Test

The following script will sequentially convert the input files to DITA format, apply the rebranding rules, and validate the structural integrity of the output.

Copy and paste this entire block into your Git Bash terminal (ensure you are still in the `prototype/` directory):

```bash
echo "=== Converting sample-001 ==="
python converter.py -i ../sample-data/input/sample-001.md -o /tmp/sample-001.dita

echo "=== Rebranding sample-001 ==="
python rebranding-engine.py -i /tmp/sample-001.dita -r rebranding-rules.json -o /tmp/sample-001-rebranded.dita

echo "=== Validating sample-001 ==="
bash validation-script.sh -f /tmp/sample-001-rebranded.dita

echo ""
echo "=== Converting Gmail Guide ==="
python converter.py -i ../sample-data/input/Gmail_Installation_Guide.docx -o /tmp/gmail.dita

echo "=== Rebranding Gmail Guide ==="
python rebranding-engine.py -i /tmp/gmail.dita -r rebranding-rules.json -o /tmp/gmail-rebranded.dita

echo "=== Validating Gmail Guide ==="
bash validation-script.sh -f /tmp/gmail-rebranded.dita

echo ""
echo "✓ All tests complete!"

```

*(Note: If the validation script returns a "Permission denied" error, run `chmod +x validation-script.sh` and try again.)*

### Step 4: Verify Outputs Against Gold Standards

The test script generates the final files in your system's temporary directory (`/tmp/`). You must manually verify these against the expected "gold standard" outputs.

1. Open the newly generated files in Cursor:
* `/tmp/sample-001-rebranded.dita`
* `/tmp/gmail-rebranded.dita`


2. Compare them side-by-side with the expected outputs located in your repository:
* `../sample-data/expected-output/sample-001-expected.dita`
* `../sample-data/expected-output/gmail-guide-expected.dita`


3. **Acceptance Criteria:** The structural tags and rebranded terminology (e.g., "Google" → "NewGoogle") must match perfectly.

---

## Troubleshooting Common Errors

* **`ModuleNotFoundError: No module named 'docx'`**: You missed Step 2. Run `pip install -r requirements.txt`.
* **`xmllint: command not found`**: The validation script utilizes `xmllint` for strict XML checking. It will gracefully skip if not installed, but for full validation, install `libxml2` (`sudo apt-get install libxml2-utils` on Linux or via Homebrew on macOS).
* **File not found errors**: Ensure you are running the commands from inside the `prototype/` directory.

---

## Next Actions & Handoff

Once you have successfully executed the end-to-end test and verified the outputs:

1. **Notify the QA Lead:** Contact **Dinil** and confirm that the environment is stable and ready for formal testing.
2. **QA Execution:** Dinil will begin rigorous testing and edge-case validation.
3. **Documentation:** Dinil must document all findings, pass/fail metrics, and known limitations in `/validation/test-results.md` by **Friday, June 26**.
""")

```

Your MD file is ready.
[file-tag: code-generated-file-a0cd1bac-ce83-4490-b624-09255cc0b813]

You can download the generated markdown file directly from the file tag above and place it in your repository. Let me know if you need any other modifications to the guide!

```