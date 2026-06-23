# Kickoff Meeting – Document Converter & Rebranding PoC

**Date:** Tue 23 June 2026, 2:00–3:00 PM IST  
**Host:** Samyak-M  
**Attendees:** All 7 team members (6 members + 1 owner)  
**Agenda:** Confirm roles, review charter & scope, identify blockers

---

## Meeting Objective

By end of meeting, all team members:
- Understand the PoC problem and scope
- Confirm their role and deliverables
- Know key dates and checkpoints
- Can identify blockers early

---

## Agenda (60 minutes)

### 1. Welcome & Context (5 min)

**Owner** opens meeting:

- Brief story: Why are we building this? (Word → DITA manual conversion is slow)
- What success looks like: Working PoC that demonstrates feasibility
- Timeline: 2 weeks to demo (22 June – 5 July)
- Team composition: 7 people, 6 distinct roles

---

### 2. Charter Review (5 min)

**Owner** walks through `/charter.md`:

**Key points:**
- Problem: Manual Word → DITA conversion + brand rebranding
- Scope: PoC, not production
- Success criteria: Demo end-to-end on 2–3 samples
- Out of scope: UI, all doc types, custom styling

**Team question:** Any unclear points?

---

### 3. Roles & Responsibilities (10 min)

**Owner** reviews `/roster.md`. Each person confirms:

