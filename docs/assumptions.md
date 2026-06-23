# Word → DITA Conversion Assumptions & Mapping Rules

**Owners:** Content Curator (Sirisha Dabiru), Domain Leads (Anshita Dhawan, Jayasree Nishanth)  
**Status:** Draft — To be confirmed at kickoff (Tue 23 June)  
**Last Updated:** [DATE]

---

## Purpose

This document defines **how Word elements convert to DITA elements** for this PoC. These rules are confirmed with real sample documents and may be refined based on what the samples actually contain.

---

## Assumptions About Input (Word Documents)

### Document Structure

- **Single document focus:** Each Word file represents one standalone document
- **Clean heading hierarchy:** Heading 1 (title) → Heading 2 (main sections) → Heading 3 (subsections)
  - No skipped levels (e.g., Heading 1 → Heading 3)
  - No Heading 4 or deeper (treated as Heading 3)
- **One title per document:** Exactly one Heading 1 at document start
- **No fragmentation:** No split chapters or linked documents

### Paragraphs & Text

- **Paragraph style:** Most text uses "Normal" or "Body Text" style
- **No complex formatting:** Colors, fonts, sizes not semantically important
- **Formatting to ignore:** Italics, bold, underline, highlighting (not preserved in DITA output)
- **Hyperlinks:** Preserved as `<xref>` elements with URLs intact
- **Special characters:** All text is UTF-8 compatible

### Lists

- **Ordered lists:** Use "List Number" or "Numbered List" style (preserved as `<ol>`)
- **Unordered lists:** Use "Bullet List" or "Unordered List" style (preserved as `<ul>`)
- **No nested lists:** Nesting allowed but flattened if complex
- **No mixed styles:** Each list is uniform (all ordered or all unordered)

### Tables

- **Simple structure:** No merged cells (or merged cells skipped with warning)
- **Header row:** First row is always header (becomes `<thead>`)
- **Data rows:** Remaining rows are data (become `<tbody>`)
- **Column count:** Consistent across all rows
- **Column width:** Not preserved (width info lost in DITA)
- **Cell content:** Text only; no nested tables, images, or complex formatting

### Images

- **Embedded images:** Extracted and referenced by filename
- **Image paths:** Stored in separate `/assets/` folder
- **References:** DITA uses `<image href="filename.png"/>`
- **Metadata:** Alt text preserved if available

### Metadata

- **Author:** Not extracted (not needed for PoC)
- **Created/Modified dates:** Not extracted
- **Document properties:** Title extracted from Heading 1
- **File name:** Referenced in conversion log

---

## Word → DITA Mapping Rules

### Headings

| Word Level | DITA Element | DITA Hierarchy | Example |
|------------|--------------|----------------|---------|
| Heading 1 | `<topic>` + `<title>` | Root element; first topic | "Product Overview" → root topic |
| Heading 2 | `<section>` + `<title>` | Direct child of `<body>` | "Features" → first-level section |
| Heading 3 | `<section>` + `<title>` | Nested within Heading 2 section | "Advanced Features" → nested section |
| Heading 4+ | Treated as Heading 3 | No deeper nesting | Flattened to level 3 |

**Rule:** One `<topic>` per document (PoC scope). Multi-document support is future work.

**Example:**
```
Word structure:
  Heading 1: "Product Guide"
    Heading 2: "Installation"
      Heading 3: "Prerequisites"
      Heading 3: "Steps"
    Heading 2: "Usage"

DITA structure:
  <topic id="product-guide">
    <title>Product Guide</title>
    <body>
      <section id="installation">
        <title>Installation</title>
        <section id="prerequisites">
          <title>Prerequisites</title>
        </section>
        <section id="steps">
          <title>Steps</title>
        </section>
      </section>
      <section id="usage">
        <title>Usage</title>
      </section>
    </body>
  </topic>
```

---

### Paragraphs

| Word Element | DITA Element | Rules |
|--------------|--------------|-------|
| Normal paragraph | `<p>` | One paragraph per line break |
| Multiple blank lines | Single `<p>` | Whitespace normalized (max 1 blank line between paras) |
| Indented text | `<p>` | Indentation ignored (no `<lq>` for PoC) |

**Rule:** Consecutive short paragraphs (< 20 words) may be merged into one `<p>` for clarity.

