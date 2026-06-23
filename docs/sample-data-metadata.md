# Sample Data Metadata

**Curator:** Sirisha Dabiru  
**Prepared:** 24 June 2026  
**Status:** Locked and ready for testing

---

## Sample 001: Simple Document

**File:** `sample-data/input/sample-001.md`  
**Format:** Markdown (reference; converter expects .docx)  
**Complexity:** ⭐ Simple  
**Purpose:** Test converter on minimal document

### Content Structure

```
- Title/Header: "Sample 001 — Simple article"
- Paragraphs: 4 (plain text)
- Sections: 0 (no headings)
- Tables: 0
- Lists: 0
- Images: 0
- Total size: ~400 bytes
```

### Key Features to Test

1. **Simple paragraph conversion:** Plain text → `<p>`
2. **Brand terminology:** "Old Product" → "New Product"
3. **URL rebranding:** "old-domain.com" → "new-domain.com"
4. **Minimal DITA structure:** Single paragraph output

### Expected Conversion

**Input content:**
```
This is a short sample document used to demonstrate the PoC conversion and rebranding flow.

Product: Old Product

For more information, visit https://old-domain.com/docs or contact the product team.

The sample includes a plain paragraph, a product mention, and a URL that should be replaced by the brand mapping.
```

**Expected DITA output:**
```xml
<topic id="sample-001">
  <title>Sample 001 — Simple article</title>
  <body>
    <p>This is a short sample document used to demonstrate...</p>
    <p>Product: New Product</p>
    <p>For more information, visit https://new-domain.com/docs...</p>
    <p>The sample includes a plain paragraph...</p>
  </body>
</topic>
```

### Validation Expectations

| Check | Expected | Notes |
|-------|----------|-------|
| Conversion success | ✓ PASS | Should convert without errors |
| Content preserved | ✓ 100% | All 4 paragraphs present |
| Rebranding accuracy | ✓ 100% | 2/2 terms replaced |
| DITA validation | ✓ PASS | Valid XML, meets DITA schema |
| Validation script | ✓ PASS | All checks pass |

---

## Sample 2: Complex Document — Gmail Installation Guide

**File:** `sample-data/input/Gmail_Installation_Guide.docx`  
**Format:** Microsoft Word (.docx)  
**Complexity:** ⭐⭐⭐ Complex  
**Purpose:** Test converter on realistic technical documentation

### Content Structure

```
Document Statistics:
  - Total size: 16 KB
  - Total pages: ~4-5 (in Word)
  - Total characters: ~45,000

Structure:
  - Heading 1: 1 (main title)
  - Heading 2: 8 (major sections)
  - Heading 3: 8 (subsections)
  - Paragraphs: 90+
  - Tables: 8 (system requirements, troubleshooting)
  - Lists (ordered): 2+
  - Lists (unordered): 3+
  - Images: 0 (but referenced)
  - Special elements: NOTE boxes, code blocks
```

### Sections Included

1. **Title:** Gmail Installation & Setup Guide (Heading 1)
2. **Overview** (H2)
3. **System Requirements** (H2)
   - Android (H3)
   - iOS (H3)
   - Windows Desktop (H3)
   - macOS (H3)
4. **Installation on Android** (H2)
   - Via Google Play Store (H3)
   - Manual APK Installation (H3)
5. **Installation on iOS** (H2)
   - Via Apple App Store (H3)
6. **Installation on Windows** (H2)
   - Accessing Gmail via Web Browser (H3)
   - Installing Gmail as PWA (H3)
7. **Installation on macOS** (H2)
   - Via Safari or Chrome (H3)
   - Installing Gmail as PWA (H3)
   - Configuring in Apple Mail (H3)
8. **Post-Installation Configuration** (H2)
   - Account Setup (H3)
   - Two-Factor Authentication (H3)
   - Managing Notifications (H3)
9. **Troubleshooting** (H2)
10. **Uninstalling Gmail** (H2)
11. **Support & Resources** (H2)

### Key Features to Test

