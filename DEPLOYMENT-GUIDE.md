# Deployment Guide: Document Intelligence PoC

This guide gives the core team a step-by-step process to implement, run, validate, and demo the Document Intelligence proof of concept.

## What This PoC Implements

The PoC has one automated pipeline:

1. Convert a Word `.docx` file to DITA-XML.
2. Apply brand terminology changes from a JSON rules file.
3. Validate the final DITA output against basic quality checks.
4. Expose the same workflow as a Claude Code plugin command.

## Repository Layout

```text
doc-intel-platform/
|-- .agents/
|-- .claude/
|   |-- plugin.json
|   `-- commands/pipeline.md
|-- docs/
|   |-- quality-criteria.md
|   |-- workflow-map.md
|   |-- assumptions.md
|   |-- sample-data-metadata.md
|   `-- meetings/
|-- prototype/
|   |-- converter.py
|   |-- rebranding-engine.py
|   |-- rebranding-rules.json
|   |-- validation-script.sh
|   `-- requirements.txt
|-- sample-data/
|   |-- input/Gmail_Installation_Guide.docx
|   |-- input/sample-001.md
|   |-- expected_output/
|   `-- brand_terminology.json
|-- results/
|   |-- README.md
|   |-- demo_guide.md
|   `-- validation_summary.md
|-- validation/
|   `-- test-results.md
|-- CHARTER.md
|-- DEPLOYMENT-GUIDE.md
|-- LEADER-DEMO-GUIDE.md
|-- OWNER-CHECKLIST.md
|-- README.md
|-- roster.md
`-- SKILLS-MARKETPLACE-GUIDE.md
```

## Folder and File Purpose

Use this section as the source of truth for what each folder and key file does.

| Path | Purpose |
| --- | --- |
| `.agents/` | Reserved local workspace folder. It is currently empty and not required for the PoC pipeline. |
| `.claude/` | Claude Code plugin package for running the PoC as a slash command. |
| `.claude/plugin.json` | Plugin manifest with name, version, description, and author. Claude Code uses this to identify the plugin. |
| `.claude/commands/` | Folder for Claude Code slash-command prompts. Each Markdown file becomes a command. |
| `.claude/commands/pipeline.md` | Defines `/pipeline`. It tells the AI agent to convert, rebrand, and validate using `$ARGUMENTS` as the input file. |
| `skill-creator plugin` | Optional Claude Code helper used only when creating or improving a reusable skill package for a marketplace repo. It is not required to run this PoC because `/pipeline` already exists. |
| `docs/` | Planning, quality, assumptions, workflow, sample metadata, and meeting documentation. |
| `docs/quality-criteria.md` | Defines what PASS, WARN, and FAIL mean for converted DITA output. Used when validation fails or needs interpretation. |
| `docs/workflow-map.md` | Explains the intended document flow from source input through conversion, review, validation, and output. |
| `docs/assumptions.md` | Captures conversion assumptions and known boundaries, such as headings, tables, images, metadata, and formatting. |
| `docs/sample-data-metadata.md` | Describes the sample files, their complexity, expected behavior, and QA expectations. |
| `docs/meetings/` | Meeting templates and notes for project coordination. |
| `prototype/` | Executable PoC implementation. This is where the actual conversion, rebranding, and validation logic lives. |
| `prototype/converter.py` | Converts Word `.docx` documents to DITA-XML. |
| `prototype/rebranding-engine.py` | Applies terminology replacement rules to the converted DITA-XML. |
| `prototype/rebranding-rules.json` | Active old-to-new brand terminology mapping file used by the rebranding engine. |
| `prototype/validation-script.sh` | Bash validator for DITA output quality checks. Requires `-f <file>` when invoked. |
| `prototype/requirements.txt` | Python dependencies required by the prototype scripts. |
| `sample-data/` | Input samples, expected reference outputs, and sample terminology data. |
| `sample-data/input/` | Source files used for testing and demos. The main demo input is `Gmail_Installation_Guide.docx`. |
| `sample-data/expected_output/` | Hand-curated DITA references for manual expected-vs-actual review. |
| `sample-data/brand_terminology.json` | Reference terminology sample. The active rules for this pipeline are in `prototype/rebranding-rules.json`. |
| `sample-data/output/` | Generated output folder created when the pipeline runs. It contains `out.dita` and `out-rebranded.dita`. |
| `results/` | Demo and validation evidence area. |
| `results/README.md` | Explains how to use the results folder. |
| `results/demo_guide.md` | Short local demo runbook for the build team. |
| `results/validation_summary.md` | Latest high-level validation summary placeholder. |
| `validation/` | Formal QA evidence folder. |
| `validation/test-results.md` | Test matrix and detailed QA results. Update this after formal runs. |
| `CHARTER.md` | Project scope, success criteria, milestones, and assumptions. |
| `DEPLOYMENT-GUIDE.md` | Core-team implementation and runbook. This is the deployment source of truth. |
| `LEADER-DEMO-GUIDE.md` | Step-by-step guide for demoing the PoC to leaders. |
| `OWNER-CHECKLIST.md` | Project owner checklist for coordination, readiness, and timeline tracking. |
| `README.md` | Architecture overview and quick-start entry point. |
| `roster.md` | Team roles, responsibilities, and ownership. |
| `SKILLS-MARKETPLACE-GUIDE.md` | Steps to publish the Claude Code plugin into a separate skills marketplace repository. |
| `.gitignore` | Git ignore rules for generated or local-only files. |
| `LICENSE` | Repository license. |

## Claude Code Plugin and Command Flow

The `.claude/` folder packages this PoC as a Claude Code plugin, but it does not replace the prototype scripts. It is an orchestration layer over the same manual commands.

- `.claude/plugin.json` is the plugin manifest. It gives Claude Code the plugin name, version, description, and owner.
- `.claude/commands/pipeline.md` defines a slash command. Claude Code exposes this file as `/pipeline`.
- `$ARGUMENTS` inside `pipeline.md` is replaced by the text typed after the slash command.

Why this helps:

- The core team does not need to remember three separate terminal commands during the demo.
- The AI agent receives the same deterministic instructions every time.
- The workflow can later be copied into a shared skills marketplace repo without changing the prototype scripts.

Example:

```text
/pipeline sample-data/input/Gmail_Installation_Guide.docx
```

Claude Code reads `.claude/commands/pipeline.md`, replaces `$ARGUMENTS` with `sample-data/input/Gmail_Installation_Guide.docx`, then runs the convert, rebrand, and validate steps in order.

## Skill-Creator Plugin Guidance

The team should not run skill-creator during the live demo. For the live demo, use the already-created `/pipeline` command.

### What Already Exists

These files are already created and should be kept:

```text
.claude/plugin.json
.claude/commands/pipeline.md
```

They are enough to run the PoC in Claude Code:

```text
/pipeline sample-data/input/Gmail_Installation_Guide.docx
```

No separate `SKILL.md`-based marketplace skill has been generated in this repo yet. If the marketplace repo requires that format, create it there with skill-creator.

### When to Use Skill-Creator

Use the skill-creator plugin only when the team wants to:

- Create a reusable marketplace skill package from this PoC.
- Add a new command beyond `/pipeline`.
- Improve the existing `/pipeline` prompt after demo feedback.
- Generate a formal skill folder if the marketplace repo expects `SKILL.md`-based skills.

Do not use skill-creator when:

- Running the normal demo.
- Running the manual converter, rebranding, or validation scripts.
- Recording validation results.

### Where to Run Skill-Creator

Run skill-creator from the repo where the new skill package should be created.

For this PoC:

- If updating the local Claude Code command, run it from this repo: `doc-intel-platform`.
- If publishing to a shared marketplace, run it from the separate marketplace repo, not this PoC repo.

Do not rely on automatic placement for team artifacts. Always give skill-creator an explicit target path.

Recommended marketplace target:

```text
skills/doc-intel-skills/
```

Recommended local target, only if creating a formal local skill folder:

```text
.claude/
```

If your installed skill-creator defaults to a personal global skills folder, such as a user profile or home directory, do not use that default for team deliverables. Personal/global placement is useful for private experimentation, but the team asset must be committed in the repo that owns the skill.

### How to Ask Skill-Creator

Use an RTCCO prompt so the generated skill is specific and repeatable.

RTCCO means:

- Role: Who the AI should act as.
- Task: What it must create or update.
- Context: Repo paths, existing files, marketplace rules, and target users.
- Constraints: Required structure, commands, naming, and things not to change.
- Output: Exact files or review summary expected.

Example prompt to create a marketplace-ready skill:

```text
Role:
You are a Claude Code skill-creator assistant for the Document Intelligence Platform team.

