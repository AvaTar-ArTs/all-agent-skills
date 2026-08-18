---
name: test-driven-development
description: "Use when implementing a feature or bug fix after planning, before writing implementation code. Enforce RED-GREEN-REFACTOR with tests first, then hand off to quality-regression-testing and verification-before-completion."
version: 2.0.0
author: Hermes Agent (adapted from obra/superpowers)
changelog:
  - "2.0.0 (2026-08-06): Appended advanced sections — Python ecosystem depth, agentic TDD, stack-specific patterns, property-based testing, mutation testing, CI integration"
  - "1.1.0: Original release"
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [testing, tdd, development, quality, red-green-refactor]
    related_skills: [systematic-debugging, writing-plans, subagent-driven-development, quality-regression-testing]
changelog:
  - "2026-08-15: Added explicit planning prerequisite and quality-verification handoff."
---

# Test-Driven Development (TDD)

## Overview

Write the test first. Watch it fail. Write minimal code to pass.

**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing.

**Violating the letter of the rules is violating the spirit of the rules.**

## When to Use

**Always:**
- New features
- Bug fixes
- Refactoring
- Behavior changes

**Exceptions (ask the user first):**
- Throwaway prototypes
- Generated code
- Configuration files

Thinking "skip TDD just this once"? Stop. That's rationalization.

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete

Implement fresh from tests. Period.

## Red-Green-Refactor Cycle

### RED — Write Failing Test

Write one minimal test showing what should happen.

**Good test:**
```python
def test_retries_failed_operations_3_times():
    attempts = 0
    def operation():
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise Exception('fail')
        return 'success'

    result = retry_operation(operation)

    assert result == 'success'
    assert attempts == 3
```
Clear name, tests real behavior, one thing.

**Bad test:**
```python
def test_retry_works():
    mock = MagicMock()
    mock.side_effect = [Exception(), Exception(), 'success']
    result = retry_operation(mock)
    assert result == 'success'  # What about retry count? Timing?
```
Vague name, tests mock not real code.

**Requirements:**
- One behavior per test
- Clear descriptive name ("and" in name? Split it)
- Real code, not mocks (unless truly unavoidable)
- Name describes behavior, not implementation

### Verify RED — Watch It Fail

**MANDATORY. Never skip.**

```bash
# Use terminal tool to run the specific test
pytest tests/test_feature.py::test_specific_behavior -v
```

Confirm:
- Test fails (not errors from typos)
- Failure message is expected
- Fails because the feature is missing

**Test passes immediately?** You're testing existing behavior. Fix the test.

**Test errors?** Fix the error, re-run until it fails correctly.

### GREEN — Minimal Code

Write the simplest code to pass the test. Nothing more.

**Good:**
```python
def add(a, b):
    return a + b  # Nothing extra
```

**Bad:**
```python
def add(a, b):
    result = a + b
    logging.info(f"Adding {a} + {b} = {result}")  # Extra!
    return result
```

Don't add features, refactor other code, or "improve" beyond the test.

**Cheating is OK in GREEN:**
- Hardcode return values
- Copy-paste
- Duplicate code
- Skip edge cases

We'll fix it in REFACTOR.

### Verify GREEN — Watch It Pass

**MANDATORY.**

```bash
# Run the specific test
pytest tests/test_feature.py::test_specific_behavior -v

# Then run ALL tests to check for regressions
pytest tests/ -q
```

Confirm:
- Test passes
- Other tests still pass
- Output pristine (no errors, warnings)

**Test fails?** Fix the code, not the test.

**Other tests fail?** Fix regressions now.

### REFACTOR — Clean Up

After green only:
- Remove duplication
- Improve names
- Extract helpers
- Simplify expressions

Keep tests green throughout. Don't add behavior.

**If tests fail during refactor:** Undo immediately. Take smaller steps.

### Repeat

Next failing test for next behavior. One cycle at a time.

## Why Order Matters

**"I'll write tests after to verify it works"**

Tests written after code pass immediately. Passing immediately proves nothing:
- Might test the wrong thing
- Might test implementation, not behavior
- Might miss edge cases you forgot
- You never saw it catch the bug

Test-first forces you to see the test fail, proving it actually tests something.

**"I already manually tested all the edge cases"**

Manual testing is ad-hoc. You think you tested everything but:
- No record of what you tested
- Can't re-run when code changes
- Easy to forget cases under pressure
- "It worked when I tried it" ≠ comprehensive

Automated tests are systematic. They run the same way every time.

**"Deleting X hours of work is wasteful"**

Sunk cost fallacy. The time is already gone. Your choice now:
- Delete and rewrite with TDD (high confidence)
- Keep it and add tests after (low confidence, likely bugs)

The "waste" is keeping code you can't trust.

**"TDD is dogmatic, being pragmatic means adapting"**

