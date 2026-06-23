# Team Roster & Role Assignments

**Project:** Document Converter & Rebranding PoC  
**Owner:** Samyak-M (Technical Writer)  
**Total Team:** 7 (1 owner + 6 members)  
**Date Assigned:** 21 June 2026

---

## Team Members & Roles

### Owner
| Name | Role | Responsibilities |
|------|------|------------------|
| **Samyak-M** | Project Owner & Coordinator | Overall timeline, scope management, blocker removal, demo rehearsal |

---

### Workflow & Domain Leads (2)

| Name | Role | Key Deliverables |
|------|------|------------------|
| **Anshita Dhawan** | Workflow Lead #1 | Map real doc transformation workflow; define DITA structure requirements |
| **Jayasree Nishanth** | Domain Lead #2 | Define quality criteria; validate conversion accuracy; create validation checklist |

**What they own:**
- `/docs/workflow-map.md` — Input → conversion → review → output flow diagram
- `/docs/quality-criteria.md` — Checklist for "good output" (metadata, formatting, structure)
- `/docs/assumptions.md` — Document how headings, tables, images, metadata should map
- Kickoff facilitation: Review charter, confirm scope with team

---

### Prototype Builders (2)

| Name | Role | Key Deliverables |
|------|------|------------------|
| **Sanjeev Patra** | Builder #1 – Converter | Build Word → DITA parser; handle python-docx integration |
| **Shashi Prabha** | Builder #2 – Rebranding | Build rebranding engine; create terminology mapping logic; write validation script |

**What they own:**
- `/prototype/converter.py` — Word .docx → DITA-XML conversion logic
- `/prototype/rebranding-engine.py` — Brand terminology search-replace with JSON mapping
- `/prototype/validation-script.sh` — Automated test runner
- Use **Cursor IDE + Claude skills** for rapid iteration
- Weekly code review with Owner

---

### Content & Data Curator (1)

| Name | Role | Key Deliverables |
|------|------|------------------|
| **Sirisha Dabiru** | Content Curator | Collect realistic sample Word docs; create expected DITA outputs; validate data quality |

**What they own:**
- `/sample-data/input/` — 2–3 Word documents (simple, complex, branded)
- `/sample-data/expected-output/` — Hand-curated expected DITA-XML for each sample
- `/docs/sample-metadata.md` — Metadata, complexity notes for each sample
- Coordinate with Domain Leads on output structure
- **By Wed 24 June:** Samples locked and committed to repo

---

### Validation & QA Lead (1)

| Name | Role | Key Deliverables |
|------|------|------------------|
| **Dinil** | QA & Validation Lead | Test converter on all samples; document pass/fail; identify edge cases |

**What they own:**
- `/validation/test-results.md` — Test matrix (input → output → expected → pass/fail)
- `/validation/edge-cases.md` — Converter fails on [X], workaround is [Y]
- `/validation/test-summary.md` — Overall quality score and blockers
- Create test matrix by Wed 24 June
- Run comprehensive tests by Mon 30 June
- Present validation findings in final demo

---

## Role Rotation Backup

In case of absence:

- **Anshita** (Workflow Lead) ← Jayasree backup
- **Jayasree** (Domain Lead) ← Anshita backup
- **Sanjeev** (Converter Builder) ← Shashi backup
- **Shashi** (Rebranding Builder) ← Sanjeev backup
- **Sirisha** (Content Curator) ← Owner can backfill for short-term
- **Dinil** (QA) ← Owner can backfill for short-term

---

## Weekly Check-In Schedule

- **Mon 22, Wed 24, Fri 27, Mon 30, Wed 2, Fri 4** — 15-min standup (9:00–9:15 AM)
- **Owner + Builders** — Code review + blocker removal (Thu 25, Thu 2)
- **Full team** — Final rehearsal (Fri 4)

---

## Status

- [x] Roster assigned
- [ ] Each member confirms role + availability (by EOB Tue 23 June)
- [ ] Kickoff meeting scheduled (Tue/Wed 23–24 June)
