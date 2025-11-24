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

## Common Errors with Example Code

1) Heavy side effects inside comprehension → Can cause bugs (use loops instead)

WRONG
# Trying to print inside comprehension:
results = [print(x) for x in range(5)]
# Prints 0 1 2 3 4, but results = [None, None, None, None, None]

CORRECT
# Use a loop for side effects:
for x in range(5):
    print(x)

2) Deeply nested comprehensions → Reduces readability (use intermediate variables)

WRONG
# Hard to read nested comprehension:
result = [[y*2 for y in range(3)] for x in range(3)]

CORRECT
# Break into steps for clarity:
inner = [y*2 for y in range(3)]
result = [inner for x in range(3)]
# Or use a loop:
result = []
for x in range(3):
    result.append([y*2 for y in range(3)])

3) Confusing generator expressions with list comprehensions → Different syntax, different behavior

WRONG
# Parentheses make it a generator (memory-efficient but not a list):
numbers = (x**2 for x in range(1000000))
print(numbers[0])  # TypeError: 'generator' object is not subscriptable

CORRECT
# Brackets make it a list:
numbers = [x**2 for x in range(10)]
print(numbers[0])  # 0

# Generators are useful for large data:
large_generator = (x**2 for x in range(1000000))  # Memory-efficient
first = next(large_generator)  # Get one value

## Related Concepts
- [[Python - Generators]]  <!-- intentionally linked even if note doesn't exist yet -->
- [[Python - Lists - Tuple vs List vs Set]]

## MOC
- This note belongs in: [[Python Fundamentals (MOC)]]
