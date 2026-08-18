# Research Source-First

Prioritizes provenance, competing evidence, and citations.

## Use When

- The user explicitly asks for `research-source-first` style.
- The problem benefits from this style's routing emphasis.

## Retrieval Profile

- Default result limit: 12
- Output format: `detailed`
- Preferred document kinds: `markdown`, `skill`, `csv`, `json`

## Output Contract

- research question
- source set
- conflicts
- synthesis
- open questions

## Guardrails

- Begin with evidence from the Brain DB.
- Explain why a selected agent or skill is relevant.
- Preserve explicit approval gates before writes, installs, cleanup, commits, or pushes.
- Do not substitute style for verification.
