# Owner's Action Checklist: Samyak-M

**Project:** Document Converter & Rebranding PoC  
**Timeline:** 22 June – 05 July 2026  
**Role:** Project Owner & Coordinator  

---

## Your Responsibilities

As owner, you are responsible for:

1. **Scope management** — No scope creep; keep team focused
2. **Timeline management** — Track deadlines; escalate slips early
3. **Blocker removal** — Unblock team members daily
4. **Communication** — Weekly syncs, clear decisions
5. **Demo readiness** — Ensure final package is ready by Wed 2 July
6. **Team morale** — Keep team motivated through 2-week sprint

---

## Phase 1: Foundation (by Monday, 22 June)

### Charter & Repo Setup

- [x] **Draft charter** (problem, scope, success criteria) — DONE ✓
- [x] **Create GitHub repo** (`doc-intel-platform` exists) — DONE ✓
- [x] **Assign roles to 6 members** — DONE ✓
  - Anshita Dhawan → Workflow Lead
  - Jayasree Nishanth → Domain Lead
  - Sanjeev Patra → Builder (Converter)
  - Shashi Prabha → Builder (Rebranding)
  - Sirisha Dabiru → Content Curator
  - Dinil → QA & Validation
- [x] **Create project structure** (docs/, prototype/, sample-data/, validation/) — DONE ✓
- [x] **Commit initial docs** (charter, roster, README, templates) — READY TO DO ✓

### By End of Day Monday (22 June)

