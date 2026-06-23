# Quality Criteria & Validation Checklist

**Owners:** Anshita Dhawan (Workflow Lead), Jayasree Nishanth (Domain Lead)  
**Status:** In Progress  
**Last Updated:** [DATE]

---

## What "Good Output" Looks Like

A successful Word → DITA conversion produces a DITA-XML file that:

1. **Is structurally valid** — Parses as XML, conforms to DITA schema
2. **Preserves content** — All source content present (100% completeness)
3. **Properly maps structure** — Headings → topics, lists → `<ol>/<ul>`, tables → `<table>`
4. **Is correctly rebranded** — All brand terms replaced per rules
5. **Passes automated checks** — Validation script reports ✓ PASS
6. **Is human-readable** — Can be reviewed and understood by domain experts

---

## Validation Tiers

### Tier 1: Structural Validity (MUST PASS)

**What:** Output is well-formed XML that matches DITA schema  
**Owner:** QA Lead (Dinil)

**Checks:**
- [ ] File is valid XML (no parse errors)
- [ ] Conforms to DITA Topic DTD (DOCTYPE declaration present)
- [ ] All tags properly nested (no unclosed tags)
- [ ] No special characters unescaped (e.g., `&` → `&amp;`)
- [ ] XML declaration present: `<?xml version="1.0" encoding="UTF-8"?>`

**Fail criteria:**
- Any XML parsing error
- Any DTD validation error

**Example PASS:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">
<topic id="sample-1">
  <title>My Document</title>
  <body>
    <p>Valid content.</p>
  </body>
</topic>
```

**Example FAIL:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<topic id="sample-1">  <!-- Missing DOCTYPE -->
  <title>My Document
  <body>  <!-- Title not closed -->
    <p>Content with & unescaped.</p>
  </body>
</topic>
```

---

### Tier 2: Content Completeness (MUST PASS)

**What:** All source content is present in output (no loss)  
**Owner:** Content Curator (Sirisha Dabiru), QA Lead (Dinil)

**Checks:**
- [ ] Paragraph count matches (± 10% for paragraph merging)
- [ ] All headings present
- [ ] All list items present
- [ ] All table rows/columns present
- [ ] All hyperlinks present
- [ ] No "[PLACEHOLDER]" or "[SKIPPED]" text in output
- [ ] Image references present (even if image files missing)

**Fail criteria:**
- Any paragraph lost
- Any heading lost
- More than 5% of content missing

**Measurement method:**
```
Source doc: 15 paragraphs, 4 headings, 2 tables (12 rows), 3 images
Output check:
- Paragraphs: 15 ✓ PASS
- Headings: 4 ✓ PASS
- Tables: 12 rows ✓ PASS
- Images: 3 references ✓ PASS
Overall: 100% content present ✓ PASS
```

---

### Tier 3: Structure Mapping (MUST PASS)

**What:** Word elements correctly map to DITA elements  
**Owner:** Domain Leads (Anshita, Jayasree), QA Lead (Dinil)

**Word → DITA Mapping Rules:**

| Word Element | DITA Element | Rules |
|--------------|--------------|-------|
| **Heading 1** | `<topic>` + `<title>` | One `<topic>` per document; title is first `<topic>` child |
| **Heading 2–3** | `<section>` + `<title>` | Nested `<section>` elements per heading level |
| **Paragraph** | `<p>` | Each paragraph is `<p>` (may merge short consecutive paras) |
| **Ordered List** | `<ol>` | Contains `<li>` items in order |
| **Unordered List** | `<ul>` | Contains `<li>` items (order irrelevant) |
| **Table** | `<table>` + `<tgroup>` + `<tbody>` | Rows as `<row>`, cells as `<entry>` |
| **Image** | `<image>` | href references filename; can be external |
| **Hyperlink** | `<xref>` or inline link | URL in href attribute |

**Checks:**
- [ ] Document has exactly one root `<topic>`
- [ ] `<topic>` has `<title>` as first child
- [ ] All `<section>` elements are inside `<body>` or other `<section>`
- [ ] All `<p>` elements inside `<body>` or `<section>`
- [ ] All lists properly structured (`<ol>`/`<ul>` → `<li>`)
- [ ] All tables have `<tgroup cols="N">` with proper `<thead>` and `<tbody>`
- [ ] No `<p>` elements inside `<section>` title (content should be in body)
- [ ] Image references use `<image href="filename"/>`
- [ ] Hyperlinks use `<xref href="url">` or inline markup

**Fail criteria:**
- Incorrect nesting (e.g., `<p>` outside body)
- Missing required elements (e.g., table without tgroup)
- Wrong element type (e.g., heading mapped to `<p>` instead of `<section>`)

**Example PASS:**
```xml
<topic id="doc1">
  <title>Document Title</title>
  <body>
    <p>Intro paragraph.</p>
    
    <section>
      <title>Section 1</title>
      <p>Content of section 1.</p>
      <ul>
        <li>Item 1</li>
        <li>Item 2</li>
      </ul>
    </section>
    
    <section>
      <title>Section 2</title>
      <table>
        <tgroup cols="2">
          <thead>
            <row>
              <entry>Col1</entry>
              <entry>Col2</entry>
            </row>
          </thead>
          <tbody>
            <row>
              <entry>Data1</entry>
              <entry>Data2</entry>
            </row>
          </tbody>
        </tgroup>
      </table>
    </section>
  </body>
</topic>
```

