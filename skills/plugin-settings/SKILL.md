---
name: plugin-settings
description: Guides the use of `.local.md` files for per-project plugin configuration, covering structure, parsing, best practices, and security. Use when making plugin behavior configurable.
---

# Plugin Configuration Pattern

## Overview

This pattern describes how to implement user-configurable settings and state for plugins using `.local.md` files. These files, typically placed in the project's root directory within a `.Codex/` folder, use YAML frontmatter for structured settings and markdown content for additional context or prompts.

## Key Characteristics

-   **File Location:** `.Codex/plugin-name.local.md` (e.g., `.Codex/my-plugin.local.md`) in the project root.
-   **Structure:** YAML frontmatter for key-value settings, followed by markdown content.
-   **Purpose:** To store user-specific configurations and state for a plugin on a per-project basis.
-   **Lifecycle:** User-managed; these files should **not** be committed to version control and must be added to `.gitignore`.
-   **Usage:** Settings can be read by hooks, commands, and agents to adapt plugin behavior.

## File Structure

### Basic Template

```markdown
---
enabled: true
setting1: value1
setting2: value2
numeric_setting: 42
list_setting: ["item1", "item2"]
---

# Additional Context

This markdown body can contain:
- Task descriptions
- Additional instructions
- Prompts to feed back to Codex
- Documentation or notes
```

### Example: Plugin State File

**.Codex/my-plugin.local.md:**
```markdown
---
enabled: true
strict_mode: false
max_retries: 3
notification_level: info
coordinator_session: team-leader
---

# Plugin Configuration

This plugin is configured for standard validation mode.
Contact @team-lead with questions.
```

## Reading Settings Files

Settings can be read and parsed from these files by various project components:

### From Hooks (Bash Scripts)

Hooks can check for the existence of the settings file and parse its YAML frontmatter to control behavior.
*   **Example Snippet (Bash):**
    ```bash
    STATE_FILE=".Codex/my-plugin.local.md"
    if [[ ! -f "$STATE_FILE" ]]; then exit 0; fi # Exit if not configured
    FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$STATE_FILE")
    ENABLED=$(echo "$FRONTMATTER" | grep '^enabled:' | sed 's/enabled: *//')
    if [[ "$ENABLED" != "true" ]]; then exit 0; fi # Exit if disabled
    # ... use enabled setting ...
    ```

### From Commands

Commands can read settings to customize their execution, prompting the user for input if settings are missing or applying defaults.

### From Agents

Agents can be instructed to check for and utilize settings from these files to adapt their behavior contextually.

## Parsing Techniques

Settings files can be parsed using standard command-line tools:
-   **Extracting Frontmatter:** Use `sed` to capture content between the `---` delimiters.
-   **Reading Specific Fields:** Employ `grep` and `sed` to extract values for `string`, `boolean`, or `numeric` fields.
-   **Reading Markdown Body:** Extract content after the second `---` delimiter using `awk`.

## Common Patterns

### Pattern 1: Feature Toggling

Use an `enabled: true/false` flag in settings to toggle feature availability for hooks or commands.

### Pattern 2: Agent State Management

Store agent-specific state (e.g., `task_number`, `pr_number`, `coordinator_session`) to coordinate multi-agent workflows.

### Pattern 3: Configuration-Driven Behavior

Define parameters like `validation_level`, `max_file_size`, or `allowed_extensions` to allow users to configure plugin behavior.

## Best Practices

-   **File Naming:** Consistently use `.Codex/plugin-name.local.md`.
-   **Gitignore:** Always add `.Codex/*.local.md` and `.Codex/*.local.json` to `.gitignore`.
-   **Defaults:** Provide sensible defaults when settings files are absent.
-   **Validation:** Validate setting values to prevent errors.
-   **Restart Requirement:** Clearly document that changes to settings files may require restarting the IDE/tool (e.g., Codex) to take effect, as hooks may not hot-reload.

## Security Considerations

