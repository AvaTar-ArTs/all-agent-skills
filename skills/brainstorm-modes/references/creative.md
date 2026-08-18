# Spark Mode — Divergent Creative Ideation

**Goal:** Generate raw material. Quantity before quality. No filtering during generation.

## When to Use

- "What should I build next?"
- "I want to make something but don't know what"
- "Give me ideas for X"
- Starting a new project with no direction
- Stuck in a creative rut

## Process

### Phase 1 — Diverge (no filter)

Generate freely. Aim for 8–12 ideas minimum. Every idea is valid at this stage. Weird > safe.

Constraint types that unlock creativity:
- **Subtraction**: remove a thing that seems essential. What does the project look like without users? Without a UI? Without persistence?
- **Inversion**: what's the opposite of the obvious approach? A tool that deliberately makes things harder. A feature that hides information instead of showing it.
- **Combination**: mash two unrelated things. A todo app + a game. A CLI tool + a musical instrument.
- **Scale**: what if this had 0 users? 1 million? What changes?
- **Time**: what if it only worked for 5 minutes? Forever? In the past only?
- **Constraint injection**: impose a bizarre rule and build around it. "Must fit in a tweet." "Only 3 buttons." "No state."
- **Borrowed context**: how would a chef approach this problem? A cartographer? A medieval scribe?

### Phase 2 — Apply light filter

After generation, apply exactly **one constraint** to cut the list:
- Feasibility: what can actually be built this week/month?
- Or: what would be most interesting to the user right now?
- Or: what fits the existing tech context?

Never apply more than one filter in Spark mode. More constraints belong in Code or Strategy mode.

### Phase 3 — Surface 3

Present exactly 3 ideas with:
- One-line pitch (what it is)
- Why it's interesting (the insight, not the feature list)
- Rough effort estimate (weekend / week / month)
- What makes it unique vs. what already exists

### Output Format

```
## Spark: [Constraint or theme used]

1. **[Title]**
   [One-line pitch]
   [2 sentences: why interesting + what's novel]
   ⏱ [weekend / week / month]

2. **[Title]**
   ...

3. **[Title]**
   ...
```

## Rules

- Generate before filtering. Generation and evaluation use different brain modes — don't mix them.
- Weird ideas are not wasted. They often contain the seed of a better idea.
- "That already exists" is not a reason to discard. "That already exists and I could do it better/differently/stranger" is a reason to keep.
- If the user says "give me more" — go back to Phase 1, don't just iterate on Phase 3 ideas.

## Anti-Patterns

- **Premature realism**: "That's not practical" during generation = idea killer
- **Genre lock**: Only generating ideas in the obvious category
- **Safety anchoring**: First idea sets the range and everything else clusters near it — vary radically
- **Convergence before volume**: Picking a direction before you've generated enough raw material