Task:
Create a reusable skill package named doc-intel-skills for a skills marketplace repo.

Context:
The working PoC already has these source files:
- .claude/plugin.json
- .claude/commands/pipeline.md
- prototype/converter.py
- prototype/rebranding-engine.py
- prototype/rebranding-rules.json
- prototype/validation-script.sh
- docs/quality-criteria.md

The skill should help users run the Word to DITA-XML pipeline through Claude Code.

Constraints:
- Keep the existing /pipeline command behavior.
- Use strict JSON for plugin.json.
- Keep YAML frontmatter at the top of pipeline.md.
- Use $ARGUMENTS as the input .docx path.
- Validation must run with: bash prototype/validation-script.sh -f sample-data/output/out-rebranded.dita
- Do not copy prototype scripts into the marketplace package unless the marketplace owner explicitly wants executable code included.
- Put the generated package under skills/doc-intel-skills/.

Output:
Create or update the marketplace skill files and summarize:
- Files created
- How to invoke the skill
- Required host repo files
- Validation checks performed
```

Example prompt to improve the existing local `/pipeline` command:

```text
Role:
You are a Claude Code skill-creator assistant.

Task:
Improve the existing local /pipeline command prompt for a live executive demo.

Context:
The command file is .claude/commands/pipeline.md.
The demo input is sample-data/input/Gmail_Installation_Guide.docx.
The pipeline converts, rebrands, and validates DITA output.

