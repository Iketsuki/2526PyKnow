---
tags: [python, list-comprehension]
moc: [[Python Fundamentals (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: identify the bracket-based comprehension syntax."
  - "Understand: explain how comprehension maps input to output."
  - "Apply: write a comprehension to transform a list."
---

# Python - Control Flow - List Comprehensions

## Concept
List comprehensions are a compact way to create lists by embedding a for-loop and optional conditionals inside square brackets. They make code concise and often more readable for simple transformations.

## Learning Objectives
- Remember: recall the `[ expression for item in iterable if condition ]` form.
- Understand: explain that it's syntactic sugar for building lists from iterables.
- Apply: use list comprehensions to transform or filter lists in short, readable expressions.

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

## Exercises by Bloom Level
- Remember
  - Write the comprehension syntax from memory.
- Understand
  - In one sentence, explain the difference between a comprehension and a for-loop that appends to a list.
- Apply
  - Given a list of numbers, write a comprehension that returns the cubes of even numbers.
- Analyze
  - Rewrite a nested comprehension as nested loops and compare readability.
- Evaluate
  - Given two ways to filter and transform a list (comprehension vs filter+map), choose which is clearer and explain why.
- Create
  - Build a small function that takes a list of dicts and returns a filtered list using a comprehension.

## Use Case / Actionability
- Use comprehensions for short, clear transformations or filtering tasks.
- Prefer loops if you need multiple statements or side effects.

## Common Errors / Things to Remember
- Avoid heavy side effects inside comprehensions (e.g., file I/O or complex state mutations).
- For deeply nested comprehensions, consider intermediate variables for clarity.
- Generator expressions use `()` and are memory-efficient for large streams.

## Related Concepts
- [[Python - Generators]]  <!-- intentionally linked even if note doesn't exist yet -->
- [[Python - Lists - Tuple vs List vs Set]]

## MOC
- This note belongs in: [[Python Fundamentals (MOC)]]
- Beginner path: [[Python - Beginner Learning Path (MOC)]]
