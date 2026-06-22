# Contributing to Document Intelligence Platform - Converter & Rebranding

Thank you for joining this project team! This guide explains how to work effectively together and contribute to the proof-of-concept.

---

## Team Commitment

Before contributing, please:

1. **Read the essentials:**
   - [PROJECT_CHARTER.md](PROJECT_CHARTER.md) — Understand scope and success criteria
   - [README.md](README.md) — Understand the overview and structure
   - [ROSTER.md](ROSTER.md) — Know your role and team members

2. **Understand the working model:**
   - You are part of a 9-10 person team with one assigned role
   - You should attend agreed working sessions (or provide async updates)
   - You own at least one concrete task
   - All work is committed to this repository — no private files or chat-only decisions
   - Blockers should be raised early with a proposed option
   - Respect the project owner's final call on scope and design decisions

---

## How to Contribute

### 1. Issues & Task Assignment

- **Check your role** in [ROSTER.md](ROSTER.md) to understand your responsibilities
- **Look for open Issues** tagged with your role or assigned to you
- **Create an Issue** if you find a blocker or need to propose a task
- **Link related work** to connect decisions, samples, and code

### 2. Repository Structure

```
doc-intel-platform/
├── PROJECT_CHARTER.md            # Read first
├── README.md                      # Project overview
├── ROSTER.md                      # Team and roles
├── CONTRIBUTING.md                # This file
├── docs/
│   ├── decisions/                 # Architectural decisions (YYYY-MM-DD_decision.md)
│   ├── meetings/                  # Meeting notes (YYYY-MM-DD_meeting_summary.md)
│   └── workflow/                  # Workflow analysis (input → outputs)
├── samples/
│   ├── input/                     # Sample input documents (.docx, .html, .md, etc.)
│   ├── expected_output/           # Expected output after transformation
│   └── brand_terminology.json     # Brand term mappings
├── src/                           # Main codebase
├── tests/                         # Validation scripts and test cases
├── results/                       # Demo output and validation reports
└── validation/
    ├── test_scenarios.md          # QA test cases
    └── results_log.md             # Test results and findings
```

**Key rule:** Everything important belongs in the repository. If it's not committed, it's not final.

### 3. Branching & Commits

- Work on feature branches: `feature/short-description` or `task/your-task-name`
- Commit frequently with clear messages: `Add Word document parser` vs. `update stuff`
- Reference Issues in commit messages: `Closes #5 - Implement DITA converter`
- Keep commits focused and atomic (one logical change per commit)

### 4. Pull Requests

- **Before opening a PR:**
  - Make sure your branch is up-to-date with `main`
  - Test locally if applicable
  - Check the PR template (if one exists) or include: what, why, how to test

- **In your PR description:**
  ```
  ## What
  Brief description of the change.
  
  ## Why
  Problem this solves or task this completes.
  
  ## How to Test
  Steps to verify the change works.
  
  ## Related Issues
  Closes #N (if applicable)
  ```

- **Code review expectations:**
  - Project owner (Samyak) or assigned reviewer will review
  - Respond to feedback promptly
  - Resolve conversations and re-request review when ready

### 5. Documentation

When you complete a task, document it:

- **Code changes:** Add docstrings and inline comments
- **Decisions:** Create `/docs/decisions/YYYY-MM-DD_decision_name.md` with reasoning
- **Meeting outcomes:** Post summary to `/docs/meetings/YYYY-MM-DD_meeting_summary.md` within 24 hours
- **Sample inputs/outputs:** Add to `/samples/input/` and `/samples/expected_output/`
- **Validation results:** Update `/validation/results_log.md` with findings

---

## Working Agreements

### Meetings

- Attend your assigned working session or provide an async update (post to `/docs/meetings/`)
- Meetings should have a clear purpose: decision, unblocker, review, or demo prep
- Meeting notes and action items go in the repository within 24 hours
- Async updates are acceptable — keep the team informed

### Blockers

- **Raise early and propose a solution:** "I'm blocked on X because Y. Suggest we Z."
- **Post as Issues** in the repository with clear context
- **Tag the project owner** if you need an immediate decision
- **Don't assume** — ask if unsure about scope or design

### Decisions

- All important decisions must be captured in the repository
- Decisions made in calls or chat should be summarized in `/docs/decisions/` within 24 hours
- Use the format: **Recommendation, Context, Alternatives Considered, Outcome**

### Code Quality

- Follow existing code patterns and style
- Write tests where applicable
- Document assumptions and edge cases
- If using prompts, scripts, or APIs, version them in the repository

---

## Example Workflows

### Workflow Lead: Adding Sample Input

```
1. Collect a realistic document (Word, HTML, etc.)
2. Create `/samples/input/sample-001-<description>.*`
3. Define expected output → `/samples/expected_output/sample-001-expected.*`
4. Document in Issue or pull request why this sample is representative
5. Commit and reference in relevant tracking issue
```

### Prototype Builder: Implementing a Feature

```
1. Create a feature branch: git checkout -b feature/word-to-xml-converter
2. Write code with docstrings
3. Test locally
4. Commit: git commit -m "Implement Word to DITA-XML conversion"
5. Open PR with description and link to related Issue
6. Address review feedback
7. Merge to main after approval
8. Update README or docs if behavior changed
```

### QA Lead: Running Validation

```
1. Follow `/validation/test_scenarios.md` for test cases
2. Run PoC on samples from `/samples/input/`
3. Compare to `/samples/expected_output/`
4. Document results (passed, failed, edge cases) in `/validation/results_log.md`
5. Raise Issues for failures or unexpected behavior
6. Commit results with summary
```

### Demo Lead: Preparing Demo Package

```
1. Collect final sample inputs and outputs
2. Write usage guide in `/docs/DEMO_GUIDE.md`
3. Take screenshots showing before/after
4. Prepare demo script with talking points
5. Test that someone else can follow the guide and reproduce results
6. Document limitations and learnings
7. Commit everything and mark demo package ready
```

---

## Communication Norms

✓ **Do:**
- Propose solutions, not just problems
- Ask questions if scope is unclear
- Celebrate progress and learnings
- Challenge ideas, not people
- Document decisions in the repository

✗ **Don't:**
- Keep important decisions in chat only
- Work in private files or personal machines without repository reference
- Commit without clear messages or comments
- Skip meetings without async updates
- Park blockers without escalating to the project owner

---

## Technology & Tools

- **Repository:** GitHub (you're here!)
- **Collaboration:** Async first, meetings only when needed
- **Tracking:** Issues, Projects, or task lists in `/docs/`
- **Source of truth:** This repository

**Tech stack for the PoC:** [To be decided by prototype builders — document in `/docs/decisions/`]

---

## Questions?

- Check [README.md](README.md) or [PROJECT_CHARTER.md](PROJECT_CHARTER.md) first
- Look at existing Issues and closed PRs for patterns
- Message your role lead or project owner
- Post an Issue if something is unclear

---

**Last Updated:** 22 June 2026  
**Project Owner:** Samyak Mukherjee (@Samyak-M)  
**Next Milestone:** Mon, 22 Jun 2026 (Charter & Roster finalized)