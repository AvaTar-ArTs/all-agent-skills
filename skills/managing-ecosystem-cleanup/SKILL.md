---
name: managing-ecosystem-cleanup
description: Use when auditing AI tool ecosystems for duplicate plugins, backup skills, and context bloat across Codex/Cursor/Gemini installations
---

# Managing Ecosystem Cleanup

## Overview

Systematically audit, report, and clean AI tool ecosystems (Codex, Cursor, Gemini, others) while maintaining reversibility through change logs.

**Core principle:** Duplicates and backups take up disk space and load into context. Clean them systematically. Never delete without a restore path.

## When to Use

Use when:
- Context bloat from duplicate plugins/skills (51%+ in messages)
- Multiple versions of same skill auto-loading
- Backup directories treated as active installations
- Marketplace duplicates (plugin from both Codex and Codex-plugins-official)
- Need to reclaim disk space without risk

**Symptoms that trigger this skill:**
- `/context` shows 70%+ token usage
- `du` shows 500MB+ in backup/duplicate directories
- Skill loading lists duplicates (notebooklm, notebooklm-backup, notebooklm-mcp)
- Plugin list shows same plugin from multiple marketplaces
- Config files reference multiple versions

## Core Pattern

### Three-Mode Cleanup System

**MODE 1: AUDIT** (read-only, safe)
```bash
ecosystem-cleanup audit [--config ecosystem-cleanup.yaml]
```
- Scans all detected tools (or specified subset)
- Identifies: backups, duplicates, stale versions
- Generates report: what wastes how much space
- Output: audit-report.json
- **Result:** Info only, nothing deleted

**MODE 2: PROPOSE** (interactive)
```bash
ecosystem-cleanup propose [--config ecosystem-cleanup.yaml]
```
- Shows audit findings
- Displays cleanup recommendations with impact
- User confirms each removal
- **Result:** What WOULD be deleted, with reasoning

**MODE 3: EXECUTE** (with change log)
```bash
ecosystem-cleanup execute [--config ecosystem-cleanup.yaml]
```
- Performs cleanup based on recommendations
- Creates `cleanup-manifest.csv` tracking:
  - Path removed
  - Type (backup/duplicate/stale)
  - Size freed
  - Timestamp
  - Reason for removal
- **Result:** Space reclaimed + recovery option

### Recovery via Change Log

```bash
# View what was removed
cat cleanup-manifest.csv

# Restore specific item
ecosystem-cleanup restore --from cleanup-manifest.csv --item notebooklm-backup

# Restore all removals
ecosystem-cleanup restore --from cleanup-manifest.csv --all
```

## Configuration

### Built-in Tool Templates (No Config Needed)

**Codex:**
```yaml
tools:
  Codex:
    paths:
      skills: ~/.Codex/skills
      plugins: ~/.Codex/plugins/cache
    duplicates_pattern: "@Codex-plugins|@Codex-plugins-official"
    backups_pattern: "*-backup*|*.tar.gz|*.bak"
```

**Cursor:**
```yaml
tools:
  cursor:
    paths:
      skills: ~/.cursor/skills
      plugins: ~/.cursor/plugins/cache
```

**Gemini:**
```yaml
tools:
  gemini:
    paths:
      skills: ~/.gemini/skills
      extensions: ~/.gemini/extensions
```

### Custom Config Override

Create `ecosystem-cleanup.yaml` in project root:
```yaml
tools:
  Codex:
    enabled: true
    paths:
      skills: /custom/path/skills
  custom-tool:
    enabled: true
    paths:
      data: /path/to/data
    duplicates_pattern: "v[0-9].*"

# Optional: specify which tools to audit
audit_scope: [Codex, cursor]  # Skip gemini
```

### Auto-Detection Flow

1. Check for built-in tool paths
2. Load custom config if exists
3. User can override: `--tools Codex,cursor` (skip detected gemini)
4. Audit only enabled tools

