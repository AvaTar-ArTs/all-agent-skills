# Design Mode — Hierarchy, Flow & Structure

**Goal:** Define what the thing is and how it's organized before building it. Output: a structure that serves the user's mental model, not the implementer's convenience.

## When to Use

- "What should the menu hierarchy look like?"
- "How do I structure this?"
- "What's the UX flow?"
- "Where should option X live?"
- Menu design, information architecture, command organization, API shape, file structure

## Process

### Phase 1 — User's mental model (not yours)

What does the user think of when they think of this thing? Not what it technically is — what the user calls it, groups it with, reaches for when they need it.

Ask:
- What task is the user trying to accomplish when they open/use this?
- What do they already know? (What existing mental model are they mapping to?)
- What do they NOT care about? (What structure exists for the implementer's benefit, not theirs?)

### Phase 2 — Identify the primary actions (top 3)

What are the 3 things users will do most often? These get the most prominent positions. Everything else is secondary.

If you can't rank the top 3, you haven't understood the use case yet. Go back to Phase 1.

### Phase 3 — Group by relationship, not by type

Group things by how a user thinks about them, not by what they technically are.

Bad grouping (by type): `[Sounds] [Textures] [Popmenus]` — categories the file system cares about
Good grouping (by use): `[During combat] [Before a pull] [Navigation] [RP / Social]` — categories the user cares about

When in doubt: ask "if the user is looking for X, what do they think of first?"

### Phase 4 — Apply progressive disclosure

Depth increases with specificity. The top level should be navigable without knowing what's inside.

Rules:
- Max 5–7 items at any one level (Miller's law — working memory limit)
- Items at the same level should be the same kind of thing
- Nesting adds cognitive load — only go deeper when necessary
- Labels at each level should make the content of the next level predictable

### Phase 5 — Draw it (even in ASCII)

Force yourself to represent the structure visually before building it. Structures look different in a diagram than they do in your head.

Minimum: a list of levels. Better: a tree. Best: a user flow from "open" to "find X" with the fewest steps.

## Output Format

```
## Design: [What you're structuring]

**Primary user goal:** [What they open this to do]
**Top 3 actions:** [In order of frequency]

### Structure

Level 1 (visible on open):
├── Group A [covers: x, y, z]
│   ├── Option 1
│   ├── Option 2
│   └── Option 3
├── Group B [covers: ...]
│   └── ...
└── Group C

### Rationale
[Why this grouping matches the user's mental model]

### What got cut / moved
[What you considered and why it's not at the top level]
```

## Anti-Patterns

- **Implementer's hierarchy**: organizing by how the code works, not how the user thinks
- **Flat list**: refusing to nest when grouping would make scanning faster
- **Deep nesting**: hiding common actions 3 levels down
- **Label ambiguity**: two items at the same level that could mean the same thing
- **Kitchen sink**: adding every possible option at the top level to "make it accessible"
- **Skipping the user's perspective**: jumping straight to structure without asking what they're trying to do
