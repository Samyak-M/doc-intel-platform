# Skills Marketplace Guide: Publishing the Document Pipeline Skill

Use this guide when adding the Claude Code plugin from this repo to a separate skills marketplace repository where other skills are maintained.

## Goal

Publish the `doc-intel-skills` plugin so other teams can install or copy the same `/pipeline` command.

The current PoC already includes the local Claude Code command files:

```text
.claude/plugin.json
.claude/commands/pipeline.md
```

Use these existing files for the live demo. No separate `SKILL.md`-based marketplace skill has been generated in this repo yet. Use skill-creator only if the marketplace repo requires a generated skill package, a `SKILL.md`-style artifact, or a refined marketplace-ready wrapper.

## When to Use Skill-Creator

Use skill-creator when:

- Creating the marketplace package for the first time.
- Converting this local Claude command into the marketplace repo's standard skill format.
- Improving `/pipeline` after feedback from the core team or leaders.
- Adding another command, such as `/pipeline-report` or `/pipeline-debug`.

Do not use skill-creator when:

- Running the live demo.
- Running `/pipeline`.
- Running the manual Python and Bash scripts.
- Recording validation results.

Run skill-creator in the target repo where the generated skill should live. For marketplace publication, that means the marketplace repo, not this PoC repo.

Always provide an explicit output directory:

```text
skills/doc-intel-skills/
```

Do not let the generated team artifact remain only in a personal/global Claude or user home directory. Personal placement is fine for experiments, but the publishable skill must be committed to the marketplace repo.

## RTCCO Prompt for Skill-Creator

Use this prompt when asking skill-creator to generate the marketplace package:

```text
Role:
You are a Claude Code skill-creator assistant for the Document Intelligence Platform team.

Task:
Create a reusable marketplace skill package named doc-intel-skills.

Context:
The working PoC already has:
- .claude/plugin.json
- .claude/commands/pipeline.md
- prototype/converter.py
- prototype/rebranding-engine.py
- prototype/rebranding-rules.json
- prototype/validation-script.sh
- docs/quality-criteria.md

The skill lets users run a Word to DITA-XML conversion pipeline from Claude Code.

Constraints:
- Preserve the /pipeline command.
- Keep $ARGUMENTS as the input .docx path.
- Use strict JSON if plugin.json is generated.
- Keep YAML frontmatter at the top of pipeline.md.
- Validation must use: bash prototype/validation-script.sh -f sample-data/output/out-rebranded.dita
- Put the package under skills/doc-intel-skills/.
- Do not copy prototype scripts unless the marketplace owner explicitly wants executable scripts included.

Output:
Create or update the marketplace skill package and report:
- Files created or changed
- How users invoke it
- Required host repo files
- Validation checks completed
```

## Source Files in This Repo

Copy these files from this repository:

```text
.claude/plugin.json
.claude/commands/pipeline.md
```

The command depends on this target project structure when installed in a Document Intelligence repo:

```text
prototype/converter.py
prototype/rebranding-engine.py
prototype/rebranding-rules.json
prototype/validation-script.sh
docs/quality-criteria.md
sample-data/output/
```

## Step 1: Create a Branch in the Marketplace Repo

In the separate skills marketplace repo:

```bash
git checkout main
git pull
git checkout -b add-doc-intel-skills
```

## Step 2: Add the Plugin Folder

Create a dedicated folder using the plugin name:

```text
skills/doc-intel-skills/
```

Copy the plugin files into that folder:

```text
skills/doc-intel-skills/.claude/plugin.json
skills/doc-intel-skills/.claude/commands/pipeline.md
```

If the marketplace repo uses a different folder convention, keep the same internal `.claude/` structure and place it under the marketplace's standard skill/plugin location.

## Step 3: Add a Marketplace README

Create:

```text
skills/doc-intel-skills/README.md
```

Recommended content:

```markdown
# doc-intel-skills

Claude Code command plugin for the Document Intelligence PoC.

## Command

`/pipeline <path-to-docx>`

## What It Does

1. Converts Word `.docx` to DITA-XML.
2. Applies brand terminology rules.
3. Validates the rebranded DITA output.

## Required Host Repo Files

- `prototype/converter.py`
- `prototype/rebranding-engine.py`
- `prototype/rebranding-rules.json`
- `prototype/validation-script.sh`
- `docs/quality-criteria.md`
```

## Step 4: Register the Skill in the Marketplace Index

If the marketplace repo has an index file, add an entry similar to:

```json
{
  "name": "doc-intel-skills",
  "version": "1.0.0",
  "description": "Document Intelligence PoC pipeline command for Word to DITA-XML conversion.",
  "path": "skills/doc-intel-skills",
  "owner": "Document Intelligence Team"
}
```

Use the existing index format in that repo. Do not invent a new registry format if one already exists.

## Step 5: Validate the Copied Files

From the marketplace repo:

```bash
python -m json.tool skills/doc-intel-skills/.claude/plugin.json
```

Then check the command file manually:

- YAML frontmatter is at the top.
- Description is present.
- `$ARGUMENTS` is used for the input `.docx`.
- Validation command uses `-f`.
- Failure handling references `docs/quality-criteria.md`.

## Step 6: Test Installation in a Fresh Consumer Repo

Use a clean checkout of this Document Intelligence repo.

1. Install or copy the skill from the marketplace.
2. Confirm `.claude/plugin.json` and `.claude/commands/pipeline.md` appear in the consumer repo.
3. Run:

```text
/pipeline sample-data/input/Gmail_Installation_Guide.docx
```

4. Confirm these outputs are produced:

```text
sample-data/output/out.dita
sample-data/output/out-rebranded.dita
```

5. Confirm validation completes with PASS, WARN, or FAIL.

## Step 7: Open the Marketplace Pull Request

PR checklist:

- Plugin folder added.
- Marketplace index updated, if applicable.
- README added.
- JSON manifest validated.
- Command tested in a fresh consumer repo.
- Owner reviewer tagged.

Suggested PR title:

```text
Add doc-intel-skills pipeline command
```

Suggested PR summary:

```markdown
Adds the Document Intelligence PoC Claude Code plugin with a `/pipeline` command that converts Word documents to DITA-XML, applies rebranding rules, and validates the output.
```

## Practical Simplifications

- Keep the marketplace package limited to the Claude plugin files and README.
- Do not copy prototype scripts into the marketplace unless the marketplace is intended to distribute code, not just skills.
- Keep version `1.0.0` until the command interface changes.
- Add screenshots only after the first successful leader demo.
- Assign one owner for marketplace publishing so plugin changes do not drift from the source repo.
