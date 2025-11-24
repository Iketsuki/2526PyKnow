---
tags: [python, io, input-types]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: input always returns strings."
  - "Understand: how to convert input to different types."
  - "Apply: read numbers, floats, and booleans correctly."
---

# Python - IO - Input Types (Strings vs Numbers vs Lists)

## Concept
`input()` always returns a **string**. To use it as a number, use `int()`, `float()`, or parse it. For multiple values, use `.split()`.

## Reading Different Types

**Read a single integer:**
```python
age = int(input('Age: '))
print(f'Next year you will be {age + 1}')
```

**Read a decimal (float):**
```python
height = float(input('Height (meters): '))
print(f'Height in cm: {height * 100}')
```

**Read multiple values from one line:**
```python
# User enters: "Alice 25 90.5"
name, age_str, score_str = input('Enter name age score: ').split()
age = int(age_str)
score = float(score_str)
```

**Read a list of numbers:**
```python
# User enters: "1 2 3 4 5"
numbers = list(map(int, input('Enter numbers: ').split()))
print(f'Sum: {sum(numbers)}')
```

**Read yes/no as boolean:**
```python
response = input('Continue? (yes/no): ').lower()
is_yes = response in ['yes', 'y']
print(is_yes)  # True or False
```

## Exercises by Bloom Level
- Remember: How to read an integer with `input()`?
- Understand: Why does `input()` return a string?
- Apply: Read a number and use it in math.
- Analyze: What's the difference between `int('5')` and `'5'`?
- Create: Read multiple inputs and process them.

## Common Errors
- Forgetting to convert before math: `int(input()) + 5` works; `input() + 5` fails.
- Not handling `.split()` correctly for multiple values.

## Related Concepts
- [[Python - Variables - Type Casting]]
- [[Python - IO - Input Basics]]
- [[Python - Strings - String Methods]]

## MOC
- Parent: [[Python - IO (MOC)]]
