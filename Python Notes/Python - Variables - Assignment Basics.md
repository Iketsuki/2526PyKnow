---
tags: [python, variables, assignment]
moc: [[Python - Variables & Types (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: assignment syntax `variable = value`."
  - "Understand: variables store values."
  - "Apply: use variables in expressions."
---

# Python - Variables - Assignment Basics

## Concept
A variable is a named container for a value. Use `=` to assign a value to a variable name.

## Example Code
```python
name = 'Alice'
age = 14
height = 5.6

print(name, age, height)
```

## Exercises by Bloom Level
- Remember: Write a simple assignment.
- Understand: What does a variable "hold"?
- Apply: Create 5 variables and use them in a sentence.
- Analyze: What happens if you assign to the same variable twice?
- Create: Build a program that stores and combines multiple variables.

## Common Errors with Example Code

1) Confusing assignment (`=`) with comparison (`==`)

WRONG
```python
if x = 5:  # SyntaxError: can't assign in expression
  print('x is 5')
```

CORRECT
```python
x = 5
if x == 5:
  print('x is 5')
```

2) Thinking assignment returns a value (no chaining like some languages)

WRONG
```python
if (x = get_value()):  # SyntaxError in Python
  print('Got value')
```

CORRECT
```python
x = get_value()
if x:
  print('Got value')
```

3) Unintended shadowing or reassignment

WRONG
```python
count = 10
def foo():
  count = count + 1  # UnboundLocalError if you expect to modify global
  return count

foo()
```

CORRECT
```python
count = 10
def foo():
  global count
  count = count + 1
  return count

foo()
```

## Related Concepts
- [[Python - Variables - Types Basics]]

## MOC
- Parent: [[Python - Variables & Types (MOC)]]
