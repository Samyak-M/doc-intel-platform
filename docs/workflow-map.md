# Workflow Mapping: Word → DITA Conversion & Rebranding

**Owners:** Anshita Dhawan (Workflow Lead), Jayasree Nishanth (Domain Lead)  
**Status:** In Progress  
**Last Updated:** [DATE]

---

## Current State: Manual Process

```
1. Source Document (Word)
   ↓
2. [MANUAL] Parse structure, extract content
   ↓
3. [MANUAL] Create DITA structure, map headings/tables/images
   ↓
4. [MANUAL] Apply brand terminology (find-replace, 10+ terms)
   ↓
5. [MANUAL] Review & validate conversion quality
   ↓
6. Output DITA-XML (approved)
```

**Pain points:**
- Steps 2–5 are purely manual
- Error-prone (missed terms, bad structure)
- ~4 hours per document (varies with complexity)
- No automated validation

---

## Desired Future State: Automated Conversion + Validation

```
1. Source Document (Word)
   ↓
2. [AUTOMATED] converter.py parses .docx structure
   ↓
3. [AUTOMATED] converter.py generates DITA-XML structure
   ↓
4. [AUTOMATED] rebranding-engine.py applies terminology mapping
   ↓
5. [AUTOMATED] validation-script.sh checks output quality
   ↓
6. Output: DITA-XML + validation report
   ↓
7. [MANUAL] Review exceptions & edge cases (if any)
   ↓
8. Final Output DITA-XML (approved)
```

**Improvements:**
- Steps 2–5 fully automated (< 2 min per document)
- Consistent terminology application
- Automated quality checks catch errors
- Manual step only for edge cases

---

## Conversion Flow Details

### Step 1: Input Preparation

**Owner:** Content Curator (Sirisha Dabiru)

**Input requirements:**
- Clean Word document (.docx format)
- Clear heading hierarchy (no skipped levels)
- No merged table cells
- Images referenced by filename (or extracted)

**Checklist before conversion:**
- [ ] Heading 1 = document title
- [ ] Heading 2–3 properly nested
- [ ] All lists formatted with list styles
- [ ] Tables have header row only
- [ ] Images are embedded or referenced clearly
- [ ] No tracked changes or comments

---

### Step 2: Parse Word Structure (converter.py)

**Owner:** Builder 1 (Sanjeev Patra)

**Input:** Word .docx file  
**Output:** Python object representing document structure

**Process:**
```python
1. Load .docx using python-docx library
2. Iterate through paragraphs, tables, images
3. Extract text, style (heading level), and metadata
4. Map Word styles to DITA semantics:
   - Heading 1 → <topic>
   - Heading 2–3 → <section>
   - List styles → <ol> or <ul>
   - Table → <table>
   - Image → <image>
5. Create nested structure (topic + sections)
6. Return JSON representation
```

**Edge cases to handle:**
- Empty headings → skip or warn
- Skipped heading levels → flatten or warn
- Complex tables → log as warning, skip cell
- Missing image references → placeholder reference

---

### Step 3: Generate DITA-XML (converter.py)

**Owner:** Builder 1 (Sanjeev Patra)

**Input:** Python structure from Step 2  
**Output:** Valid DITA-XML file

**DITA Structure:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
<topic id="unique-id">
  <title>Document Title</title>
  <body>
    <p>Introductory paragraph...</p>
    
    <section>
      <title>Section 1</title>
      <p>Content...</p>
      <table>
        <tgroup cols="2">
          <thead>
            <row>
              <entry>Header 1</entry>
              <entry>Header 2</entry>
            </row>
          </thead>
          <tbody>
            <row>
              <entry>Data</entry>
              <entry>Data</entry>
            </row>
          </tbody>
        </tgroup>
      </table>
    </section>
  </body>
</topic>
```

**Validation checks:**
- Valid XML schema
- All required DITA elements
- Proper nesting (no orphans)
- Unique IDs for all topics/sections

---

### Step 4: Apply Rebranding (rebranding-engine.py)

**Owner:** Builder 2 (Shashi Prabha)

**Input:** DITA-XML file + rebranding-rules.json  
**Output:** Rebranded DITA-XML file

**Rebranding rules format:**
```json
{
  "terminology_mappings": [
    { "old": "OldBrand", "new": "NewBrand", "case_sensitive": true },
    { "old": "legacy-feature", "new": "current-feature", "case_sensitive": false },
    { "old": "outdated", "new": "updated", "regex": false }
  ]
}
```

**Process:**
```python
1. Load DITA-XML into memory (XML parser)
2. Load rebranding rules from JSON
3. For each rule:
   - Search all text nodes in DITA-XML
   - Apply replacement (respecting case_sensitive, regex flags)
   - Log replacements made
