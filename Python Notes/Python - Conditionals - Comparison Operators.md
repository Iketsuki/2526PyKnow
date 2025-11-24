---
tags: [python, conditionals, comparison, operators]
moc: [[Python - Conditionals (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: all comparison operators and their symbols."
  - "Understand: what each operator means and returns."
  - "Apply: use comparisons in conditions."
  - "Analyze: comparing different data types."
---

# Python - Conditionals - Comparison Operators

## Concept
**Comparison operators** — Compare two values and return True or False. The main operators are: `==` (equal), `!=` (not equal), `<` (less than), `>` (greater than), `<=` (less than or equal), `>=` (greater than or equal).

## Quick Reference

```python
==  # Equal to
!=  # Not equal to
<   # Less than
>   # Greater than
<=  # Less than or equal to
>=  # Greater than or equal to
```

## Real Examples

```python
x = 10
y = 5

# Equal to
print(x == 10)      # True
print(x == y)       # False

# Not equal to
print(x != 5)       # True
print(x != y)       # True

# Less than / Greater than
print(x < 15)       # True
print(x > 5)        # True

# Less than or equal / Greater than or equal
print(x <= 10)      # True
print(x >= 10)      # True
```

## Comparing Different Types

```python
# Numbers
print(5 == 5.0)     # True (int == float works)
print(5 < 10)       # True

# Strings (alphabetical comparison)
print('apple' == 'apple')  # True
print('apple' < 'banana')  # True (alphabetically)
print('apple' != 'Apple')  # True (case-sensitive!)

# Booleans
print(True == 1)    # True (boolean can equal number)
print(False == 0)   # True

# Lists
print([1, 2] == [1, 2])  # True (content matters)
print([1, 2] != [2, 1])  # True (order matters)
```

## Real-World Examples

```python
# Age check
age = 18

if age >= 18:
    print('Adult')
else:
    print('Minor')

# Score grading
score = 85

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')

# String validation
name = 'Alice'

if name != '':
    print(f'Hello, {name}')

# Range check
temperature = 25

if 20 <= temperature <= 30:
    print('Comfortable temperature')
```

## Common Errors with Example Code

### Error 1: Using = instead of ==
```python
# WRONG: Using assignment = instead of comparison ==
if x = 5:
    print('x is 5')  # SyntaxError!

# CORRECT: Use == for comparison
if x == 5:
    print('x is 5')

# Remember: = assigns, == compares
x = 5  # Assignment
if x == 5:  # Comparison
    pass
```

### Error 2: Comparing different types unexpectedly
```python
# WRONG: Comparing string to number
if '10' == 10:
    print('Match')  # Prints nothing (False)

# They are NOT equal! String '10' != integer 10

# CORRECT: Convert types or compare same types
if int('10') == 10:
    print('Match')  # Now prints (True)

# Or:
if '10' == str(10):
    print('Match')  # Also True
```

### Error 3: Forgetting case sensitivity in string comparisons
```python
# WRONG: Assuming case-insensitive comparison
password = 'MyPassword'

if password == 'mypassword':
    print('Correct')  # Doesn't print (case mismatch!)

# CORRECT: Convert to same case for comparison
if password.lower() == 'mypassword':
    print('Correct')  # Prints (case-insensitive)

# Or be explicit:
if password == 'MyPassword':
    print('Correct')
```

### Error 4: Using != instead of ==
```python
# WRONG: Using wrong operator
if age != 18:
    print('Not exactly 18')  # Prints for any age except 18

# But if you meant to check if adult:
if age >= 18:
    print('Adult')  # Correct operator

# CORRECT: Know what you're checking
if age == 18:
    print('Exactly 18')  # True only for 18

if age != 18:
    print('Not 18')  # True for anything except 18
```

### Error 5: Chained comparisons with wrong logic
```python
# WRONG: Comparing single variable to multiple values
if 10 < x < 20:
    print('Between 10 and 20')  # Works correctly

# BUT this is WRONG:
if 10 > x > 20:
    print('x is greater than 10 and greater than 20')
    # NEVER prints! (x can't be both > 10 AND > 20 unless it's > 20)

# CORRECT: Chained comparisons work left to right
if 10 < x < 20:
    print('x between 10 and 20')

# ALSO CORRECT: Multiple separate comparisons
if x > 10 and x < 20:
    print('x between 10 and 20')
```

## Exercises by Bloom Level

- **Remember**: List all comparison operators.
- **Understand**: Difference between `=` and `==`? What does `<=` mean?
- **Apply**: Write comparisons for different types (numbers, strings, booleans).
- **Analyze**: Can you compare strings? How? What about case sensitivity?
- **Create**: Use comparisons in a decision program (age checker, grade calculator, etc.).

## Related Concepts
- [[Python - Conditionals - If-Else Basics]]
- [[Python - Conditionals - Boolean Logic (and-or-not)]]
- [[Python - Conditionals - Truthiness]]

## MOC
- Parent: [[Python - Conditionals (MOC)]]
