---
tags: [python, conditionals, nested, if-statements]
moc: [[Python - Conditionals (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: nested `if` statement syntax."
  - "Understand: when nesting is appropriate vs using boolean logic."
  - "Apply: write multi-level decision logic."
  - "Analyze: simplify nested ifs with `and`/`or`."
---

# Python - Conditionals - Nested Conditions

## Concept
**Nested conditions** — Place `if` statements inside `if` blocks to create multi-level decisions. Useful for sequential checks, but often can be simplified with boolean logic.

## Basic Structure

```python
if outer_condition:
    # First level check
    if inner_condition:
        # Both conditions are true
        print('Both true')
    else:
        # Outer is true, inner is false
        print('Outer yes, inner no')
else:
    # Outer condition is false
    print('Outer false')
```

## Real Examples

```python
# Example 1: Age and license check
age = 18
has_license = True

if age >= 16:
    if has_license:
        print('Can drive')
    else:
        print('Get a license')
else:
    print('Too young to drive')

# Example 2: Grade assignment (nested elif)
score = 85

if score >= 90:
    print('A')
elif score >= 80:
    if score >= 85:
        print('B+ (high B)')
    else:
        print('B (low B)')
elif score >= 70:
    print('C')
else:
    print('F')

# Example 3: Login system
username = 'alice'
password = 'secret123'
is_admin = True

if username == 'alice':
    if password == 'secret123':
        if is_admin:
            print('Admin login successful')
        else:
            print('User login successful')
    else:
        print('Wrong password')
else:
    print('User not found')
```

## Nested with elif

```python
# Nested with elif (more complex logic)
user_type = 'student'
age = 25

if user_type == 'student':
    if age < 18:
        print('High school student')
    elif age < 25:
        print('College student')
    else:
        print('Grad student')
elif user_type == 'teacher':
    if age < 30:
        print('New teacher')
    else:
        print('Experienced teacher')
else:
    print('Unknown user type')
```

## When to Use Nesting vs Boolean Logic

```python
# NESTED (less readable)
if age >= 16:
    if has_license:
        print('Can drive')

# BOOLEAN LOGIC (more readable)
if age >= 16 and has_license:
    print('Can drive')

# Sometimes nesting is clearer:
if username:
    if username in approved_users:
        if has_paid:
            print('Access granted')
        else:
            print('Payment required')
    else:
        print('User not approved')

# This is acceptable nesting - checks are sequential
```

## Common Errors with Example Code

### Error 1: Indentation errors with nested ifs
```python
# WRONG: Incorrect indentation
age = 18
if age >= 16:
if has_license:  # Not indented! SyntaxError
    print('Can drive')

# CORRECT: Proper indentation
if age >= 16:
    if has_license:
        print('Can drive')
```

### Error 2: Using nesting instead of boolean logic
```python
# WRONG: Over-nested and hard to read
if name:
    if email:
        if phone:
            if age >= 18:
                print('Can register')

# CORRECT: Use boolean logic for cleaner code
if name and email and phone and age >= 18:
    print('Can register')
```

### Error 3: Forgetting that nesting changes what runs
```python
# WRONG: Assuming both ifs check independently
user = 'alice'
password = 'wrong'

if user == 'alice':
    print('User found')
    
    if password == 'secret':
        print('Correct password')
    
print('Done')  # This ALWAYS prints

# If you wanted to stop on wrong password:
# CORRECT: Use elif/else
if user == 'alice':
    if password == 'secret':
        print('Login successful')
    else:
        print('Wrong password')
else:
    print('User not found')

print('Done')
```

### Error 4: Nesting when variables don't exist in outer scope
```python
# WRONG: Using variable from inner scope outside
if age >= 18:
    status = 'adult'

# This WORKS because Python doesn't have block scope
print(status)  # 'adult' (variable exists)

# BUT this is confusing. Variables created inside functions don't leak out:
def check():
    if True:
        x = 10
    print(x)  # Works - no function scope issue

check()

# In functions:
def check2():
    if True:
        x = 10
    # x exists here
    
# x does NOT exist here (function scope)
```

### Error 5: Deep nesting is hard to follow
```python
# WRONG: Too deeply nested (hard to read)
if condition1:
    if condition2:
        if condition3:
            if condition4:
                if condition5:
                    print('Finally!')

# CORRECT: Break into helper function
def should_process():
    return condition1 and condition2 and condition3 and condition4 and condition5

if should_process():
    print('Finally!')

# OR: Check for failures early (guard clause)
if not condition1:
    return
if not condition2:
    return
if not condition3:
    return
if not condition4:
    return
if not condition5:
    return

print('Finally!')
```

## Exercises by Bloom Level

- **Remember**: Write a nested `if` statement.
- **Understand**: When is nesting useful vs using `and`/`or`?
- **Apply**: Create a 3-level decision tree.
- **Analyze**: Simplify nested ifs with `and` operator.
- **Create**: Build a complex decision system (quiz, game rules, etc.).

## Tips
- Use boolean logic (`and`/`or`) instead of nesting for clarity.
- Don't nest more than 2-3 levels deep.
- Consider helper functions for complex conditions.
- Use early returns to avoid excessive nesting.

## Related Concepts
- [[Python - Conditionals - Boolean Logic (and-or-not)]]
- [[Python - Conditionals - If-Else Basics]]
- [[Python - Conditionals - Compound Logic]]

## MOC
- Parent: [[Python - Conditionals (MOC)]]