4. Write updated DITA-XML
5. Generate replacement report (term → count)
```

**Edge cases:**
- Term appears in XML tags (skip)
- Term is partial match in larger word (warn)
- Multiple rules conflict (apply in order, log)
- No matches found (warn if > 10% of expected)

---

### Step 5: Validate Output (validation-script.sh)

**Owner:** QA Lead (Dinil)

**Input:** Rebranded DITA-XML file + expected output (for comparison)  
**Output:** Validation report (pass/fail/warnings)

**Validation checks:**
```bash
✓ XML is well-formed (no parsing errors)
✓ Matches DITA schema (topic.dtd)
✓ All required elements present (<topic>, <title>, <body>)
✓ No orphaned content (every <p> in <body> or <section>)
✓ All IDs are unique
✓ All sections properly titled
✓ Table structure is valid
✓ Brand terminology applied (matches expected count)
✓ No placeholder text remains (e.g., "[IMAGE]")
```

**Output format:**
```
=== Validation Report: sample-1-rebranded.dita ===
Status: PASS
- XML structure: ✓ Valid
- DITA schema: ✓ Conformant
- Brand terms: ✓ 15/15 replaced (expected: 15)
- Warnings: None
- Pass rate: 100%

=== Validation Report: sample-2-rebranded.dita ===
Status: PASS with warnings
- XML structure: ✓ Valid
- DITA schema: ✓ Conformant
- Brand terms: ✓ 12/12 replaced
- Warnings:
  - Table 1: Row 3 skipped (merged cells)
  - Image: "logo.png" referenced but not found
- Pass rate: 95%
```

---

### Step 6–7: Review & Approval (Manual)

**Owner:** Domain Lead (Jayasree Nishanth), Content Curator (Sirisha Dabiru)

**Process:**
1. QA shares validation report
2. Review any WARNINGS (not PASS items)
3. Decide: Accept as-is or request converter improvements
4. Document decision (e.g., "Skip merged cells; acceptable for PoC")
5. Approve final output

---

## Quality Criteria & Success Metrics

**See:** `/docs/quality-criteria.md`

Key metrics:
- **Conversion speed:** < 2 min per document
- **Accuracy:** 95%+ of content correctly mapped
- **Completeness:** 100% of source content present in output
- **Terminology:** 100% of brand terms correctly replaced
- **Validation pass rate:** 90%+ on test samples

---

## Team Checkpoints & Review Gates

| Date | Checkpoint | Owner | Pass Criteria |
|------|-----------|-------|---------------|
| Wed 24 Jun | Sample data locked | Curators | 2–3 representative docs ready |
| Fri 27 Jun | Converter skeleton | Builders | Can parse Word → JSON structure |
| Fri 27 Jun | Rebranding config | Builders | rules.json with 10+ terms |
| Mon 30 Jun | Converter complete | Builders | Passes on all samples |
| Mon 30 Jun | Scope frozen | Owner | No new features after this |
| Wed 2 Jul | Test matrix complete | QA | All samples tested & documented |

---

## Assumptions & Constraints

**Assumptions:**
- Word documents follow standard structure (no custom formats)
- DITA output is single-document (no topic fragments)
- Metadata is limited to title + source filename
- No complex styling (italics, colors) need to be preserved

**Constraints:**
- Python 3.8+ required (not Python 2)
- python-docx library used (no alternatives)
- Rebranding rules are static JSON (not dynamic database)
- No multi-language support in PoC

---

## Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Word doc structure is inconsistent | Converter fails on some samples | Curators validate samples; Owner reviews before conversion |
| DITA schema validation too strict | Rebranding blocks on schema errors | Use permissive schema; document any violations |
| Rebranding rules incomplete | Some terms missed in output | QA creates comprehensive term list; Curators validate |
| Sample data not representative | Real docs fail post-PoC | Curators collect diverse samples (simple, complex, branded) |

---

## Dependencies & Hand-offs

```
Curators → Builders: Sample data + assumptions.md (by Wed 24 Jun)
Builders → QA: converter.py + rebranding-engine.py (by Fri 27 Jun)
QA → Domain Leads: test-results.md (by Mon 30 Jun)
Domain Leads → Owner: sign-off on approach (by Mon 30 Jun)
All → Demo Lead: final demo materials (by Wed 2 Jul)
```

---

## Next Steps

1. [ ] Finalize assumptions with team (Tue 23 Jun kickoff)
2. [ ] Lock sample data (Wed 24 Jun)
3. [ ] Define DITA structure in detail (see `/docs/assumptions.md`)
4. [ ] Create rebranding rules baseline (see `/prototype/rebranding-rules.json`)
5. [ ] Set up git repo with above docs (done by Mon 22 Jun)

---

**Owner Sign-off:**

- [ ] Anshita Dhawan — Workflow defined
- [ ] Jayasree Nishanth — Quality criteria defined
- [ ] Samyak-M — Workflow approved

---

**Last updated:** [DATE]  
**Next review:** 24 June 2026
