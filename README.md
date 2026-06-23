# Document Intelligence Platform PoC

This repository contains a practical proof of concept for converting Word documents to DITA-XML, applying brand terminology updates, validating the output, and exposing the workflow as a Claude Code command.

## Platform Architecture

The PoC is organized as a small document-processing platform with four layers:

```text
User / Demo Operator
  |
  | manual terminal commands OR Claude Code /pipeline command
  v
Orchestration Layer
  |-- .claude/plugin.json
  `-- .claude/commands/pipeline.md
  |
  v
Processing Layer
  |-- prototype/converter.py
  |-- prototype/rebranding-engine.py
  `-- prototype/validation-script.sh
  |
  v
Data and Rules Layer
  |-- sample-data/input/
  |-- prototype/rebranding-rules.json
  |-- sample-data/expected_output/
  `-- docs/quality-criteria.md
  |
  v
Evidence and Handoff Layer
  |-- sample-data/output/
  |-- validation/test-results.md
  |-- results/validation_summary.md
  |-- DEPLOYMENT-GUIDE.md
  |-- LEADER-DEMO-GUIDE.md
  `-- SKILLS-MARKETPLACE-GUIDE.md
```

## How the Platform Works

1. A user provides a Word `.docx` file.
2. The converter reads the Word document with `python-docx`.
3. The converter writes DITA-XML to `sample-data/output/out.dita`.
4. The rebranding engine reads `prototype/rebranding-rules.json`.
5. The rebranding engine writes updated DITA-XML to `sample-data/output/out-rebranded.dita`.
6. The validation script checks XML structure, DITA structure, content signals, metadata, and file health.
7. QA records PASS, WARN, or FAIL in `validation/test-results.md`.
8. The demo team uses the guides to explain value, limitations, and next steps.

## Current PoC Flow

```text
sample-data/input/Gmail_Installation_Guide.docx
  -> prototype/converter.py
  -> sample-data/output/out.dita
  -> prototype/rebranding-engine.py
  -> sample-data/output/out-rebranded.dita
  -> prototype/validation-script.sh
  -> PASS, WARN, or FAIL
```

## Components

| Component | Path | Purpose |
| --- | --- | --- |
| Converter | `prototype/converter.py` | Converts Word `.docx` content into DITA-XML. |
| Rebranding engine | `prototype/rebranding-engine.py` | Applies terminology mappings to DITA XML text nodes. |
| Rebranding rules | `prototype/rebranding-rules.json` | Stores old-to-new brand terminology mappings. |
| Validator | `prototype/validation-script.sh` | Performs repeatable output quality checks. |
| Claude plugin manifest | `.claude/plugin.json` | Defines the local Claude Code plugin metadata. |
| Claude slash command | `.claude/commands/pipeline.md` | Defines `/pipeline` and tells Claude Code how to run the workflow. |
| Quality criteria | `docs/quality-criteria.md` | Explains how PASS, WARN, and FAIL should be interpreted. |
| Test results | `validation/test-results.md` | Captures formal QA evidence. |
| Skill-creator plugin | External Claude Code plugin | Optional helper for creating or improving a reusable marketplace skill. It is not required for running the current PoC. |

## Repository Inventory

This section explains every top-level folder and the important files inside it.

### `.agents/`

Reserved local workspace folder. It is currently empty and is not required for the PoC pipeline.

### `.claude/`

Claude Code plugin package for running the pipeline as a slash command.

| File | Purpose |
| --- | --- |
| `.claude/plugin.json` | Plugin manifest for `doc-intel-skills`. It defines plugin name, version, description, and author. |
| `.claude/commands/pipeline.md` | Slash-command prompt. Claude Code exposes it as `/pipeline` and uses `$ARGUMENTS` as the input `.docx` path. |

### `docs/`

Project knowledge base for workflow, assumptions, quality, sample data, and meetings.

