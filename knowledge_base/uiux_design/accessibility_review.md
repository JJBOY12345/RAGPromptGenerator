---
title: Accessibility Review Checklist
category: uiux_design
subcategory: accessibility
tags: [accessibility, wcag, a11y]
difficulty: beginner
depth: lightweight
retrieval_keywords: [accessibility audit, wcag checklist, contrast checker]
use_case: Retrieve for WCAG compliance checks.
placeholder_count: 2
version: "1.0"
---
# Accessibility Review Checklist
## Purpose
Provides a rapid WCAG 2.2 accessibility checklist to verify contrast, tap targets, and screen reader labels.
## Required Context
- Component Name: {{COMPONENT_NAME}}
- Target WCAG Level: {{TARGET_LEVEL}}
## Template
Act as an expert Accessibility Auditor. Review {{COMPONENT_NAME}} against {{TARGET_LEVEL}} standards. Verify: 1. Perceivable (contrast 4.5:1), 2. Operable (keyboard paths, 48x48px hit areas), 3. Robust (ARIA mapping).
## Best Practices
1. Ensure all elements can be focused using only TAB and ENTER keys.
2. Require empty alt tags for decorative elements.