**Example:**
```
Word text:
  "This is paragraph 1."
  [blank line]
  "This is paragraph 2."

DITA output:
  <p>This is paragraph 1.</p>
  <p>This is paragraph 2.</p>
```

---

### Lists

#### Ordered Lists (Numbered)

| Word Element | DITA Element | Rules |
|--------------|--------------|-------|
| Numbered list | `<ol>` | Each item becomes `<li>` |
| List item | `<li>` | Text content preserved; numbering auto-generated |

**Rule:** Numbering style (1, 2, 3 vs. a, b, c) not preserved; DITA uses default decimal numbering.

**Example:**
```
Word:
  1. First step
  2. Second step
  3. Third step

DITA:
  <ol>
    <li>First step</li>
    <li>Second step</li>
    <li>Third step</li>
  </ol>
```

#### Unordered Lists (Bullets)

| Word Element | DITA Element | Rules |
|--------------|--------------|-------|
| Bulleted list | `<ul>` | Each item becomes `<li>` |
| List item | `<li>` | Text content preserved; bullet style auto-generated |

**Rule:** Bullet style (•, -, ◦) not preserved; DITA uses default bullet style.

**Example:**
```
Word:
  • Item A
  • Item B
  • Item C

DITA:
  <ul>
    <li>Item A</li>
    <li>Item B</li>
    <li>Item C</li>
  </ul>
```

---

### Tables

#### Table Structure

| Word Element | DITA Element | Rules |
|--------------|--------------|-------|
| Table | `<table>` | Top-level element for table |
| Table with headers | `<tgroup cols="N">` | N = number of columns |
| Header row | `<thead>` | First row only |
| Data rows | `<tbody>` | All rows after header |
| Table row | `<row>` | One per row |
| Table cell | `<entry>` | One per cell |

**Rule:** First row is always treated as header. If document doesn't follow this, it must be cleaned before conversion.

**Example:**
```
Word table:
  | Name | Age | City |
  |------|-----|------|
  | Alice | 30 | NYC |
  | Bob | 25 | LA |

DITA output:
  <table>
    <tgroup cols="3">
      <colspec colname="col1"/>
      <colspec colname="col2"/>
      <colspec colname="col3"/>
      <thead>
        <row>
          <entry>Name</entry>
          <entry>Age</entry>
          <entry>City</entry>
        </row>
      </thead>
      <tbody>
        <row>
          <entry>Alice</entry>
          <entry>30</entry>
          <entry>NYC</entry>
        </row>
        <row>
          <entry>Bob</entry>
          <entry>25</entry>
          <entry>LA</entry>
        </row>
      </tbody>
    </tgroup>
  </table>
```

#### Table Limitations

| Situation | Action | Why |
|-----------|--------|-----|
| Merged cells | Skip or flatten (log warning) | DITA `<entry>` doesn't support rowspan/colspan |
| Table with no header | Treat first row as header | PoC assumes all tables have headers |
| Nested tables | Skip inner table (log warning) | DITA doesn't support nested tables in this PoC |
| Table with images | Skip image, keep text | Images in cells not supported; content preserved |

---

### Images

| Word Element | DITA Element | Rules |
|--------------|--------------|-------|
| Embedded image | `<image>` | Reference by filename |
| Image alt text | `@alt` attribute | Preserved if available |
| Image path | `@href` attribute | Points to `/assets/` folder |

**Rule:** Images are extracted to `/sample-data/assets/` and referenced by filename.

**Example:**
```
Word:
  [Embedded image: logo.png, alt text: "Company Logo"]

DITA:
  <image href="assets/logo.png" alt="Company Logo"/>
```

**Limitations:**
- Image size/scaling not preserved
- Captions not converted (treated as paragraph text before image)

---

### Hyperlinks

| Word Element | DITA Element | Rules |
|--------------|--------------|-------|
| External URL | `<xref href="URL">` | Full URL preserved |
| Email link | `<xref href="mailto:email">` | Converted to mailto link |
| Bookmark/anchor | `<xref href="#anchor">` | Internal reference |
| Link text | Link text preserved | Shown to user |

**Example:**
```
Word:
  Click here for more info (hyperlinked to https://example.com)

DITA:
  Click <xref href="https://example.com">here</xref> for more info
```

---

### Special Elements (Not Converted)

These Word elements are **not converted** for PoC (logged as skipped):

