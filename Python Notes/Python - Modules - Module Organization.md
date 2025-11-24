---
tags: [python, modules, organization]
moc: [[Python - Modules (MOC)]]
difficulty: Beginner
bloom_level: Analyze
learning_objectives:
  - "Remember: module naming and structure."
  - "Understand: organizing code into modules."
  - "Apply: design module boundaries."
---

# Python - Modules - Module Organization

## Concept
Organize related functions into modules. Use clear names and group logically (math functions in one module, UI in another).

## Example Code
```python
# math_utils.py (math functions)
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# file_utils.py (file functions)
def read_and_count_lines(filename):
    with open(filename) as f:
        return len(f.readlines())

# main.py
from math_utils import calculate_average
from file_utils import read_and_count_lines
```

## Exercises by Bloom Level
- Remember: Why organize into modules?
- Understand: Grouping principles?
- Apply: Reorganize code into modules.
- Analyze: Module dependencies.
- Create: Design a multi-module program.

## Common Errors with Example Code

1) Poor module boundaries (too many responsibilities in one module)

WRONG
```python
# everything.py - too many jobs!
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def save_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(str(data))

def fetch_from_database():
    # ... database code ...
    pass
```

CORRECT
```python
# math_utils.py
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# file_utils.py
def save_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(str(data))

# db_utils.py
def fetch_from_database():
    pass
```

2) Unclear module names (ambiguous purpose)

WRONG
```python
# utils.py - what is this for?
# helpers.py - unclear
# stuff.py - too vague
```

CORRECT
```python
# math_utils.py
# file_operations.py
# database_helpers.py
# string_formatters.py
```

3) Creating circular dependencies (modules import each other)

WRONG
```python
# module_a.py
from module_b import helper

# module_b.py
from module_a import other_helper  # circular!
```

CORRECT
```python
# Refactor: create module_c.py with shared code
# module_a.py imports from module_c
# module_b.py imports from module_c
```

Short tips:
- One module = one purpose.
- Use descriptive names (not 'utils' or 'helpers').
- Avoid circular imports by organizing dependencies in layers.

## MOC
- Parent: [[Python - Modules (MOC)]]
