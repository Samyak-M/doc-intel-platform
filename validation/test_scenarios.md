# Validation & QA Test Scenarios

This document defines the test cases and scenarios for validating the proof-of-concept.

## Test Scenario Template

```
### Scenario N: [Short Description]

**Objective:** What are we testing?

**Input:** 
- Document type: [e.g., Word .docx]
- Content: [Description]
- Sample location: `/samples/input/sample-NNN-*`

**Expected Output:**
- Format: [e.g., DITA-XML]
- Key transformations: [List]
- Location: `/samples/expected_output/sample-NNN-*`

**Acceptance Criteria:**
- [ ] Output format is correct
- [ ] Brand terminology is applied
- [ ] Metadata is preserved/normalized
- [ ] No content loss
- [ ] Validation report generated

**Status:** Pending / In Progress / Passed / Failed  
**Notes:** Any observations or edge cases
```

---

## Test Scenarios

### Scenario 1: Basic Word Document to DITA-XML

**Objective:** Test basic conversion of a simple Word document to DITA-XML format.

**Input:**
- Document type: Microsoft Word (.docx)
- Content: Simple technical article with heading, paragraphs, bullet points
- Sample location: `/samples/input/sample-001-simple-article.docx`

**Expected Output:**
- Format: DITA-XML (.xml)
- Key transformations:
  - Heading → `<title>`
  - Paragraphs → `<p>`
  - Bullet points → `<ul>/<li>`
- Location: `/samples/expected_output/sample-001-expected.xml`

**Acceptance Criteria:**
- [ ] Output is valid DITA-XML
- [ ] Structure is preserved
- [ ] All text content is present
- [ ] Formatting is normalized

**Status:** Pending  
**Notes:** TBD

---

### Scenario 2: Brand Terminology Replacement

**Objective:** Test that brand terminology is consistently replaced across a document.

**Input:**
- Document type: HTML file
- Content: Marketing copy with outdated brand terms
- Sample location: `/samples/input/sample-002-marketing-copy.html`

**Expected Output:**
- Format: HTML (.html)
- Key transformations:
  - "Old Product Name" → "New Product Name"
  - "old-url.com" → "new-url.com"
- Location: `/samples/expected_output/sample-002-expected.html`

**Acceptance Criteria:**
- [ ] All brand terms are replaced
- [ ] No accidental replacements in URLs or code
- [ ] Content meaning preserved
- [ ] Validation report shows term mapping

**Status:** Pending  
**Notes:** TBD

---

### Scenario 3: Metadata Normalization

**Objective:** Test that document metadata is preserved and normalized.

**Input:**
- Document type: Word document with custom metadata
- Metadata: Author, creation date, custom properties
- Sample location: `/samples/input/sample-003-metadata.docx`

**Expected Output:**
- Format: DITA-XML with metadata headers
- Key transformations:
  - Custom metadata → standardized properties
  - Dates normalized to ISO 8601
- Location: `/samples/expected_output/sample-003-expected.xml`

**Acceptance Criteria:**
- [ ] Metadata is extracted
- [ ] Dates are in ISO 8601 format
- [ ] All metadata is preserved
- [ ] Validation report lists metadata

**Status:** Pending  
**Notes:** TBD

---

### Scenario 4: Complex Formatting Cleanup

**Objective:** Test that complex formatting is cleaned up appropriately.

**Input:**
- Document type: Word document with inconsistent formatting
- Content: Mixed fonts, colors, line spacing, etc.
- Sample location: `/samples/input/sample-004-messy-formatting.docx`

**Expected Output:**
- Format: Normalized HTML or DITA-XML
- Key transformations:
  - Consistent font and size
  - Logical emphasis (bold/italic preserved, color removed)
  - Normalized spacing
- Location: `/samples/expected_output/sample-004-expected.html`

**Acceptance Criteria:**
- [ ] Logical formatting is preserved
- [ ] Unnecessary formatting is removed
- [ ] Output is clean and readable
- [ ] Validation report notes cleanup actions

**Status:** Pending  
**Notes:** TBD

---

## Edge Cases to Consider

- [ ] Very large documents (10,000+ words)
- [ ] Documents with images and embedded media
- [ ] Documents with tables and complex structures
- [ ] Documents with special characters or Unicode
- [ ] Multiple columns or nested lists
- [ ] Hyperlinks and cross-references
- [ ] Footnotes and endnotes
- [ ] Comments and tracked changes

## Known Limitations (To Be Documented)

[As validation proceeds, document what works well and what doesn't]

---

## Test Results Log

See `results_log.md` for detailed test execution results.

---

**Status:** Test scenarios being finalized  
**Owner:** Validation / QA Lead  
**Last Updated:** 22 June 2026