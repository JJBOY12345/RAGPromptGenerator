import os
import re
import json

KB_DIR = "knowledge_base"

def analyze_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Extract Headings
    headings = []
    lines = content.splitlines()
    for line in lines:
        if line.startswith("#"):
            headings.append(line.strip())
            
    # 2. Check Code Blocks
    # Find all code blocks like ```lang ... ```
    code_blocks = re.findall(r"```([a-zA-Z0-9_\-\+]*)\n(.*?)```", content, re.DOTALL)
    
    # Determine if code blocks contain actual implementations or are just abstract specs
    has_implementation = False
    impl_samples = []
    for lang, block in code_blocks:
        block_clean = block.strip()
        # If it contains common language statements, schemas, or actual code lines
        # (avoiding cases where it's just a placeholder block like {{CODE}})
        if len(block_clean) > 0 and not block_clean.startswith("{{") and not block_clean.endswith("}}"):
            # If it has more than a few lines, or contains specific structural syntax
            if "\n" in block_clean or len(block_clean) > 30:
                has_implementation = True
                impl_samples.append((lang, block_clean[:100] + "..."))

    # 3. Check Placeholder Compliance
    # Look for {{PLACEHOLDER}}
    double_braces = re.findall(r"\{\{([a-zA-Z0-9_]+)\}\}", content)
    # Look for [placeholder] or <placeholder> or {placeholder}
    brackets = re.findall(r"\[([a-zA-Z0-9_ ]+)\]", content)
    angle_brackets = re.findall(r"\<([a-zA-Z0-9_ ]+)\>", content)
    single_braces = re.findall(r"(?<!\{)\{([a-zA-Z0-9_]+)\}(?!\})", content)

    # 4. Downstream Leakage Risk indicators
    leakage_indicators = []
    content_lower = content.lower()
    
    # Check for specific leak patterns
    if "create table" in content_lower or "insert into" in content_lower:
        leakage_indicators.append("SQL Schema / DDL Statements")
    if "const express" in content_lower or "app.get(" in content_lower or "app.post(" in content_lower:
        leakage_indicators.append("REST API Route Code")
    if "import " in content_lower or "def " in content_lower:
        if any(lang in ["python", "py"] for lang, _ in code_blocks):
            leakage_indicators.append("Python Code Snippets")
    if "#promptengineering" in content_lower or "here is a linkedin" in content_lower:
        leakage_indicators.append("SaaS/LinkedIn Post Drafts")
    if "week 1" in content_lower or "week 2" in content_lower:
        leakage_indicators.append("Hardcoded Weekly Schedules")
    if "question 1:" in content_lower or "option a" in content_lower:
        leakage_indicators.append("Quiz Questions/Answers")
    if "strengths:" in content_lower or "weaknesses:" in content_lower:
        leakage_indicators.append("SWOT Analysis Terms with Colons")
    if "sony a7r" in content_lower or "90mm f/" in content_lower:
        leakage_indicators.append("Camera Specific Settings (e.g. Sony A7R)")

    # 5. Determine Compliance Classifications
    # Template-Compliant: Provides instructions rather than final output
    is_template_compliant = True
    if has_implementation or any(ind in leakage_indicators for ind in ["SQL Schema / DDL Statements", "REST API Route Code", "SaaS/LinkedIn Post Drafts", "Hardcoded Weekly Schedules", "Quiz Questions/Answers"]):
        is_template_compliant = False
        
    # Placeholder-Compliant: Uses double curly braces, avoids hardcoded values
    is_placeholder_compliant = len(double_braces) > 0 and len(brackets) == 0 and len(angle_brackets) == 0
    
    # Blueprint Alignment & Context Contamination
    # We inspect standard headings vs obsolete ones.
    # Obsolete or custom headers: "## Required Context", "## Optional Configuration", "## Best Practices", "## Common Mistakes"
    obsolete_headings = []
    for h in headings:
        h_clean = h.replace("#", "").strip().lower()
        if "required context" in h_clean or "optional configuration" in h_clean or "best practices" in h_clean or "common mistakes" in h_clean:
            obsolete_headings.append(h)
            
    is_blueprint_aligned = len(obsolete_headings) == 0
    
    return {
        "filepath": filepath,
        "headings": headings,
        "obsolete_headings": obsolete_headings,
        "code_blocks": [(lang, sample) for lang, sample in impl_samples],
        "placeholders": {
            "double_braces_count": len(double_braces),
            "brackets_count": len(brackets),
            "angle_brackets_count": len(angle_brackets),
            "single_braces_count": len(single_braces)
        },
        "leakage_indicators": leakage_indicators,
        "is_template_compliant": is_template_compliant,
        "is_placeholder_compliant": is_placeholder_compliant,
        "is_blueprint_aligned": is_blueprint_aligned,
        "has_implementation": has_implementation
    }

def main():
    results = []
    for root, dirs, files in os.walk(KB_DIR):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                res = analyze_file(filepath)
                results.append(res)
                
    # Save the audit data
    with open("scratch/kb_audit_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    print(f"Audited {len(results)} files. Saved results to scratch/kb_audit_results.json")

if __name__ == "__main__":
    main()
