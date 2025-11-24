---
tags: [python, conditionals, logic, operators, precedence, short-circuit]
moc: [[Python - Conditionals (MOC)]]
difficulty: Intermediate
bloom_level: Analyze
learning_objectives:
  - "Remember: operator precedence order (NOT > AND > OR)."
  - "Understand: what short-circuit evaluation is and why it matters."
  - "Apply: use parentheses to control precedence in complex conditions."
  - "Analyze: predict evaluation order and short-circuiting behavior."
---

# Python - Conditionals - Operator Precedence & Short-Circuit Evaluation

## Concept
When combining multiple operators (AND, OR, NOT), Python evaluates them in a specific **precedence order**. Also, Python uses **short-circuit evaluation** — it stops evaluating as soon as it knows the result.

## Precedence Order (Highest to Lowest)

```
1. NOT (highest priority)
2. AND (middle priority)
3. OR  (lowest priority)
```

This means:
- `not x and y` → `(not x) and y`  ← NOT evaluated first
- `x and y or z` → `(x and y) or z`  ← AND evaluated before OR
- `x or y and z` → `x or (y and z)`  ← AND evaluated before OR

## Real Examples

```python
# Example 1: Precedence without parentheses
x = 5
y = 10
z = 15

# Evaluated as: (x > 3) and (y < 20) or (z > 12)
if x > 3 and y < 20 or z > 12:
    print('Condition true')  # Prints: evaluated as True or True = True

# Rewrite clearly with parentheses:
if (x > 3 and y < 20) or (z > 12):
    print('Condition true')  # Same result, clearer intent

# Example 2: NOT has highest priority
is_student = False
is_working = True

# Evaluated as: (not is_student) and is_working
if not is_student and is_working:
    print('Adult working')  # Prints: True and True = True

# Example 3: AND evaluated before OR
age = 25
has_license = True
has_insurance = False

# Evaluated as: (age >= 21 and has_license) or has_insurance
if age >= 21 and has_license or has_insurance:
    print('Can drive')  # Prints: True or False = True

# Rewrite with parentheses for clarity:
if (age >= 21 and has_license) or has_insurance:
    print('Can drive')
```

## Short-Circuit Evaluation

**What is it?** Python stops evaluating conditions as soon as it knows the final result.

### AND Short-Circuiting

```python
# AND stops when it finds False
# If first is False, second is never checked

x = 5
y = 10

# Returns False immediately (stops at x > 10)
if x > 10 and y > 5:  # x > 10 is False, so AND is False
    print('Both true')
else:
    print('First is false')  # Prints: y > 5 not evaluated!

# Example: Checking list length before accessing element
items = []

# WRONG: Will crash if items is empty
if items[0] > 5 and len(items) > 0:
    print('First item greater than 5')

# CORRECT: Check length first (short-circuit prevents crash)
if len(items) > 0 and items[0] > 5:
    print('First item greater than 5')  # Safe: items is checked first
```

### OR Short-Circuiting

```python
# OR stops when it finds True
# If first is True, second is never checked

x = 5
y = 10

# Returns True immediately (stops at x < 10)
if x < 10 or y < 5:  # x < 10 is True, so OR is True
    print('At least one true')  # Prints: y < 5 not evaluated!

# Example: Fallback values
user_name = None
default_name = 'Guest'

# Use 'or' for defaults (old style, pre-3.10)
name = user_name or default_name  # Returns 'Guest' (stops at first truthy)
print(name)  # Guest

# Modern style (Python 3.10+)
name = user_name if user_name else default_name
print(name)  # Guest
```

## Execution Order With Print Statements

```python
def check(n, name):
    print(f'Checking {name}')
    return n > 5

print('--- AND Example ---')
# AND: stops at first False
result = check(3, 'A') and check(10, 'B')
# Prints: Checking A
# B is NEVER checked because A is False

print('\n--- OR Example ---')
# OR: stops at first True
result = check(10, 'A') or check(3, 'B')
# Prints: Checking A
# B is NEVER checked because A is True

print('\n--- No Short-Circuit ---')
# Both checked (using separate if statements)
if check(3, 'A'):
    print('A is true')
if check(10, 'B'):
    print('B is true')
# Prints: Checking A, then Checking B (both evaluated)
```

## Common Errors with Example Code

### Error 1: Forgetting precedence, adding unnecessary parentheses
```python
# Correct (AND before OR):
if x > 5 and y < 10 or z == 0:
    pass

# WRONG: Adding parentheses that change meaning
if x > 5 and (y < 10 or z == 0):  # Different logic!
    pass

# CORRECT: Use parentheses only when intent differs from precedence
if x > 5 and y < 10 or z == 0:  # Clear without parentheses
    pass

if (x > 5 and y < 10) or z == 0:  # Explicitly clear (same as above)
    pass
```

### Error 2: Not using short-circuit to prevent crashes
```python
# WRONG: Can crash with index error
items = [5, 10]
if items[0] > 100 and items[1] > 20:
    print('Both large')

# If items is empty, items[0] crashes BEFORE 'and' check
items = []
if items[0] > 100 and items[1] > 20:  # IndexError!
    pass

# CORRECT: Use short-circuit to check length first
if len(items) > 0 and items[0] > 100:
    print('First item is large')  # Safe: len() prevents crash
```

### Error 3: Side effects from short-circuiting
```python
def log_and_check(value):
    print(f'Checking {value}')  # Side effect
    return value > 5

# WRONG: Assuming both functions are called
if log_and_check(3) or log_and_check(10):
    pass
# Prints only: Checking 3
# log_and_check(10) NOT called due to short-circuit!

# CORRECT: If you need both to execute, use separate statements
if log_and_check(3):
    pass
if log_and_check(10):
    pass
# Prints: Checking 3, then Checking 10 (both executed)
```

### Error 4: Complex nesting without clarity
```python
# WRONG: Hard to follow precedence
if a > 5 and b < 10 or c == 0 and d != 5 or e > 20:
    print('?')  # Which conditions matter?

# CORRECT: Use parentheses for clarity
if (a > 5 and b < 10) or (c == 0 and d != 5) or (e > 20):
    print('Clear intent')
```

### Error 5: Confusing short-circuit with logical result
```python
# WRONG: Assuming 'and' returns True/False
result = 5 and 10
print(result)  # Prints: 10 (not True!)

# CORRECT: 'and' returns last evaluated value (truthy/falsy)
result = 5 and 10  # Returns 10 (last value)
print(result == True)  # False! (10 == True is False)

# CORRECT: Use boolean conversion
result = bool(5 and 10)
print(result)  # Prints: True

# How short-circuit works with return values:
result = False and 10  # Returns False (stops here, 10 not evaluated)
print(result)  # False

result = True or 20  # Returns True (stops here, 20 not evaluated)
print(result)  # True
```

## Exercises by Bloom Level

- **Remember**: List the operator precedence order (NOT, AND, OR).
- **Understand**: Explain why `if len(items) > 0 and items[0] == 5:` is safer than the reverse.
- **Apply**: Add parentheses to clarify this condition: `if x > 5 and y < 10 or z == 0:`.
- **Analyze**: Rewrite `if a > 5 and b < 10 or c == 0 and d != 5:` with explicit parentheses showing precedence.
- **Create**: Build a function that uses short-circuit evaluation to prevent errors when checking nested values.

## Related Concepts
- [[Python - Conditionals - AND Operator]]
- [[Python - Conditionals - OR Operator]]
- [[Python - Conditionals - NOT Operator]]
- [[Python - Conditionals - Boolean Logic (and-or-not)]]

## MOC
- Parent: [[Python - Conditionals (MOC)]]
