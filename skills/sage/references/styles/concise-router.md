# Concise Router

Returns the smallest useful capability route.

## Use When

- The user explicitly asks for `concise-router` style.
- The problem benefits from this style's routing emphasis.

## Retrieval Profile

- Default result limit: 5
- Output format: `compact`
- Preferred document kinds: `skill`, `command`

## Output Contract

- intent
- top capabilities
- best evidence path
- next action

## Guardrails

- Begin with evidence from the Brain DB.
- Explain why a selected agent or skill is relevant.
- Preserve explicit approval gates before writes, installs, cleanup, commits, or pushes.
- Do not substitute style for verification.
