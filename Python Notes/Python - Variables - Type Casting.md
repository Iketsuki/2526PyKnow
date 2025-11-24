---
tags: [python, variables, casting]
moc: [[Python - Variables & Types (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `int()`, `float()`, `str()` syntax."
  - "Understand: when and why to cast types."
  - "Apply: convert between types in programs."
---

# Python - Variables - Type Casting

## Concept
Type casting converts a value from one type to another. Common casts: `int()`, `float()`, `str()`.

## Example Code
```python
age_str = input('Age: ')      # Returns a string
age = int(age_str)            # Cast to int

price = 9.99
price_str = str(price)        # Cast to string

num = 42
decimal = float(num)          # Cast to float
```

## Exercises by Bloom Level
- Remember: Write `int('5')` and predict the result.
- Understand: Why do we cast `input()` to `int()`?
- Apply: Read two numbers and compute their sum.
- Analyze: What happens if you `int('hello')`?
- Create: Build a program that takes string input and does math.

## Common Errors
- Casting invalid strings (e.g., `int('3.5')` fails; use `float()` first).

## Related Concepts
- [[Python - Variables - Types Basics]]
- [[Python - IO - Input Basics]]

## MOC
- Parent: [[Python - Variables & Types (MOC)]]
