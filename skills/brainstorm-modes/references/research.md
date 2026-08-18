# Research Mode — Gap Analysis & Synthesis

**Goal:** Turn raw information into an identified gap or actionable insight. Output: the gap, not the data.

## When to Use

- "What does the community need?"
- "What's already been done?"
- "What are people asking for?"
- "Is there a market for X?"
- "What am I missing?"
- Pre-ideation: before generating ideas, survey what exists

## Process

### Phase 1 — Define the research question precisely

Vague question = vague output. Before gathering anything, write the question as a single sentence that could have a yes/no or specific answer.

Bad: "What do users want?"
Good: "What mod types are requested on Homecoming forums but don't exist in the community library?"

### Phase 2 — Identify sources

Where does the answer live? Enumerate them before searching:
- Primary sources: the actual community, the actual codebase, the actual data
- Secondary sources: forum posts, docs, prior research
- Gaps in coverage: what sources don't exist or aren't accessible?

### Phase 3 — Gather (time-boxed)

Search, read, collect. Set a time limit or result limit before starting. Unbounded research is procrastination.

Tag each finding: `evidence` (directly answers the question), `signal` (suggestive but indirect), `noise` (irrelevant).

### Phase 4 — Synthesize

Look at the `evidence` pile. What pattern emerges?
- What's consistent across sources?
- What's contradictory?
- What's conspicuously absent?

Absence is data. If everyone is asking for X but no one has built it, that's the gap.

### Phase 5 — State the gap

Write the gap in one sentence: "X exists but Y is missing" or "There is demand for Z but no supply."

The gap is the output. All data is in service of naming the gap clearly.

### Phase 6 — Validate (optional but high-value)

Before acting on the gap: can you find one more piece of confirming evidence? One disconfirming piece? What would change your conclusion?

## Output Format

```
## Research: [The question]

### Sources consulted
- [Source 1]: [what it covers, how authoritative]
- [Source 2]: ...

### Key findings
| Finding | Source | Type |
|---|---|---|
| ... | ... | evidence / signal / noise |

### Pattern
[2–3 sentences on what the findings say together]

### The Gap
"[X exists / is happening] but [Y is missing / not being served]."

### Confidence
[high / medium / low] — [what would change this]
```

## Anti-Patterns

- **Data hoarding**: gathering more and more without synthesizing
- **Confirmation search**: only looking at sources likely to confirm what you already think
- **Gap-less research**: summarizing what you found without identifying the actionable gap
- **Infinite scoping**: refining the question forever instead of answering the one you have
- **Treating signal as evidence**: "people seem to want" ≠ "people are asking for"
