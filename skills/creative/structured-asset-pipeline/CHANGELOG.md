# Changelog

## 2026-07-08

### Fixed

- Restored `SKILL.md` from a zero-byte file to a valid skill document.
- Added YAML frontmatter delimited by `---` with `name`, `description`, `version`, `license`, and `metadata`.
- Added a concise progressive-disclosure body with workflow, options, hard rules, adapter pattern, references, and pitfalls.

### Verified

- Confirmed `SKILL.md` frontmatter delimiters are present on lines 1 and 8.
- Confirmed `SKILL.md` is 119 lines, under the 500-line target from the build spec.
- Ran `python -m pytest tests/test_paths.py -q` from the installed skill root: 5 passed.

### Notes

- Pytest emitted cache-write warnings for `.pytest_cache` because the sandbox could not write cache files in the installed skill directory. The tested behavior passed.
