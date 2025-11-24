---
tags: [python, math, operators]
moc: [[Python - Practical Math (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: all arithmetic operators."
  - "Understand: what each operator does."
  - "Apply: use operators in calculations."
---

# Python - Math - Arithmetic Operators

## Concept
Python has operators: `+` (add), `-` (subtract), `*` (multiply), `/` (divide), `//` (floor divide), `%` (modulo), `**` (power).

## Basic Operators

```python
a = 10
b = 3

print(a + b)      # 13
print(a - b)      # 7
print(a * b)      # 30
print(a / b)      # 3.333...
print(a // b)     # 3 (floor)
print(a % b)      # 1 (remainder)
print(a ** b)     # 1000 (10 to power 3)
```

## Real-World Uses

**Division vs Floor Division:**
```python
# Regular division (decimal)
price = 20
split_by = 3
per_person = price / split_by  # 6.666...

# Floor division (whole)
cookies = 20
kids = 3
per_kid = cookies // kids      # 6
leftover = cookies % kids      # 2
```

**Exponent (Power):**
```python
# Square a number
side = 5
area = side ** 2               # 25

# Cube a number
side = 3
volume = side ** 3             # 27

# Square root (power 0.5)
import math
sqrt_16 = 16 ** 0.5            # 4.0
```

**Modulo (Remainder):**
```python
# Check if even
num = 8
if num % 2 == 0:
    print('Even')

# Check if divisible by 5
score = 25
if score % 5 == 0:
    print('Divisible by 5')
```

## Exercises by Bloom Level
- Remember: What does `//` do?
- Understand: When use `/` vs `//`?
- Apply: Use modulo to check divisibility.
- Analyze: Compare `**` vs repeated `*`.
- Create: Build calculations using multiple operators.

## Common Errors with Example Code

1) Division by zero (ZeroDivisionError)

WRONG
```python
result = 10 / 0  # ZeroDivisionError: division by zero
```

CORRECT
```python
divisor = 0
if divisor != 0:
    result = 10 / divisor
else:
    result = None
```

2) Confusing `/` (decimal) with `//` (floor division)

WRONG
```python
cookies = 7
kids = 2
per_kid = cookies / kids
print(per_kid)  # 3.5 (but you wanted whole cookies)
```

CORRECT
```python
cookies = 7
kids = 2
per_kid = cookies // kids   # 3 (whole cookies)
leftover = cookies % kids   # 1 (leftover)
```

3) Misunderstanding modulo (remainder, not division)

WRONG
```python
result = 10 % 3  # expecting 3 remainder 1
# but forgetting % gives only the remainder
print(result)  # 1 (just remainder)
```

CORRECT
```python
dividend = 10
divisor = 3
quotient = dividend // divisor  # 3
remainder = dividend % divisor  # 1
print(f'{dividend} ÷ {divisor} = {quotient} R {remainder}')
```

## Related Concepts
- [[Python - Math - Operator Precedence]]
- [[Python - Math - Calculator Basics]]

## MOC
- Parent: [[Python - Practical Math (MOC)]]
