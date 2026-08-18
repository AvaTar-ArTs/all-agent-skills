# Adapter Contract

Every adapter in `scripts/adapters/` implements this contract. One adapter = one backend.

## CLI

```
python scripts/adapters/<backend>.py --spec /abs/spec.yaml --out /abs/out.ext [--dry-run] [--timeout SEC]
```

- `--spec`: absolute path to unit spec YAML (exit 1 if relative)
- `--out`: absolute path for output asset (exit 1 if relative)
- `--dry-run`: validate + print planned request; no network; exit 0 if valid
- `--timeout`: overall timeout in seconds (backend-specific default)

## Exit codes (R11)

| Code | Meaning |
|------|---------|
| 0 | Success; asset written and verified; JSON result on stdout |
| 1 | Invalid / validation error |
| 2 | Auth / missing credentials |
| 3 | Backend API / network / polling failure |
| 4 | Post-write verification failed |
| 5 | Unsupported operation for this backend |

## Stdout JSON (one line)

**Success:**
```json
{"ok": true, "backend": "openai_images", "unit_id": "01-cover", "out": "/abs/...", "bytes": 184320, "model": "gpt-image-1", "request_id": null, "duration_ms": 12345, "dry_run": false}
```

**Failure:**
```json
{"ok": false, "backend": "openai_images", "unit_id": "01-cover", "error_code": 3, "error": "HTTP 429 rate limited", "retryable": true}
```

All progress / diagnostic text goes to **stderr**. Stdout's last line is always machine-parseable JSON.

## Hard requirements

1. `--out` must be absolute (`os.path.isabs`). If not, exit 1.
2. Create parent directory of `--out` if absent (`os.makedirs(..., exist_ok=True)`).
3. If `--out` already exists and is non-empty, **refuse overwrite** by default (exit 1) — the skill performs R4 backup before calling the adapter.
4. Read only allowed fields from spec; ignore unknown keys (forward-compat).
5. No interactive prompts inside adapters.
6. Never print env var values. Print only the var name when reporting missing ones.

## Shared library (`scripts/common/`)

| Module | Key exports |
|--------|------------|
| `paths.py` | `require_abs()`, `ensure_parent()`, `backup_with_timestamp()`, `refuse_overwrite()` |
| `verify.py` | `verify_nonempty(path, min_bytes=1)` |
| `secrets.py` | `redact(text)`, `assert_no_secrets(text)` |
| `envload.py` | `require_env(*names)`, `get_env(name, default)` |
| `result.py` | `success_json(...)`, `error_json(...)` |

## Adding a new backend

1. Create `scripts/adapters/{name}.py` implementing this contract.
2. Create `references/backends/{name}.md` documenting env vars, allowed params, cost/latency, failure modes.
3. Add the backend name to `BACKEND_MAP` in `scripts/pipeline_dry_run.py`.
4. Add a fixture spec and a dry-run test to `tests/test_adapter_cli_shape.py`.
No changes to `SKILL.md` required.
