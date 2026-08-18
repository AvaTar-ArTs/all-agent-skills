---
name: workspace-ecosystem-audit
description: Provides a methodology and tools for deep inventory and purpose-aware review of local AI/agent ecosystems, focusing on identifying configurations, code, dependencies, and potential risks. Use for understanding and managing your development environment.
---

# Workspace Ecosystem Audit

## Overview

This skill provides a methodology and script for conducting a deep inventory and purpose-aware review of local AI/agent ecosystems. It helps to index, summarize, and reason about files beyond just their names, capturing their intent, code function, and configuration roles across various development environments.

## Key Components

-   **Inventory Script (`scripts/inventory.py`):** A Python script to scan directories, collect file metadata (path, size, type, hash, preview), and output a structured JSON manifest.
-   **Workflow:** A defined process for using the script, slicing the data, reading and summarizing files, identifying risks, and refreshing the inventory.
-   **Reading Guidance:** Prioritization for examining configuration files, agent states, code, and logs.

## Methodology

### 1. Scanning and Inventory

Run the `inventory.py` script against specified root directories (e.g., `.Codex`, `.gemini`, `.qwen`, `.codex`). Use flags to tune the scan (e.g., `--max-hash-bytes`, `--max-preview-bytes`) to manage performance and output size. The output is a JSON file containing detailed metadata for each scanned file.

### 2. Data Slicing and Analysis

Use tools like `jq`, `pandas`, or custom scripts to filter the JSON manifest by file type, path prefix, size, or modification time. This allows for manageable batches of files to be analyzed.

### 3. File Purpose and Intent Review

For selected files or directories:
-   **Read Content:** Use `read_file` or command-line tools (`rg`, `python`) to inspect content.
-   **Summarize:** Capture the file's intent (configuration, code, log, asset, cache).
-   **Identify Risks:** Look for secrets, PII, redundant caches, broken links, or upgrade opportunities.

### 4. Risk Assessment and Action Planning

Based on the review, identify actionable items:
-   **Secrets Management:** Flag sensitive information that needs secure handling.
-   **Cache Cleanup:** Identify large or stale caches for potential removal.
-   **Refactoring Opportunities:** Note code duplication or areas that could benefit from improved structure.
-   **Documentation Gaps:** Identify components lacking adequate explanation.

## Script Usage

The `inventory.py` script offers several flags:
-   `--roots`: Specify directories to scan.
-   `--out FILE`: Define the output JSON file path.
-   `--max-hash-bytes N`: Limit hashing to files under N bytes.
-   `--max-preview-bytes N`: Store only the first N bytes of text files.
-   `--follow-symlinks`: Include targets of symbolic links.
-   `--exclude-dir-name`: Skip specified directories (e.g., `.git`, `.cache`).

## Reading Guidance

Prioritize the review of:
-   Configuration files (`*.json`, `*.toml`, `*.yaml`, `.md` frontmatter)
-   Agent state and history (`history.jsonl`, `sessions/`)
-   Code and scripts
-   Sensitive information placeholders
-   Large cache files

## Best Practices

-   **Batching:** Process findings in manageable batches.
-   **Version Control:** Keep the `inventory.json` file under version control to track changes over time.
-   **Iterative Refinement:** Re-run scans after making changes to verify impact.
-   **Security First:** Be cautious when handling files identified as potential secrets or PII.

---

## Generalization Notes

The core principles of an ecosystem audit—inventory, analysis, risk identification, and action planning—are general. While the provided script and target directories are specific to a local AI/agent setup, the methodology can be applied to any project to gain a comprehensive understanding of its components and potential issues.

## Quick Start
- Run the inventory script for target roots (defaults cover all agent dirs):
  ```bash
  python scripts/inventory.py \
    --roots ~/.Codex ~/.Codex-server-commander ~/.codex ~/.cursor ~/.gemini ~/.grok ~/.qodo ~/.qwen \
    --out ~/.codex/skills/workspace-ecosystem-audit/inventory.json
  ```
- Open the JSON in any viewer; sort by `type`, `ext`, `size_bytes`, or `mtime_iso` to find hotspots.
- For semantic/file-purpose review, sample paths from the manifest and read inline with `rg -n "" <path>` or `python - <<'PY' ...`.


## Workflow (batches recommended)
1. **Scan**: run `inventory.py` with `--max-hash-bytes` and `--max-preview-bytes` tuned to avoid huge files.
2. **Slice**: use jq or pandas to filter by `ext`, `type`, or `path_prefix` (per directory) for manageable batches.
3. **Read & Summarize**: for each slice, summarize intent: configs, creds placeholders, logs, caches, code, assets. Capture findings in your working notes or a new `summary_<dir>.md`.
4. **Risk/Action**: mark secrets, redundant caches, broken links, and upgrade opportunities (extensions, agents, models).
5. **Refresh**: re-run scans after changes; keep `inventory.json` versioned.


## Script Flags
- `--roots ...` space-delimited list of directories.
- `--out FILE` output JSON (default `inventory.json` in CWD).
- `--max-hash-bytes N` hash only files ≤ N bytes (default 2_000_000).
- `--max-preview-bytes N` store first N bytes of text-ish files (default 4000).
- `--follow-symlinks` to include symlink targets (default: record link only).
- `--exclude-dir-name .git .cache ...` to skip noisy trees.


## References
- Targets list: `references/targets.md`
- Enriched audit-data index: `references/workspace-ecosystem-audit-data-index.csv`
- Audit-data docs inventory: `references/workspace-ecosystem-audit-data-docs.csv`
- Use `rg --files` + `rg -n` for fast content search.
- For large JSONL (histories), sample with `python - <<'PY' ...` to avoid loading whole files.


## Validation
- Optional: `python scripts/inventory.py --roots ... --out /tmp/inventory.json --max-hash-bytes 0 --max-preview-bytes 0` for fastest structural map.
