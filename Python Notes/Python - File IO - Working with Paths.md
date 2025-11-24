---
tags: [python, file-io, paths]
moc: [[Python - File IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: relative vs absolute paths."
  - "Understand: where files are created."
  - "Apply: work with file paths."
---

# Python - File IO - Working with Paths

## Concept
Paths can be relative (from current folder) or absolute (full path). Use `pathlib` or `os.path` for portability.

## Example Code
```python
# Relative
with open('data.txt', 'r') as f:
    pass

# Absolute (Windows)
with open('C:\\Users\\Name\\data.txt', 'r') as f:
    pass

# Using pathlib (modern)
from pathlib import Path
p = Path('data.txt')
```

## Exercises by Bloom Level
- Remember: Open a file with a path.
- Understand: Relative vs absolute?
- Apply: Work with different paths.
- Analyze: Why use `pathlib`?
- Create: Build cross-platform file utilities.
 
## Common Errors with Example Code

### Error 1: Using wrong path separators (platform-specific)
```python
# WRONG: Hardcoding Unix-style paths on Windows
open('/home/user/data.txt', 'r')  # FileNotFoundError on Windows

# CORRECT: Use pathlib or os.path.join
from pathlib import Path
Path('data.txt').read_text()

from os import path
path.join('folder', 'file.txt')
```

### Error 2: Assuming current working directory
```python
# WRONG: Relative path failing because CWD differs
open('data.txt', 'r')  # FileNotFoundError when CWD is different

# CORRECT: Make paths relative to script file or use absolute paths
from pathlib import Path
BASE = Path(__file__).parent
with open(BASE / 'data.txt', 'r') as f:
  content = f.read()
```

### Error 3: Forgetting to escape backslashes on Windows
```python
# WRONG: Unescaped backslash creates escape sequences
open('C:\Users\name\data.txt', 'r')  # May work but fragile

# BETTER: Use raw strings or pathlib
open(r'C:\Users\name\data.txt', 'r')
from pathlib import Path
Path('C:/Users/name/data.txt').read_text()
```

### Error 4: Not handling missing parent directories when writing
```python
# WRONG: Writing to nested folder without creating it
with open('logs/2025/nov/log.txt', 'w') as f:
  f.write('log')  # FileNotFoundError if folder missing

# CORRECT: Create parents first
from pathlib import Path
Path('logs/2025/nov').mkdir(parents=True, exist_ok=True)
with open('logs/2025/nov/log.txt', 'w') as f:
  f.write('log')
```

### Error 5: Mixing Path and str incorrectly
```python
# WRONG: Passing Path to APIs expecting str in some older libs
p = Path('data.txt')
some_api(p)  # Might error if API expects str

# CORRECT: Convert to str when needed
some_api(str(p))
```

## MOC
- Parent: [[Python - File IO (MOC)]]
