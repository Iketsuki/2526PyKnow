---
tags: [python, modules, basics]
moc: [[Python - Modules (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: what modules are."
  - "Understand: why use modules."
  - "Apply: import and use modules."
---

# Python - Modules - What are Modules

## Concept
Modules are files with Python code (functions, classes, variables) that can be imported and reused.

## Example Code
```python
import random
print(random.randint(1, 10))
```

## Exercises by Bloom Level
- Remember: Define a module.
- Understand: Why not write everything in one file?
- Apply: Import a module.
- Analyze: Standard library vs third-party modules?
- Create: Build a program using modules.

## Common Errors with Example Code

1) Trying to import before installing (third-party modules)

WRONG
```python
import numpy  # ImportError: No module named 'numpy'
# (numpy not installed yet)
```

CORRECT
```python
# First, install from terminal/PowerShell:
# pip install numpy
# Then in code:
import numpy as np
```

2) Misspelling a module or function name (NameError)

WRONG
```python
import random
choice = random.choise([1, 2, 3])  # typo: choise instead of choice
```

CORRECT
```python
import random
choice = random.choice([1, 2, 3])
```

3) Not understanding different import styles (confusing syntax)

WRONG
```python
from math import *  # imports everything, unclear what's available
result = sqrt(16)  # where did sqrt come from?
```

CORRECT
```python
from math import sqrt, pi
# Or:
import math
result = math.sqrt(16)
```

Short tips:
- Know which modules are built-in (math, random, etc).
- Install third-party modules with pip first.
- Use clear import styles: prefer `import module` or `from module import name`.

## MOC
- Parent: [[Python - Modules (MOC)]]
