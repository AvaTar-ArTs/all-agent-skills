# Parity Tests

Use these checks to verify a capability translated cleanly across hosts.

## Minimum Checks

- Same trigger phrase activates the capability in both hosts.
- Same input produces the same functional outcome.
- Same guardrails are enforced.
- Same failure modes are documented.
- Same tests or equivalent proofs exist in both renderings.

## Sample Test Prompts

1. "Map this workflow into a skill, agent, hook, and command without changing the behavior."
2. "Mirror this capability into Gemini and keep the trigger and output contract equivalent."
3. "Show me the capability matrix for this workflow and identify any host-specific drift."

## Passing Criteria

- No missing trigger coverage
- No contract mismatch
- No undocumented host-specific behavior
- No loss of verification depth

