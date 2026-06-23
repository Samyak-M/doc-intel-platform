#!/usr/bin/env python3
"""
Rebranding Engine — Brand Terminology Mapper

Applies brand terminology mappings to DITA-XML documents using configurable
rules from JSON. Performs search-replace with case-sensitivity and regex support.

Usage:
    python rebranding-engine.py --input document.dita --rules rules.json --output document-rebranded.dita
    python rebranding-engine.py -i doc.dita -r rules.json -o doc-new.dita --verbose

Rules format (JSON):
    {
      "terminology_mappings": [
        {
          "old": "OldTerm",
          "new": "NewTerm",
          "case_sensitive": true,
          "regex": false,
          "description": "Main product name"
        }
      ]
    }

Author: Document Converter Team
Version: 1.0
Date: June 2026
"""

import argparse
import sys
import json
import logging
import re
from pathlib import Path
from datetime import datetime
from xml.etree import ElementTree as ET


class RebranchingEngine:
    """Apply brand terminology mappings to DITA-XML documents."""
    
    def __init__(self, verbose=False):
        """Initialize rebranding engine."""
        self.verbose = verbose
        self.logger = self._setup_logging()
        self.rules = []
        self.replacements_made = {}
        self.replacement_log = {
            'input_file': None,
            'output_file': None,
            'rules_file': None,
            'timestamp': datetime.now().isoformat(),
            'total_rules': 0,
            'total_replacements': 0,
            'replacements_by_rule': {},
            'warnings': []
        }
    
    def _setup_logging(self):
        """Configure logging output."""
        logger = logging.getLogger(__name__)
        logger.handlers.clear()
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG if self.verbose else logging.INFO)
        return logger
    
    def rebrand(self, input_file, rules_file, output_file):
        """Main rebranding workflow."""
        try:
            self.logger.info(f"Starting rebranding: {input_file}")
            self.replacement_log['input_file'] = input_file
            self.replacement_log['output_file'] = output_file
            self.replacement_log['rules_file'] = rules_file
            
            # Load rules
            if not self._load_rules(rules_file):
                return False
            
            # Load DITA document
            tree = ET.parse(input_file)
            root = tree.getroot()
            
            # Apply replacements to all text nodes
            self._apply_replacements(root)
            
            # Write output
            self._write_output(tree, output_file)
            
            self.logger.info(f"✓ Rebranding successful: {output_file}")
            self._print_summary()
            return True
            
        except FileNotFoundError as e:
            self.logger.error(f"File not found: {e}")
            return False
        except json.JSONDecodeError:
            self.logger.error(f"Invalid JSON in rules file: {rules_file}")
            return False
        except ET.ParseError:
            self.logger.error(f"Invalid XML in input file: {input_file}")
            return False
        except Exception as e:
            self.logger.error(f"Rebranding failed: {str(e)}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return False
    
    def _load_rules(self, rules_file):
        """Load rebranding rules from JSON file."""
        try:
            with open(rules_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.rules = data.get('terminology_mappings', [])
            self.replacement_log['total_rules'] = len(self.rules)
            
            self.logger.info(f"Loaded {len(self.rules)} rebranding rules")
            
            # Validate rules
            for i, rule in enumerate(self.rules):
                if 'old' not in rule or 'new' not in rule:
                    self.logger.warning(f"Rule {i} missing 'old' or 'new' field")
                    self.replacement_log['warnings'].append(
                        f"Rule {i}: Missing required field (old/new)"
                    )
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to load rules: {str(e)}")
            return False
    
    def _apply_replacements(self, element):
        """Recursively apply replacements to all text nodes."""
        # Process text content
        if element.text:
            element.text = self._replace_text(element.text)
        
        # Process tail content (text after closing tag)
        if element.tail:
            element.tail = self._replace_text(element.tail)
        
        # Process child elements recursively
        for child in element:
            self._apply_replacements(child)
    
    def _replace_text(self, text):
        """Apply all rebranding rules to text."""
        result = text
        
        for rule in self.rules:
            old_term = rule.get('old', '')
            new_term = rule.get('new', '')
            case_sensitive = rule.get('case_sensitive', True)
            use_regex = rule.get('regex', False)
            description = rule.get('description', old_term)
            
            if not old_term or not new_term:
                continue
            
            try:
                if use_regex:
                    # Regex replacement
                    flags = 0 if case_sensitive else re.IGNORECASE
                    pattern = re.compile(old_term, flags)
                    count = len(pattern.findall(result))
                else:
                    # Simple string replacement
                    if case_sensitive:
                        count = result.count(old_term)
                        result = result.replace(old_term, new_term)
                    else:
                        # Case-insensitive replacement
                        pattern = re.compile(re.escape(old_term), re.IGNORECASE)
                        matches = pattern.finditer(result)
                        offsets = []
                        for match in matches:
                            offsets.append((match.start(), match.end()))
                        
                        # Replace from end to start to preserve offsets
                        for start, end in reversed(offsets):
                            result = result[:start] + new_term + result[end:]
                        count = len(offsets)
                
                if count > 0:
                    self.replacement_log['total_replacements'] += count
                    self.replacement_log['replacements_by_rule'][old_term] = {
                        'new_term': new_term,
                        'count': count,
                        'description': description
                    }
                    self.logger.debug(
                        f"Replaced '{old_term}' → '{new_term}' ({count}x)"
                    )
            
            except re.error as e:
                warning = f"Regex error in rule '{old_term}': {str(e)}"
                self.logger.warning(warning)
                self.replacement_log['warnings'].append(warning)
        
        return result
    
    def _write_output(self, tree, output_file):
        """Write modified DITA document to file."""
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Register DITA namespace
        ET.register_namespace('', 'http://www.oasis-open.org/committees/dita/dtd')
        
        # Write with XML declaration
        tree.write(
            output_file,
            encoding='utf-8',
            xml_declaration=True,
            method='xml'
        )
        
        self.logger.info(f"Wrote rebranded document: {output_file}")
    
    def _print_summary(self):
        """Print rebranding summary."""
        print("\n" + "="*60)
        print("REBRANDING SUMMARY")
        print("="*60)
        print(f"Input:        {self.replacement_log['input_file']}")
        print(f"Rules:        {self.replacement_log['rules_file']}")
        print(f"Output:       {self.replacement_log['output_file']}")
        print(f"Timestamp:    {self.replacement_log['timestamp']}")
        print(f"Total Rules:  {self.replacement_log['total_rules']}")
        print(f"Total Replacements: {self.replacement_log['total_replacements']}")
        print(f"Status:       ✓ SUCCESS")
        
        if self.replacement_log['replacements_by_rule']:
            print("\nReplacements by rule:")
            for old_term, info in self.replacement_log['replacements_by_rule'].items():
                print(f"  • '{old_term}' → '{info['new_term']}': {info['count']} replacements")
        
        if self.replacement_log['warnings']:
            print(f"\nWarnings:     {len(self.replacement_log['warnings'])}")
            for w in self.replacement_log['warnings']:
                print(f"  ⚠ {w}")
        
        print("="*60 + "\n")


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description='Apply brand terminology mappings to DITA-XML documents',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python rebranding-engine.py -i doc.dita -r rules.json -o doc-rebranded.dita
  python rebranding-engine.py --input doc.dita --rules rules.json --output doc-new.dita --verbose

Rules JSON format:
  {
    "terminology_mappings": [
      {
        "old": "OldBrand",
        "new": "NewBrand",
        "case_sensitive": true,
        "regex": false,
        "description": "Main brand name"
      }
    ]
  }
        '''
    )
    
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Input DITA-XML file'
    )
    parser.add_argument(
        '-r', '--rules',
        required=True,
        help='Rebranding rules (JSON file)'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output DITA-XML file (rebranded)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    engine = RebranchingEngine(verbose=args.verbose)
    success = engine.rebrand(args.input, args.rules, args.output)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
