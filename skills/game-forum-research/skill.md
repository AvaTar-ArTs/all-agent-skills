---
name: game-forum-research
description: Use when researching a game community forum to find unmet needs, tool gaps, or distribution opportunities. Triggers on "what does the community need", "what are players asking for", "find forum gaps", "research game mod requests", "what's most searched on the forum", "survey game tools forum", or any community demand research task. Always use this skill before building a new mod, tool, or feature — it encodes the gather → synthesize → gap pattern for game forums.
---

# Game Forum Research

Community gap analysis pattern for game tool/mod forums.
Derived from Homecoming City of Heroes "Tools, Utilities & Downloads" research.
Produces actionable gap statements, not raw data dumps.

---

## Process: Gather → Synthesize → State the Gap

The output is **the gap** — what players want but can't get — not a summary of what exists.

---

## Phase 1 — Gather

### Sort by engagement, not recency

```
Forum URL + ?sortby=replies&sortdirection=desc
```

Replies = sustained engagement. Views = reach. The ratio tells the story:
- **High replies, high views** → actively discussed, community-maintained
- **Low replies, high views** → reference content people consume silently (install guides, maps)
- **Many replies, low views** → niche topic with a vocal subgroup

### Scan at minimum 3 pages

Page 1 = active/recent. Pages 2-3 = established tools with view history.

### Look for thread clustering

If 3+ threads cover the same topic, that topic has high unmet demand OR high existing supply. Determine which:
- If those threads point to the same tool → high supply, satisfied demand
- If those threads each propose different partial solutions → unsatisfied demand cluster

### The "Not even sure if this is possible but..." signal

Any thread with this energy indicates a gap no existing tool has filled. Note thread title + reply count.

---

## Phase 2 — Synthesize

Build a table ranked by views × replies:

| Thread | Replies | Views | Category | Status |
|---|---|---|---|---|
| [thread name] | N | Nk | Audio/Tool/Map/etc | Saturated / Partial / Gap |

### Category saturation analysis

A category is **saturated** when multiple high-quality tools compete for the same use case.
A category is a **gap** when player demand is visible but no tool satisfies it.

**Saturation signals:**
- 3+ threads in the same category
- Each tool thread has its own dedicated discussion
- Players ask "which one should I use?" questions

**Gap signals:**
- Threads asking "is this possible?"
- Partial tools that work for some players but not others (e.g., Windows-only)
- High views, low replies (people looked but left unsatisfied)
- Player posts describing workarounds in lieu of a proper tool

---

## Phase 3 — State the Gap

One gap statement per finding, structured as:

```
Gap: [what is missing]
Evidence: [thread title, replies, views]
Player type: [who specifically has this pain]
Existing partial solutions: [if any]
Opportunity: [what a new tool would need to do differently]
```

**Example:**
```
Gap: Mac-native build planner
Evidence: "Seeking remedial instructions to successfully install MIDS Reborn on my iMac" (19 replies, 1.8k views)
Player type: Mac players who can't run WinForms apps natively
Existing partial solutions: Mids' Reborn via Wine (unreliable), Hero Companion (new, July 2026)
Opportunity: Avalonia port of Mids' or web-based alternative — Mac users have no reliable tool today
```

---

## Distribution platform audit (do once per forum)

For any game mod forum, identify the canonical distribution platform:

| Signal | Look for |
|---|---|
| Pinned thread with installer link | Dominant distribution tool |
| High-download external site | CMI-style platform |
| Author cross-posts | Where creators already publish |
| "Download from X" in replies | Community-endorsed platform |

**Key question:** Does the platform accept community submissions? If yes, what format?
For CoH: cityofheroes.dev accepts `.pigg` files via author accounts (contact Michiyo).

---

## Audio mod research heuristic

Audio mod threads consistently outperform in views across game modding forums because:
- Audio is subjective → more discussion per thread
- Audio mods affect all playtime, not just one activity
- Nostalgia threads ("restore the old music") have long tails

If audio demand is visible, it's usually underfilled. Check for:
- Compilation threads (one thread collecting many mods) → reply there, don't create competing thread
- "Is it possible to change X sound?" threads → unmet demand signal

---

## Update cycle

Re-run research every 3-6 months. Forum demand shifts with game patches.
Store findings in a `references/forum-gaps.md` file beside the skill or project.

**CoH research file:** `~/.agent-skills/skills/coh-mod/references/forum-gaps.md`

---

## References

- [[brainstorm-modes]] — Research mode: gather → synthesize → gap
- [[coh-mod]] — CoH mod creation pipeline
- [[coh-mod-publisher]] — distribution after gap is identified and mod is built
