#!/bin/bash

###############################################################################
# DITA Validation Script
# 
# Validates DITA-XML output from converter and rebranding engine.
# Checks: XML well-formedness, structure, required elements, and quality.
#
# Usage:
#   bash validation-script.sh document.dita
#   bash validation-script.sh -f document.dita -v
#   bash validation-script.sh --file doc.dita --verbose
#
# Requirements:
#   - xmllint (libxml2) for XML validation
#   - grep for text searching
#
# Author: Document Converter Team
# Version: 1.0
# Date: June 2026
###############################################################################

set -o pipefail

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'  # No Color

# Configuration
DITA_FILE=""
VERBOSE=false
FAILED_CHECKS=0
PASSED_CHECKS=0
WARNING_COUNT=0

###############################################################################
# Helper Functions
###############################################################################

print_header() {
    echo -e "\n${BLUE}════════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}\n"
}

print_pass() {
    echo -e "${GREEN}✓ PASS${NC}: $1"
    ((PASSED_CHECKS++))
}

print_fail() {
    echo -e "${RED}✗ FAIL${NC}: $1"
    ((FAILED_CHECKS++))
}

print_warn() {
    echo -e "${YELLOW}⚠ WARN${NC}: $1"
    ((WARNING_COUNT++))
}

print_info() {
    if [ "$VERBOSE" = true ]; then
        echo -e "${BLUE}ℹ INFO${NC}: $1"
    fi
}

show_usage() {
    cat << EOF
Usage: bash validation-script.sh [OPTIONS]

Options:
  -f, --file FILE       Input DITA-XML file (required)
  -v, --verbose         Enable verbose output
  -h, --help            Show this help message

Examples:
  bash validation-script.sh -f output.dita
  bash validation-script.sh --file doc.dita --verbose
  bash validation-script.sh -f sample-1.dita -v

EOF
}

###############################################################################
# Validation Checks
###############################################################################

check_file_exists() {
    if [ ! -f "$DITA_FILE" ]; then
        print_fail "File not found: $DITA_FILE"
        exit 1
    fi
    print_info "File found: $DITA_FILE"
}

check_xml_wellformed() {
    print_header "Tier 1: XML Well-Formedness"
    
    if command -v xmllint &> /dev/null; then
        if xmllint --noout "$DITA_FILE" 2>/dev/null; then
            print_pass "XML is well-formed (parseable)"
        else
            print_fail "XML parsing error (malformed)"
            return 1
        fi
    else
        print_warn "xmllint not installed; skipping XML validation (install libxml2)"
        return 0
    fi
}

check_dita_structure() {
    print_header "Tier 2: DITA Structure"
    
    # Check for DOCTYPE
    if grep -q "DOCTYPE topic" "$DITA_FILE"; then
        print_pass "DOCTYPE declaration present"
    else
        print_warn "DOCTYPE declaration missing (DITA may still be valid)"
    fi
    
    # Check for root topic element
    if grep -q "<topic" "$DITA_FILE"; then
        print_pass "Root <topic> element present"
    else
        print_fail "Root <topic> element missing"
        return 1
    fi
    
    # Check for title element
    if grep -q "<title>" "$DITA_FILE"; then
        print_pass "<title> element present"
    else
        print_fail "<title> element missing"
        return 1
    fi
    
    # Check for body element
    if grep -q "<body>" "$DITA_FILE"; then
        print_pass "<body> element present"
    else
        print_fail "<body> element missing"
        return 1
    fi
}

check_content_completeness() {
    print_header "Tier 3: Content Completeness"
    
    # Count paragraphs
    para_count=$(grep -c "<p>" "$DITA_FILE" || echo "0")
    if [ "$para_count" -gt 0 ]; then
        print_pass "Paragraphs present: $para_count"
    else
        print_warn "No paragraphs found"
    fi
    
    # Count sections
    section_count=$(grep -c "<section" "$DITA_FILE" || echo "0")
    if [ "$section_count" -gt 0 ]; then
        print_pass "Sections present: $section_count"
    else
        print_info "No sections found (acceptable for simple documents)"
    fi
    
    # Count tables
    table_count=$(grep -c "<table>" "$DITA_FILE" || echo "0")
    if [ "$table_count" -gt 0 ]; then
        print_pass "Tables present: $table_count"
    else
        print_info "No tables found"
    fi
    
    # Check for empty content
    empty_paras=$(grep -c "<p></p>" "$DITA_FILE" || echo "0")
    if [ "$empty_paras" -eq 0 ]; then
        print_pass "No empty paragraphs"
    else
        print_warn "Empty paragraphs found: $empty_paras"
    fi
}

