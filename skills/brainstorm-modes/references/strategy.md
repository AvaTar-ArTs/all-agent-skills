# Strategy Mode — Goal Clarification & Decision Framing

**Goal:** Clarify the real goal (often not what was stated), enumerate options with honest tradeoffs, and make a defensible recommendation. Output: a decision with documented reasoning, not a list of possibilities.

## When to Use

- "Should we even do this?"
- "What's the right priority?"
- "We could do A or B or C — which one?"
- "What's the risk of X?"
- "Is this worth doing?"
- Roadmap decisions, scope calls, build-vs-buy, resource allocation

## Process

### Phase 1 — Clarify the actual goal

The stated goal is often not the real goal. Ask: "What would success look like 6 months from now?"

Common patterns:
- "I want to add feature X" → actual goal: "users need to be able to do Y"
- "I want to fix bug Z" → actual goal: "the system should be reliable for use case W"
- "I want to build this tool" → actual goal: "I want to stop doing this manually"

Write the actual goal before proceeding. If you're wrong, the user will correct you — that's the point.

### Phase 2 — Surface the real constraints

What's actually limiting the options? Common constraints:
- **Time**: when does this need to be done?
- **Effort**: how much time can realistically be spent?
- **Risk tolerance**: how bad is it if this fails or is wrong?
- **Reversibility**: how easy is it to undo this decision?
- **Dependencies**: what does this block or is blocked by?

Surface these before generating options. Options that violate constraints are waste.

### Phase 3 — Generate options (include "do nothing")

Always include "don't do this" as an option. Sometimes the right answer is to not act.

For each option:
- What does it actually entail?
- What does it give you?
- What does it cost? (time, risk, complexity, debt)
- What does it foreclose? (what you can't do if you pick this)

### Phase 4 — Score on what matters

Pick 2–3 decision criteria based on the constraints. Score each option honestly.

Common criteria:
- **Impact**: how much does this move the actual goal?
- **Effort**: how much does this cost?
- **Risk**: how bad is the worst case?
- **Reversibility**: how easy to undo if wrong?
- **Speed to value**: when do you see results?

### Phase 5 — Recommend with explicit reasoning

State the recommendation. Then write:
- Why this wins on the criteria that matter
- What you're knowingly trading away
- Under what conditions a different option would win

A recommendation without explicit reasoning is an opinion, not a decision.

### Phase 6 — State what would change this

What new information would cause you to reconsider? Write it. This keeps the decision revisable without re-doing the whole analysis.

## Output Format

```
## Decision: [What you're deciding]

**Actual goal:** [Restated from Phase 1]
**Key constraints:** [2–3 limiting factors]

### Options

| Option | Gives you | Costs | Forecloses |
|---|---|---|---|
| A | ... | ... | ... |
| B | ... | ... | ... |
| Do nothing | ... | ... | ... |

### Scoring

| Criterion | A | B | Do nothing |
|---|---|---|---|
| Impact | 3 | 2 | 0 |
| Effort | 1 | 3 | 3 |
| Risk | 2 | 2 | 1 |

### Recommendation: [Option]

**Why:** [2–3 sentences]
**Trade-off accepted:** [What you're giving up]
**Would change if:** [Conditions under which a different option wins]
```

## Anti-Patterns

- **Stated-goal trap**: optimizing for what was asked instead of what was needed
- **Option anchoring**: framing all options around the first idea proposed
- **Omitting "do nothing"**: always include it — sometimes it wins
- **Criteria inflation**: scoring 8 criteria when 3 would decide it
- **Hedged recommendation**: "it depends" without saying what it depends on
- **Recency weighting**: overweighting the most recent constraint you heard about
