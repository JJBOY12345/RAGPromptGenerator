---
title: Application Security & Threat Auditor
category: software_development
subcategory: security_audit
tags: [security-audit, owasp, cyber-security]
difficulty: advanced
depth: medium
retrieval_keywords: [security audit, owasp top 10, penetration threat]
use_case: Retrieve to audit application code or architectures against security concerns.
placeholder_count: 2
version: "1.0"
---
# Application Security & Threat Auditor
## Purpose
Drives security audits of application architectures or source codes mapped against OWASP vulnerabilities.
## When to Retrieve This Template
- "Do a security audit on this SQL query structure."
- "Perform threat modeling on our OAuth2 login architecture."
- "Scan this API gateway setup for OWASP vulnerabilities."
## Prompt Framework
You are an expert Cybersecurity Auditor. Scan the provided architecture or code for {{SECURITY_CONCERNS}} in this {{APPLICATION_TYPE}} system. Focus on OWASP Top 10 vulnerabilities.
## Required Context
- Application Type: {{APPLICATION_TYPE}}
- Security Concerns: {{SECURITY_CONCERNS}}
## Optional Configuration
- Compliance Target: [OWASP | PCI-DSS | GDPR | SOC2]
## Example Prompt
Audit a Node.js REST API managing user metadata against SQL Injection and access control.
## Best Practices
1. Scrub raw production credentials or keys before starting audits.
2. Prioritize vulnerabilities using standard risk levels (Critical, High, Medium, Low).
3. Supply secure, corrected copy-pasteable configuration or code solutions.