TDD IS pragmatic:
- Finds bugs before commit (faster than debugging after)
- Prevents regressions (tests catch breaks immediately)
- Documents behavior (tests show how to use code)
- Enables refactoring (change freely, tests catch breaks)

"Pragmatic" shortcuts = debugging in production = slower.

**"Tests after achieve the same goals — it's spirit not ritual"**

No. Tests-after answer "What does this do?" Tests-first answer "What should this do?"

Tests-after are biased by your implementation. You test what you built, not what's required. Tests-first force edge case discovery before implementing.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Tests after achieve same goals" | Tests-after = "what does this do?" Tests-first = "what should this do?" |
| "Already manually tested" | Ad-hoc ≠ systematic. No record, can't re-run. |
| "Deleting X hours is wasteful" | Sunk cost fallacy. Keeping unverified code is technical debt. |
| "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. |
| "Need to explore first" | Fine. Throw away exploration, start with TDD. |
| "Test hard = design unclear" | Listen to the test. Hard to test = hard to use. |
| "TDD will slow me down" | TDD faster than debugging. Pragmatic = test-first. |
| "Manual test faster" | Manual doesn't prove edge cases. You'll re-test every change. |
| "Existing code has no tests" | You're improving it. Add tests for the code you touch. |

## Red Flags — STOP and Start Over

If you catch yourself doing any of these, delete the code and restart with TDD:

- Code before test
- Test after implementation
- Test passes immediately on first run
- Can't explain why test failed
- Tests added "later"
- Rationalizing "just this once"
- "I already manually tested it"
- "Tests after achieve the same purpose"
- "Keep as reference" or "adapt existing code"
- "Already spent X hours, deleting is wasteful"
- "TDD is dogmatic, I'm being pragmatic"
- "This is different because..."

**All of these mean: Delete code. Start over with TDD.**

## Verification Checklist

Before marking work complete:

- [ ] Every new function/method has a test
- [ ] Watched each test fail before implementing
- [ ] Each test failed for expected reason (feature missing, not typo)
- [ ] Wrote minimal code to pass each test
- [ ] All tests pass
- [ ] Output pristine (no errors, warnings)
- [ ] Tests use real code (mocks only if unavoidable)
- [ ] Edge cases and errors covered

Can't check all boxes? You skipped TDD. Start over.

## When Stuck

| Problem | Solution |
|---------|----------|
| Don't know how to test | Write the wished-for API. Write the assertion first. Ask the user. |
| Test too complicated | Design too complicated. Simplify the interface. |
| Must mock everything | Code too coupled. Use dependency injection. |
| Test setup huge | Extract helpers. Still complex? Simplify the design. |

## Hermes Agent Integration

### Running Tests

Use the `terminal` tool to run tests at each step:

```python
# RED — verify failure
terminal("pytest tests/test_feature.py::test_name -v")

# GREEN — verify pass
terminal("pytest tests/test_feature.py::test_name -v")

# Full suite — verify no regressions
terminal("pytest tests/ -q")
```

### With delegate_task

When dispatching subagents for implementation, enforce TDD in the goal:

```python
delegate_task(
    goal="Implement [feature] using strict TDD",
    context="""
    Follow test-driven-development skill:
    1. Write failing test FIRST
    2. Run test to verify it fails
    3. Write minimal code to pass
    4. Run test to verify it passes
    5. Refactor if needed
    6. Commit

    Project test command: pytest tests/ -q
    Project structure: [describe relevant files]
    """,
    toolsets=['terminal', 'file']
)
```

### With systematic-debugging

Bug found? Write failing test reproducing it. Follow TDD cycle. The test proves the fix and prevents regression.

Never fix bugs without a test.

## Testing Anti-Patterns

- **Testing mock behavior instead of real behavior** — mocks should verify interactions, not replace the system under test
- **Testing implementation details** — test behavior/results, not internal method calls
- **Happy path only** — always test edge cases, errors, and boundaries
- **Brittle tests** — tests should verify behavior, not structure; refactoring shouldn't break them

## Final Rule

```
Production code → test exists and failed first
Otherwise → not TDD
```

No exceptions without the user's explicit permission.

---

# Advanced Patterns (v2.0)

> The following sections extend the base skill with ecosystem-specific patterns. The Iron Law and RED-GREEN-REFACTOR cycle above remain unchanged and non-negotiable. These sections answer *how* to apply TDD to specific technical contexts.

## Python Ecosystem — Advanced pytest

### Fixtures and Scope

