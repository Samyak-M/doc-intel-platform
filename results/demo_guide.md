# Demo Guide: Running the PoC demo

This guide shows the minimum steps to run the proof-of-concept demo included in this repository. The PoC intentionally targets a minimal, reproducible pipeline that demonstrates document ingestion, simple transformation, brand-term replacement, and a basic validation summary.

Prerequisites

- Python 3.8+ installed and on your PATH
- (Optional) A virtual environment is recommended

Quick setup

```bash
# from repo root
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.\.venv\Scripts\activate  # Windows PowerShell

# Install dependencies (none required for this stub; this file contains notes)
pip install -r requirements.txt
```

Prepare sample inputs

- Place at least one input file in `samples/input/`. The demo accepts text, Markdown, and HTML files and will create simple placeholder outputs for binary formats like .docx.
- Example files:
  - `samples/input/sample-001.md`
  - `samples/input/sample-002.html`

Brand terminology file

- Default: `samples/brand_terminology.json`
- Edit this file to add mappings that will be applied during the rebranding step.

Run the demo

```bash
python src/main.py --input samples/input --output results --terms samples/brand_terminology.json
```

What this script does (minimal stub)

1. Scans `samples/input/` for files.
2. For text-based files (.md, .txt, .html): reads content, applies brand-term replacements, and writes a transformed file to `results/demo_output/` (XML/HTML placeholder).
3. For binary files (example: .docx): creates a small placeholder XML noting the source filename in `results/demo_output/`.
4. Produces a `results/validation_summary.md` that lists processed files, how many replacements were applied, and basic notes on the transformation.
5. Copies original/after files into `results/before_after/` for quick comparison.

Output layout

- `results/demo_output/` — transformed output files (placeholders for PoC)
- `results/before_after/` — original and after files for manual inspection
- `results/validation_summary.md` — short validation report and transformation notes

How to validate

- Open `results/validation_summary.md` to see which files were processed and which terms changed.
- Inspect `results/before_after/` to confirm replacements or structural changes.

Next steps to evolve this PoC

- Replace the placeholder conversion logic with a real converter (e.g., python-docx → DITA-XML) in `src/`.
- Add unit tests in `tests/` and validation rules in `validation/`.
- Expand the validation report to include structural checks and XML schema validation.

---

Owner: Demo & Documentation Lead
Last updated: 22 June 2026