Constraints:
- Do not change prototype Python or Bash scripts.
- Keep the command name /pipeline.
- Keep the exact converter, rebranding, and validation commands.
- Keep validation failure reporting to exactly 5 bullets using PASS, WARN, or FAIL.
- Keep the prompt concise and deterministic.

Output:
Update .claude/commands/pipeline.md and report what changed.
```

### Skill-Creator Output Checklist

After using skill-creator, verify:

- The generated files are in the intended repo and folder.
- `plugin.json` parses as JSON, if a Claude plugin manifest is generated.
- `pipeline.md` starts with YAML frontmatter.
- `$ARGUMENTS` is preserved in the command prompt.
- Validation uses `-f`.
- The marketplace package explains required host repo files.
- The generated files are committed with the marketplace or PoC repo, not left only in a personal/global skills folder.

## Prerequisites

- Python 3.10 or 3.11 recommended for the PoC
- Git
- Git Bash on Windows, or Bash on macOS/Linux, for `prototype/validation-script.sh`
- Optional: `xmllint` from libxml2 for stricter XML checks
- Claude Code, if the team wants to run the `.claude` plugin command

Important setup notes:

- Avoid Python 3.14 for the current pinned dependencies. In local testing, `lxml==4.9.2` failed to install on Python 3.14 because it tried to compile from source and could not find libxml2 headers.
- On Windows, install Git for Windows and use Git Bash for validation commands. PowerShell is fine for Python-only commands.
- If multiple Python versions are installed on Windows, create the virtual environment with Python 3.11:

```bash
py -3.11 -m venv .venv
```

## Step 1: Clone and Open the Repo

```bash
git clone <repo-url>
cd doc-intel-platform
```

Open the repo root in Cursor, VS Code, or Claude Code.

## Step 2: Create a Local Python Environment

From the repo root:

```bash
python -m venv .venv
```

On Windows with multiple Python versions, prefer:

```bash
py -3.11 -m venv .venv
```

Activate it:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Git Bash, macOS, or Linux
source .venv/Scripts/activate
```

If using macOS or Linux, the activation path may be:

```bash
source .venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install -r prototype/requirements.txt
```

Expected result: `python-docx`, `lxml`, and `colorama` install successfully.

## Step 4: Run the Manual Pipeline

Run these commands from the repo root.

### 4.1 Convert Word to DITA

```bash
python prototype/converter.py --input sample-data/input/Gmail_Installation_Guide.docx --output sample-data/output/out.dita
```

Expected result:

- `sample-data/output/out.dita` is created.
- The terminal prints a conversion summary.

### 4.2 Apply Brand Terminology

```bash
python prototype/rebranding-engine.py --input sample-data/output/out.dita --rules prototype/rebranding-rules.json --output sample-data/output/out-rebranded.dita
```

Expected result:

- `sample-data/output/out-rebranded.dita` is created.
- The terminal prints replacement counts.

### 4.3 Validate the Rebranded Output

```bash
bash prototype/validation-script.sh -f sample-data/output/out-rebranded.dita
```

Expected result:

- Validation prints tiered checks.
- Exit code is `0` for PASS or PASS with warnings.
- Exit code is `1` for FAIL.

## Step 5: Run the Claude Code Plugin Command

This is the recommended demo path once the manual pipeline has been proven.

### 5.1 Confirm Plugin Files Exist

The plugin files must be present in the repo root:

- `.claude/plugin.json`
- `.claude/commands/pipeline.md`

### 5.2 Open the Repo in Claude Code

Open `doc-intel-platform` as the active workspace. Claude Code discovers local commands from `.claude/commands/`.

### 5.3 Invoke the Skill Command