| File | Purpose |
| --- | --- |
| `docs/workflow-map.md` | Shows how documents move from source input through conversion, validation, and review. |
| `docs/quality-criteria.md` | Defines PASS, WARN, and FAIL expectations for DITA output. |
| `docs/assumptions.md` | Captures mapping assumptions and known limits for headings, tables, images, and formatting. |
| `docs/sample-data-metadata.md` | Explains the sample inputs, expected outputs, complexity, and QA expectations. |
| `docs/meetings/kickoff-meeting-template.md` | Meeting template for project kickoff. |
| `docs/meetings/2026-06-23-sync.md` | Captured sync notes. |

### `prototype/`

Executable PoC implementation.

| File | Purpose |
| --- | --- |
| `prototype/converter.py` | Converts Word `.docx` files to DITA-XML. |
| `prototype/rebranding-engine.py` | Applies terminology mappings to DITA-XML. |
| `prototype/rebranding-rules.json` | Active brand terminology rules used by the rebranding engine. |
| `prototype/validation-script.sh` | Validates generated DITA output. Invoke with `-f <dita-file>`. |
| `prototype/requirements.txt` | Python dependencies for the prototype. |

### `sample-data/`

Sample inputs, expected reference outputs, and terminology samples.

| File or Folder | Purpose |
| --- | --- |
| `sample-data/input/Gmail_Installation_Guide.docx` | Main Word input for the demo pipeline. |
| `sample-data/input/sample-001.md` | Simple reference sample retained for metadata and lightweight comparison. |
| `sample-data/expected_output/gmail-guide-expected.dita` | Hand-curated reference DITA for the Gmail guide. |
| `sample-data/expected_output/sample-001-expected.dita` | Hand-curated reference DITA for the simple sample. |
| `sample-data/brand_terminology.json` | Reference terminology data. The active pipeline uses `prototype/rebranding-rules.json`. |
| `sample-data/output/` | Generated at runtime. Contains `out.dita` and `out-rebranded.dita` after the pipeline runs. |

### `results/`

Demo and validation evidence folder.

| File | Purpose |
| --- | --- |
| `results/README.md` | Explains how to store demo and validation evidence. |
| `results/demo_guide.md` | Short local demo guide for the build team. |
| `results/validation_summary.md` | Latest high-level validation status placeholder. |

### `validation/`

Formal QA evidence folder.

| File | Purpose |
| --- | --- |
| `validation/test-results.md` | Test matrix and detailed validation notes. Update this after formal test runs. |

### Root Files

| File | Purpose |
| --- | --- |
| `README.md` | Architecture overview, component map, and quick start. |
| `DEPLOYMENT-GUIDE.md` | Single source of truth for implementing and running the PoC. |
| `LEADER-DEMO-GUIDE.md` | Step-by-step leader demo runbook. |
| `SKILLS-MARKETPLACE-GUIDE.md` | Instructions for publishing the Claude plugin to a separate marketplace repo. |
| `CHARTER.md` | Scope, timeline, success criteria, and project assumptions. |
| `OWNER-CHECKLIST.md` | Owner coordination checklist and readiness tracker. |
| `roster.md` | Team roles and responsibilities. |
| `.gitignore` | Ignore rules for generated and local files. |
| `LICENSE` | Repository license. |

## Claude Code Plugin and Skills

The `.claude/` folder makes the PoC easier to run through Claude Code.

- `plugin.json` identifies the plugin as `doc-intel-skills`.
- `commands/pipeline.md` becomes the `/pipeline` command.
- `$ARGUMENTS` represents the input file path passed by the user.

Run in Claude Code:

```text
/pipeline sample-data/input/Gmail_Installation_Guide.docx
```

Claude Code then follows the prompt in `.claude/commands/pipeline.md` and runs:

```bash
python prototype/converter.py --input sample-data/input/Gmail_Installation_Guide.docx --output sample-data/output/out.dita
python prototype/rebranding-engine.py --input sample-data/output/out.dita --rules prototype/rebranding-rules.json --output sample-data/output/out-rebranded.dita
bash prototype/validation-script.sh -f sample-data/output/out-rebranded.dita
```

