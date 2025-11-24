---
tags: [python, math, rounding]
moc: [[Python - Practical Math (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: rounding function syntax."
  - "Understand: why decimal precision matters."
  - "Apply: use round() and formatting."
---

# Python - Math - Rounding & Precision

## Concept
**Rounding** shortens decimals. **Precision** means decimal places. Use `round(value, places)` to round, or formatting to display.

## Basic Rounding

```python
# round(value, decimal_places)
price = 19.567
print(round(price, 2))  # 19.57
print(round(price, 1))  # 19.6
print(round(price, 0))  # 20

# No argument = round to integer
print(round(3.7))       # 4
print(round(3.2))       # 3
```

## Real-World Examples

**Money (always 2 decimals):**
```python
# Bill split
total = 47.83
people = 3
per_person = total / people
print(per_person)           # 15.943333...
print(round(per_person, 2)) # 15.94

# Price after discount
original = 29.99
discount_percent = 0.15
discounted = original - (original * discount_percent)
print(round(discounted, 2))  # 25.49
```

**Test Scores (0 decimals):**
```python
# Average of exams
scores = [88.5, 91.2, 78.8, 85.3]
average = sum(scores) / len(scores)
print(round(average))  # 86
```

**Geometry (1-2 decimals):**
```python
import math
radius = 5
area = math.pi * (radius ** 2)
print(area)              # 78.53981...
print(round(area, 2))    # 78.54
```

## Formatting (Display Without Changing Value)

```python
value = 3.14159

# Show only 2 decimals
print(f'{value:.2f}')   # 3.14

# Show only 1 decimal
print(f'{value:.1f}')   # 3.1

# Show 3 decimals
print(f'{value:.3f}')   # 3.142
```

**Difference: `round()` changes value, formatting just displays:**
```python
price = 19.567
rounded = round(price, 2)  # Now 19.57 in memory
formatted = f'{price:.2f}' # Shows 19.57, but price is still 19.567

print(rounded)    # 19.57
print(price)      # 19.567
```

## Common Issues

**Banker's Rounding (Python 3):**
```python
print(round(2.5))   # 2 (rounds to even)
print(round(3.5))   # 4 (rounds to even)
```

**Floating Point Errors:**
```python
print(0.1 + 0.2)                # 0.30000000000000004
print(round(0.1 + 0.2, 1))      # 0.3 (fixes it)
print(f'{0.1 + 0.2:.1f}')       # 0.3
```

## Common Errors with Example Code

### Error 1: Forgetting that round() returns a number, not a string
```python
# WRONG: Expecting round() to return a string for display
price = 19.567
result = round(price, 2)
print(type(result))  # <class 'float'>

# If you try to do string operations:
# print(result.upper())  # AttributeError: 'float' has no attribute 'upper'

# CORRECT: Use formatting if you need a string
formatted = f'{price:.2f}'
print(type(formatted))  # <class 'str'>
print(formatted)  # '19.57'
```

### Error 2: Using round() instead of formatting for display
```python
# WRONG: Modifying the actual value when you just want display
price = 19.567
price = round(price, 2)  # Now price is 19.57 (actual value changed)

# CORRECT: Use formatting to display without changing value
price = 19.567
print(f'{price:.2f}')  # Display as 19.57, but price is still 19.567

# Use round() only when you actually need the rounded value
tax = price * 0.08
tax = round(tax, 2)  # Now tax is rounded (you need the actual value)
print(tax)
```

### Error 3: Banking rounding confusion
```python
# WRONG: Assuming round(2.5) = 3
print(round(2.5))  # 2 (rounds to nearest EVEN number!)
print(round(3.5))  # 4

# This is Python 3's banker's rounding (rounds to nearest even)

# CORRECT: Use Decimal for precise rounding if needed
from decimal import Decimal, ROUND_HALF_UP

price = Decimal('2.5')
rounded = price.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
print(rounded)  # 3 (traditional rounding)
```

### Error 4: Floating point precision errors
```python
# WRONG: Comparing floats without rounding
balance = 0.1 + 0.2
print(balance)  # 0.30000000000000004

if balance == 0.3:
    print('Equal')  # Doesn't print! (due to floating point error)

# CORRECT: Round before comparing
balance = round(0.1 + 0.2, 1)
if balance == 0.3:
    print('Equal')  # Prints!

# OR: Use Decimal for financial calculations
from decimal import Decimal
balance = Decimal('0.1') + Decimal('0.2')
print(balance)  # 0.3 (exact)
```

### Error 5: Rounding negative numbers incorrectly
```python
# WRONG: Forgetting how round() works with negatives
print(round(-2.5))  # -2 (rounds to nearest even)
print(round(-3.5))  # -4 (rounds to nearest even)

# CORRECT: Remember banker's rounding applies to negatives too
print(round(-2.5))  # -2 (to nearest even)
print(round(-3.5))  # -4 (to nearest even)

# For consistent rounding:
from decimal import Decimal, ROUND_HALF_UP
value = Decimal('-2.5')
rounded = value.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
print(rounded)  # -3 (traditional rounding)
```

## Exercises by Bloom Level

- **Remember**: What does `round(3.7, 1)` return?
- **Understand**: Why format money to 2 decimals?
- **Apply**: Round a calculation to 2 places.
- **Analyze**: Difference between `round()` and formatting.
- **Create**: Build a cost calculator with proper rounding.

## Related Concepts
- [[Python - Math - Arithmetic Operators]]
- [[Python - Math - Money & Budget]]
- [[Python - Math - Calculator Basics]]

## MOC
- Parent: [[Python - Practical Math (MOC)]]
