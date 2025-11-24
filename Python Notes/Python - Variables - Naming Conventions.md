---
tags: [python, variables, naming, conventions]
moc: [[Python - Variables & Types (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: naming rules and Python conventions."
  - "Understand: why good names matter for code readability."
  - "Apply: choose clear, descriptive variable names."
  - "Analyze: readability impact of naming choices."
---

# Python - Variables - Naming Conventions

## Concept
**Variable naming conventions** — Follow Python's `snake_case` style (lowercase with underscores). Good names are descriptive and make code readable.

## Naming Rules

```python
# VALID names:
name = 'Alice'
age = 25
_private = 'internal'  # Leading underscore by convention
first_name = 'Bob'
count123 = 10

# INVALID names:
# 123count = 10  # Can't start with number
# first-name = 'Bob'  # Hyphens not allowed
# first name = 'Bob'  # Spaces not allowed
# class = 'CS'  # 'class' is a reserved keyword
```

## Naming Conventions

```python
# snake_case (Python standard)
user_name = 'alice'
total_score = 100
is_active = True

# CamelCase (for class names, not variables)
class UserAccount:
    pass

# CONSTANTS (ALL_CAPS)
MAX_ATTEMPTS = 3
PI = 3.14159
DATABASE_URL = 'localhost'
```

## Good vs Bad Names

```python
# BAD: Too vague
a = 15
x = [1, 2, 3]
d = {'key': 'value'}

# GOOD: Descriptive
student_age = 15
numbers = [1, 2, 3]
config = {'key': 'value'}

# BAD: Redundant
name_string = 'Alice'  # Already a string!
age_number = 25
user_list = ['alice', 'bob']

# GOOD: Simple and clear
name = 'Alice'
age = 25
users = ['alice', 'bob']
```

## Real Examples

```python
# Example 1: Clear variable names
student_name = 'Alice'
student_grade = 'A'
passing_score = 70

# Example 2: Boolean names (is_ prefix)
is_active = True
has_permission = False
is_admin = False

# Example 3: Plural for collections
students = ['Alice', 'Bob', 'Charlie']
scores = [90, 85, 78]
settings = {'theme': 'dark', 'lang': 'en'}
```

## Exercises by Bloom Level

- **Remember**: Name three rules for valid variable names.
- **Understand**: Why use descriptive names? Compare readability.
- **Apply**: Rename vague variables in given code.
- **Analyze**: Compare readability of `x` vs `user_score`.
- **Create**: Refactor a program with poor variable names.

## Common Errors with Example Code

### Error 1: Starting variable name with number
```python
# WRONG: Can't start with number
3days = 72  # SyntaxError!

# CORRECT: Start with letter or underscore
days_3 = 72
num_3_days = 72
```

### Error 2: Using spaces or hyphens in names
```python
# WRONG: Spaces not allowed
first name = 'Alice'  # SyntaxError!

# WRONG: Hyphens not allowed
first-name = 'Alice'  # This is subtraction!

# CORRECT: Use underscores
first_name = 'Alice'
```

### Error 3: Using Python keywords as names
```python
# WRONG: Reserved keywords (can't use)
class = 'CS'  # SyntaxError! 'class' is reserved
for = 10  # SyntaxError! 'for' is reserved
def = 'function'  # SyntaxError! 'def' is reserved
if = True  # SyntaxError! 'if' is reserved

# CORRECT: Choose different names
my_class = 'CS'
loop_count = 10
define = 'function'
condition = True
```

### Error 4: Confusing case sensitivity
```python
# WRONG: Assuming names are case-insensitive
name = 'Alice'
Name = 'Bob'
print(name)  # 'Alice' (different from Name!)

# Python is case-sensitive! name and Name are different variables

# CORRECT: Use consistent naming
first_name = 'Alice'
last_name = 'Smith'
```

### Error 5: Choosing meaningless names
```python
# WRONG: Names don't describe purpose
d = [1, 2, 3, 4, 5]  # What is d?
f = lambda x: x * 2  # What does f do?
temp = {}  # What does temp store?

# CORRECT: Use descriptive names
test_scores = [1, 2, 3, 4, 5]
double_value = lambda x: x * 2
user_settings = {}
```

## Rules Summary

- Start with letter or underscore.
- Use only letters, numbers, underscores.
- Case-sensitive (`name` ≠ `Name`).
- No spaces or hyphens.
- Avoid Python keywords (`class`, `for`, `def`, etc.).

## Conventions Summary

- Use `snake_case` for variables and functions.
- Use `CamelCase` for class names.
- Use `ALL_CAPS` for constants.
- Use `is_` prefix for booleans (`is_active`, `has_permission`).
- Use descriptive names that explain purpose.

## Related Concepts
- [[Python - Variables & Types - Types Basics]]
- [[Python - Variables - Mutability & Immutability]]

## MOC
- Parent: [[Python - Variables & Types (MOC)]]