```python
# conftest.py — session-scoped fixtures for expensive setup
@pytest.fixture(scope="session")
def tmp_music_dir(tmp_path_factory):
    d = tmp_path_factory.mktemp("music")
    shutil.copy("tests/fixtures/sample.mp3", d / "sample.mp3")
    return d

@pytest.fixture
def in_memory_db():
    """Fresh SQLite DB per test — never touches real databases."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE tracks (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, tags TEXT)")
    yield conn
    conn.close()

@pytest.fixture(autouse=True)
def isolate_filesystem(tmp_path, monkeypatch):
    """Redirect all writes to tmp_path for every test automatically."""
    monkeypatch.chdir(tmp_path)
    return tmp_path
```

### Parametrize to Eliminate Redundant Tests

```python
# WRONG — three nearly identical test bodies
def test_normalize_mp3(): ...
def test_normalize_wav(): ...
def test_normalize_with_numbers(): ...

# RIGHT — one parametrized test
@pytest.mark.parametrize("input_name,expected", [
    ("My Song (feat. Artist).mp3", "my-song-feat-artist.mp3"),
    ("Track 01 - Title.mp3", "track-01-title.mp3"),
    ("LOUD CAPS.mp3", "loud-caps.mp3"),
    ("song with   spaces.mp3", "song-with-spaces.mp3"),
])
def test_normalize_filename(input_name, expected):
    assert normalize(input_name) == expected
```

### Markers for Selective Runs

```python
# conftest.py
def pytest_configure(config):
    config.addinivalue_line("markers", "slow: marks tests as slow (>500ms)")
    config.addinivalue_line("markers", "integration: marks tests that use real I/O or external tools")
    config.addinivalue_line("markers", "audio: marks tests that require audio fixture files")
```

```bash
# Fast loop — unit tests only
pytest -m "not slow and not integration and not audio"
# Full suite
pytest
```

---

## Stack-Specific Patterns

### SQLite Catalog Testing

Never test against production databases (`shared.sqlite`, real music catalogs). Always use `:memory:`.

```python
def test_search_by_genre_returns_only_matching(in_memory_db):
    insert_track(in_memory_db, title="A", genre="Industrial")
    insert_track(in_memory_db, title="B", genre="Folk")
    results = search_by_genre(in_memory_db, "Industrial")
    assert len(results) == 1
    assert results[0]["title"] == "A"
```

### ffmpeg Wrapper Testing

Test command construction separately from subprocess invocation. Gate real ffmpeg calls behind `@pytest.mark.integration`.

```python
# Test command construction (pure function, no subprocess)
def test_build_ffmpeg_command_for_wav_conversion():
    cmd = build_ffmpeg_command(input_path=Path("in.mp3"), output_path=Path("out.wav"), overwrite=True)
    assert cmd == ["ffmpeg", "-y", "-i", "in.mp3", "out.wav"]

# Test subprocess is called (mock the call)
def test_convert_calls_subprocess(mocker):
    mock_run = mocker.patch("subprocess.run", return_value=MagicMock(returncode=0))
    convert_mp3_to_wav(Path("in.mp3"), Path("out.wav"))
    mock_run.assert_called_once()

# Real conversion — only runs where ffmpeg is installed
@pytest.mark.integration
@pytest.mark.skipif(shutil.which("ffmpeg") is None, reason="ffmpeg not installed")
def test_real_conversion_produces_output_file(tmp_path, sample_mp3):
    output = tmp_path / "output.wav"
    convert_mp3_to_wav(sample_mp3, output)
    assert output.exists() and output.stat().st_size > 0
```

### Batch Processor Testing

```python
def test_batch_converts_all_mp3_in_directory(tmp_path):
    for name in ["track_01.mp3", "track_02.mp3"]:
        (tmp_path / name).write_bytes(b"fake-mp3-data")
    result = batch_convert(input_dir=tmp_path, output_format="wav")
    assert result.processed == 2 and result.failed == 0

def test_batch_reports_failures_without_stopping(tmp_path):
    (tmp_path / "good.mp3").write_bytes(b"valid")
    (tmp_path / "corrupt.mp3").write_bytes(b"")
    result = batch_convert(input_dir=tmp_path, output_format="wav")
    assert result.processed == 1 and result.failed == 1
```

### Static Site Generation Testing

```python
def test_generate_track_page_includes_schema_org(tmp_path, sample_track_metadata):
    generate_track_page(metadata=sample_track_metadata, output_path=tmp_path / "track.html")
    html = (tmp_path / "track.html").read_text()
    assert sample_track_metadata["title"] in html
    assert '"@type": "MusicRecording"' in html
```

---

## Agentic TDD — Testing AI Workflow Outputs

### Test Prompt Construction, Not AI Responses

```python
def test_build_seo_prompt_includes_required_fields(sample_track_metadata):
    prompt = build_seo_description_prompt(metadata=sample_track_metadata)
    assert sample_track_metadata["title"] in prompt
    assert sample_track_metadata["genre"] in prompt
    assert len(prompt) < 4000  # within token budget
```

