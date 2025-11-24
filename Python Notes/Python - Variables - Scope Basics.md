---
tags: [python, variables, scope]
moc: [[Python - Variables & Types (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: what scope means."
  - "Understand: variables inside functions have local scope."
  - "Apply: avoid scope-related bugs."
---

# Python - Variables - Scope Basics

## Concept
Scope defines where a variable is accessible. Variables created inside a function exist only inside that function (local scope). Variables outside functions are global.

## Example Code
```python
name = 'Alice'  # Global scope

def greet():
    greeting = f'Hello, {name}!'  # Can use global 'name'
    return greeting

print(greet())
# print(greeting)  # Error: 'greeting' not in this scope
```

## Exercises by Bloom Level
- Remember: What is local scope?
- Understand: Where can a local variable be used?
- Apply: Write a function that uses both local and global variables.
- Analyze: What happens if a local var has the same name as a global var?
- Create: Demonstrate scope with multiple functions.

## Common Errors with Example Code

1) Using a local variable outside its function (NameError)

WRONG
```python
def greet():
  message = 'Hello'

print(message)  # NameError: name 'message' is not defined
```

CORRECT
```python
def greet():
  message = 'Hello'
  return message

msg = greet()
print(msg)  # 'Hello'
```

2) Modifying a global variable inside a function without `global`

WRONG
```python
count = 0
def inc():
  count += 1  # UnboundLocalError: local variable 'count' referenced before assignment

inc()
```

CORRECT
```python
count = 0
def inc():
  global count
  count += 1

inc()
print(count)  # 1
```

3) Expecting local changes to affect caller variables for immutables

WRONG
```python
def set_to_zero(x):
  x = 0

value = 5
set_to_zero(value)
print(value)  # still 5
```

CORRECT
```python
def set_to_zero(x):
  return 0

value = 5
value = set_to_zero(value)
print(value)  # 0
```

## MOC
- Parent: [[Python - Variables & Types (MOC)]]