- [ ] **Confirm you're the project owner** (message project organizers)
- [ ] **Send charter + roster to team** (email or Slack link to repo)
- [ ] **Schedule kickoff for Tue 23 or Wed 24 June** (1 hour, all 7 people)
- [ ] **Create Git branch structure:**
  - main = production-ready code
  - develop = integration branch (optional)
  - feature/* = individual branches per person/feature
- [ ] **Share this checklist with team** (shows what you're tracking)

---

## Phase 2: Discovery & Setup (by Wednesday, 24 June)

### Tuesday 23 June

**Before kickoff:**
- [ ] Review charter, roster, README one more time
- [ ] Prepare 2–3 talking points on why this PoC matters
- [ ] Have DITA schema reference ready (to share with team)
- [ ] Note any questions or concerns

**Kickoff meeting (2:00–3:00 PM IST):**
- [ ] Lead meeting using `/kickoff-meeting-template.md`
- [ ] Take detailed notes on blockers raised
- [ ] Confirm each person's role + deliverables
- [ ] Assign action items (see template)
- [ ] Clarify escalation path: "If you're stuck, tell me ASAP"

**After kickoff:**
- [ ] Update assumptions.md or other docs based on feedback
- [ ] Send thank-you summary email to team (recap key decisions)
- [ ] Unblock any immediate issues (access, setup, resources)

### Wednesday 24 June

**By EOD:**
- [ ] Curators (Sirisha) have committed sample Word docs + expected DITA outputs
- [ ] Domain Leads (Anshita + Jayasree) have finalized assumptions.md + quality-criteria.md
- [ ] QA (Dinil) has created test matrix template in `/validation/`
- [ ] All team members confirmed availability in writing (email or comment on repo)

**Your action:**
- [ ] Review & approve sample data quality (with curators)
- [ ] Review assumptions.md & quality-criteria.md (stamp as final)
- [ ] Check: Does everyone have git access + Python environment?
- [ ] If blockers: Resolve today; don't let them carry to next week

**By EOD Wednesday:**
- [ ] All Phase 1 & 2 documents committed to repo (charter, roster, README, workflow-map, assumptions, quality-criteria)
- [ ] Builders (Sanjeev + Shashi) have cloned repo + set up environment
- [ ] All dependencies resolved; no team member should be waiting on anyone else

---

## Phase 3A: Execution Setup (by Friday, 27 June)

### Thursday 25 June

**Morning:**
- [ ] 15-min code review with Builders (Sanjeev + Shashi)
  - Check converter.py skeleton (Word parsing structure)
  - Check rebranding-rules.json structure (10+ sample rules)
  - Any code issues? Flag and help unblock
- [ ] Standup with whole team (9:00–9:15 AM IST)
  - Who's blocked? What's the blocker? Who fixes it?
  - Sanjeev: "Converter parses Word structure ✓"
  - Shashi: "Rebranding rules ready ✓"
  - Others: "Samples ready ✓", "Quality criteria final ✓"

**By EOD:**
- [ ] Builders have committed working skeleton code to repo
- [ ] No critical blockers for next day's demo

### Friday 27 June

**Morning standup (9:00 AM):**
- [ ] All: Any blockers before demo?
- [ ] Builders: Code ready to run on sample data?
- [ ] QA (Dinil): Ready to test output?

**Afternoon: First PoC Demo**
- [ ] Builders demo converter running on sample-1.docx:
  1. Input: sample-1.docx
  2. Run: `python converter.py --input sample-data/input/sample-1.docx --output /tmp/output.dita`
  3. Output: Valid DITA-XML file created
  4. Quick check: "Does it look right?" (ask domain leads)
- [ ] Builders demo rebranding on output:
  1. Run: `python rebranding-engine.py --input /tmp/output.dita --rules prototype/rebranding-rules.json --output /tmp/output-rebranded.dita`
  2. Output: Rebranded DITA-XML created
  3. Check: "Are brand terms replaced?"
- [ ] QA (Dinil) runs validation script:
  1. Run: `bash prototype/validation-script.sh -f /tmp/output-rebranded.dita`
  2. Output: Validation report (pass/fail)

**Your action during demo:**
- [ ] Take notes on what works + what fails
- [ ] Ask: "Is this good enough for Mon 30?"
- [ ] If major issues: Plan fixes for tomorrow
- [ ] If minor issues: Log in edge-cases.md for now

**After demo:**
- [ ] Record demo video (optional; for dry-run practice)
- [ ] Builders commit final code + test results
- [ ] Update test-results.md with Fri 27 results

---

## Phase 3B: Validation & Freeze (by Monday, 30 June)

### Friday 27 EOD – Saturday 28 (if weekend work)

- [ ] QA (Dinil) runs comprehensive tests on ALL samples:
  - sample-1: converter → rebranding → validation
  - sample-2: converter → rebranding → validation
  - sample-3: converter → rebranding → validation
- [ ] Dinil documents:
  - Pass/fail for each sample (in test-results.md)
  - Edge cases found (in edge-cases.md)
  - Workarounds if any

### Monday 30 June (Scope Freeze Day)

**By 10:00 AM:**
- [ ] Standup with whole team (9:00–9:15 AM IST)
  - QA presents test results (what passed, what failed?)
  - Team discusses: Acceptable failures vs. critical bugs?
  - Owner decision: "Scope locked; no new features"

**By EOD:**
- [ ] Test matrix complete + signed off by QA (Dinil)
- [ ] Edge cases documented + acknowledged by team
- [ ] Any critical bugs fixed; minor issues logged as "known limitation"
- [ ] Builders: Code is stable; only bug fixes until demo (no new features)
- [ ] All code committed to repo

**Key decision point:**
- [ ] Does converter work on ≥ 70% of samples? YES → proceed to demo prep ✓
- [ ] Does rebranding work correctly? YES → proceed to demo prep ✓
- [ ] Does validation catch issues? YES → proceed to demo prep ✓
- [ ] If any NO: Pause; assess if fixable by Wed 2 July; escalate if not

---

## Phase 4: Demo Prep (by Wednesday, 2 July)

### Tuesday 1 July

- [ ] Code review with Builders (final polish)
  - Clean up comments, readme in code
  - Any last-minute edge case fixes
  - Commit final version by EOD Tue

### Wednesday 2 July

**By EOD:**
- [ ] Demo package ready in repo:
  - [ ] README.md complete (setup, usage, limitations)
  - [ ] charter.md finalized
  - [ ] roster.md finalized
  - [ ] workflow-map.md finalized
  - [ ] quality-criteria.md finalized
  - [ ] assumptions.md finalized
  - [ ] test-results.md complete with pass/fail matrix
  - [ ] edge-cases.md complete with workarounds
  - [ ] converter.py + rebranding-engine.py ready to run
  - [ ] validation-script.sh ready to run
  - [ ] sample-data/input/ with 2–3 Word docs
  - [ ] sample-data/expected_output/ with hand-curated DITA outputs
  - [ ] demo-narrative.md written (problem → approach → demo → learnings)

**Your actions:**
- [ ] Review all docs for clarity + consistency
- [ ] Check: Is everything a non-technical person can understand?
- [ ] Does README tell someone how to run the PoC? YES → proceed
- [ ] Are edge cases honestly documented? YES → proceed

---

## Phase 5: Demo Rehearsal (by Friday, 4 July)

### Thursday 3 July

**Dry-run prep:**
- [ ] Each speaker reviews their section (see below)
- [ ] Builders practice demo commands (converter + rebranding + validation)
- [ ] QA prepares to present test matrix
- [ ] Domain Leads prepare to present workflow insights

### Friday 4 July

**Full dry-run (10:00–11:00 AM IST):**
- [ ] Owner: Opens with 2-min problem statement + scope
- [ ] Builders: 5-min demo of converter running on sample-1
  - Word doc → DITA-XML → Rebranded DITA → Validation report
  - "What did we learn?" (challenges, workarounds)
- [ ] QA: 3-min presentation of test matrix
  - How many samples passed? Which passed/failed?
  - What's the pass rate? 70%? 90%? 100%?
- [ ] Domain Leads: 2-min on workflow insights
  - How does converter fit into real doc workflow?
  - What's next after PoC?
- [ ] All: 5-min discussion
  - "Are we ready for Sunday?"
  - "Any last-minute fixes needed?"

**Your action during dry-run:**
- [ ] Time each section (should fit in 15–20 min total)
- [ ] Note: Is the story clear? Does it make sense to stakeholders?
- [ ] Ask: "What surprised you during this PoC?"
- [ ] Identify last-minute fixes (should be quick)

**After dry-run:**
- [ ] Gather feedback
- [ ] Make quick fixes if critical
- [ ] Confirm demo is production-ready by EOD Fri

---

## Final Presentation (Sunday, 5 July)

### Saturday 4 July (if prep needed)

- [ ] Final code review + any last-minute fixes
- [ ] Rehearse one more time if needed

### Sunday 5 July (Demo Day)

**Before presentation:**
- [ ] Check: All files in repo? All code runs? All docs complete?
- [ ] Builders test demo commands one final time
- [ ] QA verifies test results are accurate

**During presentation (30–40 minutes total):**
- [ ] Owner: Problem statement + PoC scope (2 min)
- [ ] Builders: Live demo
  1. Convert sample-1.docx → DITA
  2. Apply rebranding
  3. Run validation
  4. Show output (before/after)
- [ ] QA: Test results + what failed + why (3 min)
- [ ] Domain Leads: Workflow insights + learnings (2 min)
- [ ] Owner: Recommendations for next phase (2 min)
- [ ] All: Q&A (10 min)

**After presentation:**
- [ ] Collect feedback
- [ ] Document lessons learned in `/docs/demo-narrative.md`

---

## Weekly Standup Checklist

**Every Mon/Wed/Fri, 9:00–9:15 AM IST**

Use this format to keep team on track:

```
STANDUP [DATE]

1. Anshita (Workflow Lead)
   Progress: [What did you do since last sync?]
   Blockers: [What's stopping you?]
   Next: [What's next?]

2. Jayasree (Domain Lead)
   Progress: 
   Blockers: 
   Next: 

3. Sanjeev (Builder – Converter)
   Progress: 
   Blockers: 
   Next: 

4. Shashi (Builder – Rebranding)
   Progress: 
   Blockers: 
   Next: 

5. Sirisha (Content Curator)
   Progress: 
   Blockers: 
   Next: 

6. Dinil (QA & Validation)
   Progress: 
   Blockers: 
   Next: 

Owner Decisions:
- Decision 1: [What did owner decide this week?]
- Decision 2: 
- Blockers Removed: [What did owner fix?]
```

---

## Critical Dates (Bookmark These)

| Date | Milestone | Decision |
|------|-----------|----------|
| **Mon 22 Jun** | Charter + Repo ready | Kickoff scheduled |
| **Tue 23 Jun, 2 PM** | Team kickoff | Roles confirmed |
| **Wed 24 Jun EOD** | Samples locked | Builders start |
| **Fri 27 Jun** | First PoC demo | What works? What fails? |
| **Mon 30 Jun EOD** | Scope frozen | No new features |
| **Wed 2 Jul EOD** | Demo package ready | Rehearsal ready |
| **Fri 4 Jul 10 AM** | Full dry-run | Go/no-go for Sunday |
| **Sun 5 Jul** | Live presentation | Demo to stakeholders |

---

## Escalation Path

**If something goes wrong, here's who to contact:**

| Situation | First Contact | Escalate To |
|-----------|---------------|------------|
| Blocker with Code | Builders (Sanjeev/Shashi) | Owner (you) |
| Blocker with Samples | Curator (Sirisha) | Owner (you) |
| Blocker with Testing | QA (Dinil) | Owner (you) |
| Blocker with Scope/Timeline | Owner (you) | Project Organizers |
| Team conflict | Owner (you) | Project Organizers |
| Major bug found late | Owner (you) | Evaluate with team |

---

## Communication Channels

- **Async updates:** Slack/Teams channel (daily)
- **Syncs:** Mon/Wed/Fri 9:00–9:15 AM (standup)
- **Code reviews:** Thu 25 Jun, Thu 2 Jul (with builders)
- **Decisions:** Email summary after each meeting
- **Escalations:** Direct to owner (you) ASAP; then project organizers if needed

---

## Success Indicators

By July 5, you should see:

- ✓ Converter runs end-to-end on ≥ 2 samples
- ✓ Rebranding rules work correctly (100% term replacement)
- ✓ Validation catches errors (test matrix shows pass/fail)
- ✓ Team is motivated + learned new skills (ask them in final debrief)
- ✓ Stakeholders understand feasibility + next steps
- ✓ Code + docs are clean + ready for handoff

---

## Notes for You

**Remember:**

1. **Scope is your job.** Say "no" to new features. If someone suggests something, say: "Great idea for phase 2; let's log it in the roadmap."

2. **Blockers are your job.** Don't let team members spin wheels. If stuck > 2 hours, escalate.

3. **Celebrate wins.** Team is working hard in 2 weeks. Acknowledge progress publicly.

4. **Document learnings.** After demo, capture what worked + what surprised you. This is gold for future projects.

5. **Be honest in demo.** Show what failed + why. Stakeholders appreciate honesty more than perfection.

---

**You've got this! 🚀**

---

**Last updated:** 21 June 2026  
**Status:** Ready to use
