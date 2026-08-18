---
name: rule-definition-patterns
description: Guides the creation of rules for pattern matching and message display upon event triggers, detailing syntax, event types, conditions, and file organization.
---

# Rule Definition Patterns

## Overview

This skill provides guidance on defining rules for monitoring events and triggering actions or messages. It details the syntax for rule configuration, including event types, matching conditions, and the structure for messages displayed upon rule activation. The focus is on abstracting the concept of rule definition, applicable to various monitoring or automation systems.

## When to Use

*   When establishing automated responses to specific events or patterns.
*   For defining conditions that trigger warnings, blocks, or custom messages.
*   When creating rules for code quality checks, security monitoring, or workflow automation.

Avoid when:
*   A simple manual check is sufficient.
*   The logic is highly specific to a single, non-reusable scenario.

## Rule File Format

Rules are typically defined in configuration files (e.g., Markdown with YAML frontmatter, JSON, or TOML) specifying name, event triggers, conditions, and actions.

### Basic Structure

```yaml
---
name: rule-identifier
enabled: true
event: bash|file|stop|prompt|all
pattern: regex-pattern-here
---

Message to show when this rule triggers.
Can include markdown formatting, warnings, suggestions, etc.
```

### Frontmatter Fields

*   **`name` (required):** Unique identifier for the rule (e.g., `warn-dangerous-rm`). Use kebab-case.
*   **`enabled` (required):** Boolean (`true`/`false`) to activate/deactivate the rule.
*   **`event` (required):** The type of event to monitor (`bash`, `file`, `stop`, `prompt`, `all`).
*   **`pattern` (simple format):** A regular expression for simple, single-condition matches.

### Advanced Format (Multiple Conditions)

For complex rules requiring multiple conditions to be met:

```yaml
---
name: complex-rule
enabled: true
event: file
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.tsx?$
  - field: new_text
    operator: contains
    pattern: console\.log\(
---

Warning message about console.log in TypeScript files.
```

**Condition Fields:**
*   **`field`:** The target of the condition (e.g., `command` for bash, `file_path`, `new_text`, `old_text`, `content` for file events).
*   **`operator`:** How to match (`regex_match`, `contains`, `equals`, `not_contains`, `starts_with`, `ends_with`).
*   **`pattern`:** The regex or string to match against.

**All conditions must match** for the rule to trigger.

## Message Body

The content following the frontmatter is displayed when a rule triggers. Good messages explain:
*   What was detected.
*   Why it's problematic.
*   Suggested alternatives or best practices.

## Event Type Guide

*   **`bash`**: Matches patterns in shell command execution.
*   **`file`**: Matches patterns in file edits, writes, or content.
*   **`stop`**: Triggers when an agent signals completion or a halt.
*   **`prompt`**: Matches patterns within user prompts (advanced).
*   **`all`**: Triggers on all events.

## Pattern Writing Tips

*   **Regex Basics:** Understand literal characters, escaping special characters (`.`, `(`, `)`), and common metacharacters (`\s`, `\d`, `\w`, `+`, `*`, `?`, `|`).
*   **Testing Patterns:** Always test regex patterns thoroughly using tools like regex101.com or Python's `re` module.
*   **Avoid Pitfalls:** Be mindful of patterns being too broad (e.g., `log`) or too specific (e.g., exact paths).

## File Organization

*   **Location:** Rules are typically stored in a designated directory (e.g., `.Codex/` or `rules/`).
*   **Naming:** Use descriptive names with `.local.md` suffix (e.g., `hookify.dangerous-rm.local.md`).
*   **Gitignore:** Add rule files to `.gitignore` if they contain sensitive info or are local configurations.

## Workflow

### Creating a Rule
1. Identify unwanted behavior or pattern.
2. Determine the relevant event type and tool.
3. Write the pattern or conditions.
4. Create the rule file with frontmatter and message.
5. Test immediately (rules often reload dynamically).

### Refining a Rule
1. Edit the rule file.
2. Adjust pattern or message.
3. Test again.

### Disabling a Rule
*   **Temporary:** Set `enabled: false` in frontmatter.
*   **Permanent:** Delete the rule file.

---

## Generalization Notes

The core concepts of defining rules, event triggers, conditions, and actions are general. The specific syntax (YAML frontmatter, regex, event types like `bash`, `file`) and file organization (`.Codex/hookify.{name}.local.md`) are implementation details of a particular system (Hookify). A generalized skill would focus on the *pattern* of rule definition, using these as examples.

This skill provides a solid foundation for rule-based automation and validation.
