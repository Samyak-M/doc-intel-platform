# Demo Guide: Document Intelligence PoC

**For:** Build team presenting the PoC locally  
**Time:** 10–15 minutes  
**Audience:** Technical or non-technical team members  

---

## Pre-Demo Setup (5 minutes before)

### Checklist

- [ ] Claude Code open with repo as active workspace
- [ ] Python environment activated (`.venv`)
- [ ] Dependencies installed: `pip install -r prototype/requirements.txt`
- [ ] Clean previous outputs: `rm -f sample-data/output/*.dita`
- [ ] Open in editor tabs:
  - `sample-data/input/Gmail_Installation_Guide.docx`
  - `prototype/rebranding-rules.json`
  - `docs/quality-criteria.md`

### If Demo Machine Fails

Have ready:
- Previously generated output files (or use expected outputs from `sample-data/expected_output/`)
- Screenshots of a successful run
- Talk track for explaining each step

---

## Demo Flow (10 minutes)

### 1. Show the Input (1 minute)

**Say:**
> "This is a real Word document about Gmail setup. It has headings, paragraphs, tables, and lists. Our PoC will convert this to DITA-XML, apply brand terminology, and validate the result."

**Show:** `sample-data/input/Gmail_Installation_Guide.docx`

### 2. Show the Rules (1 minute)

**Say:**
> "These are the brand terminology rules. We can update brand language without touching the converter code. Today's rules change 'Gmail' to 'NewGmail' and similar terms."

**Show:** `prototype/rebranding-rules.json` (scroll through to show ~10 rules)

### 3. Run the Pipeline (3 minutes)

**Say:**
> "Let's run the entire pipeline with one command. This will convert, rebrand, and validate in sequence."

**In Claude Code chat, run:**

```text
/pipeline sample-data/input/Gmail_Installation_Guide.docx
```

**What happens:**
- Step 1 (Converter): Word → DITA (creates `Gmail_Installation_Guide-output.dita`)
- Step 2 (Rebranding): Updates brand terms (creates `Gmail_Installation_Guide-rebranded.dita`)
- Step 3 (Validation): Checks quality (returns PASS, WARN, or FAIL)

**Expected output in Claude Code:**
```
SUCCESS: All validation checks passed.
Output files:
  - DITA (original):  sample-data/output/Gmail_Installation_Guide-output.dita
  - DITA (rebranded): sample-data/output/Gmail_Installation_Guide-rebranded.dita
```

### 4. Show the Outputs (3 minutes)

**Show:** `sample-data/output/Gmail_Installation_Guide-output.dita`

**Point out:**
- Valid DITA-XML structure
- Topic, title, body, sections, paragraphs, tables are present
- No obvious content loss

**Show:** `sample-data/output/Gmail_Installation_Guide-rebranded.dita`

**Point out:**
- Compare with output.dita to show brand terms were replaced
- Example: "Gmail" → "NewGmail"
- No other content changed

### 5. Show Validation (2 minutes)

**Say:**
> "Validation checks our output against quality criteria. Let's see what was checked."

**Show:** Validation output from Claude Code (should show PASS checks and maybe some WARN)

**Show:** `docs/quality-criteria.md`

**Explain the levels:**
- **PASS:** Check succeeded
- **WARN:** Check passed with warnings (acceptable for PoC)
- **FAIL:** Check failed (would block in production)

---

## Talk Track (What to Say)

### Opening (30 seconds)

> "Documentation teams spend time converting Word docs to DITA, updating brand language, and checking quality. This PoC automates those steps using Python scripts and a Claude Code plugin."

### During Conversion (1 minute)

> "Step 1 reads the Word document and writes DITA-XML. We're converting headings to sections, paragraphs to paragraphs, and tables to DITA tables. The output preserves structure but not formatting."

### During Rebranding (30 seconds)

> "Step 2 applies controlled terminology changes from JSON rules. Updating rules doesn't require code changes. Content owners can review and edit the rules directly."

### During Validation (1 minute)

> "Step 3 validates the output. We check XML structure, DITA structure, content presence, metadata, and file health. The PASS/WARN/FAIL status gives the team a clear quality gate."

### Closing (30 seconds)

> "This is a working PoC, not production software. It shows that the core workflow is automatable. Next steps would be more samples, stronger validation, batch processing, and integration with our documentation platform."

---

## Demo Success Criteria

✓ Pipeline runs without errors  
✓ Output files are created with correct names  
✓ Rebranding is visible (term replacements appear in output)  
✓ Validation completes and reports status  
✓ Audience understands the three steps  
✓ Limitations are stated plainly  

---

## If Something Breaks

**During the demo:**

1. **Don't debug.** Say: "Let me check the logs."
2. **Show the command that failed:** Print the exact line from Claude Code.
3. **Use manual fallback:**
   ```bash
   # Run steps manually if /pipeline fails
   python prototype/converter.py --input sample-data/input/Gmail_Installation_Guide.docx --output sample-data/output/Gmail_Installation_Guide-output.dita
   python prototype/rebranding-engine.py --input sample-data/output/Gmail_Installation_Guide-output.dita --rules prototype/rebranding-rules.json --output sample-data/output/Gmail_Installation_Guide-rebranded.dita
   bash prototype/validation-script.sh sample-data/output/Gmail_Installation_Guide-rebranded.dita
   ```
4. **If that also fails:** Use previously generated outputs and explain: "Here's what a successful run produces."
5. **Read quality criteria:** Open `docs/quality-criteria.md` and report 5 bullets (PASS, WARN, FAIL) based on what you know about the output.

---

## Demo Narrative

**Problem:** "Documentation migration is slow and error-prone. Word-to-DITA conversion requires manual restructuring."

**Approach:** "We built a PoC pipeline: convert → rebrand → validate. One Claude Code command runs all three steps."

**Demo:** "Watch as we convert a real Word doc, apply brand terminology, and validate in ~30 seconds."

**Learnings:**
- Basic conversion works well for structure (headings, paragraphs, tables).
- Rebranding with rules is reliable and doesn't require code changes.
- Validation catches missing elements and structure issues.

**Limitations:**
- Does not preserve formatting (colors, fonts, images).
- DITA output needs manual review before use.
- Scope is PoC; production would need logging, error handling, batch support.

**Next Steps:**
- Test on more samples.
- Publish plugin to skills marketplace.
- Plan production discovery phase.

---

## One-Liner Talking Points

- "One command converts, rebrands, and validates."
- "Rules are JSON; no code changes needed."
- "Output is DITA-XML; compatible with standard tools."
- "This is feasibility-proven, not production-ready."

---

## Post-Demo

- Record the demo output (optional) by taking screenshots.
- Update `results/validation_summary.md` with results.
- Update `validation/test-results.md` with timestamp and PASS/WARN/FAIL status.
- Ask audience: "What would you need to use this in production?"
