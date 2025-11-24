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

## Common Errors
- Using a variable outside the scope it was defined in.

## MOC
- Parent: [[Python - Variables & Types (MOC)]]
