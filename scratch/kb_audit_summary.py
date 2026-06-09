import json

with open("scratch/kb_audit_results.json", "r", encoding="utf-8") as f:
    results = json.load(f)

# Sort results by filename for readability
results.sort(key=lambda x: x["filepath"])

total_files = len(results)
template_compliant_count = 0
placeholder_compliant_count = 0
blueprint_aligned_count = 0
leakage_risk_count = 0
contamination_risk_count = 0

audit_table = []
high_risk_files = []

for r in results:
    filepath = r["filepath"].replace("\\", "/")
    filename = filepath.split("/")[-1]
    
    # Assess classifications
    is_template = r["is_template_compliant"]
    is_placeholder = r["is_placeholder_compliant"]
    is_blueprint = r["is_blueprint_aligned"]
    
    has_leakage = len(r["leakage_indicators"]) > 0 or r["has_implementation"]
    has_contamination = len(r["obsolete_headings"]) > 0
    
    if is_template:
        template_compliant_count += 1
    if is_placeholder:
        placeholder_compliant_count += 1
    if is_blueprint:
        blueprint_aligned_count += 1
    if has_leakage:
        leakage_risk_count += 1
    if has_contamination:
        contamination_risk_count += 1
        
    # Determine risk level
    risk_level = "LOW"
    if has_leakage and has_contamination:
        risk_level = "HIGH"
        high_risk_files.append((filename, filepath, "Leakage & Contamination", r["leakage_indicators"], r["obsolete_headings"]))
    elif has_leakage:
        risk_level = "MEDIUM"
        if len(r["leakage_indicators"]) >= 2:
            risk_level = "HIGH"
            high_risk_files.append((filename, filepath, "Multiple Leakage Indicators", r["leakage_indicators"], r["obsolete_headings"]))
    elif has_contamination:
        risk_level = "MEDIUM"
        
    # Format placeholders string
    ph = r["placeholders"]
    ph_str = f"Double: {ph['double_braces_count']} | Brackets: {ph['brackets_count']} | Single: {ph['single_braces_count']}"
    
    # Format leakage string
    leak_str = ", ".join(r["leakage_indicators"]) if r["leakage_indicators"] else ("Code Blocks" if r["has_implementation"] else "None")
    
    # Format obsolete headings
    obs_str = ", ".join([h.replace("#", "").strip() for h in r["obsolete_headings"]]) if r["obsolete_headings"] else "None"
    
    audit_table.append(
        f"| [{filename}](file:///{filepath}) | {'PASS' if is_template else 'FAIL'} | {'PASS' if is_placeholder else 'FAIL'} | {risk_level} | {leak_str} | {obs_str} |"
    )

with open("scratch/kb_audit_report.md", "w", encoding="utf-8") as out:
    out.write("# Knowledge Base Programmatic Audit Report\n\n")
    out.write("### Summary Statistics\n")
    out.write(f"- Total Files Audited: {total_files}\n")
    out.write(f"- Template-Compliant Files (No direct code/execution): {template_compliant_count} / {total_files} ({template_compliant_count/total_files*100:.1f}%)\n")
    out.write(f"- Placeholder-Compliant Files (Double curly braces, no raw brackets): {placeholder_compliant_count} / {total_files} ({placeholder_compliant_count/total_files*100:.1f}%)\n")
    out.write(f"- Blueprint Aligned Files (No obsolete/custom headers): {blueprint_aligned_count} / {total_files} ({blueprint_aligned_count/total_files*100:.1f}%)\n")
    out.write(f"- Downstream Leakage Risk Files (Contains finished output/code): {leakage_risk_count} / {total_files} ({leakage_risk_count/total_files*100:.1f}%)\n")
    out.write(f"- Context Contamination Risk Files (Obsolete headers present): {contamination_risk_count} / {total_files} ({contamination_risk_count/total_files*100:.1f}%)\n\n")

    out.write("### File Audit Table\n")
    out.write("| File Name | Template-Compliant | Placeholder-Compliant | Risk Level | Leakage Risk | Contamination (Obsolete Headers) |\n")
    out.write("| --- | :---: | :---: | :---: | --- | --- |\n")
    for line in audit_table:
        out.write(line + "\n")
    out.write("\n")

    out.write("### High Risk Files Detail\n")
    for name, path, reason, leaks, headings in high_risk_files:
        out.write(f"#### [{name}](file:///{path})\n")
        out.write(f"- **Risk Reason**: {reason}\n")
        out.write(f"- **Leakage Details**: {leaks}\n")
        out.write(f"- **Contaminating Headers**: {[h.replace('#', '').strip() for h in headings]}\n\n")

print("Audit summary report written to scratch/kb_audit_report.md")
