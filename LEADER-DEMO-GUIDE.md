# Leader Demo Guide: Document Intelligence PoC

Use this guide to give a clear, repeatable demo to leaders. The goal is to show business value, not implementation details.

## Demo Outcome

By the end of the demo, leaders should understand:

- The current manual Word-to-DITA and rebranding workflow can be partially automated.
- Brand terminology updates can be controlled through rules, no code changes needed.
- Validation gives the team an objective quality checkpoint.
- The PoC is ready for structured feedback, not production rollout.

---

## Before the Demo

### Environment Setup (5 minutes before)

1. **Python check:** Confirm Python 3.10 or 3.11
   ```bash
   python --version
   ```

2. **Dependencies installed:**
   ```bash
   pip install -r prototype/requirements.txt
   ```

3. **Git Bash ready** (Windows only) for validation script

4. **Clean outputs:**
   ```bash
   rm -f sample-data/output/*.dita
   ```

### Editor Tabs Ready

Open in tabs (don't close; switch between them during demo):

- `sample-data/input/Gmail_Installation_Guide.docx`
- `prototype/rebranding-rules.json`
- `docs/quality-criteria.md`

### Claude Code Setup

- Open repo as workspace in Claude Code
- Test `/pipeline` command once before demo to ensure it works
- Have Claude Code terminal visible for running the command

---

## Demo Flow (15–20 minutes)

### Step 1: Problem Statement (2 minutes)

**Say:**

> "Today, document teams spend significant time converting Word documents to DITA-XML format and updating brand terminology. This manual process is slow and error-prone. 
>
> This PoC tests whether we can automate the repeatable parts: conversion, terminology updates, and validation."

**Show:** A simple problem diagram (verbally or on screen):
```
Word Doc → Manual DITA Conversion → Manual Rebranding → Manual Validation → Approved
```

---

### Step 2: Show the Input (2 minutes)

**Show:** `sample-data/input/Gmail_Installation_Guide.docx`

**Say:**

> "This is a real example: a technical installation guide with headings, paragraphs, step-by-step lists, and tables. Our PoC focuses on structure, not formatting."

**Honest context:**

> "We're not claiming perfect formatting preservation. This is a PoC for feasibility, not a production system."

---

### Step 3: Show the Rules (2 minutes)

**Open:** `prototype/rebranding-rules.json`

**Say:**

> "These are our brand terminology rules. We can update brand language without touching the converter code. This example changes 'Gmail' to 'NewGmail' and similar terms.
>
> Rules are JSON—reviewable and editable by content owners without a developer."

**Scroll through a few rules** to show the structure.

---

### Step 4: Run the Pipeline (5 minutes)

**In Claude Code chat, run:**

```text
/pipeline sample-data/input/Gmail_Installation_Guide.docx
```

**Say while it runs:**

> "This single command orchestrates three steps:
>
> 1. **Converter:** Word → DITA-XML  
> 2. **Rebranding:** Apply terminology updates  
> 3. **Validator:** Check quality  
>
> All three run automatically, and output preserves the original filename for traceability."

**Watch the output.** Expected response from Claude Code:

```
SUCCESS: All validation checks passed.

Output files:
  - DITA (original):  sample-data/output/Gmail_Installation_Guide-output.dita
  - DITA (rebranded): sample-data/output/Gmail_Installation_Guide-rebranded.dita
```

---

### Step 5: Show the Outputs (3 minutes)

**Open:** `sample-data/output/Gmail_Installation_Guide-output.dita`

**Say:**

> "This is the converted DITA-XML. It has valid topic structure, headings as sections, paragraphs, tables—all semantically tagged."

**Point out:**
- XML declaration and DOCTYPE
- Root `<topic>` element
- Proper nesting of sections and paragraphs
- Tables converted to DITA table format

**Then open:** `sample-data/output/Gmail_Installation_Guide-rebranded.dita`

**Say:**

> "This is the rebranded version. Watch as I search for 'NewGmail'—the terminology rule was applied throughout."

**Perform a side-by-side comparison:**
- In output.dita: "Gmail"
- In rebranded.dita: "NewGmail"

**Say:**

> "The rebranding engine applied 77 replacements consistently. No other content was changed—just the terminology."

---

### Step 6: Show Validation (2 minutes)

**Show the validation output** from Claude Code (scroll back to see the report):

```
Validation Summary
Passed checks: 9
Failed checks: 0
Warnings: 4
Status: PASS with warnings
```

**Open:** `docs/quality-criteria.md`

**Say:**

> "Here's our quality criteria. This file explains what each check means:
>
> - **PASS:** The check succeeded. Example: 'Root topic element exists.'  
> - **WARN:** The check passed with a note worth reviewing. Example: 'DOCTYPE declaration missing, but DITA is still valid.'  
> - **FAIL:** The check failed. This would block the output in production."

**Explain the four warnings briefly:**
1. xmllint not installed (optional enhancement)
2. DOCTYPE declaration missing (but DITA is still valid)
3. Title placement (minor formatting note)
4. Empty paragraphs detection (non-blocking)

**Say:**

> "For this PoC, PASS with warnings is acceptable. In production, we'd make warnings into blockers."

---

### Step 7: Closing and Decision Ask (3–5 minutes)

**Summarize:**

> "In 15 minutes, we:
> 1. Took a real Word document
> 2. Converted it to valid DITA-XML
> 3. Applied controlled brand terminology updates
> 4. Validated the output against quality criteria
>
> All with a single command."

**Honesty:**

> "This is a working PoC, not production software. It proves the core workflow is automatable and that we can build quality controls around it."

**Ask for a decision:**

> "For next steps, we need your guidance on three options:
>
> 1. **Expand the PoC:** Test on more sample documents and refine the rules.  
> 2. **Plan production:** Fund a discovery phase to understand integration needs, batch processing, error handling.  
> 3. **Pause:** We can revisit when content owners provide stronger requirements or DITA acceptance criteria."

---

## Expected Questions and Answers

| Question | Answer |
|----------|--------|
| **Is this production-ready?** | No. It's a feasibility PoC. Production would need logging, error handling, batch support, and integration testing. |
| **Can it handle all Word documents?** | No. Current scope is representative samples with standard structure (headings, paragraphs, tables, lists). Special formatting, embedded objects, or custom styles would need additional work. |
| **How long is a conversion?** | Typical example (this Gmail guide): 30–60 seconds for all three steps combined. Speed scales with document size. |
| **Can the rules be changed without developers?** | Yes. Rules are JSON in `prototype/rebranding-rules.json`. Content owners can edit them directly without touching code. |
| **What's the quality gate?** | Validation script plus manual review using `docs/quality-criteria.md`. In production, this would be automated and gated. |
| **What would production need?** | Logging, error reporting, batch processing, UI/integration layer, stronger validation, integration with our documentation platform, and testing on hundreds of samples. |
| **How long would production take?** | Rough estimate: 4–6 months for discovery, implementation, testing, and launch. Depends on scope and platform integration requirements. |

---

## Demo Success Criteria

✓ Pipeline runs without errors in front of leaders  
✓ Final DITA output is visible and explainable  
✓ Rebranding changes are visible (term replacements)  
✓ Validation status is explained clearly  
✓ Limitations are stated plainly (not hidden)  
✓ Leaders understand the three-step workflow  
✓ Decision ask is clear (expand, plan, or pause)  

---

## If Something Breaks During the Demo

**Do not debug.** Instead:

1. **Show the error clearly:**
   ```
   FAILED: Step [1/2/3] - [Description]
   Command: [exact command that failed]
   ```

2. **Acknowledge it:**
   > "We hit an issue with the converter. Let me fall back to a previously generated output."

3. **Use backup outputs:**
   - Have `sample-data/expected_output/gmail-guide-expected.dita` available
   - Or have a screenshot of a successful run

4. **Continue the narrative:**
   > "Here's what a successful run produces. [Show the expected output.] You can see the same DITA structure, rebranding, and validation."

5. **Recover gracefully:**
   - Open `docs/quality-criteria.md`
   - Manually report 5 bullets (PASS, WARN, FAIL) based on what you know
   - Continue with the decision ask

---

## Backup Scenarios

### Scenario 1: Pipeline Fails

Use previously generated outputs from `sample-data/expected_output/` or take screenshots during earlier rehearsal.

### Scenario 2: Validation Fails

Open `docs/quality-criteria.md` and generate a 5-bullet summary of PASS/WARN/FAIL status based on the output.

### Scenario 3: Terminal Issues

Use manual commands as fallback:

```bash
python prototype/converter.py --input sample-data/input/Gmail_Installation_Guide.docx --output sample-data/output/Gmail_Installation_Guide-output.dita
python prototype/rebranding-engine.py --input sample-data/output/Gmail_Installation_Guide-output.dita --rules prototype/rebranding-rules.json --output sample-data/output/Gmail_Installation_Guide-rebranded.dita
bash prototype/validation-script.sh sample-data/output/Gmail_Installation_Guide-rebranded.dita
```

---

## Key Talking Points to Emphasize

1. **Automation is real:** One command replaces three manual steps.
2. **Rules are safe:** Brand terminology changes don't require code changes.
3. **Validation is measurable:** PASS/WARN/FAIL gives objective quality metrics.
4. **This is a PoC:** Honest about what it does and doesn't do.
5. **Next phase is clear:** Expand, plan, or pause—all viable paths.

---

## Demo Timing

| Step | Time |
|------|------|
| Problem statement | 2 min |
| Show input | 2 min |
| Show rules | 2 min |
| Run pipeline | 5 min |
| Show outputs | 3 min |
| Show validation & criteria | 2 min |
| Closing + decision ask | 3 min |
| **Total** | **19 min** |
| Q&A (optional) | 10 min |

---

## One-Liners for Leaders

- "One command converts, rebrands, and validates."
- "Rules are JSON—content owners can edit without developers."
- "This proves the workflow is automatable."
- "Quality gates are measurable: PASS, WARN, or FAIL."
- "Production would add logging, integration, and batch support."
