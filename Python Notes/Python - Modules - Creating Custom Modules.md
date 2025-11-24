---
tags: [python, modules, custom]
moc: [[Python - Modules (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: creating a module file."
  - "Understand: how Python finds modules."
  - "Apply: write and import custom modules."
---

# Python - Modules - Creating Custom Modules

## Concept
Create a `.py` file with functions or classes, then import it as a module.

## Example Code
```python
# mymath.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# main.py
from mymath import add
print(add(5, 3))
```

## Exercises by Bloom Level
- Remember: Create a simple module file.
- Understand: How does import find the file?
- Apply: Write and use a custom module.
- Analyze: Organize multiple functions in a module.
- Create: Build a utility module for repeated tasks.

## MOC
- Parent: [[Python - Modules (MOC)]]
