---
tags: [python, list-comprehension]
moc: [[Python Fundamentals (MOC)]]
---

# Python - Control Flow - List Comprehensions

## Concept
List comprehensions are a compact way to create lists by embedding a for-loop and optional conditionals inside square brackets. They make code concise and often more readable for simple transformations.

## Syntax
```python
[ expression for item in iterable if condition ]
```

## Example Code
```python
# Example: square numbers from 0 to 9
squares = [x*x for x in range(10)]
print(squares)

# With a condition: only even squares
even_squares = [x*x for x in range(10) if x % 2 == 0]
print(even_squares)
```

## Use Case / Actionability
- Use for simple transformations or filtering when building lists.
- Prefer explicit loops for complex logic or when multiple statements are required.

## Common Errors / Things to Remember
- Avoid putting heavy side effects in a comprehension; prefer loops if needed.
- For nested comprehensions, prefer intermediate variables for readability.
- Don't confuse generator expressions (use parentheses) with list comprehensions (brackets).

## Related Concepts
- [[Python - Generators]]  <!-- intentionally linked even if note doesn't exist yet -->
- [[Python - Lists - Tuple vs List vs Set]]

## MOC
- This note belongs in: [[Python Fundamentals (MOC)]]