---

### Tier 4: Rebranding Accuracy (MUST PASS)

**What:** All brand terminology correctly replaced  
**Owner:** Builders (Sanjeev, Shashi), QA Lead (Dinil)

**Checks:**
- [ ] All old terms replaced with new terms
- [ ] Replacement count matches expected count (within ±1)
- [ ] No old terms remain in output text (grep for old terms returns 0 matches)
- [ ] New terms appear correct number of times
- [ ] Case sensitivity respected (e.g., "Brand" ≠ "brand" if rule is case-sensitive)

**Measurement method:**
```
Rebranding rules:
- "OldBrand" → "NewBrand" (case-sensitive)
- "oldfeature" → "newfeature" (case-insensitive)

Source doc contains:
- "OldBrand" 5 times
- "oldfeature" 3 times
- "OldFeature" 2 times (should not be replaced if rule is case-sensitive)

Expected output:
- "NewBrand" 5 times
- "newfeature" 3 times (all lowercase)
- "OldFeature" 2 times (unchanged)

Validation:
- grep "OldBrand" output.dita → 0 matches ✓ PASS
- grep "NewBrand" output.dita → 5 matches ✓ PASS
- grep "oldfeature" output.dita → 0 matches ✓ PASS
- grep "newfeature" output.dita → 3 matches ✓ PASS
```

**Fail criteria:**
- Any old term present in output (should be 0)
- Replacement count differs by > 1 from expected
- Case-sensitivity rules not respected

---

### Tier 5: Metadata & Identifiers (SHOULD PASS)

**What:** Identifiers and metadata are consistent  
**Owner:** Domain Leads (Anshita, Jayasree)

**Checks:**
- [ ] Document has unique `id` attribute on root `<topic>`
- [ ] All `<section>` elements have unique `id` attributes
- [ ] No duplicate IDs in output
- [ ] Source filename referenced in metadata or README
- [ ] Conversion timestamp or version noted (optional)

**Example:**
```xml
<topic id="sample-1-main">
  <title>Document Title</title>
  <body>
    <section id="sample-1-section-1">
      <title>Section 1</title>
      ...
    </section>
  </body>
</topic>
```

**Fail criteria:**
- Duplicate IDs (validator will detect)
- Missing IDs on key elements (acceptable as warning)

---

## Scoring & Pass Criteria

### Overall Quality Score

```
Score = (Tier1_Pass + Tier2_Pass + Tier3_Pass + Tier4_Pass + Tier5_Pass) / 5 * 100%

Tier 1 (Structural): MUST PASS (if fail → 0%)
Tier 2 (Content): MUST PASS (if fail → 0%)
Tier 3 (Structure): MUST PASS (if fail → 0%)
Tier 4 (Rebranding): MUST PASS (if fail → 0%)
Tier 5 (Metadata): SHOULD PASS (if fail → 80%)
```

### Pass/Fail Determination

| Score | Status | Action |
|-------|--------|--------|
| 100% | ✓ EXCELLENT | Ready for demo |
| 90–99% | ✓ GOOD | Ready for demo (minor notes) |
| 80–89% | ⚠ ACCEPTABLE | Document workarounds; ready with caveats |
| < 80% | ✗ FAIL | Converter needs fixes; do not use |

---

## Test Matrix Template

**For each sample document:**

| Sample | Structural Valid | Content Complete | Structure Mapped | Rebranding 100% | Metadata OK | Overall Score | Status | Notes |
|--------|-----------------|------------------|------------------|-----------------|------------|---|--------|-------|
| sample-1 | ✓ | ✓ | ✓ | ✓ | ✓ | 100% | ✓ PASS | Ready for demo |
| sample-2 | ✓ | ✓ | ✓ | ✓ | ⚠ | 90% | ✓ PASS | Tables partially skipped (see edge cases) |
| sample-3 | ✓ | ✓ | ✓ | ✓ | ✓ | 100% | ✓ PASS | Ready for demo |

**Document in:** `/validation/test-results.md`

---

## Known Acceptable Deviations

These items are **acceptable failures for PoC** (document in edge cases, don't block pass):

- [ ] Images are referenced but files not found (placeholder href)
- [ ] Merged table cells skipped (log warning, continue conversion)
- [ ] Complex formatting (italics, colors) not preserved
- [ ] Bullet style numbers not preserved (style → bullet only)
- [ ] Hyperlinks with complex formatting may lose styling
- [ ] Footnotes/endnotes not converted (logged as skipped)

**Key rule:** If content is present but formatting is degraded, it's acceptable. If content is lost, it's a FAIL.

---

## Validation Commands

**Manual checks (Domain Leads):**
```bash
# Check if XML is valid
xmllint output.dita

# Count old vs. new terms
grep -o "OldBrand" output.dita | wc -l
grep -o "NewBrand" output.dita | wc -l

# Check for "[PLACEHOLDER]" markers
grep -i placeholder output.dita
```

**Automated checks (QA):**
```bash
bash prototype/validation-script.sh -f output.dita
```

---

## Sign-Off

Domain Leads confirm quality criteria:

- [ ] **Anshita Dhawan** — Structure mapping rules approved
- [ ] **Jayasree Nishanth** — Quality scoring method approved

Project Owner confirms acceptance:

- [ ] **Samyak-M** — Quality criteria finalized

---

**Last updated:** [DATE]  
**Next review:** 25 June 2026
