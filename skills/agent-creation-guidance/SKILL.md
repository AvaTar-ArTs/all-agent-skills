---
name: agent-creation-guidance
description: Guides the process of designing and creating autonomous agents, detailing structure, system prompts, triggering conditions, and development best practices.
---

# Agent Creation Guidance

## Overview

This skill guides the process of designing and creating autonomous agents. It covers fundamental aspects like agent structure, defining triggering conditions, crafting effective system prompts, and adhering to development best practices. Agents are designed for autonomous, multi-step tasks, distinct from simple commands.

## Agent File Structure

Agents are typically defined in Markdown files with YAML frontmatter.

### Complete Format

```markdown
---
name: agent-identifier
description: Use this agent when [triggering conditions]. Examples:

<example>
Context: [Situation description]
user: "[User request]"
assistant: "[How assistant should respond and use this agent]"
<commentary>
[Why this agent should be triggered]
</commentary>
</example>

<example>
[Additional example...]
</example>

model: inherit # Or specific model like sonnet, opus, haiku
color: blue    # Visual identifier
tools: ["Read", "Write", "Grep"] # Optional tool restriction
---

You are [agent role description]...

**Your Core Responsibilities:**
1. [Primary responsibility]
2. [Secondary responsibility]

**Analysis Process:**
[Step-by-step workflow]

**Output Format:**
[What to return]

**Edge Cases:**
Handle these situations:
- [Edge case 1]: [How to handle]
---
```

## Frontmatter Fields

### `name` (required)
- Agent identifier for namespacing and invocation.
- Format: lowercase, numbers, hyphens only (3-50 characters).
- Pattern: Must start and end with alphanumeric.

### `description` (required)
- Defines triggering conditions and provides concrete examples. Crucial for agent discovery.
- **Format:** Must start with "Use this agent when..." and include multiple `<example>` blocks.
- **Content:** Include triggering conditions, agent purpose, constraints, and success criteria. Be specific about when NOT to use the agent.
- **Best practices:** 200-1,000 characters with 2-4 examples.

### `model` (required)
- Specifies the AI model to use (`inherit`, `sonnet`, `opus`, `haiku`). `inherit` is recommended.

### `color` (required)
- Visual identifier for the agent (e.g., `blue`, `cyan`, `green`, `yellow`, `red`).

### `tools` (optional)
- Array of allowed tool names. Defaults to all tools if omitted.
- Best practice: Limit tools to the minimum needed.

## System Prompt Design

The markdown body becomes the agent's system prompt. Write in the second person ("You are...", "You will...").

### Structure

**Standard template:**
```markdown
You are [role] specializing in [domain].

**Your Core Responsibilities:**
1. [Primary responsibility]
2. [Secondary responsibility]

**Analysis Process:**
1. [Step one]
2. [Step two]

**Quality Standards:**
- [Standard 1]

**Output Format:**
[What to return]

**Edge Cases:**
Handle these situations:
- [Edge case 1]: [How to handle]
```

### Best Practices

✅ **DO:**
- Use second person.
- Be specific about responsibilities and process.
- Define output format and quality standards.
- Address edge cases.

❌ **DON'T:**
- Use first person.
- Be vague or generic.
- Omit process steps or quality guidance.

## Agent Organization

Agents are typically organized within an `agents/` directory. Namespacing can be used for subdirectories.

## Validation Rules

*   **Identifier:** 3-50 chars, lowercase, hyphens, alphanumeric start/end.
*   **Description:** 10-5,000 chars, includes triggers and examples.
*   **System Prompt:** 20-10,000 chars, clear structure.
