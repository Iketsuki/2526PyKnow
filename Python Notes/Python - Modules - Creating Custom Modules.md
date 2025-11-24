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

## Common Errors with Example Code

1) Module file is not in the right folder (ModuleNotFoundError)

WRONG
```python
# main.py in c:/projects/
# mymath.py in c:/projects/utils/

from mymath import add  # Can't find it!
```

CORRECT
```python
# Option 1: move mymath.py to same folder as main.py
# OR
# Option 2: add folder to Python path
import sys
sys.path.append('utils')
from mymath import add
```

2) Circular imports (each module imports the other)

WRONG
```python
# module_a.py
from module_b import helper_b

def helper_a():
    return helper_b()

# module_b.py
from module_a import helper_a  # circular!
```

CORRECT
```python
# Reorganize: put shared code in a third module
# shared.py contains the common function
# module_a.py and module_b.py both import from shared.py
```

3) Forgetting to use __name__ guard (code runs on import)

WRONG
```python
# calculator.py
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Prints when imported!
```

CORRECT
```python
# calculator.py
def add(a, b):
    return a + b

if __name__ == '__main__':
    result = add(5, 3)
    print(result)  # Only runs when executed directly
```

Short tips:
- Keep module files in the same folder or use sys.path.
- Avoid circular imports by organizing code into shared modules.
- Use `if __name__ == '__main__':` guard for executable code.

## MOC
- Parent: [[Python - Modules (MOC)]]
