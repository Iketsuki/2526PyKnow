---
tags: [python, conditionals, logic, operators]
moc: [[Python - Conditionals (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: and, or, not operators and their truth tables."
  - "Understand: how to combine multiple operators in conditions."
  - "Apply: build complex conditions with proper precedence."
  - "Analyze: operator precedence and short-circuit evaluation."
---

# Python - Conditionals - Compound Logic

## Concept
**Compound logic** — Combine multiple conditions with `and`, `or`, `not` operators to build complex decision rules. `and` requires all conditions true, `or` needs at least one true, `not` inverts a condition.

> **Note**: This note provides an overview. For detailed operator behavior, short-circuiting, and precedence rules, see the focused operator notes below.

## Quick Reference: Individual Operators

- **[[Python - Conditionals - AND Operator]]** — Both conditions must be true
- **[[Python - Conditionals - OR Operator]]** — At least one condition must be true
- **[[Python - Conditionals - NOT Operator]]** — Inverts/reverses a boolean value
- **[[Python - Conditionals - Operator Precedence & Short-Circuit]]** — Evaluation order and short-circuit behavior

## Real-World: Game Access

```python
def can_play_game(age, has_permission, is_banned):
    '''Check if player can play'''
    
    # Must be age appropriate
    # AND have parent permission
    # AND not banned
    if age >= 13 and has_permission and not is_banned:
        return True
    
    return False

# Test cases
print(can_play_game(14, True, False))  # True
print(can_play_game(10, True, False))  # False (too young)
print(can_play_game(14, False, False))  # False (no permission)
print(can_play_game(14, True, True))   # False (banned)
```

## Real-World: Score Range

```python
def get_grade_compound(score):
    '''Return letter grade using compound comparisons'''
    if 90 <= score <= 100:  # Compound comparison
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

print(get_grade_compound(85))  # B
```

## Real-World: Data Validation

```python
def is_valid_email(email):
    '''Simple email validation using compound conditions'''
    has_at = '@' in email
    has_dot = '.' in email.split('@')[-1] if has_at else False
    has_length = len(email) > 5
    
    return has_at and has_dot and has_length

print(is_valid_email('alice@example.com'))  # True
print(is_valid_email('alice@example'))      # False (no dot)
print(is_valid_email('alice example.com'))  # False (no @)
```

## Real-World: Discount Calculator

```python
def calculate_discount(age, membership, purchase_amount):
    '''Calculate discount based on multiple criteria'''
    discount = 0
    
    # Senior or student
    if age >= 65 or age < 18:
        discount += 0.10  # 10% off
    
    # Member discount
    if membership:
        discount += 0.05  # 5% off
    
    # Large purchase
    if purchase_amount >= 100:
        discount += 0.05  # 5% off
    
    # Max 20% discount
    discount = min(discount, 0.20)
    
    final_price = purchase_amount * (1 - discount)
    return round(final_price, 2)

# Test
print(calculate_discount(70, True, 150))  # Senior + member + bulk = 20%
print(calculate_discount(16, False, 50))  # Student = 10%
```

## Best Practices for Complex Conditions

```python
# GOOD: Clear and readable
if age >= 18 and has_license and not is_suspended:
    print('Can drive')

# BAD: Too many conditions in one line (hard to follow)
if a and b or c and d or e and f:
    pass

# BETTER: Break into logical parts
is_adult = age >= 18
is_qualified = has_license and not is_suspended

if is_adult and is_qualified:
    print('Can drive')

# BEST: Use helper functions
def is_valid_player(age, score, banned):
    return age >= 13 and score >= 50 and not banned

if is_valid_player(14, 75, False):
    print('Can play')
```

## Understanding Precedence

```python
# Operator precedence: NOT > AND > OR

# This condition:
if age > 18 and has_license or is_admin:
    pass

# Is evaluated as:
if (age > 18 and has_license) or is_admin:
    pass

# Use parentheses for clarity:
if (age > 18 and has_license) or is_admin:
    print('Can access')
```

## Common Errors with Example Code

### Error 1: Forgetting precedence (AND before OR)
```python
# WRONG: Assuming OR binds tighter than AND
if allow_guest or user_role == 'admin' and not is_banned:
    print('Access granted')

# Is evaluated as: allow_guest or (user_role == 'admin' and not is_banned)
# Admin who IS banned still gets access (maybe not intended!)

# CORRECT: Use parentheses for clarity
if allow_guest or (user_role == 'admin' and not is_banned):
    print('Access granted')

# OR if you meant something different:
if (allow_guest or user_role == 'admin') and not is_banned:
    print('Access granted')
```

### Error 2: Using AND when OR is needed
```python
# WRONG: Using AND for exclusive checks (always False!)
if status == 'active' and status == 'pending':
    print('Do something')  # Never prints! status can't be both

# CORRECT: Use OR for multiple possible values
if status == 'active' or status == 'pending':
    print('Do something')

# EVEN BETTER: Use 'in'
if status in ['active', 'pending']:
    print('Do something')
```

### Error 3: Incorrect negation of compound conditions
```python
# WRONG: Negating without considering De Morgan's Law
if not (age >= 18 and has_id):
    print('Cannot enter')

# This is equivalent to:
if age < 18 or not has_id:
    print('Cannot enter')

# But writing it wrong:
if not age >= 18 and not has_id:  # Wrong precedence!
    print('Cannot enter')

# CORRECT: Apply De Morgan's Law
# not (A and B) = (not A) or (not B)
if age < 18 or not has_id:
    print('Cannot enter')
```

### Error 4: Confusing the evaluation of compound conditions
```python
# WRONG: Forgetting short-circuit evaluation
items = []

if len(items) > 0 and items[0] == 'x':
    print('First item is x')

# This is SAFE because AND short-circuits (len() > 0 is False first)

# But this is WRONG order:
if items[0] == 'x' and len(items) > 0:
    print('First item is x')  # Will crash! items[0] evaluated first

# CORRECT: Check length/existence first
if len(items) > 0 and items[0] == 'x':
    print('First item is x')
```

### Error 5: Over-complicating conditions with unnecessary operators
```python
# WRONG: Too complex and hard to read
if not (not is_valid or not is_approved) and has_permission:
    print('Proceed')

# CORRECT: Simplify using De Morgan's Law
# not (not A or not B) = A and B
if is_valid and is_approved and has_permission:
    print('Proceed')

# ALSO ACCEPTABLE: Break into helper variable
is_fully_approved = is_valid and is_approved
if is_fully_approved and has_permission:
    print('Proceed')
```

## Exercises by Bloom Level

- **Remember**: What do `and`, `or`, `not` do?
- **Understand**: Why break complex conditions into multiple lines?
- **Apply**: Build a function with 3+ compound conditions.
- **Analyze**: Trace precedence in: `a and b or c and d`.
- **Create**: Build an access control system with multiple criteria.

## See Also

- **Detailed Operator Guides** (see quick reference above)
- [[Python - Conditionals - Boolean Logic (and-or-not)]]
- [[Python - Conditionals - Comparison Operators]]
- [[Python - Conditionals - If-Else Basics]]
- [[Python - Conditionals - Truthiness]]

## MOC
- Parent: [[Python - Conditionals (MOC)]]