- **Name & role**
- **Key deliverables** (what they're building/creating)
- **Handoff timeline** (when do others depend on my work?)

**For each role, ask:**

- "Do you understand the deliverables?"
- "Any concerns about timeline or dependencies?"

**Role-specific notes:**

1. **Anshita Dhawan** (Workflow Lead)
   - Owns: workflow-map.md, quality-criteria.md
   - Deadline: Wed 24 June (draft), Mon 30 June (final)
   - Handoff to: Jayasree (review), Builders (reference for conversion rules)

2. **Jayasree Nishanth** (Domain Lead)
   - Owns: assumptions.md, quality sign-off
   - Deadline: Wed 24 June, Mon 30 June
   - Handoff to: Builders, QA (testing criteria)

3. **Sanjeev Patra** (Builder – Converter)
   - Owns: converter.py (Word → DITA logic)
   - Deadline: Fri 27 June (skeleton), Mon 30 June (complete)
   - Handoff to: QA (testing)
   - Tool: Cursor IDE + Claude

4. **Shashi Prabha** (Builder – Rebranding)
   - Owns: rebranding-engine.py, rebranding-rules.json
   - Deadline: Fri 27 June (rules + skeleton), Mon 30 June (complete)
   - Handoff to: QA (testing)
   - Tool: Cursor IDE + Claude

5. **Sirisha Dabiru** (Content Curator)
   - Owns: sample-data/ (input Word docs + expected DITA outputs)
   - Deadline: Wed 24 June (samples locked)
   - Handoff to: Builders (test data), QA (validation baseline)
   - Key: Sample quality determines test quality

6. **Dinil** (QA & Validation)
   - Owns: test-results.md, edge-cases.md
   - Deadline: Fri 27 June (first tests), Mon 30 June (comprehensive)
   - Handoff to: Owner (sign-off), Demo Lead (presentation)
   - Key: Must identify what works AND what fails honestly

---

### 4. Critical Dates & Checkpoints (5 min)

Walk through timeline:

| Checkpoint | Owner | What | Status |
|-----------|-------|------|--------|
| **Wed 24 Jun** | Curators | Samples locked | Blocker if missed |
| **Fri 27 Jun** | Builders | Converter skeleton + Rebranding rules | First demo internally |
| **Mon 30 Jun** | Owner | Scope frozen | No new features after |
| **Mon 30 Jun** | All | Comprehensive testing | QA sign-off |
| **Wed 2 Jul** | All | Demo package ready | Dry-run prep |
| **Fri 4 Jul** | All | Full dry-run | Last chance to fix |
| **Sun 5 Jul** | All | Live presentation | Go/no-go decision |

**Key rule:** If a date is missed, escalate to Owner immediately. Don't try to catch up alone.

---

### 5. Deliverables & Code Repos (5 min)

**Where does work go?**

- **Code:** `/prototype/` directory
- **Docs:** `/docs/` directory
- **Samples:** `/sample-data/` directory
- **Tests:** `/validation/` directory

**How to contribute:**

```bash
git clone https://github.com/Samyak-M/doc-intel-platform.git
cd doc-intel-platform
git checkout main
git pull
git checkout -b feature/your-feature
# Make changes
git commit -m "Clear message"
git push origin feature/your-feature
# Open PR
```

**Code review:** Owner or relevant lead reviews before merge to main.

---

### 6. Blocker Identification & Removal (15 min)

**Now's the time to flag issues early.**

For each person, ask:

1. **"Do you have everything you need to start?"**
   - Access to code editors?
   - Python environment?
   - Sample data (for Builders)?
   - DITA schema docs (for Domain Leads)?

2. **"What could slow you down?"**
   - Unclear requirements?
   - Dependency on someone else's work?
   - Technical setup issues?
   - Time availability?

3. **"How can we unblock you?"**

**Common blockers & solutions:**

| Blocker | Solution | Owner |
|---------|----------|-------|
| "I don't know Python" | Cursor + Claude can help; no expert Python needed | Builders + Owner |
| "DITA structure unclear" | Domain Leads will clarify in assumptions.md | Jayasree + Anshita |
| "Sample data not ready" | Owner can provide placeholder samples | Sirisha + Owner |
| "Need access to repo" | Owner adds SSH key or GitHub access | Owner |
| "Unclear what 'good output' looks like" | See quality-criteria.md; ask Domain Leads | Jayasree + Anshita |

**Document blockers:** Owner captures in meeting notes.

---

### 7. Weekly Sync & Communication (5 min)

**How do we stay connected?**

- **Weekly standup:** Mon/Wed/Fri, 9:00–9:15 AM IST (15 min)
  - Each person: 1–2 sentences on progress + blockers
- **Slack/Teams channel:** For async updates between syncs
- **Code review:** Thursdays (Builders + Owner, 15 min)
- **Final rehearsal:** Fri 4 July, 10:00 AM IST (1 hour)

**Escalation path:**
1. If stuck, ask your role lead (e.g., Builders → ask Owner)
2. If still stuck, escalate to Owner
3. Owner escalates to project organizers if needed

---

### 8. Questions & Clarifications (10 min)

**Open floor:**

- "What if my sample Word doc has merged cells?"
- "Can I use JavaScript instead of Python?"
- "What if the converter takes 5 minutes instead of 2?"
- "Do we need to handle footnotes?"

**Owner notes:** Clarify and update docs if needed.

---

### 9. Closing (5 min)

**Owner recap:**

- "We're building a Word → DITA converter PoC in 2 weeks"
- "Success = working demo on real samples + honest learnings"
- "Scope locked; if new ideas come up, flag but don't build"
- "Blockers come to me, early"
- "Let's build something cool and learn a ton"

**Next steps:**
- [ ] Curators finalize samples by Wed 24 June
- [ ] Domain Leads finalize quality criteria by Wed 24 June
- [ ] Builders set up development environment by Tue 23 June evening
- [ ] All: Confirm role availability (email Owner by EOD Tue 23 June)
- [ ] Owner: Schedule code review time for Thu 25 June

**Meeting ends.** Builders can stay for 10-min tech setup chat if needed.

---

## Meeting Notes (To Fill In)

**Date:** Tue 23 June 2026

**Attendees (actual):**
- [ ] Samyak-M
- [ ] Anshita Dhawan
- [ ] Jayasree Nishanth
- [ ] Sanjeev Patra
- [ ] Shashi Prabha
- [ ] Sirisha Dabiru
- [ ] Dinil

**Key Decisions Made:**

1. Role confirmations:
   - Anshita: Workflow Lead ✓
   - Jayasree: Domain Lead ✓
   - Sanjeev: Builder (Converter) ✓
   - Shashi: Builder (Rebranding) ✓
   - Sirisha: Content Curator ✓
   - Dinil: QA Lead ✓

2. Samples status:
   - [ ] Sample 1: [Name/description]
   - [ ] Sample 2: [Name/description]
   - [ ] Sample 3: [Name/description]

3. Blockers raised:
   - Blocker 1: [Description] → Solution: [Action]
   - Blocker 2: [Description] → Solution: [Action]

4. Tech setup needs:
   - Python version to use: ____
   - Cursor IDE available: Yes/No
   - Git access: Yes/No
   - DITA schema resource: [URL or file location]

5. Sample data handoff:
   - Curators commit samples to `/sample-data/input/` by: **Wed 24 June, EOD**
   - Domain Leads define DITA mapping in `/docs/assumptions.md` by: **Wed 24 June, EOD**
   - Builders begin converter skeleton by: **Thu 25 June**

**Action Items:**

| Owner | Action | Due |
|-------|--------|-----|
| Samyak-M | Update assumptions.md with blockers discussed | Tue 23 Jun EOD |
| Samyak-M | Share DITA schema reference with team | Tue 23 Jun EOD |
| Sirisha | Commit 2–3 sample Word docs to repo | Wed 24 Jun EOD |
| Anshita + Jayasree | Finalize quality-criteria.md and assumptions.md | Wed 24 Jun EOD |
| Sanjeev + Shashi | Set up Python environment + Cursor; review converter skeleton | Thu 25 Jun morning |
| Dinil | Create test matrix template in `/validation/` | Wed 24 Jun EOD |

---

**Meeting recorded?** No / Yes (link: _____)  
**Notes reviewed by:** [Name] on [Date]

---

**Next meeting:** Fri 27 June, 5:00 PM IST (First PoC demo + feedback)
