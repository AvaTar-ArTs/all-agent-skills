# Logic Mode — System Tracing & Mechanics Reasoning

**Goal:** Understand how something actually works before deciding what to do about it. Output: a traced understanding of the system, its invariants, and its failure modes.

## When to Use

- "What happens if X and Y are both true?"
- "How does this chain of events play out?"
- "What are the edge cases here?"
- "I don't understand why this behaves this way"
- "What's the constraint I'm working within?"
- Debugging unexpected behavior
- Game mechanics, rule systems, workflow reasoning

## Process

### Phase 1 — State the system

Write down what you know the system does. Not what it should do — what it actually does. Keep it to observable facts, not assumptions.

Ask: what are the inputs? What are the outputs? What state does it maintain between calls/steps/turns?

### Phase 2 — Trace a path

Pick the most important scenario and walk through it step by step. Write each step explicitly. No skipping.

At each step, ask:
- What state are we in?
- What decision or transition happens here?
- What changes?

Write it as numbered steps, not prose. Prose hides logical gaps.

### Phase 3 — Find the invariant

What must always be true, no matter the path? Write it as a statement: "X is always Y" or "X can never be Z."

Invariants are the load-bearing assumptions. Violating them breaks the system. Knowing them tells you where the safe boundaries are.

### Phase 4 — Enumerate failure modes

What can go wrong at each step? Work through them:
- What if the input is missing/null/malformed?
- What if two events happen simultaneously or out of order?
- What if a step succeeds but the effect is wrong?
- What if the invariant is violated?

Failure mode enumeration is not pessimism — it's the cheapest form of testing.

### Phase 5 — State the conclusion

Now that you've traced the system: what does this tell you about the decision you need to make? What approach respects the invariants? What would break them?

## Output Format

```
## Logic Trace: [What you're analyzing]

### System (observed facts)
- Inputs: ...
- Outputs: ...
- State: ...

### Step-by-Step Trace (happy path)
1. [State] → [Action] → [New state]
2. ...
3. ...

### Invariant
"[X] is always [Y]" or "The system can never [Z]."

### Failure Modes
| Scenario | What breaks | Severity |
|---|---|---|
| ... | ... | low/med/high |

### Conclusion
[What the trace tells you about the decision at hand]
```

## Anti-Patterns

- **Prose tracing**: writing "and then" instead of numbered steps — gaps hide in the "and thens"
- **Assumption tracing**: tracing what the system should do instead of what it does
- **Skipping failure modes**: "that can't happen" is the most common cause of production bugs
- **Conclusion before trace**: deciding the answer before walking through the system
- **Stopping at happy path**: the interesting logic is always in the edge cases
