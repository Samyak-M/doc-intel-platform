# Sample Data

This folder contains the input documents, expected outputs, and terminology samples used by the Document Intelligence PoC.

## Structure

```text
sample-data/
|-- input/
|   |-- Gmail_Installation_Guide.docx
|   `-- sample-001.md
|-- expected_output/
|   |-- gmail-guide-expected.dita
|   `-- sample-001-expected.dita
`-- brand_terminology.json
```

The pipeline writes generated files to `sample-data/output/`.

## Primary Demo Input

Use this file for the main leader demo:

```text
sample-data/input/Gmail_Installation_Guide.docx
```

It is the best current sample because it exercises the Word-to-DITA converter and produces a visible DITA output for review.

## Expected Outputs

Expected outputs are manual reference baselines:

- `sample-data/expected_output/gmail-guide-expected.dita`
- `sample-data/expected_output/sample-001-expected.dita`

Use them for manual comparison during QA. The current PoC does not include an automated diff gate.

## Brand Rules

The active rebranding rules used by the pipeline are in:

```text
prototype/rebranding-rules.json
```

`sample-data/brand_terminology.json` is retained as sample/reference terminology data.

## Adding New Samples

When adding a new sample:

1. Add the input file under `sample-data/input/`.
2. Add a matching expected DITA output under `sample-data/expected_output/`.
3. Document the sample purpose in `docs/sample-data-metadata.md`.
4. Run the pipeline and record results in `validation/test-results.md`.
5. Avoid committing confidential customer content unless it has been approved and sanitized.
