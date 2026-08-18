---
name: coh-mod-publisher
description: Use when publishing, submitting, or distributing City of Heroes mods. Triggers on "post mod to forum", "submit to CMI", "upload to cityofheroes.dev", "write forum post for mod", "submit to Solarverse thread", or any distribution action for a .pigg mod file. Encodes the full pipeline from built .pigg → forum thread → CMI index. Always use this skill when a CoH mod is ready for public release.
---

# CoH Mod Publisher

Complete distribution pipeline for City of Heroes mods built in `mods-mine/`.
Covers three channels: Homecoming forum, cityofheroes.dev (CMI), and community reply threads.

## Prerequisites

- `.pigg` file built via `CoHModdingTool.app`
- `info.json` in the mod's `mods-mine/<MOD_ID>/` directory
- `narrate.py` available at `~/.agent-skills/skills/coh-mod-narrator/scripts/narrate.py`

---

## Step 1 — Generate forum assets

```bash
python3 ~/.agent-skills/skills/coh-mod-narrator/scripts/narrate.py <MOD_ID>
```

Outputs three sections:
- **Forum post** (BBCode, ready to paste)
- **Bind card** (plain text for post footer)
- **Submission metadata** (thread title, forum section, tags, version)

---

## Step 2 — Choose the right forum thread

| Mod type | Primary post location | Secondary (if applicable) |
|---|---|---|
| Audio (sound replacement) | **Reply to Solarverse's SFX thread** (483 replies, 90.9k views) | New thread in Tools, Utilities & Downloads |
| Audio (login/ambient music) | Reply to "Is there a way to change the Intro Screen/Music?" thread | New thread |
| Popmenu (RP-focused) | New thread: Tools, Utilities & Downloads | Tag: `popmenu`, `rp` |
| Popmenu (combat/QoL) | New thread: Tools, Utilities & Downloads | Tag: `popmenu`, `qol` |
| Texture/UI | New thread: Tools, Utilities & Downloads | — |

**Always reply to Solarverse's SFX thread** for audio mods. Never create a competing thread.
Thread URL: search "Solarverse's SFX Consolidated List of Mods" in forum/60.

### Thread title formula
```
[Mod] <Name> — <One-line pitch under 60 chars>
```

---

## Step 3 — Forum submission checklist

Before posting:
- [ ] Status in `info.json` is `"ready"` (not `"draft"`)
- [ ] `.pigg` file tested in-game on Mac (LaunchCat path) and confirmed working
- [ ] Notes field in `info.json` is clean (no internal paths — `narrate.py` strips them)
- [ ] Bind command confirmed working in-game
- [ ] Screenshot or short description of what the menu looks like

Post format order:
1. BBCode post from `narrate.py`
2. Bind card as a `[code]` block
3. Attach `.pigg` file directly to the forum post

---

## Step 4 — Submit to cityofheroes.dev (CMI)

CMI is the dominant distribution platform — 31k+ downloads on top mods (Vidiotmaps benchmark).

1. Register at cityofheroes.dev — check for `/register` URL or contact Michiyo via forum DM (`@Michiyo` in Tools, Utilities & Downloads)
2. Category mapping:
   - Popmenus → **Popmenus** (currently 4 mods, all by AboveTheChemist — high opportunity)
   - Audio → **Audio**
   - Texture → **Graphics**
3. Upload the `.pigg` file with:
   - Name: matches `info.json` `name` field
   - Description: from `info.json` `description` (first 2 sentences)
   - Author: `AvatarArts`
   - Tags: from `info.json` `tags` array

---

## Step 5 — Update `data/mods.json`

After publishing, update the mod's entry in `~/CoX-mod-Adventure/data/mods.json`:
- Add `"forum_url"` with the thread link
- Update `"status"` to `"published"`
- Add `"cmi_url"` once listed on cityofheroes.dev

---

## Audience targeting reference

| Mod | Target player type | Forum hook |
|---|---|---|
| EverlastingRP | RP mains on Everlasting who type emotes 40×/session | Everlasting RP community threads |
| NewPlayerEssentials | Level 1s who don't know /afk or the inspiration tray | New player help threads |
| CoXPhotoMode | Screenshot artists who lose shots hunting /screenshotui 0 | Screenshot sharing threads |
| CoXFastTravel | Alts cycling through Null the Gull every session | General QoL threads |
| EpicLevelUp | Vets who've leveled 50 toons and hate the default boing | Solarverse SFX thread |
| GRLoginMusic | Players who remember Going Rogue login from 2010 | Solarverse SFX thread / Intro music thread |

---

## References

- [[coh-mod]] — mod creation pipeline and info.json schema
- [[coh-mod-narrator]] — forum post + bind card generation
- [[forum-gaps]] — community demand signals and distribution strategy
- Forum section: forums.homecomingservers.com/forum/60
- CMI platform: cityofheroes.dev/mods