-   **Sanitize Input:** Escape user input carefully when writing settings files to prevent injection.
-   **Validate File Paths:** Sanitize any file paths read from settings to prevent path traversal vulnerabilities.
-   **Permissions:** Ensure settings files have restrictive permissions (e.g., `chmod 600`).

---

## Generalization Notes

The pattern of using `.local.md` files with YAML frontmatter for per-project configuration is a widely applicable concept. While examples might reference specific tools or environments (like `.Codex/` paths), the underlying mechanism of structured, user-managed, non-version-controlled configuration is general.

### Extract Frontmatter

```bash
# Extract everything between --- markers
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$FILE")
```


### Read Individual Fields

**String fields:**
```bash
VALUE=$(echo "$FRONTMATTER" | grep '^field_name:' | sed 's/field_name: *//' | sed 's/^"\(.*\)"$/\1/')
```

**Boolean fields:**
```bash
ENABLED=$(echo "$FRONTMATTER" | grep '^enabled:' | sed 's/enabled: *//')
# Compare: if [[ "$ENABLED" == "true" ]]; then
```

**Numeric fields:**
```bash
MAX=$(echo "$FRONTMATTER" | grep '^max_value:' | sed 's/max_value: *//')
# Use: if [[ $MAX -gt 100 ]]; then
```


### Read Markdown Body

Extract content after second `---`:

```bash
# Get everything after closing ---
BODY=$(awk '/^---$/{i++; next} i>=2' "$FILE")
```


### Pattern 1: Temporarily Active Hooks

Use settings file to control hook activation:

```bash
#!/bin/bash
STATE_FILE=".Codex/security-scan.local.md"

# Quick exit if not configured
if [[ ! -f "$STATE_FILE" ]]; then
  exit 0
fi

# Read enabled flag
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$STATE_FILE")
ENABLED=$(echo "$FRONTMATTER" | grep '^enabled:' | sed 's/enabled: *//')

if [[ "$ENABLED" != "true" ]]; then
  exit 0  # Disabled
fi

# Run hook logic
# ...
```

**Use case:** Enable/disable hooks without editing hooks.json (requires restart).


## Creating Settings Files


### Template Generation

Provide template in plugin README:

```markdown

## Configuration

Create `.Codex/my-plugin.local.md` in your project:

\`\`\`markdown
---
enabled: true
mode: standard
max_retries: 3
---

# Plugin Configuration

Your settings are active.
\`\`\`

After creating or editing, restart Codex for changes to take effect.
```


### File Naming

✅ **DO:**
- Use `.Codex/plugin-name.local.md` format
- Match plugin name exactly
- Use `.local.md` suffix for user-local files

❌ **DON'T:**
- Use different directory (not `.Codex/`)
- Use inconsistent naming
- Use `.md` without `.local` (might be committed)


### Gitignore

Always add to `.gitignore`:

```gitignore
.Codex/*.local.md
.Codex/*.local.json
```

Document this in plugin README.


### Defaults

Provide sensible defaults when settings file doesn't exist:

```bash
if [[ ! -f "$STATE_FILE" ]]; then
  # Use defaults
  ENABLED=true
  MODE=standard
else
  # Read from file
  # ...
fi
```


### Validation

Validate settings values:

```bash
MAX=$(echo "$FRONTMATTER" | grep '^max_value:' | sed 's/max_value: *//')

# Validate numeric range
if ! [[ "$MAX" =~ ^[0-9]+$ ]] || [[ $MAX -lt 1 ]] || [[ $MAX -gt 100 ]]; then
  echo "⚠️  Invalid max_value in settings (must be 1-100)" >&2
  MAX=10  # Use default
fi
```


### Restart Requirement

**Important:** Settings changes require Codex restart.

Document in your README:

```markdown

## Changing Settings

After editing `.Codex/my-plugin.local.md`:
1. Save the file
2. Exit Codex
3. Restart: `Codex` or `cc`
4. New settings will be loaded
```

