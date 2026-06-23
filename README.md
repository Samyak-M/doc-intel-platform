# Document Converter & Rebranding PoC

**Status:** Proof of Concept (22 June – 05 July 2026)  
**Owner:** Samyak-M  
**Team:** 7 members (see [roster.md](./roster.md))

---

## The Problem

Documentation teams manually convert Word documents to DITA-XML and update brand terminology separately—a slow, error-prone process. This PoC automates both workflows to show feasibility and effort.

---

## What This PoC Does

✓ **Converts** Word (.docx) files to DITA-XML  
✓ **Rebrand** terminology using configurable JSON mapping  
✓ **Validates** output against quality criteria  
✓ **Documents** edge cases and workarounds  

---

## What This PoC Does NOT Do

✗ Production UI or platform  
✗ Full styling/formatting preservation  
✗ All document types (focus: text, headings, tables, basic images)  
✗ Multi-language support

---

## Quick Start

### Prerequisites

- Python 3.8+
- `pip install python-docx`
- Git (to clone repo)

### Installation

```bash
git clone https://github.com/Samyak-M/doc-intel-platform.git
cd doc-intel-platform/prototype/document-converter
pip install -r requirements.txt
```

### Run Converter on Sample Data

```bash
# Convert one sample Word file to DITA-XML
python converter.py --input sample-data/input/sample-1.docx --output sample-data/output/sample-1.dita

# Apply rebranding rules
python rebranding-engine.py --input sample-data/output/sample-1.dita --rules prototype/rebranding-rules.json --output sample-data/output/sample-1-rebranded.dita

# Run validation tests
bash prototype/validation-script.sh
```

---

## Project Structure

```
doc-intel-platform/
├── charter.md                    ← One-page project scope & success criteria
├── roster.md                     ← Team roles and responsibilities
├── README.md                     ← You are here
│
├── /docs
│   ├── workflow-map.md           ← Input → conversion → review → output
│   ├── quality-criteria.md       ← What "good output" looks like
│   ├── assumptions.md            ← Mapping rules (headings, tables, images)
│   ├── sample-metadata.md        ← Notes on each sample Word doc
│   └── /meetings
│       └── 2026-06-22-kickoff.md ← Kickoff notes & decisions
│
├── /sample-data
│   ├── /input                    ← Original Word documents
│   │   ├── sample-1.docx
│   │   ├── sample-2.docx
│   │   └── sample-3.docx
│   └── /expected-output          ← Hand-curated expected DITA-XML
│       ├── sample-1.dita
│       ├── sample-2.dita
│       └── sample-3.dita
│
├── /prototype
│   ├── converter.py              ← Word → DITA parser
│   ├── rebranding-engine.py      ← Terminology mapping logic
│   ├── rebranding-rules.json     ← Brand term mappings
│   ├── validation-script.sh      ← Test runner
│   └── requirements.txt          ← Python dependencies
│
└── /validation
    ├── test-results.md           ← Pass/fail matrix
    ├── edge-cases.md             ← Known limitations & workarounds
    └── test-summary.md           ← Overall quality score
```

---

## How to Use: Step by Step

### 1. Prepare Your Word Document

Organize your document with:
- Clear heading hierarchy (Heading 1, Heading 2, etc.)
- Simple tables (no merged cells recommended)
- Brand terms to be updated (e.g., "OldBrand" → "NewBrand")

### 2. Configure Rebranding Rules

Edit `/prototype/rebranding-rules.json`:

```json
{
  "terminology_mappings": [
    { "old": "OldBrand", "new": "NewBrand" },
    { "old": "legacy-term", "new": "current-term" },
    { "old": "OutdatedFeature", "new": "UpdatedFeature" }
  ]
}
```

### 3. Run Conversion

```bash
python converter.py --input your-doc.docx --output your-doc.dita
```

**Output:** DITA-XML file with structure:
- `<topic>` wrapper with unique ID
- `<title>` extracted from heading
- `<body>` with `<p>` for paragraphs, `<table>` for tables
- Metadata preservation where possible

### 4. Apply Rebranding

```bash
python rebranding-engine.py --input your-doc.dita --rules prototype/rebranding-rules.json --output your-doc-rebranded.dita
```

### 5. Validate Output

```bash
bash prototype/validation-script.sh your-doc-rebranded.dita
```

**Validation checks:**
- Valid XML structure
- All required DITA elements present
- Headings properly mapped
- Brand terminology correctly applied
- No orphaned content

---

## Conversion Details

### Word Structure → DITA-XML

