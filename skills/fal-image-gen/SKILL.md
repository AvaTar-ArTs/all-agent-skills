---
name: fal-image-gen
description: "Generate images via FAL.ai using FLUX, Krea, Ideogram, Recraft and other models. Use when asked to create, generate, or make images, art, or visuals — especially for AvatarArts/TrashCats brand work."
---

# FAL Image Generation Skill

Generates images through the FAL.ai API using your configured `FAL_KEY`.

## Quick Model Reference

| Model ID | Speed | Price | Best For |
|---|---|---|---|
| `fal-ai/flux-2/klein/9b` | <1s | $0.006/MP | Fastest drafts, crisp text |
| `fal-ai/flux-2-pro` | ~6s | $0.03/MP | Studio photorealism |
| `fal-ai/z-image/turbo` | ~2s | $0.005/MP | Fast general purpose |
| `fal-ai/ideogram/v3` | ~5s | $0.03–0.09 | Typography, text-in-image |
| `fal-ai/recraft/v4/pro/text-to-image` | ~8s | $0.25 | Brand systems, design |
| `fal-ai/krea/v2/medium/text-to-image` | ~20s | $0.030 | Illustration, anime, art styles |
| `fal-ai/krea/v2/large/text-to-image` | ~45s | $0.060 | Photorealism, film grain |
| `fal-ai/nano-banana-pro` | ~8s | $0.15 | Gemini 3 Pro, complex reasoning |
| `fal-ai/qwen-image` | ~12s | $0.02/MP | Complex text rendering |
| `fal-ai/gpt-image-2` | ~20s | $0.04–0.06 | SOTA text + photorealism |

## Default Model
`fal-ai/krea/v2/large/text-to-image` — set in `~/.hermes/config.yaml`

## AvatarArts / TrashCats Style Prompts

For Steven's brand universe, use these style anchors:

**TrashCats / ichoTAKU aesthetic:**
```
punk raccoon character, hot pink and black color palette, graffiti typography,
anarchist iconography, neon signs, urban dystopia, manga-influenced line art,
Japanese katakana text, heartbreak motifs, gritty street art style
```

**AvatarArts gallery style:**
```
AI digital art, bioluminescent, glitch effects, cyberpunk palette,
multisensory visual narrative, high contrast, editorial quality
```

**QuantumForgeLabs / technical:**
```
quantum computing visualization, neural network topology art, 
circuit board aesthetics, holographic interface, dark tech aesthetic
```

## Usage in Hermes

Switch model per-session:
```
hermes config set image_gen.model fal-ai/flux-2-pro
```

Or ask directly in chat:
```
generate an image of [prompt] using flux-2-pro
```

## Switching via config.yaml

Edit `~/.hermes/config.yaml`:
```yaml
image_gen:
  provider: fal
  model: fal-ai/krea/v2/large/text-to-image  # change this line
```
