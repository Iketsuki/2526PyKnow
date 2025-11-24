---
tags: [python, functions, return]
moc: [[Python - Functions (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `return` syntax."
  - "Understand: functions send back values."
  - "Apply: use return values in code."
---

# Python - Functions - Return Values

## Concept
Use `return` to send a value back from a function. Functions without explicit returns return `None`.

## Example Code
```python
def square(x):
    return x * x

result = square(5)
print(result)           # 25
```

## Exercises by Bloom Level
- Remember: Write a function that returns a value.
- Understand: What happens if you don't return?
- Apply: Build a function that returns a computed value.
- Analyze: Compare functions with/without returns.
- Create: Chain function calls together.

## Common Errors
- `print()` inside a function doesn't return; use `return`.

## Related Concepts
- [[Python - Functions - Definition Basics]]

## MOC
- Parent: [[Python - Functions (MOC)]]
