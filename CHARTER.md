# Document Converter & Rebranding PoC - Project Charter

**Project Owner:** Samyak-M  
**Timeline:** 22 June – 05 July 2026  
**Roster:** 7 people (1 owner + 6 members)

---

## Problem Statement

Documentation teams spend significant time manually converting Word documents to DITA-XML format and applying brand terminology updates. This manual process is error-prone and slow, blocking migration of legacy content to structured documentation systems.

**Specific pain points:**
- Word → DITA conversion requires manual restructuring
- Brand terminology cleanup happens separately, creating quality gaps
- No validation mechanism to catch conversion errors

---

## Target Users

- **Documentation teams** needing to migrate from Word to DITA-XML
- **Content managers** responsible for brand terminology compliance
- **Technical writers** managing rebranding across large document sets

---

## Scope: What We're Building

**In scope:**
- Automated Word (.docx) to DITA-XML conversion
- Brand terminology rebranding engine (search-replace with mapping rules)
- Quality validation checklist for output
- Demonstration on 2–3 representative samples

**Out of scope:**
- Full production platform or UI
- Every document type (focus on text, headings, tables, basic images)
- Custom styling preservation
- Multi-language support

---

## Expected Outputs

**Code:**
- `converter.py`: Word → DITA parser using python-docx
- `rebranding-engine.py`: Terminology mapping and replacement
- `validation-script.sh`: Test runner and quality check

**Documentation:**
- Workflow diagram (input → conversion → review → output)
- Quality criteria & assumptions
- README with setup, usage, and limitations

**Demo assets:**
- 2–3 before/after sample transformations
- Test results matrix (what passed, what failed)
- Honest learnings and recommendations for next phase

---

## Success Criteria

✓ **Demonstrable end-to-end flow:** Converter runs on real sample data  
✓ **Quality validation:** Test matrix shows pass/fail for all samples  
✓ **Edge cases documented:** Team knows what doesn't work  
✓ **Repo well-organized:** Charter, roster, workflow, code, tests all clear  
✓ **Team alignment:** All 7 members understand scope and blockers  

---

## Key Dates

| Milestone | Date | Owner |
|-----------|------|-------|
| Charter, repo, roles assigned | Mon 22 June | Samyak-M |
| Sample data locked | Wed 24 June | Curators + Owner |
| First PoC (end-to-end demo) | Fri 27 June | Builders |
| Scope frozen | Mon 30 June | Samyak-M |
| Demo package ready | Wed 2 July | All |
| Full dry-run | Fri 4 July | All |
| Live presentation | Sun 5 July | All |

---

## Decision: Repo Location

Using existing repo: **doc-intel-platform** (main branch)  
New subdirectory: `/prototype/document-converter/`

---

## Assumptions

- Team has access to Python environment + Cursor IDE
- Sample Word documents are representative of real conversion needs
- DITA-XML structure is fixed (not custom per client)
- Brand terminology list is available or will be curated by Week 1

---

## What Success Looks Like (Post-Demo)

A working, tested prototype that:
- Converts a sample Word doc to valid DITA-XML in < 2 minutes
- Applies brand terminology rules consistently
- Passes quality validation on 70%+ of test cases
- Is documented enough for another team to understand next steps
- Gives stakeholders honest insight into effort for production version