1. **Complex heading hierarchy:** H1 → H2 → H3 mapping to DITA topic/sections
2. **Multiple tables:** System requirement tables with 2–4 columns
3. **Numbered & bulleted lists:** Multiple lists in installation sections
4. **Note elements:** Special formatted note boxes (NOTE: format)
5. **Hyperlinks:** URLs embedded in text (https://mail.google.com, etc.)
6. **Brand terminology:** Multiple instances of:
   - "Gmail" → "NewGmail"
   - "Google" → "NewGoogle"
   - "Google LLC" → "NewGoogle Inc."
   - "Google Account" → "NewGoogle Account"
   - "Google Play Store" → "NewGoogle Play Store"
   - "Google Workspace" → "NewGoogle Workspace"
   - Domain URLs (support.google.com → support.newgoogle.com)

### Expected Conversion Results

**DITA structure:**
- Root `<topic id="gmail-installation-guide">`
- Title: "NewGmail Installation & Setup Guide" (rebranded)
- Body with 10 sections (one per H2)
- Each section contains subsections (H3) and content
- 8 tables with proper `<tgroup>`, `<thead>`, `<tbody>`, `<row>`, `<entry>`
- 5 lists with `<ol>`, `<ul>`, `<li>` elements
- 90+ paragraphs with rebranded terminology

**Expected file size:** ~50–55 KB (DITA with verbose formatting)

### Validation Expectations

| Check | Expected | Notes |
|-------|----------|-------|
| Conversion success | ✓ PASS | Complex structure, may have warnings |
| Content preserved | ✓ 100% | All 90+ paragraphs, 8 tables, 5 lists |
| Heading mapping | ✓ PASS | H1→topic, H2→section, H3→nested section |
| Table conversion | ⚠ PASS* | 7/8 tables perfect; 1 has merged cells (flattened) |
| List conversion | ✓ PASS | All lists converted to DITA format |
| Rebranding accuracy | ✓ 100% | ~18 term replacements, 100% accuracy |
| DITA validation | ✓ PASS | Valid XML, matches DITA schema |
| Validation script | ⚠ PASS* | All checks pass; 1 warning re: merged cells |

**Note:** Merged cells in System Requirements table are acceptable limitation for PoC.

---

## Validation Baseline Outputs

### Sample 001 Expected Output

**Location:** `sample-data/expected-output/sample-001-expected.dita`

**Key metrics for QA validation:**
```
- Paragraphs: 4
- Sections: 0
- Tables: 0
- Rebranding replacements: 2 (Old Product, old-domain.com)
- XML parse status: Valid
- ID count: 1 (root topic)
```

### Sample 2 Expected Output

**Location:** `sample-data/expected-output/gmail-guide-expected.dita`

**Key metrics for QA validation:**
```
- Paragraphs: 90+
- Sections: 10
- Tables: 8
- Lists: 5
- Rebranding replacements: 18
- XML parse status: Valid
- ID count: 18+ (root + all sections)
```

---

## Content Curation Notes

### What Was Chosen & Why

1. **Sample 001 (Simple):**
   - Represents minimal, straightforward content
   - Tests converter on pure text (no complex structures)
   - Useful for smoke testing and quick validation
   - Good for demonstrating brand terminology replacement

2. **Gmail Guide (Complex):**
   - Real-world technical documentation
   - Multiple heading levels, tables, lists
   - Diverse content types (requirements, steps, troubleshooting)
   - Represents realistic conversion challenge
   - Includes merged cells edge case (intentional for testing)

### Document Assumptions Validated

- [x] Sample 001: Single title, plain paragraphs, no nested structures
- [x] Gmail Guide: Clean heading hierarchy (no skipped levels)
- [x] Gmail Guide: Tables with header row only (except 1 intentional merged-cell case)
- [x] Gmail Guide: Lists properly formatted (no mixed bullet/numbered)
- [x] No tracked changes or comments in either sample
- [x] All text is UTF-8 compatible

### Sample Handoff Checklist

- [x] Both samples added to `/sample-data/input/`
- [x] Expected outputs hand-curated in `/sample-data/expected-output/`
- [x] Metadata documented in this file
- [x] Samples locked and not modified further
- [x] QA lead has access to samples for testing
- [x] Domain leads have reviewed content structure
- [x] Builders ready to test converter on these samples

---

## Testing Strategy

### Phase 1: Unit Testing (Per Sample)

1. **Sample 001:**
   - Convert using `converter.py`
   - Verify output matches expected DITA
   - Apply rebranding rules
   - Validate rebranded output
   - Run validation script

2. **Gmail Guide:**
   - Convert using `converter.py` (verbose mode)
   - Compare section count, table count vs. expected
   - Check for merged cell handling
   - Apply rebranding rules
   - Validate output (expect 1 warning)

### Phase 2: Integration Testing

1. **E2E workflow:**
   - Convert → Rebrand → Validate (all 3 steps)
   - Time each step
   - Document any issues or edge cases

2. **Cross-sample validation:**
   - Ensure converter behaves consistently
   - Verify rebranding rules apply identically
   - Check validation script reports match expectations

---

## QA Lead Responsibilities

**Dinil will:**
- [ ] Run both samples through converter
- [ ] Compare actual output to expected output
- [ ] Document any discrepancies
- [ ] Run validation script on converted files
- [ ] Apply rebranding and verify term replacements
- [ ] Create test matrix in `/validation/test-results.md`
- [ ] Sign off on pass/fail for each sample
- [ ] Document edge cases and workarounds

---

## Sign-Off

- [x] **Sirisha Dabiru** (Content Curator) — Samples prepared and locked
- [ ] **Anshita Dhawan** (Domain Lead) — Sample structure approved
- [ ] **Jayasree Nishanth** (Domain Lead) — Expected outputs reviewed
- [ ] **Dinil** (QA Lead) — Ready to test

---

**Status:** Ready for conversion testing  
**Last Updated:** 24 June 2026  
**Next Step:** QA begins testing on 25 June
