---
name: mythic-atlas
description: >
  Generate a complete Mythic Atlas delivery bundle — personalized symbolic poster brief,
  clean poster copy, philosophical manuscript, animation prompt, metadata, and ZIP — from
  a customer YAML or JSON intake profile. Use this skill whenever the user mentions a
  "soul blueprint," "mythic atlas," "personalized mythology poster," wants to run the
  Mythic Atlas Engine, needs to fill out a customer intake profile, wants to generate
  esoteric/symbolic creative artifacts from birth data and values, or is preparing a
  delivery bundle for a customer. Invoke even if the user just drops a YAML file with
  fields like full_name, birth_date, values, life_themes, or style.
---

# Mythic Atlas Engine Skill

The Mythic Atlas Engine turns a customer intake (YAML or JSON) into a personalized
symbolic artifact package. One command produces 7 files + a delivery ZIP ready to hand off.

**Engine location:** `skills/mythic-atlas/scripts/mythic_atlas_engine.py`  
**Intake template:** `skills/mythic-atlas/references/intake_template.yaml`  
**Style guide:** `skills/mythic-atlas/references/style_presets.md`

---

## Workflow

### 1. Get or build the intake profile

If the user already has a YAML or JSON file, use it directly.

If they don't, help them fill one out. Required fields only:

```yaml
full_name: ""       # legal or full name for numerology calculations
display_name: ""    # name shown large on the poster
birth_date: ""      # YYYY-MM-DD  (also accepts MM/DD/YYYY or "Month DD, YYYY")
```

All other fields are optional but make the output richer. Read
`references/intake_template.yaml` to show the user a complete example with annotations.
Walk them through it conversationally — don't dump the full schema at once.

**Critical fields to ask about if missing:**
- `style` — which visual surface? (Read `references/style_presets.md` and present options)
- `values` and `life_themes` — these drive the archetype and manuscript; defaults exist but personal ones are far better
- `verified_astrology` — only supply placements you can confirm; leave blank rather than invent
- `portrait_mode` — default is `symbolic_no_person`; change only if customer explicitly requests otherwise

### 2. Run the engine

```bash
pip install PyYAML -q
python <skill_dir>/scripts/mythic_atlas_engine.py \
  --input <path/to/profile.yaml> \
  --out <path/to/output_dir>
```

The engine prints the path to `delivery_bundle.zip` when done.

**Output structure:**
```
output/
  01_master_brief.md        — full profile + calculated numerology (JSON)
  02_poster_prompt.txt      — image generation prompt (style + symbolism + constraints)
  03_negative_prompt.txt    — what to exclude from the image
  04_manuscript.md          — long-form philosophical portrait (~700 words)
  05_animation_prompt.txt   — 10-second loop animation brief
  06_metadata.json          — complete record with disclaimer and UTC timestamp
  07_clean_poster_copy.txt  — text-safe poster copy for typography reconstruction
  delivery_bundle.zip       — all 7 files zipped for delivery
```

### 3. Review the outputs before delivery

The engine calculates numerology deterministically, but human review is required before
delivery. Check:

- **Spelling** of all names, dates, places — image models will embed these literally
- **Astrology accuracy** — only `verified_astrology` fields you supplied appear; if blank,
  the prompt says "broad solar-sign symbolism only, do not invent placements"
- **`07_clean_poster_copy.txt`** — this is the typographic source of truth; the poster
  prompt may render text imperfectly, so always deliver clean copy alongside the image

### 4. Deliver

Send the customer `delivery_bundle.zip`. For higher tiers (Chronicle / Legacy / Studio),
additional rounds of style variants, family editions, or motion packages follow the same
`--input` / `--out` pattern with different `style:` values.

---

## Numerology — what the engine calculates

The engine handles these safely (deterministic math only):

| Field | Method |
|---|---|
| Life path | Digit-sum of full birth date; master numbers 11, 22, 33 preserved |
| Birthday number | Day of birth reduced to single digit (masters preserved) |
| Destiny number | Pythagorean letter-sum of full name |
| Soul urge | Vowels only (A E I O U Y) |
| Personality number | Consonants only |
| Solar sign | Date-based sun sign; no other placements |

**Never invented by the engine:** Moon sign, rising sign, houses, aspects, planetary
degrees, Human Design body graph, I Ching hexagram. Supply these via `verified_astrology`
and `human_design` fields if the customer has a real chart.

---

## Style selection

When the user isn't sure which style to use, read `references/style_presets.md` and
present the 5 options with a one-line description. Ask: who is this for, and what's the
emotional register — rebellious, heirloom, rustic, scholarly, folk?

The style key must be one of:
`punk_occult` · `wood_relief` · `woodburned_infographic` · `sepia_heritage` · `museum_esoteric`

---

## Ethics and framing

The engine embeds a disclaimer in `06_metadata.json`. The language throughout uses:
- "Symbolically, this may suggest…"
- "This tradition associates…"
- "As a creative archetype…"

Never position the output as prediction, diagnosis, or scientific fact. If a customer
asks whether their life path "proves" something, redirect to the product's actual promise:
*a beautifully crafted map of meaning, not a fixed destiny.*

---

## Product tiers (for quoting / scoping)

| Tier | Deliverables |
|---|---|
| Explorer | 1 style, poster prompt + clean copy + ZIP |
| Chronicle | Poster + manuscript + animation prompt + print copy |
| Legacy | Multiple style editions, long narrative, family edition, motion package |
| Studio | Commercial license for creators, memorial artists, genealogists, boutique print shops |

---

## Troubleshooting

**`YAML requires PyYAML`** → run `pip install PyYAML`

**`Missing required field`** → `full_name`, `display_name`, or `birth_date` is absent from the intake

**`Unknown style`** → the `style:` value doesn't match one of the 5 preset keys exactly

**Date parse error** → use `YYYY-MM-DD`, `MM/DD/YYYY`, or `Month DD, YYYY`

**Life path seems wrong** → verify: master numbers 11, 22, 33 are intentionally NOT reduced further
