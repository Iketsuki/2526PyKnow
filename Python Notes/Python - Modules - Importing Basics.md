---
tags: [python, modules, importing, imports]
moc: [[Python - Modules (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: import syntax variations."
  - "Understand: `import module` vs `from module import function`."
  - "Apply: import modules and access their contents."
  - "Analyze: when to use each import style."
  - "Create: organize imports and understand module hierarchy."
---

# Python - Modules - Importing Basics

## What is a Module?

A **module** is code that someone else wrote to help you. It's like a toolbox with tools inside.

Python comes with many built-in modules:
- `math` — for math functions
- `random` — for random numbers
- `datetime` — for dates and times

## Importing a Module

Use `import` to load a module:

```python
import math
print(math.sqrt(9))  # 3.0
```

When you import a module, you use the name followed by a dot:
```
math.sqrt()  ← module.function()
```

## Method 1: Import the Whole Module

```python
import math

print(math.sqrt(16))  # 4.0
print(math.pi)       # 3.14159...
print(math.ceil(3.2)) # 4
```

Use `module.function()` for everything.

## Method 2: Import One Function

```python
from math import sqrt

print(sqrt(16))  # 4.0
# No module name needed!
```

Use the function name directly.

## Real-World Examples

**Using Random Numbers**
```python
import random

number = random.randint(1, 10)
print(number)
```

**Using Time**
```python
import datetime

today = datetime.datetime.now()
print(today)
```

**Using Multiple Functions**
```python
from math import sqrt, pi

print(sqrt(25))  # 5.0
print(pi)       # 3.14159...
```

## Which Method to Use?

**Use `import module` if:**
- You use many functions from the module
- You want to be clear which module each function comes from

**Use `from module import function` if:**
- You use only one or two functions
- You use them many times and want shorter code

## Exercise Examples

**Remember:**
```python
import math
```

**Understand:**
What's the difference?
```python
import math
print(math.sqrt(9))
```
vs
```python
from math import sqrt
print(sqrt(9))
```

**Apply:**
```python
import random
number = random.randint(1, 100)
print(number)
```

## Common Errors with Example Code

1) Forgetting the module name prefix

WRONG
```python
import math
print(sqrt(16))  # Error!
```

CORRECT
```python
import math
print(math.sqrt(16))  # With math.
```

2) Using `import` but trying to use the short name

WRONG
```python
from math import sqrt
print(math.sqrt(16))  # Error! math not imported
```

CORRECT
```python
from math import sqrt
print(sqrt(16))  # Without math.
```

3) Trying to use a function that isn't imported

WRONG
```python
from math import sqrt
print(math.ceil(3.2))  # Error! ceil not imported
```

CORRECT
```python
from math import sqrt, ceil
print(ceil(3.2))  # Now it's imported
```

## Tips
- Use **`import module`** for whole modules
- Use **`from module import function`** for specific functions
- Always use the **correct name** when calling
- Check the **module name** first!

## Related Concepts
- [[Python - Modules - Module Overview]]
- [[Python - Functions - Definition Basics]]

## MOC
- Parent: [[Python - Modules (MOC)]]

### Error 3: Name conflicts without aliasing
```python
# WRONG: Name conflict, second import overwrites first
from math import sqrt
from numpy import sqrt  # Overwrites math's sqrt!

# Now which sqrt is it? Ambiguous!

# CORRECT: Use aliases
from math import sqrt as math_sqrt
from numpy import sqrt as numpy_sqrt

result1 = math_sqrt(4)
result2 = numpy_sqrt([4, 9])
```

### Error 4: ImportError from wrong module name
```python
# WRONG: Typo in module name
import maths  # Should be 'math', not 'maths'

# ImportError: No module named 'maths'

# CORRECT: Use correct module name
import math
```

### Error 5: Importing before installing third-party modules
```python
# WRONG: Trying to use module that isn't installed
import requests  # ImportError: No module named 'requests'

# CORRECT: Install first (in terminal)
# pip install requests
# Then import:
import requests
```

## Import Best Practices

```python
# ✓ GOOD: Clear and organized
import os
import sys
from datetime import datetime

import numpy as np

from myproject.utils import process_data
from myproject.config import DEFAULT_PATH

# ✓ GOOD: Use aliases for readability
import numpy as np  # Everyone knows 'np'
import pandas as pd  # Everyone knows 'pd'

# ✓ GOOD: Import only what you use
from math import sqrt, ceil  # Specific imports

# ✗ BAD: Import everything
from math import *  # Bad practice

# ✗ BAD: Importing inside loops
for i in range(1000):
    from math import sqrt  # Imports every iteration!

# ✓ GOOD: Import at top of file
from math import sqrt
for i in range(1000):
    result = sqrt(i)  # Use imported function
```

## Tips
- **Import at top of file** — Don't scatter imports throughout.
- **Use specific imports** — `from math import sqrt` rather than `import math`  when possible.
- **Avoid `from module import *`** — It's unclear what you're using.
- **Use aliases** for clarity — `import numpy as np` is clearer than `import numpy`.
- **Organize imports** — Standard library, third-party, local (in order).
- **Check module name** — Common mistake: `maths` vs `math`.
- **Use try-except** for optional modules — Handle missing dependencies gracefully.

## Related Concepts
- [[Python - Modules - What are Modules]]
- [[Python - Modules - Creating Custom Modules]]
- [[Python - Modules - Common Modules (random-math-etc)]]

## MOC
- Parent: [[Python - Modules (MOC)]]