### Validate Output Shape, Not Content

```python
def test_ai_metadata_response_conforms_to_schema(mocker):
    mocker.patch("openai.chat.completions.create", return_value=MagicMock(
        choices=[MagicMock(message=MagicMock(content='{"title": "...", "tags": ["punk"], "description": "..."}'))]
    ))
    result = generate_track_metadata(lyrics="...", genre="Industrial Punk")
    assert isinstance(result["title"], str)
    assert isinstance(result["tags"], list) and len(result["tags"]) > 0
    assert isinstance(result["description"], str) and len(result["description"]) >= 10
    # NEVER: assert result["tags"] == ["punk", "industrial"]

def test_ai_response_parser_handles_malformed_json_gracefully():
    result = parse_ai_response("Not JSON at all.")
    assert result is not None  # fallback, not raise
    assert "title" in result
```

### Enforce TDD in Subagent Instructions

When dispatching via `subagent-driven-development`:

```python
delegate_task(
    goal="Implement track metadata normalizer using strict TDD",
    context="""
    Follow test-driven-development skill exactly:
    1. Write failing test FIRST — pytest tests/test_normalizer.py -v → confirm RED
    2. Write minimal code in src/normalizer.py
    3. pytest tests/test_normalizer.py -v → confirm GREEN
    4. pytest tests/ -q → confirm no regressions
    Do NOT write src/ code before step 1 confirms RED.
    """
)
```

---

## Property-Based Testing (Hypothesis)

Install: `pip install hypothesis`

Use when testing transformation functions. Hypothesis generates hundreds of random inputs automatically.

```python
from hypothesis import given, strategies as st

@given(st.text(min_size=1, max_size=200))
def test_normalize_filename_never_raises(filename):
    result = normalize(filename)
    assert isinstance(result, str)

@given(st.text(min_size=1, max_size=200))
def test_normalize_filename_is_idempotent(filename):
    assert normalize(normalize(filename)) == normalize(filename)

@given(st.integers(min_value=0, max_value=500_000))
def test_format_duration_handles_any_seconds(seconds):
    result = format_duration(seconds)
    assert isinstance(result, str) and ":" in result
```

**When to use Hypothesis:**
- Any normalization, parsing, or transformation function
- Any function where invariants should hold for all inputs
- Any function processing user-controlled strings

---

## Mutation Testing (mutmut)

Install: `pip install mutmut`

Mutation testing modifies your source code in small ways and checks whether your tests catch the change. If tests pass after a mutation, you have a coverage gap.

```bash
# Run mutations on a specific module
mutmut run --paths-to-mutate src/catalog.py --tests-dir tests/
# Show results
mutmut results
# Show surviving mutations (the gaps)
mutmut show [id]
```

**Common surviving mutations and what they mean:**
- Changed `==` to `!=` → you're not asserting on the result
- Removed `failed += 1` → you're not asserting on error count
- Changed `>` to `>=` → missing boundary condition test

---

## Pre-commit and CI Integration

### pyproject.toml

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = ["--tb=short", "--strict-markers", "-q"]
markers = [
    "slow: marks tests as slow",
    "integration: marks tests that use real I/O or external tools",
    "audio: marks tests requiring audio fixtures",
]

[tool.coverage.run]
source = ["src"]
branch = true

[tool.coverage.report]
fail_under = 80
show_missing = true
```

### Pre-commit hook

```yaml
repos:
  - repo: local
    hooks:
      - id: pytest-unit
        name: pytest (unit only)
        entry: pytest -m "not slow and not integration and not audio" -q
        language: system
        pass_filenames: false
        always_run: true
```

---

## v2.0 Verification Checklist

This superset checklist includes all v1.1 checks plus advanced additions:

- [ ] Every new function/method has a test (v1.1)
- [ ] Watched each test fail before implementing (v1.1)
- [ ] Each test failed for expected reason — missing feature, not typo (v1.1)
- [ ] Wrote minimal code to pass each test (v1.1)
- [ ] All tests pass (v1.1)
- [ ] Output pristine — no errors, warnings (v1.1)
- [ ] Tests use real code; mocks only where unavoidable (v1.1)
- [ ] Edge cases and errors covered (v1.1)
- [ ] Repeated test bodies replaced with `@pytest.mark.parametrize` (v2.0)
- [ ] Database tests use `:memory:` — never real catalog files (v2.0)
- [ ] External process tests (ffmpeg, CLI) split into command-construction + subprocess tests (v2.0)
- [ ] Transformation functions covered by at least one `@given` Hypothesis test (v2.0)
- [ ] AI output tests assert on shape/schema, not specific content (v2.0)
- [ ] Slow/integration tests marked and excluded from fast loop (v2.0)
- [ ] `coverage` threshold defined in `pyproject.toml` (v2.0)
