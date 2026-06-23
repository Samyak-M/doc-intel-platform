# Leader Demo Guide: Document Intelligence PoC

Use this guide to give a clear, repeatable demo to leaders. The goal is to show business value, not every implementation detail.

## Demo Outcome

By the end of the demo, leaders should understand:

- The current manual Word-to-DITA and rebranding workflow can be partially automated.
- Brand terminology updates can be controlled through rules.
- Validation gives the team an objective quality checkpoint.
- The PoC is ready for structured feedback, not production rollout.

## Before the Demo

1. Open the repo in Claude Code or Cursor.
2. Confirm the demo machine uses Python 3.10 or 3.11, not Python 3.14.
3. On Windows, confirm Git Bash is installed for the validation step.
4. Confirm dependencies are installed:

```bash
pip install -r prototype/requirements.txt
```

3. Delete old generated outputs if they exist, or explain that the demo will overwrite them:

```text
sample-data/output/out.dita
sample-data/output/out-rebranded.dita
```

4. Open these files in editor tabs:

- `sample-data/input/Gmail_Installation_Guide.docx`
- `prototype/rebranding-rules.json`
- `docs/quality-criteria.md`
- `.claude/commands/pipeline.md`

Do not run skill-creator during the leader demo. The demo should use the already-created `/pipeline` command. Skill-creator is only for preparing or improving reusable marketplace skills outside the live demo flow.

## Demo Script

### Step 1: State the Problem

Say:

"Today, document teams spend time converting Word content to DITA, updating brand language, and checking quality manually. This PoC tests whether we can automate the repeatable parts."

### Step 2: Show the Input

Show:

```text
sample-data/input/Gmail_Installation_Guide.docx
```

Explain:

- This is the source Word document.
- The PoC focuses on headings, paragraphs, lists, tables, and terminology.
- It does not claim perfect production-grade formatting preservation.

### Step 3: Show the Rules

Open:

```text
prototype/rebranding-rules.json
```

Explain:

- Brand terms are controlled in JSON.
- Updating rules does not require changing converter code.
- The same rule file can be reviewed by content or brand owners.

### Step 4: Run the Pipeline

Preferred Claude Code command:

```text
/pipeline sample-data/input/Gmail_Installation_Guide.docx
```

Manual fallback:

```bash
python prototype/converter.py --input sample-data/input/Gmail_Installation_Guide.docx --output sample-data/output/out.dita
python prototype/rebranding-engine.py --input sample-data/output/out.dita --rules prototype/rebranding-rules.json --output sample-data/output/out-rebranded.dita
bash prototype/validation-script.sh -f sample-data/output/out-rebranded.dita
```

### Step 5: Show the Outputs

Open:

```text
sample-data/output/out.dita
sample-data/output/out-rebranded.dita
```

Point out:

- DITA topic structure was generated.
- Terminology updates were applied.
- Output is text-based, reviewable, and compatible with downstream DITA workflows.

### Step 6: Show Validation

Show the terminal validation result and open:

```text
docs/quality-criteria.md
```

Explain:

- PASS means no failed checks.
- WARN means the PoC found something to review but still completed.
- FAIL means the output should not be accepted without investigation.

### Step 7: Close With the Decision Ask

Ask leaders for one of these decisions:

- Continue PoC with more sample documents.
- Fund a production discovery phase.
- Pause until content owners provide stronger DITA acceptance criteria.

## Expected Questions and Practical Answers

| Question | Answer |
| --- | --- |
| Is this production ready? | No. It is a working PoC for feasibility and workflow validation. |
| Can it process all Word files? | No. Current scope is representative samples with basic structure. |
| Can rules be changed without code? | Yes. Rebranding rules live in `prototype/rebranding-rules.json`. |
| What is the quality gate? | `prototype/validation-script.sh` plus manual review using `docs/quality-criteria.md`. |
| What would production need? | More samples, stronger validation, logging, batch processing, error reporting, and integration with the content platform. |

## Demo Success Criteria

- Pipeline completes in front of leaders.
- Final DITA output is visible.
- Rebranding is visible in the output.
- Validation status is explained clearly.
- Limitations are stated plainly.

## Backup Plan

If the live run fails:

1. Do not debug deeply during the leadership demo.
2. Show the command that failed.
3. Open `docs/quality-criteria.md`.
4. Report the status in exactly five bullets using PASS, WARN, or FAIL.
5. Continue with the previously generated or expected output file if available.
