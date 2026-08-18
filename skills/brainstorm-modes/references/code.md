# Code Mode — Technical Option Enumeration

**Goal:** Choose the right technical approach before writing any code. Output: a chosen approach with documented reasoning.

## When to Use

- "How should I implement X?"
- "Which library/framework/pattern should I use?"
- "What architecture makes sense here?"
- "Should I use A or B?"

## Process

### Phase 1 — Enumerate options (don't skip)

List ALL viable approaches, even ones you'll reject. Minimum 3. Missing an option here means you'll revisit the decision halfway through implementation.

For each option, capture:
- What it is (one sentence)
- Core mechanism (how it actually works)
- What it requires (dependencies, knowledge, infra)

### Phase 2 — Score against criteria

Pick 3–4 evaluation criteria from this list (match to the actual project constraints):
- **Dev speed** — how fast to implement from scratch?
- **Runtime performance** — CPU, memory, latency profile
- **Maintainability** — how hard to change 6 months from now?
- **Debuggability** — when it breaks, how easy to diagnose?
- **Dependency risk** — unmaintained packages, breaking APIs
- **Reversibility** — how hard to undo this choice?
- **Testability** — can it be unit/integration tested cleanly?
- **Existing codebase fit** — consistent with patterns already in use?

Score each option 1–3 per criterion. Don't average — identify what matters most and weight it.

### Phase 3 — Recommend with reasoning

State the recommendation. Include:
- Why this option wins on the criteria that matter most
- What you're explicitly trading away (honest about downsides)
- What would change the recommendation (conditions under which another option wins)

### Phase 4 — Spike before commitment (for uncertain choices)

If the decision is high-stakes and reversibility is low: recommend a 1–2 hour spike before committing. Define what the spike needs to prove. Do not extend spike into implementation.

## Output Format

```
## Technical Decision: [What you're deciding]

### Options

| Option | Mechanism | Requires |
|---|---|---|
| A | ... | ... |
| B | ... | ... |
| C | ... | ... |

### Evaluation

| Criterion | A | B | C |
|---|---|---|---|
| Dev speed | 2 | 3 | 1 |
| Maintainability | 3 | 2 | 2 |
| ... | | | |

### Recommendation: Option [X]

**Why:** [2–3 sentences on why this wins]
**Trade-off:** [What you're giving up]
**Would change if:** [Conditions under which a different option wins]
```

## Anti-Patterns

- **Familiarity bias**: picking what you already know without comparing alternatives
- **Recency bias**: using the library you saw last week
- **Complexity default**: reaching for a framework when a function would do
- **Premature optimization**: choosing the fastest option when dev speed is the constraint
- **Analysis paralysis**: scoring 8 criteria when 3 would suffice
