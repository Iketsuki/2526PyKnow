---
tags: [python, file-io, opening, files]
moc: [[Python - File IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `open()` function syntax and file modes."
  - "Understand: the difference between file modes ('r', 'w', 'a', etc)."
  - "Apply: open files safely with `with` statement."
  - "Analyze: when to use different file modes and access methods."
  - "Create: file-based programs that handle multiple files."
---

# Python - File IO - Opening Files

## Concept
Use `open(filename, mode)` to access files. Always close with `with` statement.

## File Modes

| Mode | Purpose | Creates if Missing | Overwrites? |
|------|---------|-------------------|-------------|
| `'r'` | Read | No (error) | — |
| `'w'` | Write | Yes | Yes |
| `'a'` | Append | Yes | No |
| `'r+'` | Read & Write | No | No |
| `'w+'` | Write & Read | Yes | Yes |
| `'x'` | Exclusive create | Yes | Error if exists |

## Basic File Opening

```python
# WRONG: Not closing the file
f = open('data.txt', 'r')
content = f.read()
# Forgot to close! File stays open

# CORRECT: Use 'with' statement (closes automatically)
with open('data.txt', 'r') as f:
    content = f.read()
# File automatically closed

# If you must close manually
f = open('data.txt', 'r')
try:
    content = f.read()
finally:
    f.close()  # Guaranteed to close
```

## File Modes Explained

### Read Mode ('r')

```python
# Read entire file
with open('data.txt', 'r') as f:
    content = f.read()
    print(content)

# Read line by line
with open('data.txt', 'r') as f:
    for line in f:
        print(line.strip())  # strip() removes newline

# Read all lines as list
with open('data.txt', 'r') as f:
    lines = f.readlines()
    print(lines[0])  # First line
```

### Write Mode ('w')

```python
# Write replaces entire file
with open('output.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.write('Line 2\n')

# File is overwritten, previous content is lost

# Write multiple lines
lines = ['First\n', 'Second\n', 'Third\n']
with open('output.txt', 'w') as f:
    f.writelines(lines)
```

### Append Mode ('a')

```python
# Append adds to end of file
with open('log.txt', 'a') as f:
    f.write('New log entry\n')

# Previous content is preserved

# Append multiple times
with open('log.txt', 'a') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')
```

### Read & Write Modes ('r+', 'w+')

```python
# 'r+': Read and write (file must exist)
with open('data.txt', 'r+') as f:
    content = f.read()
    f.write('\nAdded at end')

# 'w+': Write and read (overwrites)
with open('data.txt', 'w+') as f:
    f.write('New content\n')
    f.seek(0)  # Go back to start
    content = f.read()
    print(content)
```

## Real Examples

```python
# Example 1: Count lines in a file
with open('poem.txt', 'r') as f:
    lines = f.readlines()
    print(f'Total lines: {len(lines)}')

# Example 2: Copy file content
with open('source.txt', 'r') as src:
    content = src.read()

with open('destination.txt', 'w') as dst:
    dst.write(content)

# Example 3: Read and process lines
with open('names.txt', 'r') as f:
    for line in f:
        name = line.strip()
        if name:  # Skip empty lines
            print(f'Hello, {name}!')

# Example 4: Append to log file
import datetime

with open('activity.log', 'a') as f:
    timestamp = datetime.datetime.now()
    f.write(f'{timestamp}: User logged in\n')

# Example 5: Build output file
output_lines = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f, 1):
        output_lines.append(f'{i}: {line}')

with open('numbered_output.txt', 'w') as f:
    f.writelines(output_lines)
```

## File Object Methods

```python
with open('data.txt', 'r') as f:
    # .read() — Read entire file as string
    content = f.read()
    
    # .readline() — Read one line
    f.seek(0)  # Go back to start
    line = f.readline()
    
    # .readlines() — Read all lines as list
    f.seek(0)
    lines = f.readlines()
    
    # .write() — Write string
    # f.write('text\n')  # Only if opened for writing
    
    # .writelines() — Write list of strings
    # f.writelines(['line1\n', 'line2\n'])
    
    # .seek(position) — Move file pointer
    f.seek(0)  # Go to beginning
    
    # .tell() — Get current position
    position = f.tell()
    
    # .close() — Close file (automatic with 'with')
    # Handled automatically with context manager
```

## Checking If File Exists

```python
import os

# Check before reading
if os.path.exists('data.txt'):
    with open('data.txt', 'r') as f:
        content = f.read()
else:
    print('File not found!')

# Using pathlib (modern approach)
from pathlib import Path

if Path('data.txt').exists():
    content = Path('data.txt').read_text()
```

## Exercises by Bloom Level

- **Remember**: Write an `open()` statement with a mode.
- **Understand**: What happens when you open a file in 'w' vs 'a' mode?
- **Apply**: Open, read/write, and close a file using `with`.
- **Analyze**: Why is `with` better than manual `close()`?
- **Create**: Build a program that reads, processes, and writes files.

## Common Errors with Example Code

### Error 1: Not closing files
```python
# WRONG: File never closes
f = open('data.txt', 'r')
content = f.read()
print(content)
# File stays open!

# CORRECT: Use 'with' statement
with open('data.txt', 'r') as f:
    content = f.read()
    print(content)
# File automatically closed
```

### Error 2: Forgetting file doesn't exist in read mode
```python
# WRONG: Trying to read non-existent file
with open('nonexistent.txt', 'r') as f:
    content = f.read()  # FileNotFoundError!

# CORRECT: Check existence or handle error
import os

if os.path.exists('nonexistent.txt'):
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
else:
    print('File not found')

# OR: Use try-except
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found')
```

### Error 3: Confusing write ('w') with append ('a')
```python
# WRONG: Using 'w' when you want to append
with open('log.txt', 'w') as f:
    f.write('Entry 1\n')

with open('log.txt', 'w') as f:  # Overwrites previous!
    f.write('Entry 2\n')

# CORRECT: Use 'a' for appending
with open('log.txt', 'a') as f:
    f.write('Entry 1\n')

with open('log.txt', 'a') as f:  # Appends, doesn't overwrite
    f.write('Entry 2\n')
```

### Error 4: Forgetting to add newlines when writing
```python
# WRONG: Lines run together
with open('output.txt', 'w') as f:
    f.write('Line 1')
    f.write('Line 2')
    f.write('Line 3')

# File contents: "Line 1Line 2Line 3"

# CORRECT: Include newlines
with open('output.txt', 'w') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')
    f.write('Line 3\n')

# File contents: 
# Line 1
# Line 2
# Line 3
```

### Error 5: Using .read() multiple times without seeking
```python
# WRONG: Second read returns empty string
with open('data.txt', 'r') as f:
    content1 = f.read()  # Reads entire file
    content2 = f.read()  # Returns '' (empty!)

# CORRECT: Seek back to start or read once
with open('data.txt', 'r') as f:
    content1 = f.read()
    f.seek(0)  # Go back to beginning
    content2 = f.read()  # Now reads again

# BETTER: Store the result
with open('data.txt', 'r') as f:
    content = f.read()
# Use 'content' multiple times
print(content)
print(content)
```

## Tips
- **Always use `with`** statement (auto-closes, handles errors).
- Use **`'r'`** for reading (file must exist).
- Use **`'w'`** for writing (overwrites existing).
- Use **`'a'`** for appending (adds to end).
- **Add `\n`** to preserve line breaks when writing.
- Use **`f.strip()`** on lines to remove trailing newline.
- Check **file existence** before opening in 'r' mode.

## Related Concepts
- [[Python - File IO - Reading Files]]
- [[Python - File IO - Writing & Appending]]
- [[Python - File IO - Context Managers]]
- [[Python - Error Handling - Try-Except Basics]]

## MOC
- Parent: [[Python - File IO (MOC)]]