| Word Element | Reason | Workaround |
|--------------|--------|-----------|
| Footnotes/endnotes | Not part of DITA topic structure | Add as appendix manually post-conversion |
| Comments/tracked changes | Editorial metadata, not content | Remove before conversion |
| Page breaks | Not relevant in DITA (flow-based) | Ignored; logical breaks via sections |
| Headers/footers | Not content; typically metadata | Document name added to metadata only |
| Text boxes | Not standard DITA | Convert as paragraphs or sections |
| Shapes/drawings | No direct DITA equivalent | Replace with description text or reference |
| Charts/graphs | Not text-based | Replace with image reference or description |

---

## Brand Terminology Mapping

### Assumptions

- **Static rules:** Terminology mappings defined once in `/prototype/rebranding-rules.json`
- **Global replacement:** All occurrences of old term → new term across document
- **Case handling:** Rules specify case-sensitive (exact match) or case-insensitive
- **Regex support:** Optional regex patterns for complex replacements

### Example Rebranding Rules

```json
{
  "terminology_mappings": [
    {
      "old": "OldBrand",
      "new": "NewBrand",
      "case_sensitive": true,
      "description": "Main brand name (exact case)"
    },
    {
      "old": "legacy-feature",
      "new": "current-feature",
      "case_sensitive": false,
      "description": "Feature name (any case)"
    },
    {
      "old": "Product v1.0",
      "new": "Product v2.0",
      "case_sensitive": true,
      "regex": false,
      "description": "Version number"
    }
  ]
}
```

### Rebranding Behavior

| Situation | Rule | Example |
|-----------|------|---------|
| Exact match (case-sensitive) | Replace | "OldBrand" → "NewBrand" (yes); "oldbrand" → not replaced |
| Case-insensitive | Replace all cases | "oldfeature", "OldFeature", "OLDFEATURE" → "newfeature" (all lowercase) |
| Partial match | May cause issues | "Old" in "OldBrand" won't be replaced separately; only full "OldBrand" replaced |
| In XML tags | Skip | `<xref href="oldbrand.html">` — href attribute not modified (keep links intact) |
| Zero matches | Log warning | If rule expects 10 replacements but finds 0, flag for review |

---

## Validation & Quality Checks

### Pre-Conversion Checklist (Content Curator)

Before samples are locked, verify:

- [ ] Document has exactly one Heading 1 (title)
- [ ] No skipped heading levels
- [ ] All lists properly formatted (no mixed styles)
- [ ] Tables have header row only
- [ ] No merged cells in tables
- [ ] Images are embedded or referenced clearly
- [ ] No tracked changes or comments
- [ ] File is saved in .docx format (not .doc)
- [ ] File is readable and not password-protected

### Post-Conversion Checks (QA)

After conversion, verify:

- [ ] Output is valid XML
- [ ] Headings map to correct DITA levels
- [ ] All content present (paragraph count matches)
- [ ] All images referenced
- [ ] All links functional
- [ ] Brand terminology applied correctly

See `/docs/quality-criteria.md` for full validation matrix.

---

## Deviation Log

When a sample doesn't follow these assumptions, document it here:

| Sample | Assumption | Deviation | Decision | Outcome |
|--------|-----------|-----------|----------|---------|
| sample-2 | "No merged cells" | Table 1 has merged header | Skip merged row, flatten | Partial loss of structure; acceptable for PoC |
| sample-3 | "One Heading 1" | Two Heading 1s (mistake in Word doc) | Use first as topic title; second as section | Content preserved; note for future |

---

## Future Enhancements

Post-PoC, consider:

1. **Multi-document support:** Split large documents into topic maps
2. **Formatting preservation:** Support italics, bold, colors in DITA markup
3. **Nested lists:** Handle multi-level bullet lists
4. **Complex tables:** Support merged cells, table headers in all rows
5. **Metadata extraction:** Capture author, dates, custom properties
6. **Footnotes/endnotes:** Convert to DITA `<fn>` elements
7. **Captions:** Map image/table captions to DITA `<fig>` elements

---

## Sign-Off

- [ ] **Sirisha Dabiru** (Content Curator) — Assumptions confirmed with samples
- [ ] **Anshita Dhawan** (Domain Lead) — Mapping rules approved
- [ ] **Jayasree Nishanth** (Domain Lead) — Quality expectations set
- [ ] **Samyak-M** (Owner) — Assumptions finalized

---

**Last updated:** [DATE]  
**Next review:** 25 June 2026 (after converter prototype)