| Word Element | DITA Element | Notes |
|--------------|--------------|-------|
| Heading 1 | `<topic>` + `<title>` | Creates top-level topic |
| Heading 2–3 | `<section>` + `<title>` | Creates nested sections |
| Paragraph | `<p>` | Plain text, no formatting |
| Ordered List | `<ol>` | Converted with `<li>` items |
| Unordered List | `<ul>` | Converted with `<li>` items |
| Table | `<table>` | Rows, columns, basic headers |
| Image | `<image>` | Referenced by filename; requires separate assets folder |
| Hyperlink | `<xref>` | URL embedded in href attribute |

### Assumptions & Limitations

**See full details:** `/docs/assumptions.md`

Key assumptions:
- Heading hierarchy is clean (no skipped levels)
- Tables don't have merged cells
- Images are not embedded; referenced by path
- No comments, tracked changes, or complex formatting

---

## Sample Outputs

See `/sample-data/expected-output/` for before/after examples:

- **sample-1.docx** → `sample-1.dita` — Simple 1–2 page doc with basic structure
- **sample-2.docx** → `sample-2.dita` — Complex multi-section doc with tables
- **sample-3.docx** → `sample-3.dita` — Doc with brand terminology to update

---

## Test Results & Known Issues

**Validation Summary:** See `/validation/test-summary.md`

| Sample | Converter | Rebranding | Validation | Status |
|--------|-----------|------------|-----------|--------|
| sample-1 | ✓ Pass | ✓ Pass | ✓ Pass | Ready |
| sample-2 | ⚠ Partial | ✓ Pass | ⚠ Warnings | See edge cases |
| sample-3 | ✓ Pass | ✓ Pass | ✓ Pass | Ready |

**Known Limitations:**

1. **Nested tables** — Not supported; converter will flatten or skip
2. **Embedded images** — Must be extracted manually; converter references by filename
3. **Complex formatting** — Italics, bold, colors not preserved in DITA
4. **Merged cells** — Table converter will fail; manual cleanup required

See `/validation/edge-cases.md` for full list and workarounds.

---

## Next Steps (Post-PoC)

Based on learnings from this PoC, next phase should:

1. **Handle edge cases** — Build robust error handling for tables, images, metadata
2. **Add UI/API** — Expose converter via web interface or REST API
3. **Integrate with platforms** — Connect to docs CMS, version control, approval workflows
4. **Scale to production** — Batch processing, logging, auditing

See `/docs/demo-narrative.md` for full recommendations.

---

## Team Roles & Who to Contact

| Role | Name | Handles |
|------|------|---------|
| **Owner** | Samyak-M | Overall coordination, scope, timeline |
| **Workflow Lead** | Anshita Dhawan | DITA structure, quality criteria |
| **Domain Lead** | Jayasree Nishanth | Validation, workflow mapping |
| **Builder 1** | Sanjeev Patra | Converter logic (converter.py) |
| **Builder 2** | Shashi Prabha | Rebranding logic (rebranding-engine.py) |
| **Content Curator** | Sirisha Dabiru | Sample data, expected outputs |
| **QA Lead** | Dinil | Testing, validation, edge cases |

---

## How to Contribute

1. **Clone or pull the latest main branch**
2. **Create a feature branch:** `git checkout -b feature/your-feature`
3. **Make changes** and test locally
4. **Commit with clear messages:** `git commit -m "Add Word table parsing support"`
5. **Push and open a pull request** to main
6. **Tag your role lead** for review

---

## Meetings & Checkpoints

- **Kickoff:** Tue 23 June, 2:00 PM IST — Confirm roles, discuss blockers
- **Weekly standup:** Mon/Wed/Fri, 9:00–9:15 AM IST — 15-min sync
- **Code review:** Thu 25, Thu 2 — Builders + Owner
- **Final rehearsal:** Fri 4 July, 10:00 AM IST — Full dry-run
- **Presentation:** Sun 5 July, 3:00 PM IST — Live demo

See `/docs/meetings/` for agendas and notes.

---

## Questions?

- **Scope questions** → Ask Samyak-M (Owner)
- **DITA structure** → Ask Anshita Dhawan or Jayasree Nishanth
- **Converter code** → Ask Sanjeev Patra
- **Rebranding logic** → Ask Shashi Prabha
- **Sample data** → Ask Sirisha Dabiru
- **Testing/validation** → Ask Dinil

---

## License & Attribution

This PoC is internal to [Your Organization]. All sample data is confidential.

---

**Last updated:** 21 June 2026  
**Next review:** 24 June 2026
