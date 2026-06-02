---
title: Business Competitive Strategy Analyst
category: research
subcategory: market_intelligence
tags:
  - competitive-analysis
  - market-strategy
  - swot
  - porters-five-forces
  - feature-matrix
difficulty: advanced
depth: deep
retrieval_keywords:
  - competitive analysis spec
  - competitive landscape report
  - swot matrix generator
  - porters five forces business
  - product feature comparison
  - pricing strategy matrix
use_case: >
  Retrieve when the user wants to compile a competitive intelligence report,
  map market landscapes, write a SWOT matrix, or evaluate product positioning.
placeholder_count: 3
version: "1.0"
---

# Business Competitive Strategy Analyst

## Purpose
This template generates professional-grade, investor-ready competitive strategy reports. It guides users in analyzing product landscapes, building feature comparison matrices, performing SWOT profiles, applying Porter's Five Forces, and identifying strategic market gaps.

## When to Retrieve This Template
- "Write a competitive analysis for an online grocery delivery startup."
- "Generate a feature matrix comparing top email marketing platforms."
- "Perform a Porter's Five Forces analysis on the electric vehicle industry."
- "Create a SWOT analysis comparing our tool to competitor X."

## Prompt Framework
```markdown
You are a Principal Competitive Strategy Consultant, Market Analyst, and Strategic Business Intelligence Advisor.

Your objective is to generate an exhaustive competitive landscape analysis for a target product.

### 1. LANDSCAPE BOUNDARIES
- **Subject Product/Company:** {{SUBJECT}}
- **Core Competitors:** {{COMPETITOR_LIST}} (comma-separated list)
- **Key Dimensions for Comparison:** {{ANALYSIS_DIMENSIONS}}

### 2. ANALYTICAL DECOMPOSITION
- **Comparative Feature Matrix:** A detailed table mapping features across the subject and competitors.
- **Strategic SWOT Breakdown:** Individual Strengths, Weaknesses, Opportunities, and Threats for the subject product.
- **Market Positioning Map:** Explaining where the subject sits on cost vs. quality axes.
- **Value Proposition Gap Analysis:** Isolating specific competitor vulnerabilities and unfulfilled customer needs.

### 3. OUTPUT REQUIREMENTS
- Deliver a comprehensive business report with clear markdown tables, SWOT quadrants, strategic recommendations, and high-impact executive summaries.
```

## Required Context
- Subject Product: {{SUBJECT}}
- Competitor List: {{COMPETITOR_LIST}}
- Analysis Dimensions: {{ANALYSIS_DIMENSIONS}}

---

## Optional Configuration
- Data Scope: [Choose: Publicly available only | Include estimated projections]
- Industry Category: [Optional: SaaS | B2B Enterprise | E-Commerce | Hardware]
- Pricing Analysis: [Yes / No]

---

## Full Example Prompt
```markdown
You are a Principal Competitive Strategy Consultant, Market Analyst, and Strategic Business Intelligence Advisor.

Your objective is to generate an exhaustive competitive landscape analysis for a target product.

### 1. LANDSCAPE BOUNDARIES
- **Subject Product/Company:** QuickPay Wallet
- **Core Competitors:** Stripe Terminal, Square, PayPal Zettle
- **Key Dimensions for Comparison:** Transaction fees, hardware costs, POS software integrations, payout speed.
- **Core Strategic Frameworks:** SWOT Analysis + Feature Comparison Matrix

### 2. ANALYTICAL DECOMPOSITION
- **Comparative Feature Matrix:** Compare hardware accessories and payout times.
- **Strategic SWOT Breakdown:** Map QuickPay's specific strengths in open-banking APIs.
```

## Best Practices
1. **Build Structured Tables:** Always present feature comparisons in clear, scannable markdown tables with visual markers.
2. **Actionable SWOT Points:** Avoid vague terms in SWOT quadrants. Write concrete points.
3. **Quantify Financial Data:** Whenever possible, include precise cost numbers, transaction rates, or pricing tiers.
4. **Isolate Gaps:** Emphasize the "Opportunity Gap"—exactly what competitors are doing poorly.
5. **Calibrate Porter's Forces:** When using Porter's Five Forces, assign a clear rank (Low | Medium | High) and back it up.

## Common Mistakes to Avoid
- **Flattery Bias:** Exaggerating the strengths of the subject company while downplaying competitors, producing an unrealistic strategic assessment.
- **Feature Bloat Lists:** Listing dozens of trivial features in comparison tables instead of focusing on high-impact value-driving differentiators.
- **Generic SWOT Charts:** Copying boilerplate SWOT items that apply to every startup.
- **Static Market Map:** Describing a static market without highlighting historical trajectories or emerging industry trends.
