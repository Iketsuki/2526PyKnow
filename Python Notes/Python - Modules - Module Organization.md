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

## MOC
- Parent: [[Python - Modules (MOC)]]
