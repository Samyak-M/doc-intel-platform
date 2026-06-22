"""
Minimal PoC conversion stub for the Document Intelligence Platform.

Usage:
  python src/main.py --input samples/input --output results --terms samples/brand_terminology.json

What it does (stub):
- Reads simple text/markdown/html files from the input directory
- Applies brand-term replacements (supports literal and regex mappings)
- Writes transformed placeholder XML files to results/demo_output/
- Copies original and transformed files to results/before_after/
- Writes a basic results/validation_summary.md file with replacement counts

Notes:
- This is a minimal, dependency-free stub intended for demos. Replace the conversion
  logic with real converters (e.g., python-docx, lxml, DITA toolchains) as needed.
"""

import argparse
import json
import re
from pathlib import Path
from typing import List, Dict


def load_terms(terms_path: Path) -> List[Dict]:
    with terms_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("brand_terms", [])


def apply_terms_to_text(text: str, terms: List[Dict]) -> (str, int):
    """Apply brand term replacements to a single text blob.
    Returns the transformed text and the total number of replacements made.
    """
    total_replacements = 0
    result = text
    for term in terms:
        old = term.get("old_term")
        new = term.get("new_term", "")
        regex = bool(term.get("regex", False))
        if not old:
            continue
        if regex:
            # Use re.sub and count replacements
            new_result, n = re.subn(old, new, result)
            result = new_result
            total_replacements += n
        else:
            # Literal replacement with word boundaries to avoid partial matches
            pattern = r"\b" + re.escape(old) + r"\b"
            new_result, n = re.subn(pattern, new, result)
            result = new_result
            total_replacements += n
    return result, total_replacements


def make_placeholder_xml(title: str, body_html: str) -> str:
    return f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<topic>
  <title>{escape_xml(title)}</title>
  <body>
{body_html}
  </body>
</topic>
"""


def escape_xml(s: str) -> str:
    return (s.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;"))


def text_to_xml_paragraphs(text: str) -> str:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    xml_pars = []
    for p in paragraphs:
        # escape and wrap in <p>
        xml_pars.append("    <p>" + escape_xml(p).replace('\n', ' ') + "</p>")
    return "\n".join(xml_pars)


def process_file(path: Path, terms: List[Dict], out_demo_dir: Path, before_after_dir: Path) -> Dict:
    summary = {"file": str(path), "replacements": 0, "output": None}
    suffix = path.suffix.lower()
    out_demo_dir.mkdir(parents=True, exist_ok=True)
    before_after_dir.mkdir(parents=True, exist_ok=True)

    if suffix in {".md", ".txt", ".html"}:
        text = path.read_text(encoding="utf-8")
        transformed, n = apply_terms_to_text(text, terms)
        summary["replacements"] = n
        # write a placeholder XML to demo output
        title = path.stem
        body_html = text_to_xml_paragraphs(transformed)
        xml = make_placeholder_xml(title, body_html)
        out_file = out_demo_dir / (path.stem + ".xml")
        out_file.write_text(xml, encoding="utf-8")
        summary["output"] = str(out_file)

        # copy before/after
        (before_after_dir / (path.stem + "-before" + suffix)).write_text(text, encoding="utf-8")
        (before_after_dir / (path.stem + "-after.xml")).write_text(xml, encoding="utf-8")

    else:
        # For binary or unknown formats, create a placeholder noting we saw the file
        note = f"Placeholder transformation for binary or unsupported file: {path.name}\n"
        note += "(Replace this with real docx->dita conversion logic in src/main.py)\n"
        xml = make_placeholder_xml(path.stem, "    <p>" + escape_xml(note) + "</p>")
        out_file = out_demo_dir / (path.stem + ".xml")
        out_file.write_text(xml, encoding="utf-8")
        summary["output"] = str(out_file)
        summary["replacements"] = 0
        (before_after_dir / (path.stem + "-before" + suffix)).write_bytes(path.read_bytes())
        (before_after_dir / (path.stem + "-after.xml")).write_text(xml, encoding="utf-8")

    return summary


def main():
    parser = argparse.ArgumentParser(description="Minimal PoC converter and rebranding stub")
    parser.add_argument("--input", required=True, help="Input directory containing sample files")
    parser.add_argument("--output", required=True, help="Output root directory for results")
    parser.add_argument("--terms", required=True, help="Brand terminology JSON file")
    args = parser.parse_args()

    input_dir = Path(args.input)
    output_root = Path(args.output)
    terms_path = Path(args.terms)

    if not input_dir.exists():
        print(f"Input directory does not exist: {input_dir}")
        return
    if not terms_path.exists():
        print(f"Terms file does not exist: {terms_path}")
        return

    terms = load_terms(terms_path)
    demo_out = output_root / "demo_output"
    before_after = output_root / "before_after"
    demo_out.mkdir(parents=True, exist_ok=True)
    before_after.mkdir(parents=True, exist_ok=True)

    summaries = []
    for p in sorted(input_dir.iterdir()):
        if p.is_file():
            s = process_file(p, terms, demo_out, before_after)
            summaries.append(s)

    # write validation summary
    summary_lines = ["# Validation Summary", "", "Processed files:", ""]
    total_replacements = 0
    for s in summaries:
        summary_lines.append(f"- {s['file']}")
        summary_lines.append(f"  - Output: {s.get('output')}")
        summary_lines.append(f"  - Replacements: {s.get('replacements', 0)}")
        summary_lines.append("")
        total_replacements += s.get('replacements', 0)

    summary_lines.append(f"Total replacements: {total_replacements}")

    output_root.mkdir(parents=True, exist_ok=True)
    (output_root / "validation_summary.md").write_text("\n".join(summary_lines), encoding="utf-8")

    print("Done. See validation summary at:", str(output_root / "validation_summary.md"))


if __name__ == "__main__":
    main()
