---
title: Professional Studio Portrait Prompt Generator
category: image_generation
subcategory: professional_portrait
tags:
  - portrait-photography
  - midjourney-prompt
  - commercial-headshot
  - lighting-setup
  - high-end-retouching
difficulty: intermediate
depth: deep
retrieval_keywords:
  - professional portrait prompt
  - studio photography prompt
  - corporate headshot generator
  - midjourney camera lens settings
  - commercial print retouches
  - lighting techniques headshot
use_case: >
  Retrieve when the user wants to generate high-end, studio-grade photographic
  portrait prompts for LinkedIn, portfolios, or commercial print.
placeholder_count: 5
version: "1.0"
---

# Professional Studio Portrait Prompt Generator

## Purpose
This template generates highly technical, photo-realistic image prompts for Midjourney, DALL-E, and Stable Diffusion. It incorporates advanced photographic parameters, real-world camera systems, precise lighting terminologies, and retoucher rules to produce magazine-quality corporate and fashion portraits.

## When to Retrieve This Template
- "Generate a Midjourney prompt for a corporate leadership headshot."
- "Create a photographic prompt for a high-end fashion magazine profile."
- "Write an image prompt that uses studio key lighting for a professional portrait."
- "How do I prompt for a clean studio headshot with natural skin textures?"
- "Design a photo-realistic portrait prompt featuring a confident executive."

## Prompt Framework
```markdown
You are a Professional Fashion & Corporate Portrait Photographer, Camera Director, and High-End Retouching Expert.

Using the provided parameters, compile a highly detailed, professional photographic prompt to generate a studio-quality portrait.

### 1. IDENTITY & SUBJECT
- **Subject Base:** {{PERSON_DESCRIPTION}} (e.g., confident professional woman, friendly appearance)
- **Identity Reference:** {{REFERENCE_IMAGE_DESCRIPTION}}

### 2. CLOTHING & STYLING
- **Outfit:** {{OUTFIT_DESCRIPTION}} (e.g., tailored dark charcoal blazer with cream silk blouse)
- **Styling Rules:** Modern, premium fabrics, minimal accessories, crisp ironed collars.

### 3. CAMERA SETUP & COMPOSITION
- **Composition Type:** [Choose: Close-up Headshot | Chest-up | Waist-up | Full body]
- **Camera System:** Shot on Hasselblad H6D-100c, 85mm f/1.4 lens, shutter speed 1/250s, ISO 64.
- **Pose & Expression:** Calm corporate gaze, slight smile, direct eye contact, relaxed shoulders.

### 4. LIGHTING & COLOR ENGINE
- **Lighting Setup:** [Choose: Rembrandt Lighting | Butterfly Key Lighting | Softbox Rim Light]
- **Color Palette & Mood:** {{COLOR_PALETTE_MOOD}} (e.g., cool corporate slate, warm cream, neutral sand)
- **Background backdrop:** Solid seamless studio backdrop, color: {{BACKGROUND_COLOR}}

### 5. TECHNICAL CONSTRAINTS & RETOUCHING
- **Retouching Rules:** Natural skin textures, visible pores, sharp eyelashes, remove transient blemishes only. No plastic skin, no CGI sheen, no over-sharpening artifacts.
- **Negative Styles:** Strictly exclude: cartoon, illustration, drawing, 3D render, dramatic movie color grading, extreme flares.
```

## Required Context
- Person Description: `{{PERSON_DESCRIPTION}}`
- Reference Image Description: `{{REFERENCE_IMAGE_DESCRIPTION}}`
- Outfit Description: `{{OUTFIT_DESCRIPTION}}`
- Color Palette Mood: `{{COLOR_PALETTE_MOOD}}`
- Background Color: `{{BACKGROUND_COLOR}}`

---

## Optional Configuration
- Aspect Ratio: `[Choose: --ar 1:1 | --ar 4:5 | --ar 16:9]`
- Render Engine Tag: `[Optional: --v 6.0 | --style raw]`
- Lens Type: `[Choose: 85mm Portrait Lens | 50mm Standard Lens]`

---

## Full Example Prompt
```markdown
You are a Professional Fashion & Corporate Portrait Photographer, Camera Director, and High-End Retouching Expert.

Using the provided parameters, compile a highly detailed, professional photographic prompt to generate a studio-quality portrait.

### 1. IDENTITY & SUBJECT
- **Subject Base:** Confident female tech executive with a friendly expression.
- **Identity Reference:** Medium close-up of a person with symmetrical facial structure.

### 2. CLOTHING & STYLING
- **Outfit:** Tailored dark navy blue blazer with a high-neck white silk shirt.
- **Styling Rules:** Modern, clean seams.

### 3. CAMERA SETUP & COMPOSITION
- **Composition Type:** Chest-up Portrait
- **Camera System:** Hasselblad H6D-100c, 85mm lens.
- **Pose & Expression:** Warm approachable smile.

### 4. LIGHTING & COLOR ENGINE
- **Lighting Setup:** Softbox Key Lighting
- **Color Palette & Mood:** Corporate Slate and Deep Navy
- **Background backdrop:** Solid grey studio backdrop
```

## Best Practices
1. **Photographic Verbs & Lenses:** Always reference specific high-end camera bodies (e.g., Hasselblad, Phase One) and focal lenses (e.g., 85mm, 105mm) to trigger photorealism.
2. **Detailed Lighting Terms:** Use real-world lighting modifiers (e.g., `octabox`, `softbox`, `silver reflector`, `split lighting`) rather than generic words like "bright light".
3. **Preserve Natural Skin:** Enforce negative constraints against "airbrushed", "plastic skin", or "beauty filters" to keep skin textures authentic.
4. **Solid Color Backdrops:** Force clean, simple backgrounds (e.g., "solid seamless studio backdrop") to ensure the subject stands out without environmental noise.
5. **Calibrate Aspect Ratios:** For corporate profiles, specify standard vertical dimensions like `--ar 4:5` (Midjourney) to match native cropping interfaces.

## Common Mistakes to Avoid
- **Generic Styling:** Writing "nice clothes" instead of specific, high-quality textiles like "tailored wool", "fine silk", or "matte cotton".
- **Cinematic Over-saturation:** Allowing heavy movie color grading, which introduces saturated oranges and teals, ruining the neutral corporate portrait look.
- **Mismatched Eye Gaze:** Forgetting to prompt "direct eye contact", which can cause generative models to render subjects looking off-camera.
- **Too Many Details:** Cluttering the background with objects, making it harder to extract a clean, isolated headshot.