Hooks cannot be hot-swapped within a session.


### Sanitize User Input

When writing settings files from user input:

```bash
# Escape quotes in user input
SAFE_VALUE=$(echo "$USER_INPUT" | sed 's/"/\\"/g')

# Write to file
cat > "$STATE_FILE" <<EOF
---
user_setting: "$SAFE_VALUE"
---
EOF
```


### Validate File Paths

If settings contain file paths:

```bash
FILE_PATH=$(echo "$FRONTMATTER" | grep '^data_file:' | sed 's/data_file: *//')

# Check for path traversal
if [[ "$FILE_PATH" == *".."* ]]; then
  echo "⚠️  Invalid path in settings (path traversal)" >&2
  exit 2
fi
```


### Permissions

Settings files should be:
- Readable by user only (`chmod 600`)
- Not committed to git
- Not shared between users


## Real-World Examples


### multi-agent-swarm Plugin

**.Codex/multi-agent-swarm.local.md:**
```markdown
---
agent_name: auth-implementation
task_number: 3.5
pr_number: 1234
coordinator_session: team-leader
enabled: true
dependencies: ["Task 3.4"]
additional_instructions: Use JWT tokens, not sessions
---

# Task: Implement Authentication

Build JWT-based authentication for the REST API.
Coordinate with auth-agent on shared types.
```

**Hook usage (agent-stop-notification.sh):**
- Checks if file exists (line 15-18: quick exit if not)
- Parses frontmatter to get coordinator_session, agent_name, enabled
- Sends notifications to coordinator if enabled
- Allows quick activation/deactivation via `enabled: true/false`


### ralph-loop Plugin

**.Codex/ralph-loop.local.md:**
```markdown
---
iteration: 1
max_iterations: 10
completion_promise: "All tests passing and build successful"
---

Fix all the linting errors in the project.
Make sure tests pass after each fix.
```

**Hook usage (stop-hook.sh):**
- Checks if file exists (line 15-18: quick exit if not active)
- Reads iteration count and max_iterations
- Extracts completion_promise for loop termination
- Reads body as the prompt to feed back
- Updates iteration count on each loop


## Quick Reference


### File Location

```
project-root/
└── .Codex/
    └── plugin-name.local.md
```


### Frontmatter Parsing

```bash
# Extract frontmatter
FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$FILE")

# Read field
VALUE=$(echo "$FRONTMATTER" | grep '^field:' | sed 's/field: *//' | sed 's/^"\(.*\)"$/\1/')
```


### Body Parsing

```bash
# Extract body (after second ---)
BODY=$(awk '/^---$/{i++; next} i>=2' "$FILE")
```


### Quick Exit Pattern

```bash
if [[ ! -f ".Codex/my-plugin.local.md" ]]; then
  exit 0  # Not configured
fi
```


## Additional Resources


### Reference Files

For detailed implementation patterns:

- **`references/parsing-techniques.md`** - Complete guide to parsing YAML frontmatter and markdown bodies
- **`references/real-world-examples.md`** - Deep dive into multi-agent-swarm and ralph-loop implementations


### Example Files

Working examples in `examples/`:

- **`read-settings-hook.sh`** - Hook that reads and uses settings
- **`create-settings-command.md`** - Command that creates settings file
- **`example-settings.md`** - Template settings file


### Utility Scripts

Development tools in `scripts/`:

- **`validate-settings.sh`** - Validate settings file structure
- **`parse-frontmatter.sh`** - Extract frontmatter fields


## Implementation Workflow

To add settings to a plugin:

1. Design settings schema (which fields, types, defaults)
2. Create template file in plugin documentation
3. Add gitignore entry for `.Codex/*.local.md`
4. Implement settings parsing in hooks/commands
5. Use quick-exit pattern (check file exists, check enabled field)
6. Document settings in plugin README with template
7. Remind users that changes require Codex restart

Focus on keeping settings simple and providing good defaults when settings file doesn't exist.