In Claude Code chat, run:

```text
/pipeline sample-data/input/Gmail_Installation_Guide.docx
```

This invokes the local `pipeline` command. The input path becomes `$ARGUMENTS` inside `.claude/commands/pipeline.md`.

### 5.4 What Claude Code Runs

The command prompt instructs the agent to execute:

```bash
python prototype/converter.py --input sample-data/input/Gmail_Installation_Guide.docx --output sample-data/output/out.dita
python prototype/rebranding-engine.py --input sample-data/output/out.dita --rules prototype/rebranding-rules.json --output sample-data/output/out-rebranded.dita
bash prototype/validation-script.sh -f sample-data/output/out-rebranded.dita
```

If validation fails, the agent must read `docs/quality-criteria.md` and report exactly five bullets using `PASS`, `WARN`, or `FAIL`.

### 5.5 When to Use Manual Commands vs. `/pipeline`

Use manual commands when:

- A developer is debugging one stage.
- QA needs to isolate converter, rebranding, or validation behavior.
- Claude Code is not available in the environment.

Use `/pipeline` when:

- Running the standard demo.
- Repeating the full workflow on the same sample.
- Showing the skill/plugin capability to leaders.

## Step 6: Verify Output Quality

Open these files:

- `sample-data/output/out.dita`
- `sample-data/output/out-rebranded.dita`
- `docs/quality-criteria.md`
- `sample-data/expected_output/gmail-guide-expected.dita`

Check:

- DITA root topic, title, body, sections, paragraphs, and tables exist.
- Brand terms from `prototype/rebranding-rules.json` were applied.
- No obvious content loss occurred.
- Validation status and warnings are understandable.
- Known limitations are documented, not hidden.

## Step 7: Record Results

This step is manual for the current PoC. There is no results-writing script yet.

Update `validation/test-results.md` after each formal test run with:

- Input file name
- Commands used
- PASS, WARN, or FAIL
- Validation output summary
- Manual review notes
- Known limitation, if any
- Owner for follow-up

Recommended process:

1. Copy the validation summary from the terminal or Claude Code response.
2. Open `validation/test-results.md`.
3. Add a dated entry with the input file, output file, validation status, and notes.
4. If the result is FAIL, also add the reason and the owner responsible for follow-up.
5. Update `results/validation_summary.md` with the latest high-level status.

Later improvement:

- Add `prototype/run-pipeline.sh` or `prototype/run-pipeline.ps1` to run all three stages and append a machine-readable result.
- Add a small reporting script only after the team agrees on the final result format.

## Step 8: Core Team Handoff

Before presenting to leaders, the core team should confirm:

- A fresh clone can run the pipeline.
- The sample Word file converts successfully.
- Rebranding changes are visible in the final DITA.
- Validation produces a readable status.
- The Claude Code `/pipeline` command is installed and usable.
- Demo instructions in `LEADER-DEMO-GUIDE.md` have been rehearsed.

## Troubleshooting

| Problem | Practical Fix |
| --- | --- |
| `ModuleNotFoundError: No module named 'docx'` | Run `pip install -r prototype/requirements.txt`. |
| `bash: command not found` on Windows | Install Git for Windows and use Git Bash. |
| `lxml==4.9.2` fails to build on Python 3.14 | Use Python 3.10 or 3.11 for the PoC virtual environment, then reinstall requirements. |
| `xmllint not installed` warning | Install libxml2 tools, or continue with reduced validation for the PoC. |
| Validation says `-f/--file argument required` | Use `bash prototype/validation-script.sh -f sample-data/output/out-rebranded.dita`. |
| Output folder missing | The converter creates it automatically when writing `sample-data/output/out.dita`. |
| Rebranding makes no changes | Check `prototype/rebranding-rules.json` and verify the input contains matching source terms. |

## Practical Improvements Recommended

- Add a one-command wrapper script later, such as `prototype/run-pipeline.sh`, after the current demo is accepted.
- Add a small `sample-data/output/.gitkeep` if the team wants the output folder visible in a fresh checkout.
- Add a formal expected-vs-actual comparison script for QA after the PoC.
- Keep Claude command prompts small and deterministic; avoid asking the agent to infer file names during the demo.
- Store marketplace publishing notes in `SKILLS-MARKETPLACE-GUIDE.md` so the plugin handoff is repeatable.

## Definition of Done

The PoC is ready for core-team sign-off when:

- Manual pipeline runs end to end.
- Claude Code `/pipeline` command runs end to end.
- Validation results are captured.
- Leader demo has been rehearsed once.
- Marketplace packaging steps are documented for the skills repository owner.
