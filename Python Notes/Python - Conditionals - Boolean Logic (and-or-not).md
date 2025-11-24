---
tags: [python, conditionals, logic, operators]
moc: [[Python - Conditionals (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `and`, `or`, `not` operators and their behavior."
  - "Understand: combining conditions with boolean logic."
  - "Apply: use boolean logic in conditionals."
  - "Analyze: simplify complex boolean expressions."
---

# Python - Conditionals - Boolean Logic (and-or-not)

## Concept
Combine conditions with logical operators: `and` (both true), `or` (at least one true), `not` (negate/invert).

## Quick Reference

```python
# AND: Both must be True
True and True   → True
True and False  → False
False and True  → False
False and False → False

# OR: At least one must be True
True or True    → True
True or False   → True
False or True   → True
False or False  → False

# NOT: Inverts the value
not True  → False
not False → True
```

## Real Examples

```python
age = 15
is_student = True

# AND: Both conditions must be true
if age >= 13 and age < 18:
    print('Teenager')  # Prints if both conditions true

# OR: At least one condition must be true
if is_student or age < 25:
    print('Eligible')  # Prints if either is true

# NOT: Negate a condition
if not is_student:
    print('Not a student')  # Prints if is_student is False

# Combining all three
if age >= 13 and not is_student:
    print('Teen non-student')  # Both must be true
```

## Detailed Examples

```python
# Example 1: AND (both must be true)
has_money = True
has_id = True

if has_money and has_id:
    print('Can buy ticket')  # Prints (both true)

has_id = False
if has_money and has_id:
    print('Can buy ticket')  # Doesn't print (one false)

# Example 2: OR (at least one must be true)
is_member = False
is_senior = True

if is_member or is_senior:
    print('Eligible for discount')  # Prints (senior is true)

is_senior = False
if is_member or is_senior:
    print('Eligible for discount')  # Doesn't print (both false)

# Example 3: NOT (negate)
is_logged_in = False

if not is_logged_in:
    print('Please log in')  # Prints (not logged in is true)
```

## Common Errors with Example Code

### Error 1: Using AND when OR is needed
```python
# WRONG: Using AND for alternative conditions
status = 'pending'

if status == 'complete' and status == 'pending':
    print('Ready')  # Never prints! (status can't be both)

# CORRECT: Use OR for alternatives
if status == 'complete' or status == 'pending':
    print('Ready')  # Prints when either is true

# BETTER: Use 'in' operator
if status in ['complete', 'pending']:
    print('Ready')
```

### Error 2: Forgetting to negate both in De Morgan's Law
```python
# WRONG: Incomplete negation
if not (has_key and has_password):
    print('Access denied')

# This is NOT the same as:
if not has_key and not has_password:
    print('Access denied')  # Wrong! De Morgan's Law violated

# CORRECT: De Morgan's Law
# not (A and B) = (not A) or (not B)
if not has_key or not has_password:
    print('Access denied')

# ALSO CORRECT: Use De Morgan's for OR
# not (A or B) = (not A) and (not B)
if not is_admin and not is_moderator:
    print('User has no special privileges')
```

### Error 3: Repeating variable in AND condition
```python
# WRONG: Redundant comparison
password = 'MyPass'

if password.isalpha() and password.isalnum():
    print('Valid')

# isalpha() checks if ALL characters are letters
# isalnum() checks if ALL are alphanumeric
# But if isalpha() is true, isalnum() is always true (letters are alphanumeric)

# CORRECT: What you probably meant
if password.isalnum() and len(password) >= 8:
    print('Strong password')
```

### Error 4: Not understanding short-circuit evaluation
```python
# WRONG: Assuming both sides of AND are always evaluated
items = []

if items[0] == 'x' and len(items) > 0:
    print('Found')  # Crashes! items[0] evaluated first

# CORRECT: Check length first (short-circuit prevents crash)
if len(items) > 0 and items[0] == 'x':
    print('Found')  # Safe: len() checked first, short-circuits

# WRONG: Assuming both sides of OR are always evaluated
def check_flag(flag):
    print('Checking flag...')
    return flag

result = True or check_flag(False)
# Function NOT called due to short-circuit (first condition already true)
```

### Error 5: Over-nesting with NOT
```python
# WRONG: Double negation is confusing
if not not is_enabled:
    print('Enabled')  # Hard to read! Same as: if is_enabled

# CORRECT: Use positive form
if is_enabled:
    print('Enabled')

# WRONG: Negating negatives
if not is_disabled:
    print('Can use')  # Awkward variable naming

# CORRECT: Use clearer variable names
if is_enabled:
    print('Can use')
```

## Exercises by Bloom Level

- **Remember**: Write an `and` condition. Write an `or` condition.
- **Understand**: When is `and` true vs `or`? What does `not` do?
- **Apply**: Check multiple conditions in one statement.
- **Analyze**: Simplify: `if not (has_key or has_password)` using De Morgan's Law.
- **Create**: Build a program with complex boolean logic (login system, permission checker, etc.).

## Tips
- Use parentheses for clarity: `(a and b) or c`.
- Remember precedence: NOT > AND > OR.
- Avoid double negation: `if not not x:` should be `if x:`.
- Use `in` for checking multiple values: `if status in ['a', 'b', 'c']`.

## Related Concepts
- [[Python - Conditionals - AND Operator]]
- [[Python - Conditionals - OR Operator]]
- [[Python - Conditionals - NOT Operator]]
- [[Python - Conditionals - If-Else Basics]]
- [[Python - Conditionals - Operator Precedence & Short-Circuit]]

## MOC
- Parent: [[Python - Conditionals (MOC)]]
