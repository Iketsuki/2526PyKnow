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

## Concept
Import modules using:
- **`import module`** — Use as `module.function()`
- **`from module import function`** — Use as `function()`
- **`from module import name as alias`** — Rename for clarity
- **`from module import *`** — Import all (generally avoid)

## Basic Import (import module)

```python
import math

# Access functions with module.function()
print(math.sqrt(16))  # 4.0
print(math.pi)  # 3.14159...
print(math.ceil(3.2))  # 4

# You have access to everything in the module
print(dir(math))  # Lists all available functions/constants
```

## From Import (from module import function)

```python
from math import sqrt, pi

# Use function directly without module prefix
print(sqrt(16))  # 4.0
print(pi)  # 3.14159...

# Only imported items are available
# print(math.ceil(3.2))  # Error: math not imported
print(ceil(3.2))  # Error: ceil not imported (not explicitly imported)
```

## Aliasing (as)

```python
# Rename to shorter name
import numpy as np
array = np.array([1, 2, 3])

# Rename specific function
from datetime import datetime as dt
today = dt.now()

# Useful for avoiding name conflicts
from PIL import Image as PILImage
from matplotlib import Image as MatplotlibImage

# Can use either without confusion
```

## Relative Imports (Modules within Modules)

```python
# Standard library: nested modules
import os.path  # path is a module within os

# Your code:
# myproject/
#   utils.py
#   helpers/
#     __init__.py
#     formatter.py

# In myproject/helpers/formatter.py:
from ..utils import process  # Go up one level, then to utils

# Or absolute import:
from myproject.utils import process
```

## Real Examples

```python
# Example 1: Using datetime module
from datetime import datetime, timedelta

today = datetime.now()
tomorrow = today + timedelta(days=1)
print(f'Today: {today}')
print(f'Tomorrow: {tomorrow}')

# Example 2: Using multiple modules
import random
import math
from statistics import mean

numbers = [random.randint(1, 10) for _ in range(5)]
average = mean(numbers)
rounded = math.ceil(average)
print(f'Numbers: {numbers}, Average: {average}, Rounded: {rounded}')

# Example 3: Avoid name conflicts
from math import sqrt as math_sqrt
from numpy import sqrt as np_sqrt

# Can use both
val1 = math_sqrt(4)  # Uses math version
val2 = np_sqrt([4, 9, 16])  # Uses numpy version

# Example 4: Import specific items you need
from string import ascii_letters, digits, punctuation

print(f'Letters: {ascii_letters}')
print(f'Digits: {digits}')

# Example 5: Conditional imports
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    np = None

if HAS_NUMPY:
    array = np.array([1, 2, 3])
else:
    array = [1, 2, 3]  # Use list instead
```

## Import Styles Comparison

| Style | Syntax | Usage | Best For |
|-------|--------|-------|----------|
| Module | `import math` | `math.sqrt()` | General use |
| Specific | `from math import sqrt` | `sqrt()` | Frequently used items |
| Alias | `import numpy as np` | `np.array()` | Long module names |
| Multiple | `from math import sqrt, pi` | `sqrt()`, `pi` | Multiple items from module |

## Standard Import Organization

```python
# Order: Standard library, third-party, local modules
import sys
import os
from datetime import datetime

import numpy as np
import pandas as pd

from myproject.utils import helper
from myproject.config import settings
```

## Exercises by Bloom Level

- **Remember**: Write `import` and `from...import` statements.
- **Understand**: Difference between import styles?
- **Apply**: Import modules and use their functions.
- **Analyze**: When to use each style for clarity?
- **Create**: Organize imports and create your own modules.

## Common Errors with Example Code

### Error 1: Using function name when module not imported
```python
# WRONG: Function used but not imported
from math import sqrt
# But then trying to use:
result = math.sqrt(16)  # NameError: name 'math' is not defined

# CORRECT: Use the imported name
result = sqrt(16)

# OR: Import the module
import math
result = math.sqrt(16)
```

### Error 2: Forgetting module name prefix
```python
# WRONG: Using function without importing it directly
import math

result = sqrt(16)  # NameError: name 'sqrt' is not defined

# CORRECT: Use module prefix or from-import
result = math.sqrt(16)

# OR:
from math import sqrt
result = sqrt(16)
```

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