This is useful for demos because the skill command standardizes the process and reduces operator mistakes.

For the live demo, use the existing `/pipeline` command. Do not run skill-creator during the demo.

Use the skill-creator plugin only when creating or improving a reusable skill package, usually for the separate skills marketplace repo. If the team uses skill-creator, run it from the target repo and give it an explicit output folder such as:

```text
skills/doc-intel-skills/
```

Use an RTCCO prompt for best results:

- Role: Define the AI as a skill-creator assistant for the Document Intelligence team.
- Task: Create or update the `doc-intel-skills` package.
- Context: Include current files, target repo, and intended users.
- Constraints: Preserve `/pipeline`, `$ARGUMENTS`, strict JSON, YAML frontmatter, and the validation command with `-f`.
- Output: Ask for exact files changed, invocation steps, required host repo files, and validation checks.

The full skill-creator workflow and example prompts are in `DEPLOYMENT-GUIDE.md`.

## Quick Start

Use Python 3.10 or 3.11 for this PoC. The pinned dependencies are not currently safe on Python 3.14 without extra native build dependencies.

From the repo root:

```bash
python -m venv .venv
```

On Windows with multiple Python versions:

```bash
py -3.11 -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Git Bash, macOS, or Linux
source .venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r prototype/requirements.txt
```

On Windows, use Git Bash for the validation script. PowerShell can run the Python commands, but `prototype/validation-script.sh` needs Bash.

Run the manual pipeline:

```bash
python prototype/converter.py --input sample-data/input/Gmail_Installation_Guide.docx --output sample-data/output/out.dita
python prototype/rebranding-engine.py --input sample-data/output/out.dita --rules prototype/rebranding-rules.json --output sample-data/output/out-rebranded.dita
bash prototype/validation-script.sh -f sample-data/output/out-rebranded.dita
```

## Repository Structure

```text
doc-intel-platform/
|-- .agents/
|-- .claude/
|   |-- plugin.json
|   `-- commands/pipeline.md
|-- docs/
|   |-- assumptions.md
|   |-- quality-criteria.md
|   |-- sample-data-metadata.md
|   |-- workflow-map.md
|   `-- meetings/
|-- prototype/
|   |-- converter.py
|   |-- rebranding-engine.py
|   |-- rebranding-rules.json
|   |-- requirements.txt
|   `-- validation-script.sh
|-- sample-data/
|   |-- input/
|   |-- expected_output/
|   |-- brand_terminology.json
|   `-- README.md
|-- results/
|   |-- README.md
|   |-- demo_guide.md
|   `-- validation_summary.md
|-- validation/
|   `-- test-results.md
|-- DEPLOYMENT-GUIDE.md
|-- LEADER-DEMO-GUIDE.md
`-- SKILLS-MARKETPLACE-GUIDE.md
```

## Important Guides

- `DEPLOYMENT-GUIDE.md` - Step-by-step implementation process for the core team.
- `LEADER-DEMO-GUIDE.md` - Step-by-step demo process for leaders.
- `SKILLS-MARKETPLACE-GUIDE.md` - Step-by-step process to add this plugin to a separate skills marketplace repository.
- `docs/quality-criteria.md` - Quality checks and reporting expectations.
- `results/demo_guide.md` - Short local demo guide for the build team.

## Scope

In scope:

- Demonstrate Word-to-DITA conversion on sample data.
- Demonstrate configurable terminology replacement.
- Demonstrate repeatable validation.
- Package the workflow as a Claude Code command.
- Document how to publish the skill to a marketplace repository.

Out of scope:

- Production UI
- Batch migration service
- Full DITA specialization support
- Perfect preservation of complex Word formatting
- Automated expected-vs-actual diff gate

## Recommended Next Steps

- Add a wrapper script after demo approval to run all three commands with one input.
- Add automated expected-vs-actual comparison for QA.
- Add more realistic sample documents before production planning.
- Publish the Claude command through the team's skills marketplace repository once reviewed.