## Quick Reference

| Scenario | Command |
|----------|---------|
| See what wastes space | `ecosystem-cleanup audit` |
| Review before cleanup | `ecosystem-cleanup propose` |
| Actually clean | `ecosystem-cleanup execute` |
| Restore deleted item | `ecosystem-cleanup restore --item notebooklm-backup` |
| View cleanup history | `cat cleanup-manifest.csv` |
| Use custom config | `ecosystem-cleanup audit --config custom.yaml` |

## Implementation

### Components

**detect-tools.sh**
- Scans system for installed AI tools
- Returns: list of found tool paths
- Respects auto-detection + user override

**audit-ecosystem.sh**
- Analyzes each tool's plugins/skills
- Identifies duplicates (name + size match)
- Finds backups (suffix patterns)
- Calculates waste
- Output: audit-report.json

**cleanup-manifest.csv**
- Logged on every removal
- Columns: path | type | size_bytes | timestamp | reason | restore_command
- Enables selective restoration

**restore-from-manifest.sh**
- Parses cleanup-manifest.csv
- Recreates deleted directories
- Can restore subset or all

### Execution Flow

```
START
  ↓
[Auto-detect tools]
  ↓
[Load config - built-in OR custom]
  ↓
[User specifies scope - all detected OR subset]
  ↓
[MODE: audit | propose | execute]
  ↓
IF audit: [Report findings] → END
IF propose: [Show recommendations] → [User confirms] → END
IF execute:
  ├→ [Backup change log]
  ├→ [Remove items]
  ├→ [Log each removal to manifest]
  └→ [Report freed space + recovery path] → END
```

## Common Mistakes

**❌ Deleting without manifest**
- Don't remove items manually, always use execute mode
- Reason: Manual deletion loses recovery information

**❌ Ignoring duplicates from different marketplaces**
- Both Codex-plugins and Codex-plugins-official versions exist
- Only keep official version, remove code-plugins duplicate

**❌ Keeping all notebooklm variants**
- notebooklm/ (304MB), notebooklm-mcp/ (75MB), notebooklm-backup (304MB)
- Pick ONE version, move others to cleanup list

**❌ Running without config on multi-tool setup**
- Auto-detection works but may miss custom paths
- Create ecosystem-cleanup.yaml if tools in non-standard locations

**✅ Always audit first**
- Run audit mode to see impact before execute
- Shows exact space savings + what will be removed

## Real-World Impact

**Before cleanup:** 142k/200k tokens (71%) - messages dominating, skills/plugins bloating context
**After cleanup:** 100-120k tokens expected (50-60%) - context freed, faster responses, cheaper API calls

**Disk savings example:**
- notebooklm backups: 446MB
- notebooklm variants: 379MB (keep 1, remove 2)
- plugin duplicates: ~3MB
- **Total: 825MB+ → ~300MB** (keeping only active versions)

**Restoration safety:** Every removal logged, selective restore possible, no data loss risk

## Testing Scenarios

### RED Phase (Baseline - No Skill)

**Pressure Test 1: Discovery**
- Agent manually audits ecosystem
- Result: Incomplete, misses duplicates, slow process

**Pressure Test 2: Cleanup Confidence**
- Agent considers deleting without manifest
- Rationalization: "I remember what I deleted"
- Result: Items unrecoverable

**Pressure Test 3: Multi-Tool Complexity**
- Agent manages Codex + Cursor duplicates
- Result: Inconsistent approach, some tools cleaned, others forgotten

### GREEN Phase (With Skill)

- Agent audits via three-mode system consistently
- Agent uses manifest for every deletion
- Agent restores selectively without guesswork
- Multi-tool cleanup is systematic

### REFACTOR Phase

- Address: "But audit takes time" → Show that manual cleanup takes longer
- Address: "Manifest is overhead" → Show restore saves hours if needed
- Address: "Can't break anything" → Show duplicates ALREADY breaking context
