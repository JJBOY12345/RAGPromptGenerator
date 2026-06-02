---
title: Product Design System & Token Architect
category: uiux_design
subcategory: design_systems
tags:
  - design-system
  - ui-ux
  - design-tokens
  - atomic-design
  - figma
difficulty: advanced
depth: deep
retrieval_keywords:
  - product design system
  - ui design tokens
  - atomic component library
  - figma style guide
  - responsive layout grids
  - typography scale system
use_case: >
  Retrieve when the user wants to compile a comprehensive visual design system,
  define styling tokens, write Figma specifications, or configure UI guidelines.
placeholder_count: 4
version: "1.0"
---

# Product Design System & Token Architect

## Purpose
This template acts as a structured engine to construct comprehensive product design system documentation. It documents semantic design tokens, color harmonies, responsive layout systems, atomic components, dark mode variants, and strict WCAG accessibility guidelines.

## When to Retrieve This Template
- "Design the typography and color token system for a banking app."
- "Create the atomic component library design for a SaaS grid interface."
- "Write a unified product UI design system specification for developers."
- "How should we name and organize our Figma tokens for light/dark modes?"
- "Generate accessibility spacing and alignment tokens matching WCAG 2.1 AA."

## Prompt Framework
```markdown
You are a Principal Product Designer & Design Systems Architect specializing in bridging visual aesthetics with frontend development engineering.

### 1. PRODUCT BRAND & IDENTITY
- **App Name:** {{PRODUCT_NAME}}
- **Product Type:** {{PRODUCT_TYPE}} (e.g., enterprise dashboard, e-commerce, mobile game)
- **Brand Tone:** {{BRAND_TONE}} (e.g., clean professional, vibrant, warm minimal)
- **Target Audience:** {{TARGET_AUDIENCE}}

### 2. CORE VISUAL ENGINE & TOKENS
- **Color Systems:** Primary, secondary, neutral, and semantic (success, error, warning, info) palettes in HSL/HEX.
- **Typography Scale:** Font families, line heights, font weights, and responsive modular type scales.
- **Spacing & Elevation:** 4px/8px grid system tokens, elevation shadow presets, and layout grids.
- **Accessibility:** Mandatory compliance with WCAG 2.1 AA guidelines (contrast ratios, minimum hit areas of 48x48px).

### 3. COMPONENT LIBRARY (ATOMIC METHODOLOGY)
1. **Atoms:** Primitives like buttons, text fields, badges, and icon wrappers (variants, states).
2. **Molecules:** Combined items like card items, search fields, input combinations.
3. **Organisms:** Structural panels like global navigators, dynamic table grids, headers.

### 4. DELIVERABLES EXPECTED
- Comprehensive Design Token Spec (CSS variables or JSON structure).
- Complete responsive grid definitions (mobile, tablet, desktop breakpoints).
- Component Anatomy charts and states (default, hover, focus, disabled, active).
```

## Required Context
- Product Name: `{{PRODUCT_NAME}}`
- Product Type: `{{PRODUCT_TYPE}}`
- Brand Tone: `{{BRAND_TONE}}`
- Target Audience: `{{TARGET_AUDIENCE}}`

---

## Optional Configuration
- Grid System: `[Choose: 8px grid | 10px grid]`
- Dark Mode Support: `[Yes / No]`
- Platform Targets: `[Choose: Web-only | Native iOS & Android | Cross-Platform]`

---

## Full Example Prompt
```markdown
You are a Principal Product Designer & Design Systems Architect specializing in bridging visual aesthetics with frontend development engineering.

### 1. PRODUCT BRAND & IDENTITY
- **App Name:** TeleHealth Connect
- **Product Type:** Patient-facing tele-medicine portal
- **Brand Tone:** Trustworthy, warm, highly accessible, calm teal
- **Target Audience:** General public, including elderly patients with visual impairments.

### 2. CORE VISUAL ENGINE & TOKENS
- **Color Systems:** High-contrast calm teals, soft warm neutrals, and crisp status colors.
- **Typography Scale:** Modern sans-serif, robust type scale for easy readability.
- **Spacing & Elevation:** Strict 8px grid token systems for layouts.
- **Accessibility:** Enforce WCAG 2.1 AAA target standard for typography contrast.

### 3. COMPONENT LIBRARY (ATOMIC METHODOLOGY)
1. **Atoms:** Inputs, buttons, labels.
2. **Molecules:** Telehealth call appointment cards.
3. **Organisms:** Calendar reservation grid pane.
```

## Best Practices
1. **Name Tokens Semantically:** Avoid color-based token names like `--blue-500`. Use semantic names like `--brand-primary` or `--action-hover`.
2. **Strict Spacing Multiples:** Maintain an 8px spacing system for consistent layouts (e.g., margins/padding as 8px, 16px, 24px, 32px, 48px).
3. **Design for Interactivity:** Define distinct token styles for hover, focus, active, and disabled interactive states.
4. **Responsive Flex Layouts:** Map layout structures to fluid grids with standard breakpoints (Mobile: 375px, Tablet: 768px, Desktop: 1440px).
5. **Legibility Contrast Rules:** Ensure all body copy achieves at least a 4.5:1 contrast ratio against the background (7:1 for AAA targets).

## Common Mistakes to Avoid
- **Hardcoded Styles:** Failing to map component properties to root design tokens, making dark mode transitions painful.
- **Small Tap Targets:** Designing interactive links or buttons under 44x44px (iOS) or 48x48px (Android), reducing mobile accessibility.
- **Font Scale Overload:** Defining more than 5 distinct font weights or line-height variants, creating an incoherent typographic rhythm.
- **Unstructured Icons:** Placing icons with mismatched boundary boxes in component assemblies, leading to alignment bugs.
