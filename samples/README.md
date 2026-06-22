# Sample Data & Test Inputs

This folder contains representative sample documents used for the proof-of-concept and demo.

## Structure

```
samples/
├── input/                      # Input documents (various formats)
├── expected_output/            # Expected output after transformation
└── brand_terminology.json      # Brand term mapping database
```

## Input Samples

Place representative input documents here. Examples:

- `sample-001-simple-article.docx` — Simple technical article in Word format
- `sample-002-marketing-copy.html` — Marketing content with brand terms
- `sample-003-metadata.docx` — Document with metadata to preserve
- `sample-004-messy-formatting.docx` — Document with complex formatting

**Criteria for good samples:**
- Representative of real documentation workflows
- Include realistic edge cases (formatting, structure, terminology)
- Varied enough to test key scenarios
- Realistic size and complexity

## Expected Output Samples

For each input sample, provide the expected transformed output:

- `sample-001-expected.xml` — Expected DITA-XML output
- `sample-002-expected.html` — Expected rebranded HTML
- `sample-003-expected.xml` — Expected DITA with normalized metadata
- `sample-004-expected.html` — Expected cleaned output

These serve as validation targets for the QA team.

## Brand Terminology Mapping

**File:** `brand_terminology.json`

Example structure:
```json
{
  "brand_terms": [
    {
      "old_term": "Old Product Name",
      "new_term": "New Product Name",
      "context": "General product references",
      "regex": false
    },
    {
      "old_term": "old-domain\\.com",
      "new_term": "new-domain.com",
      "context": "URL replacement",
      "regex": true
    },
    {
      "old_term": "Legacy System",
      "new_term": "Modern Platform",
      "context": "System names",
      "regex": false
    }
  ]
}
```

## Usage

1. **For Prototype Development:**
   - Use `/input/` samples to build and test the conversion logic
   - Compare actual output to `/expected_output/` samples

2. **For Validation:**
   - Run PoC on all input samples
   - Compare results to expected outputs
   - Document pass/fail results in `/validation/results_log.md`

3. **For Demo:**
   - Use diverse samples to show different capabilities
   - Include before/after visualizations
   - Demonstrate realistic workflows

---

## Adding New Samples

When adding a new sample:

1. **Place input file** in `/input/` with clear naming: `sample-NNN-description.ext`
2. **Create expected output** in `/expected_output/` with same number: `sample-NNN-expected.ext`
3. **Document the sample** in the appropriate test scenario in `/validation/test_scenarios.md`
4. **Commit both files** together with a clear message

Example commit:
```
git add samples/input/sample-005-complex-tables.docx
git add samples/expected_output/sample-005-expected.xml
git commit -m "Add sample 005: Complex table structures for validation"
```

---

## Confidentiality & Permissions

If using real customer or confidential documents:
- Redact sensitive information before committing
- Add a note referencing the original location (e.g., "Based on internal doc XYZ")
- Get approval before committing if required
- Link to access permissions or references in the commit message

---

**Last Updated:** 22 June 2026  
**Owner:** Content & Data Curators  
**Next Update:** Wed, 24 Jun 2026 (Discovery milestone)