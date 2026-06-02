---
title: Commercial Product Photography Prompt Generator
category: image_generation
subcategory: product_photography
tags:
  - product-photography
  - midjourney-prompt
  - commercial-advertising
  - e-commerce
  - lighting-rig
difficulty: advanced
depth: deep
retrieval_keywords:
  - product photography prompt
  - commercial product photography
  - e-commerce hero shot
  - midjourney lighting studio
  - macro lens camera setup
  - advertising product visual
use_case: >
  Retrieve when the user wants to generate high-end, commercial-grade product
  advertising visuals, e-commerce catalog shots, or flat lay layouts.
placeholder_count: 6
version: "1.0"
---

# Commercial Product Photography Prompt Generator

## Purpose
This template generates professional, studio-grade commercial product photography prompts for Midjourney, DALL-E, and Stable Diffusion. It specifies camera lens parameters, precise lighting rigs, styled props, background environments, and negative constraints to yield commercial-ready advertisements.

## When to Retrieve This Template
- "Generate a Midjourney prompt for a luxury perfume bottle advertisement."
- "Create a commercial photography prompt for an e-commerce skincare product."
- "Write an image prompt for a flat lay layout of tech gadgets."
- "How do I prompt a clean, white-background product catalog shot?"
- "Design a creative ad mockup prompt featuring a sports beverage bottle."

## Prompt Framework
```markdown
You are a Principal Commercial Product Photographer, Advertising Art Director, and Studio Lighting Designer.

Your task is to compile a highly technical, high-impact prompt for commercial product rendering.

### 1. PRODUCT BRAND & IDENTITY
- **Product Name:** {{PRODUCT_NAME}}
- **Product Category:** {{PRODUCT_CATEGORY}} (e.g., luxury cosmetics, smart electronics, organic beverage)
- **Brand Mood:** {{BRAND_MOOD}} (e.g., minimalist elegance, technical futuristic, playful organic)

### 2. SCENE STYLING & SET DESIGN
- **Shot Type:** [Choose: Hero Studio Shot | Lifestyle Setup | Flat Lay Layout | Macro Close-up | Dynamic Action Shot]
- **Background & Set:** {{BACKGROUND_STYLE}} (e.g., matte white cyclorama, raw concrete podium, splashing water surface)
- **Props & Styling Elements:** {{PROP_DESCRIPTION}} (e.g., raw botanicals, matching packaging box, none)

### 3. STUDIO LIGHTING RIG & COLOR ENGINE
- **Lighting Rig:** [Choose: Softbox Diffused Light | Dual-Rim Backlighting | Natural Golden Hour Window Light | High-Contrast Spotlights]
- **Color Grading:** {{COLOR_GRADE}} (e.g., clean neutral whites, warm editorial gold, cool high-tech blues)
- **Reflections & Textures:** Matte surfaces, pristine glass refractions, high-definition metallic finishes.

### 4. TECHNICAL CAMERA SPECS
- **Camera Setup:** Captured on Sony A7R V, 90mm f/2.8 Macro lens, focus stacked for edge-to-edge sharpness.
- **Composition Constraints:** Rule of thirds, ample negative space for text overlays, balanced center alignment.
- **Negative Styles:** Strictly exclude: dust, fingerprints, scratches, busy background clutter, unrealistic CGI sheen, watermark.
```

## Required Context
- Product Name: `{{PRODUCT_NAME}}`
- Product Category: `{{PRODUCT_CATEGORY}}`
- Brand Mood: `{{BRAND_MOOD}}`
- Background Style: `{{BACKGROUND_STYLE}}`
- Prop Description: `{{PROP_DESCRIPTION}}`
- Color Grade: `{{COLOR_GRADE}}`

---

## Optional Configuration
- Output Ratio: `[Choose: --ar 1:1 | --ar 16:9 | --ar 4:3]`
- Render Version: `[Optional: --v 6.0 --style raw]`
- Studio Style: `[Choose: Minimalist | Natural Ambient | Dramatic Studio]`

---

## Full Example Prompt
```markdown
You are a Principal Commercial Product Photographer, Advertising Art Director, and Studio Lighting Designer.

Your task is to compile a highly technical, high-impact prompt for commercial product rendering.

### 1. PRODUCT BRAND & IDENTITY
- **Product Name:** Aura Essence Oil
- **Product Category:** Organic Skincare Serum
- **Brand Mood:** Minimalist elegance and natural purity.

### 2. SCENE STYLING & SET DESIGN
- **Shot Type:** Hero Studio Shot
- **Background & Set:** Smooth, dry sandstone block platform surrounded by soft rippling water.
- **Props & Styling Elements:** Scattered eucalyptus leaves.

### 3. STUDIO LIGHTING RIG & COLOR ENGINE
- **Lighting Rig:** Natural Golden Hour Window Light
- **Color Grading:** Warm editorial gold
- **Reflections & Textures:** Clean glass container.

### 4. TECHNICAL CAMERA SPECS
- **Camera Setup:** Sony A7R V, 90mm Macro lens.
- **Composition Constraints:** Center alignment, negative space on top.
```

## Best Practices
1. **Focus Stack Terminology:** Explicitly write "focus stacked for edge-to-edge sharpness" to ensure the entire product remains in focus, avoiding excessive blur.
2. **Specify Background Platforms:** Use structured staging surfaces (e.g., "cyclorama wall", "travertine podium", "acrylic block") to keep products physically grounded.
3. **Pristine Product Details:** Enforce clean textures via constraints: "no fingerprints", "no dust specs", "pristine reflection mapping".
4. **Define Space for Copy:** Direct the composition to include "negative space for advertising copy" to ensure the image is immediately useful for marketing.
5. **Calibrate Reflections:** Mention surface interactions, e.g., "crisp refraction in glass bottle", "soft diffused satin metal reflection".

## Common Mistakes to Avoid
- **Vague Backgrounds:** Asking for "a beautiful background" instead of defining explicit set elements (like "minimal beige concrete wall").
- **Blurry Product Borders:** Allowing shallow depth-of-field to blur the product name or packaging edges. Always request high-sharpness macro settings.
- **Fingerprints and Dust:** Failing to exclude surface imperfections, which ruins the clean e-commerce feel.
- **Distracting Props:** Adding too many complex props that pull focus away from the primary brand package.
