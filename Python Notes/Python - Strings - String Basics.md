---
tags: [python, strings, basics]
moc: [[Python - Strings (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: how to create strings."
  - "Understand: single vs double quotes."
  - "Apply: use strings in programs."
---

# Python - Strings - String Basics

## Concept
Strings are text, created with single `'` or double `"` quotes. Triple quotes `'''` or `"""` allow multi-line.

## Example Code
```python
name = 'Alice'
message = "Hello, World!"
multiline = '''Line 1
Line 2
Line 3'''
```

## Exercises by Bloom Level
- Remember: Create a string.
- Understand: Why two quote styles?
- Apply: Use both styles in a program.
- Analyze: When use triple quotes?
- Create: Build a program with complex text.

## Common Errors with Example Code

1) Mismatched quotes → Opening and closing quotes must match

WRONG
name = 'Alice"  # SyntaxError: mismatched quotes

CORRECT
name = 'Alice'  # Both single
name = "Alice"  # Both double

2) Forgetting quotes around string → Variable or value treated as code, not string

WRONG
message = Hello World  # NameError: name 'Hello' is not defined

CORRECT
message = 'Hello World'  # Quotes make it a string
print(message)  # Hello World

3) Using wrong quote style for apostrophes → Quotes inside string conflict

WRONG
message = 'It's great'  # SyntaxError! The apostrophe breaks the string

CORRECT
# Use double quotes when string contains apostrophe:
message = "It's great"
print(message)  # It's great

# Or escape the quote:
message = 'It\'s great'
print(message)  # It's great

# Or use triple quotes for multi-line:
message = '''It's great
and awesome'''
print(message)

## Related Concepts
- [[Python - Strings - String Methods]]

## MOC
- Parent: [[Python - Strings (MOC)]]
