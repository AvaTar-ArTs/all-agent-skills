# Python <3.12 f-string Compatibility Fixes

## Problem: Nested f-strings with same quote character

Python 3.12+ allows reusing the same quote character in nested f-strings.
Python <3.12 does NOT. This pattern:

```python
content = f"""# Title
## Section
{f"""
### Subsection
Value: {name}
"""
}"""
```

Fails with `SyntaxError: f-string: expecting '}'` on Python <3.12.

## Fix: Extract inner f-string to a variable

```python
# BEFORE (broken on <3.12)
content = f"""# Title
## Section
{f"""
### Subsection
Value: {name}
"""
}"""

# AFTER (works everywhere)
_subsection = f"""
### Subsection
Value: {name}
"""

content = f"""# Title
## Section
{_subsection}
"""
```

## Conditional pattern

```python
# BEFORE (broken on <3.12)
content = f"""Header
{f"""API setup for {name}
export {name}_TOKEN="..."
""" if api_support else f"""Manual setup
No API available.
"""}
Footer"""

# AFTER (works everywhere)
setup_section = f"""API setup for {name}
export {name}_TOKEN="..."
""" if api_support else f"""Manual setup
No API available.
"""

content = f"""Header
{setup_section}
Footer"""
```

## Ruff detection

Ruff flags this as `invalid-syntax`:
```
invalid-syntax: Cannot reuse outer quote character in f-strings on Python 3.9
(syntax was added in Python 3.12)
```

This is NOT auto-fixable by ruff. Must be fixed manually.