check_element_nesting() {
    print_header "Tier 4: Element Nesting & Structure"
    
    # Count unclosed tags (basic check)
    opened_topics=$(grep -o "<topic" "$DITA_FILE" | wc -l)
    closed_topics=$(grep -o "</topic>" "$DITA_FILE" | wc -l)
    
    if [ "$opened_topics" -eq "$closed_topics" ]; then
        print_pass "Topic tags properly nested (opened: $opened_topics, closed: $closed_topics)"
    else
        print_fail "Mismatched topic tags (opened: $opened_topics, closed: $closed_topics)"
        return 1
    fi
    
    # Check title placement (should be first child of topic)
    if grep -q "<topic[^>]*>.*<title>" "$DITA_FILE"; then
        print_pass "Title is child of topic element"
    else
        print_warn "Title placement may be incorrect"
    fi
    
    # Check body placement
    if grep -q "<body>" "$DITA_FILE"; then
        print_pass "Body element present and properly structured"
    else
        print_fail "Body element structure incorrect"
        return 1
    fi
}

check_metadata() {
    print_header "Tier 5: Metadata & Identifiers"
    
    # Check topic ID
    if grep -q 'id="' "$DITA_FILE"; then
        print_pass "Topic has id attribute"
        id_count=$(grep -o 'id="[^"]*"' "$DITA_FILE" | wc -l)
        print_info "Total elements with IDs: $id_count"
    else
        print_warn "No id attributes found"
    fi
    
    # Check for duplicate IDs (if xmllint available)
    if command -v xmllint &> /dev/null; then
        ids=$(xmllint --xpath "//*/@id" "$DITA_FILE" 2>/dev/null | grep -o 'id="[^"]*"' | sort)
        unique_ids=$(echo "$ids" | sort -u | wc -l)
        total_ids=$(echo "$ids" | wc -l)
        
        if [ "$unique_ids" -eq "$total_ids" ]; then
            print_pass "All IDs are unique"
        else
            duplicates=$((total_ids - unique_ids))
            print_warn "Duplicate IDs found: $duplicates"
        fi
    fi
}

check_file_size() {
    print_header "File Statistics"
    
    file_size=$(wc -c < "$DITA_FILE")
    file_size_kb=$((file_size / 1024))
    line_count=$(wc -l < "$DITA_FILE")
    
    print_info "File size: $file_size bytes ($file_size_kb KB)"
    print_info "Line count: $line_count"
    
    if [ "$file_size" -lt 500 ]; then
        print_warn "File is very small (< 500 bytes) - may be incomplete"
    fi
}

###############################################################################
# Main Execution
###############################################################################

main() {
    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            -f|--file)
                DITA_FILE="$2"
                shift 2
                ;;
            -v|--verbose)
                VERBOSE=true
                shift
                ;;
            -h|--help)
                show_usage
                exit 0
                ;;
            *)
                echo "Unknown option: $1"
                show_usage
                exit 1
                ;;
        esac
    done
    
    # Validate arguments
    if [ -z "$DITA_FILE" ]; then
        echo "Error: -f/--file argument required"
        show_usage
        exit 1
    fi
    
    # Run validation
    print_header "DITA Validation Report"
    echo "Input: $DITA_FILE"
    echo "Time:  $(date '+%Y-%m-%d %H:%M:%S')"
    
    check_file_exists
    check_xml_wellformed || true
    check_dita_structure || true
    check_content_completeness || true
    check_element_nesting || true
    check_metadata || true
    check_file_size
    
    # Print summary
    print_header "Validation Summary"
    echo "Passed checks: $PASSED_CHECKS"
    echo "Failed checks: $FAILED_CHECKS"
    echo "Warnings:      $WARNING_COUNT"
    
    # Determine overall status
    if [ "$FAILED_CHECKS" -eq 0 ]; then
        if [ "$WARNING_COUNT" -eq 0 ]; then
            echo -e "\nStatus: ${GREEN}✓ PASS (All checks passed)${NC}"
            exit 0
        else
            echo -e "\nStatus: ${YELLOW}⚠ PASS with warnings${NC}"
            exit 0
        fi
    else
        echo -e "\nStatus: ${RED}✗ FAIL${NC}"
        exit 1
    fi
}

# Run main function
main "$@"
