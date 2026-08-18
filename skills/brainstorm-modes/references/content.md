# Content Mode — Copy, Voice & Writing

**Goal:** Generate the right words in the right voice for the right audience. Output: copy that fits the context, not generic text.

## When to Use

- "What should this say?"
- "Write the menu labels / option names / flavor text"
- "What tone should this have?"
- "Write the description for X"
- "How should I phrase this?"
- Documentation, in-game text, UI copy, error messages, tooltips

## Process

### Phase 1 — Audience + context

Before writing a word: who is reading this? In what state? What do they need to feel or understand?

Ask:
- Who is the reader? (New user vs. expert. Friend vs. stranger. In-game vs. documentation.)
- What do they already know?
- What do they need to do / feel / understand after reading this?
- What's the reading context? (Under pressure? Scanning? Immersed?)

### Phase 2 — Voice

Pick one of these voice axes for each:
- **Formal ↔ Casual**: "Select an option" vs "Pick one"
- **Expert ↔ Accessible**: assumes jargon vs. explains it
- **Warm ↔ Neutral**: "Here's a tip!" vs "Tip:"
- **Terse ↔ Verbose**: one word vs a sentence
- **In-universe ↔ Meta**: "Contact Ghost Widow" vs "Go to Arachnos"

State the voice before generating copy. Changing voice mid-generation produces inconsistent output.

### Phase 3 — Generate variations (not just one)

Always generate at least 3 variations for key pieces of copy. The first one is almost never the best.

Variation axes:
- Length (shorter, longer, same information)
- Tone (more formal, more casual)
- Framing (what to do vs. what not to do)
- Specificity (generic vs. concrete)

### Phase 4 — Cut ruthlessly

Remove:
- Filler words ("just", "simply", "basically", "really")
- Redundant qualifiers ("very unique", "completely empty")
- Throat-clearing ("This option allows you to...")
- Passive voice where active is clearer
- Explanation of what the reader can see ("Click the button" when there's a button labeled "Click")

### Phase 5 — Consistency check

Is this consistent with other copy in the same context? Same capitalization style? Same label format? Same level of detail?

## Output Format

```
## Copy: [What you're writing]

**Audience:** [Who's reading + their context]
**Voice:** [2–3 axis descriptors]

### Variations

1. [Short/formal/terse version]
2. [Medium/balanced version]  
3. [Longer/warmer/more context version]

### Recommendation: Variation [N]
[One sentence on why]
```

## Special cases

**Menu / UI labels**: Terse wins. 1–3 words. Verb first for actions ("Build", "Stage", "Install"). Noun first for categories ("Mods", "Targeting", "Travel").

**Error messages**: State what happened, not what didn't. "File not found" > "Could not load file". Include what to do next when possible.

**In-universe/flavor text**: Pick one register and hold it. CoH OOC wrappers: `(( double parens ))`. Actions: `*asterisks*`. Dialogue: plain. Never mix.

**Documentation**: Imperative mood. "Run this command" not "You should run this command". Code blocks for everything executable.

## Anti-Patterns

- **Generic default**: writing "Description" as a label placeholder
- **Voice drift**: starting formal and going casual mid-document
- **Over-explaining**: writing what the reader can already see
- **First draft shipping**: picking the first thing generated without generating alternatives
- **Jargon for insiders**: assuming the reader knows terms they might not
