---
tags: [python, math, absolute, roots]
moc: [[Python - Practical Math (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: abs(), math.sqrt() functions."
  - "Understand: absolute value and square roots."
  - "Apply: use in distance and physics problems."
---

# Python - Math - Absolute Values & Roots

## Concept
**Absolute Value** (`abs()`) removes the minus sign. **Square Root** (`**0.5` or `math.sqrt()`) finds the root.

## Absolute Value

```python
print(abs(5))       # 5
print(abs(-5))      # 5
print(abs(-3.2))    # 3.2
```

## Real-World: Distance & Difference

**Height Difference:**
```python
your_height = 165  # cm
friend_height = 172
difference = your_height - friend_height
print(abs(difference))  # 7 (not -7)
```

**Temperature Change:**
```python
morning_temp = 12   # celsius
evening_temp = 8
change = evening_temp - morning_temp
print(f'Temp changed {abs(change)} degrees')  # 4 degrees
```

**Test Score Difference:**
```python
your_score = 78
target_score = 85
gap = your_score - target_score
print(f'You need {abs(gap)} more points')  # 7 points
```

## Square Roots

```python
import math

print(math.sqrt(16))    # 4.0
print(math.sqrt(25))    # 5.0
print(math.sqrt(2))     # 1.414...

# Or use power 0.5
print(16 ** 0.5)        # 4.0
```

## Real-World: Distance & Area

**Pythagorean Theorem (distance):**
```python
import math

# Two points: (3, 4) and (0, 0)
dx = 3  # horizontal distance
dy = 4  # vertical distance

distance = math.sqrt(dx**2 + dy**2)
print(distance)  # 5.0
```

**Side from Area:**
```python
import math

area = 64  # square area
side = math.sqrt(area)
print(side)  # 8.0
```

**Speed Calculation (velocity formula):**
```python
import math

# v = sqrt(2 * a * d)
acceleration = 9.8
distance = 50
velocity = math.sqrt(2 * acceleration * distance)
print(round(velocity, 2))  # 31.3 m/s
```

## Combining Abs & Roots

```python
import math

# Pythagorean with negative coordinates
x1, y1 = 3, 4
x2, y2 = -2, -5

dx = abs(x2 - x1)  # 5
dy = abs(y2 - y1)  # 9

distance = math.sqrt(dx**2 + dy**2)
print(distance)  # 10.3 (approx)
```

## Exercises by Bloom Level
- Remember: What's `abs(-10)`?
- Understand: Why use `abs()` for differences?
- Apply: Use `sqrt()` for distance.
- Analyze: Compare `abs(-5)` vs `(-5)**2`.
- Create: Build a distance calculator for points.

## Common Errors with Example Code

1) Forgetting to import math module → `math.sqrt()` not available without import

WRONG
result = math.sqrt(16)  # NameError: name 'math' is not defined

CORRECT
import math
result = math.sqrt(16)
print(result)  # 4.0

2) Taking square root of negative number → No real solution (causes error)

WRONG
import math
result = math.sqrt(-1)  # ValueError: math domain error

CORRECT
import math
number = -16
if number >= 0:
    result = math.sqrt(number)
else:
    print('Cannot take sqrt of negative')

3) Wrong exponent for square root → `16 ** 1/2` evaluates wrong (use `16 ** 0.5`)

WRONG
result = 16 ** 1/2  # = (16 ** 1) / 2 = 8 (wrong!)
print(result)  # 8

CORRECT
result = 16 ** 0.5  # = square root
print(result)  # 4.0

# Or use math.sqrt:
import math
result = math.sqrt(16)
print(result)  # 4.0

## Related Concepts
- [[Python - Math - Arithmetic Operators]]
- [[Python - Math - Geometry & Shapes]]
- [[Python - Math - Operator Precedence]]

## MOC
- Parent: [[Python - Practical Math (MOC)]]
