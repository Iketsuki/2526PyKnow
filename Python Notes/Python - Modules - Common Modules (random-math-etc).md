---
tags: [python, modules, common]
moc: [[Python - Modules (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: useful standard modules."
  - "Understand: what each module offers."
  - "Apply: use common modules in programs."
---

# Python - Modules - Common Modules (random, math, etc)

## Concept
Standard library includes `random` (chance), `math` (calculations), `datetime` (dates/times), `os` (system), `json` (data format).

## Example Code
```python
import random
print(random.choice(['a', 'b', 'c']))

import math
print(math.pi)

import datetime
print(datetime.datetime.now())
```

## Exercises by Bloom Level
- Remember: Name 3 useful modules.
- Understand: What does `random.choice()` do?
- Apply: Use `math` for calculations.
- Analyze: When use `random` vs hardcoded data?
- Create: Build a program with multiple modules.

## Common Errors with Example Code

1) Forgetting to import before using (NameError)

WRONG
```python
value = random.choice([1, 2, 3])  # NameError: name 'random' is not defined
```

CORRECT
```python
import random
value = random.choice([1, 2, 3])
print(value)
```

2) Using `import random` then trying to use wrong name

WRONG
```python
import math
result = math.sqrt(16)
area = π * r**2  # NameError: name 'π' is not defined
```

CORRECT
```python
import math
result = math.sqrt(16)
area = math.pi * r**2
```

3) Not handling random values that might be None or edge cases

WRONG
```python
import random
items = []
chosen = random.choice(items)  # IndexError if empty
print(chosen)
```

CORRECT
```python
import random
items = [1, 2, 3]
if items:
    chosen = random.choice(items)
    print(chosen)
else:
    print('No items to choose from')
```

Short tips:
- Always import before using a module.
- Remember `math.pi`, not `π`.
- Check list is non-empty before using `random.choice()`.

## MOC
- Parent: [[Python - Modules (MOC)]]
