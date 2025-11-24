---
tags: [python, math, modulo]
moc: [[Python - Practical Math (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: modulo operator syntax."
  - "Understand: what remainder means."
  - "Apply: use for divisibility checks."
---

# Python - Math - Modulo & Divisibility

## Concept
**Modulo** (`%`) gives the remainder after division. `a % b` = remainder when `a` divided by `b`.

## Basic Modulo

```python
print(10 % 3)   # 1 (10 / 3 = 3 remainder 1)
print(20 % 5)   # 0 (20 / 5 = 4 remainder 0)
print(7 % 2)    # 1 (7 / 2 = 3 remainder 1)
print(8 % 3)    # 2 (8 / 3 = 2 remainder 2)
```

## Real-World: Divisibility Checks

**Even or Odd:**
```python
num = 15
if num % 2 == 0:
    print('Even')
else:
    print('Odd')  # Prints this
```

**Divisible by 5:**
```python
score = 125
if score % 5 == 0:
    print('Divisible by 5')
```

**Divisible by 3:**
```python
students = 28
if students % 3 == 0:
    print('Perfect groups of 3')
else:
    leftover = students % 3
    print(f'{leftover} students left over')  # 1 student
```

## Real-World: Distribution with Remainder

**Cookies to Kids:**
```python
cookies = 23
kids = 4

per_kid = cookies // 4  # 5 per kid
leftover = cookies % 4  # 3 left

print(f'Each kid gets {per_kid} cookies')
print(f'{leftover} cookies left')
```

**Money Distribution:**
```python
total_money = 500
people = 3

per_person = total_money // people  # 166
remainder = total_money % people    # 2

print(f'Each gets ${per_person}')
print(f'${remainder} unspent')
```

**Hours to Minutes:**
```python
total_seconds = 3661

hours = total_seconds // 3600
leftover = total_seconds % 3600

minutes = leftover // 60
seconds = leftover % 60

print(f'{hours}h {minutes}m {seconds}s')  # 1h 1m 1s
```

## Combining Modulo & Conditions

**Day of Week (cycling):**
```python
day_number = 10
days_in_week = 7

position_in_week = day_number % days_in_week
print(position_in_week)  # 3 (Wednesday if counting from 0)
```

**Every nth Item:**
```python
# Print every 5th number
for i in range(1, 26):
    if i % 5 == 0:
        print(i, end=' ')  # 5 10 15 20 25
```

**Leap Year Check:**
```python
year = 2024

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('Leap year')
else:
    print('Not leap year')
```

## Exercises by Bloom Level
- Remember: What's `17 % 5`?
- Understand: Why is `20 % 5 == 0`?
- Apply: Use modulo to check if divisible by 3.
- Analyze: Why use `% 10` to get last digit?
- Create: Build a score checker (multiples of 10).

## Common Errors with Example Code

1) Confusing `/` and `%` operators → Division vs remainder (very different!)

WRONG
print(7 / 2)   # 3.5 (division - returns decimal)
print(7 % 2)   # 1 (modulo - returns remainder)
# Easy to mix these up!

CORRECT
# Use `/` for division:
quotient = 7 / 2  # 3.5
print(quotient)

# Use `%` for remainder:
remainder = 7 % 2  # 1
print(remainder)

2) Modulo with zero → Causes ZeroDivisionError (can't divide by 0)

WRONG
result = 10 % 0  # ZeroDivisionError: integer division or modulo by zero

CORRECT
divisor = 0
if divisor != 0:
    result = 10 % divisor
else:
    print('Cannot divide by 0')

3) Negative modulo behavior → Python rounds down (result can be surprising)

WRONG
# Easy to expect -7 % 3 = -1, but:
result = (-7) % 3
print(result)  # 2 (not -1!) - Python rounds toward negative infinity

CORRECT
# Understand Python's modulo:
print(7 % 3)    # 1
print((-7) % 3) # 2 (rounds down)
print(7 % (-3)) # -2 (rounds down)

# For absolute difference:
a, b = -7, 3
remainder = abs(a) % abs(b)
print(remainder)  # 1

## Related Concepts
- [[Python - Math - Arithmetic Operators]]
- [[Python - Math - Operator Precedence]]
- [[Python - Conditionals - If-Else Basics]]

## MOC
- Parent: [[Python - Practical Math (MOC)]]
