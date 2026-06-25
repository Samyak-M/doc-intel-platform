Role:
You are an experienced AI workflow architect and content strategist for enterprise documentation automation.

Task:
Design a robust Claude Code plugin bundle for the Document Intelligence Platform. You will generate a single, deterministic pipeline command (`pipeline.md`) that orchestrates a Word-to-DITA conversion, rebranding, and validation flow, along with its required plugin manifest (`plugin.json`).

Context:
Repository: Samyak-M/doc-intel-platform
Primary setup reference: SETUP-AND-DEPLOY.md
Primary demo input example: sample-data/input/Gmail\_Installation\_Guide.docx

Host repo assets (where the scripts live):

* prototype/converter.py
* prototype/rebranding-engine.py
* prototype/rebranding-rules.json
* prototype/validation-script.sh
* docs/quality-criteria.md

Constraints:

1. Architecture Structure:

   * The output must reflect a standard Claude Code plugin bundle containing exactly two files: `plugin.json` (at the root of the bundle) and `commands/pipeline.md` (inside the commands directory).
   * Do not generate background skills (SKILL.md) or agents. Keep this strictly as a manual slash-command.
2. Input Contract for the Command:

   * Use $ARGUMENTS as the required input .docx path.
   * If $ARGUMENTS is missing, the command must return a concise usage message and halt execution immediately.
3. Execution Sequence:

   * The command must execute the following scripts in this exact order. Do not deviate from these paths or add extra stages:
Step 1: python prototype/converter.py --input $ARGUMENTS --output sample-data/output/out.dita
Step 2: python prototype/rebranding-engine.py --input sample-data/output/out.dita --rules prototype/rebranding-rules.json --output sample-data/output/out-rebranded.dita
Step 3: bash prototype/validation-script.sh sample-data/output/out-rebranded.dita
4. Failure Handling:

   * The agent must stop immediately if any step fails.
   * If a failure occurs, report the failed step, the exact command that failed, and suggest a practical next action.
5. Validation Reporting (Strict Output):

   * If Step 3 (validation) fails, the agent MUST read `docs/quality-criteria.md`.
   * Based on that file, return exactly 5 bullet points summarizing the validation status.
   * Each bullet must begin with the exact word PASS, WARN, or FAIL.
6. File Formatting Requirements:

   * `commands/pipeline.md`: Must include YAML frontmatter at the top containing only a `description` field. Keep the prompt body deterministic and concise. Do not rewrite or alter the underlying prototype scripts.
   * `plugin.json`: Must be strict, valid JSON containing `name`, `version`, `description`, and `author` (Document Intelligence Team). The description must clearly state the convert + rebrand + validate behavior.

Output format:

1. Provide the complete code blocks for:

   * plugin.json
   * commands/pipeline.md
2. Provide a concise implementation summary including:

   * Expected command usage example (e.g., /namespace:pipeline <path>).
   * Required host-repo dependencies.

