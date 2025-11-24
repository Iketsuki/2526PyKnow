---
tags: [python, conditionals, logic, operators]
moc: [[Python - Conditionals (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: NOT operator syntax and symbol (not)."
  - "Understand: how NOT inverts a boolean value."
  - "Apply: use NOT to check opposite conditions."
---

# Python - Conditionals - NOT Operator

## Concept
**NOT operator** — Inverts/reverses a boolean value. `not True` becomes `False`, and `not False` becomes `True`. Useful for checking opposite conditions.

## Basic Syntax

```python
if not condition:
    # Runs if condition is False
    
# Double negative (avoid)
if not not condition:
    # Same as just: if condition
```

## Real Examples

```python
# Check if NOT raining
is_raining = False

if not is_raining:
    print('Go outside')  # This runs

# Check if list is empty
items = []
if not items:
    print('List is empty')
    # Better than: if len(items) == 0

# Check if NOT logged in
is_logged_in = False

if not is_logged_in:
    print('Please log in')

# Check if file NOT found
file_exists = False

if not file_exists:
    print('File not found')
    # Better than: if file_exists == False

# Negate comparison
age = 12

if not (age >= 18):
    print('Too young')
    # Same as: if age < 18
```

## Truth Table

```
not True   → False
not False  → True
```

## Common Errors with Example Code

### Error 1: Using == False instead of 'not'
```python
# WRONG: Verbose and not Pythonic
if is_valid == False:
    print('Invalid')

# CORRECT: Use 'not'
if not is_valid:
    print('Invalid')

# ALSO CORRECT: Use !=
if is_valid != True:
    print('Invalid')
```

### Error 2: Double negation
```python
# WRONG: Confusing double negative
if not not is_enabled:
    print('Enabled')  # Hard to read!

# CORRECT: Just use the positive
if is_enabled:
    print('Enabled')
```

### Error 3: NOT with complex conditions
```python
# WRONG: Can be unclear
if not (age >= 18 and has_license):
    print('Cannot drive')

# CORRECT: Use De Morgan's Law
# not (A and B) = (not A) or (not B)
if age < 18 or not has_license:
    print('Cannot drive')

# ALSO CLEAR: Explicit version
if not age >= 18 or not has_license:
    print('Cannot drive')
```

### Error 4: Confusing empty/falsy checks
```python
# WRONG: Checking length when 'not' is simpler
if len(items) == 0:
    print('Empty')

# CORRECT: Use 'not items'
if not items:
    print('Empty')

# ALSO WORKS: Falsy check
if not items:  # Empty list is falsy
    print('Empty')

# WRONG: Assuming strings work like lists
if not password:
    print('No password')  # Correct for empty string

password = ''  # Empty string
if not password:
    print('No password')  # This prints (empty string is falsy)
```

### Error 5: NOT with 'in' operator
```python
# WRONG: Double negative is confusing
if not 'apple' in items:
    print('No apple')  # Works but unclear

# CORRECT: Use 'not in'
if 'apple' not in items:
    print('No apple')  # Clearer

# BOTH WORK: But prefer 'not in'
if not ('apple' in items):  # Extra parentheses, harder to read
    print('No apple')
```

## Exercises by Bloom Level

- **Remember**: Write a NOT condition to check if something is NOT true.
- **Understand**: Explain why `if not is_empty:` is preferred over `if is_empty == False:`.
- **Apply**: Create a function that warns if a password is NOT strong enough.
- **Analyze**: Rewrite `if not (x >= 5 and x <= 10):` using AND/OR instead of NOT.
- **Create**: Build a security check that denies access if NOT authenticated and NOT on whitelist.

## Related Concepts
- [[Python - Conditionals - AND Operator]]
- [[Python - Conditionals - OR Operator]]
- [[Python - Conditionals - Boolean Logic (and-or-not)]]
- [[Python - Conditionals - Truthiness]]

## MOC
- Parent: [[Python - Conditionals (MOC)]]


[Python - Conditionals - AND Operator]: <Python - Conditionals - AND Operator.md> "Python - Conditionals - AND Operator"
[Python - Conditionals - OR Operator]: <Python - Conditionals - OR Operator.md> "Python - Conditionals - OR Operator"
[Python - Conditionals - Boolean Logic (and-or-not)]: <Python - Conditionals - Boolean Logic (and-or-not).md> "Python - Conditionals - Boolean Logic (and/or/not)"
[Python - Conditionals - Truthiness]: <Python - Conditionals - Truthiness.md> "Python - Conditionals - Truthiness"
[Python - Conditionals (MOC)]: <../MOCs/Python - Conditionals (MOC).md> "Python - Conditionals (MOC)"
