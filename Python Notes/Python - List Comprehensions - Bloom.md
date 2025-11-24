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

## Common Errors with Example Code

1) Heavy side effects inside comprehension → Can cause unexpected None values (use loops instead)

WRONG
# Trying to modify state inside comprehension (confusing):
results = []
values = [x for x in range(5) if results.append(x) is None]
# This works but is unreadable and bad practice

CORRECT
# Use a loop for operations with side effects:
results = []
for x in range(5):
    results.append(x)

2) Deeply nested comprehensions → Hard to read (break into steps)

WRONG
# Complex nested comprehension:
matrix = [[j for j in range(3)] for i in range(3)]
# Hard to understand at a glance

CORRECT
# Make it clearer with intermediate variables:
row = [j for j in range(3)]
matrix = [row for i in range(3)]

# Or explicit loop:
matrix = []
for i in range(3):
    matrix.append([j for j in range(3)])

3) Confusing generator expressions `()` with list comprehensions `[]` → Different behavior

WRONG
numbers = (x**2 for x in range(100))  # Generator
print(numbers[0])  # TypeError: 'generator' is not subscriptable

CORRECT
numbers = [x**2 for x in range(100)]  # List
print(numbers[0])  # 0 (direct access works)

# Use generators for memory efficiency with large data
generator = (x**2 for x in range(1000000))  # Doesn't compute all upfront
first_value = next(generator)  # 0

## Related Concepts
- [[Python - Generators]]  <!-- intentionally linked even if note doesn't exist yet -->
- [[Python - Lists - Tuple vs List vs Set]]

## MOC
- This note belongs in: [[Python Fundamentals (MOC)]]
- Beginner path: [[Python - Beginner Learning Path (MOC)]]
