# Decisions Log

This folder contains all major architectural and design decisions made during the project.

## How to Document a Decision

When your team makes an important decision, create a file with this format:

**File name:** `YYYY-MM-DD_decision_title.md`  
**Example:** `2026-06-22_tech_stack_selection.md`

### Template

```markdown
# Decision: [Title]

**Date:** YYYY-MM-DD  
**Owner:** [Your name]  
**Status:** Proposed / Decided / Implemented / Superseded  

## Context

What problem prompted this decision? What's the background?

## Recommendation

What decision did we make and why?

## Alternatives Considered

1. Option A — Trade-offs and why we didn't choose this
2. Option B — Trade-offs and why we didn't choose this

## Outcome / Implementation

How will this decision be implemented? Any follow-up tasks?

## Related Issues / PRs

[Link to relevant GitHub issues or PRs]
```

## Decisions Index

*New decisions will be logged here as the team makes them.*

| Date | Title | Status | Owner |
|------|-------|--------|-------|
| 2026-06-22 | Prototype tech stack for converter | Proposed | Prototype Lead |
| 2026-06-22 | Document format strategy (Word → DITA-XML) | Proposed | Workflow Lead |
| 2026-06-22 | Brand terminology mapping approach | Proposed | Data Curator |

---

## Starter Decision Record

### Decision: Prototype Tech Stack for Converter

**Date:** 2026-06-22  
**Owner:** Prototype Lead (TBD)  
**Status:** Proposed

#### Context

We need a small, reproducible prototype that converts Word-based content into a structured XML format (DITA-XML) and performs brand-term cleanup. The prototype must be simple to run by other team members and use open-source components where practical.

#### Recommendation

Use a minimal Python-based toolchain:

- **Core language:** Python 3.10+ for portability and available libraries
- **Document reading:** `python-docx` to parse `.docx` files when direct XML parsing is sufficient
- **Transformation:** `pandoc` (command-line) for general format conversions; custom conversion scripts using `lxml` for targeted DITA-XML output
- **Brand cleanup:** YAML/JSON-driven terminology mapping + simple rules implemented in Python (regex / token-based replacement with context awareness)
- **Validation:** Small Python test harness to run conversions on sample inputs and produce a validation summary (counts of transformed sections, missing mappings, examples of ambiguous replacements)

**Rationale:** Python has broad team familiarity, many libraries for document parsing/manipulation, and is easy to run cross-platform. Pandoc provides fast conversions for many formats and can bootstrap DITA-XML which can then be cleaned by custom scripts.

#### Alternatives Considered

1. **Java-based toolchain (Apache POI + custom XSLT)** — More mature XML tooling but higher setup complexity for contributors; steeper learning curve
2. **Pure Pandoc + Lua filters** — Efficient but adds another language surface area for the team; less flexibility for brand-specific rules
3. **Cloud-based document processing APIs** — Faster for prototyping but adds external dependencies; may not be available offline

#### Outcome / Implementation

- Prototype Lead to create `2026-06-22_tech_stack_decision.md` with chosen tools, versions, and installation steps
- Create sample inputs in `samples/input/` (Word documents) and `samples/expected_output/` (DITA-XML)
- Implement `scripts/convert.py` demonstrating one complete input → DITA-XML output flow
- Document any third-party dependencies in `requirements.txt` and `setup_instructions.md`

#### Related Issues / PRs

- (Links to GitHub issues will be added once team issues are created)

---

**Last Updated:** 22 June 2026
