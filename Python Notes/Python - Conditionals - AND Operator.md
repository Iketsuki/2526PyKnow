---
tags: [python, conditionals, logic, operators]
moc: [[Python - Conditionals (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: AND operator syntax with two or more conditions."
  - "Understand: when AND requires all conditions to be true."
  - "Apply: use AND to combine multiple checks in conditionals."
---

# Python - Conditionals - AND Operator

## Concept
**AND operator** — Requires **all** conditions to be true. If any condition is false, the entire expression is false. Useful for multiple requirements.

## Basic Syntax

```python
if condition1 and condition2:
    # Runs ONLY if both are true
    
# Multiple conditions
if condition1 and condition2 and condition3:
    # ALL must be true
```

## Real Examples

```python
# Age AND score check
age = 15
score = 85

if age >= 13 and score >= 80:
    print('Qualified for tournament')

# Password validation: length AND alphanumeric
password = 'MyPass123'
if len(password) >= 8 and password.isalnum():
    print('Password is strong')

# Login check: username AND password
username = 'alice'
password = 'secure123'

if username == 'alice' and password == 'secure123':
    print('Login successful')
else:
    print('Invalid credentials')

# Range check: minimum AND maximum
score = 75
if score >= 0 and score <= 100:
    print('Score is valid')

# Cleaner with single operator
if 0 <= score <= 100:
    print('Score is valid')  # Chained comparison
```

## Truth Table

```
True  and True   → True
True  and False  → False
False and True   → False
False and False  → False
```

## Common Errors with Example Code

### Error 1: Using OR instead of AND
```python
# WRONG: Only one needs to be true
if age >= 13 or score >= 80:
    print('Qualified')  # Can qualify with just age!

# CORRECT: Both must be true
if age >= 13 and score >= 80:
    print('Qualified')  # Both required
```

### Error 2: Repeating variable name incorrectly
```python
# WRONG: This doesn't work
if score >= 70 and <= 100:
    print('Valid')  # SyntaxError!

# CORRECT: Repeat variable or use chaining
if score >= 70 and score <= 100:
    print('Valid')

# BETTER: Use chained comparison
if 70 <= score <= 100:
    print('Valid')
```

### Error 3: Forgetting AND requires ALL to be true
```python
# WRONG: Expects this to pass with one condition
if x > 5 and x < 10:
    print('In range')

x = 3
# This does NOT print (x is not > 5)

# CORRECT: Understand AND is strict
x = 7
if x > 5 and x < 10:
    print('In range')  # This prints (both conditions true)
```

## Exercises by Bloom Level

- **Remember**: Write an AND condition with two boolean variables.
- **Understand**: Explain why `age > 18 and age < 65` filters to working-age adults.
- **Apply**: Build a login checker that requires both username AND password to match.
- **Analyze**: Compare when to use AND vs. when to use chained comparisons.
- **Create**: Build an age/height eligibility check for a roller coaster.

## Related Concepts
- [[Python - Conditionals - OR Operator]]
- [[Python - Conditionals - NOT Operator]]
- [[Python - Conditionals - Boolean Logic (and-or-not)]]
- [[Python - Conditionals - Truthiness]]

## MOC
- Parent: [[Python - Conditionals (MOC)]]
