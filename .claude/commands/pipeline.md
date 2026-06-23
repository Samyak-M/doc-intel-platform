---
description: "Run the Word to DITA conversion pipeline — convert, rebrand, and validate."
---

## Role
You are an AI agent operating the Document Intelligence Platform pipeline.

## Task
Run the Word to DITA conversion pipeline sequentially for the input Word document provided in `$ARGUMENTS`.

## Context
The input `.docx` file path is supplied through `$ARGUMENTS`. The pipeline converts the document to DITA-XML, applies brand terminology updates, and validates the final output.

## Constraints
- Execute the steps in order and do not skip any step.
- Stop and report the failing command if a step fails.
- If validation fails, read `docs/quality-criteria.md` and report `PASS`, `WARN`, or `FAIL` in exactly 5 bullet points.
- Use the exact commands shown below.

## Output
Report each pipeline step and its result.

## Steps

1. Convert

```bash
python prototype/converter.py --input $ARGUMENTS --output sample-data/output/out.dita
```

2. Rebrand

```bash
python prototype/rebranding-engine.py --input sample-data/output/out.dita --rules prototype/rebranding-rules.json --output sample-data/output/out-rebranded.dita
```

3. Validate

```bash
bash prototype/validation-script.sh -f sample-data/output/out-rebranded.dita
```
