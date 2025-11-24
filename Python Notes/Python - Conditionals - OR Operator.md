---
tags: [python, conditionals, logic, operators]
moc: [[Python - Conditionals (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: OR operator syntax with two or more conditions."
  - "Understand: when OR requires at least one condition to be true."
  - "Apply: use OR to check multiple alternatives."
---

# Python - Conditionals - OR Operator

## Concept
**OR operator** — Requires **at least one** condition to be true. If any condition is true, the entire expression is true. Useful for checking alternatives.

## Basic Syntax

```python
if condition1 or condition2:
    # Runs if EITHER is true (or both)
    
# Multiple conditions
if condition1 or condition2 or condition3:
    # At least ONE must be true
```

## Real Examples

```python
# Weekend check
day = 'Saturday'

if day == 'Saturday' or day == 'Sunday':
    print('It is weekend!')

# Grade check: pass if A, B, or C
grade = 'B'
if grade == 'A' or grade == 'B' or grade == 'C':
    print('Passing grade')

# Better: use 'in' operator
if grade in ['A', 'B', 'C']:
    print('Passing grade')

# User role check: admin OR moderator
role = 'admin'
if role == 'admin' or role == 'moderator':
    print('Has elevated permissions')

# Game state: paused OR stopped
state = 'paused'
if state == 'paused' or state == 'stopped':
    print('Game is not running')
```

## Truth Table

```
True  or True   → True
True  or False  → True
False or True   → True
False or False  → False
```

## Common Errors with Example Code

### Error 1: Using AND instead of OR
```python
# WRONG: Both must be true (impossible)
if day == 'Saturday' and day == 'Sunday':
    print('Weekend')  # Never runs (day can't be both)

# CORRECT: At least one
if day == 'Saturday' or day == 'Sunday':
    print('Weekend')  # Runs on either day
```

### Error 2: Repeating condition incorrectly
```python
# WRONG: Too verbose and hard to read
if x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
    print('Small number')

# CORRECT: Use 'in' operator
if x in [1, 2, 3, 4, 5]:
    print('Small number')

# Alternative: Use range
if x in range(1, 6):
    print('Small number')
```

### Error 3: Forgetting OR only needs ONE true condition
```python
# WRONG: Expecting both to be true for OR
if age >= 18 or has_license:
    can_drive = True

age = 16
has_license = False
# This does NOT set can_drive (both are false)

# CORRECT: Understand OR needs just one
age = 20
has_license = False
if age >= 18 or has_license:
    can_drive = True  # This runs (age >= 18 is true)
```

### Error 4: Confusing negation with OR
```python
# WRONG: Not correct logic
if not grade == 'A' or not grade == 'B':
    print('Not A or B')  # Always true!

# CORRECT: Use proper logic
if grade != 'A' and grade != 'B':
    print('Not A or B')

# Alternative: Use 'not in'
if grade not in ['A', 'B']:
    print('Not A or B')
```

## Exercises by Bloom Level

- **Remember**: Write an OR condition to check if something is red OR blue.
- **Understand**: Explain why `weekend = day == 'Saturday' or day == 'Sunday'` is a valid alternative check.
- **Apply**: Create a function that allows access if username is 'admin' OR password is 'secret'.
- **Analyze**: Compare `x == 1 or x == 2 or x == 3` vs `x in [1, 2, 3]`. Which is better?
- **Create**: Build a game logic that ends if player_health <= 0 OR boss_health <= 0.

## Related Concepts
- [[Python - Conditionals - AND Operator]]
- [[Python - Conditionals - NOT Operator]]
- [[Python - Conditionals - Boolean Logic (and-or-not)]]
- [[Python - Conditionals - Truthiness]]

## MOC
- Parent: [[Python - Conditionals (MOC)]]
