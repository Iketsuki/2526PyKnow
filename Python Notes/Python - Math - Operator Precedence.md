---
tags: [python, math, precedence]
moc: [[Python - Practical Math (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: order of operations (PEMDAS)."
  - "Understand: why precedence matters."
  - "Apply: write expressions with correct precedence."
---

# Python - Math - Operator Precedence

## Concept
Python follows PEMDAS: **P**arentheses, **E**xponents, **M**ultiply/**D**ivide (left-to-right), **A**dd/**S**ubtract (left-to-right).

## Why Precedence Matters

```python
# Without understanding precedence:
result1 = 2 + 3 * 4
print(result1)  # 14, not 20

# Multiply first (precedence), then add
# 3 * 4 = 12, then 2 + 12 = 14

# Use parentheses to override
result2 = (2 + 3) * 4
print(result2)  # 20
```

## Real-World Examples

**Money Calculation:**
```python
# Without parentheses (wrong precedence for intent)
price = 25
discount = 0.2  # 20% off
quantity = 3

total_wrong = price - discount * quantity  # 25 - 0.6 = 24.4
total_right = (price - discount * price) * quantity  # Apply discount first
print(total_right)

# Better: use clear formula
discount_amount = price * discount
discounted_price = price - discount_amount
total = discounted_price * quantity
print(total)
```

**Distance Calculation:**
```python
# Formula: distance = speed * time + acceleration * (time^2) / 2
speed = 30
time = 2
acceleration = 5

distance = speed * time + acceleration * (time ** 2) / 2
print(distance)  # 30*2 + 5*4/2 = 60 + 10 = 70

# Precedence: power first, then multiply/divide left-to-right, then add
```

**Grade Calculation:**
```python
# Average of 3 exams
exam1 = 85
exam2 = 90
exam3 = 78

# Wrong (forgotten parentheses)
average_wrong = exam1 + exam2 + exam3 / 3  # Divides only exam3
print(average_wrong)  # 85 + 90 + 26 = 201

# Right (parentheses)
average_right = (exam1 + exam2 + exam3) / 3
print(average_right)  # 253 / 3 = 84.33
```

## Order Reference
1. `**` (exponent)
2. `*`, `/`, `//`, `%` (multiply/divide, left-to-right)
3. `+`, `-` (add/subtract, left-to-right)

Parentheses override everything.

## Exercises by Bloom Level
- Remember: What's PEMDAS?
- Understand: Why is `2 + 3 * 4` = 14, not 20?
- Apply: Add parentheses to fix `5 + 3 * 2 - 1`.
- Analyze: Compare `2 ** 3 * 4` vs `2 ** (3 * 4)`.
- Create: Build a multi-step calculation (recipe, budget).

## Common Errors with Example Code

1) Forgetting parentheses for grouped operations (incorrect precedence)

WRONG
```python
# Calculate average of three numbers
result = 85 + 90 + 78 / 3
print(result)  # 201 (divides only 78, not sum)
```

CORRECT
```python
# Parentheses ensure sum first, then divide
result = (85 + 90 + 78) / 3
print(result)  # 84.333...
```

2) Assuming exponents are left-to-right (they're right-to-left)

WRONG
```python
result = 2 ** 3 ** 2
# If left-to-right: (2 ** 3) ** 2 = 8 ** 2 = 64
# But Python does: 2 ** (3 ** 2) = 2 ** 9 = 512
```

CORRECT
```python
result = 2 ** (3 ** 2)  # Explicit: 2 ** 9 = 512
print(result)  # 512

# Use parentheses to control evaluation order
result2 = (2 ** 3) ** 2  # 8 ** 2 = 64
print(result2)  # 64
```

3) Division chains are left-to-right (not intuitive)

WRONG
```python
result = 20 / 2 / 2
# This is: (20 / 2) / 2 = 10 / 2 = 5
# (not 20 / (2 / 2) = 20)
```

CORRECT
```python
# Be explicit for clarity
result = (20 / 2) / 2  # 5
print(result)

result2 = 20 / (2 / 2)  # 20 (different!)
print(result2)
```

## Related Concepts
- [[Python - Math - Arithmetic Operators]]
- [[Python - Math - Rounding & Precision]]
- [[Python - Math - Calculator Basics]]

## MOC
- Parent: [[Python - Practical Math (MOC)]]
