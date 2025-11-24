---
tags: [python, file-io, context-managers, with]
moc: [[Python - File IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `with` statement syntax."
  - "Understand: why `with` is safer than manual close()."
  - "Apply: always use `with` for files and resources."
  - "Analyze: context manager protocol (__enter__, __exit__)."
  - "Create: custom context managers for other resources."
---

# Python - File IO - Context Managers

## Concept
The `with` statement (context manager) automatically closes files even if errors occur. Prevents resource leaks.

## Why `with` Matters

```python
# BAD: File might not close if error occurs
f = open('data.txt', 'r')
content = f.read()
# What if an error happens here?
f.close()  # Might never execute!

# GOOD: Guarantees closure even with errors
with open('data.txt', 'r') as f:
    content = f.read()
# File always closes here, no matter what
```

## Basic Syntax

```python
# Single file
with open('data.txt', 'r') as f:
    content = f.read()

# Multiple files
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    outfile.write(infile.read())

# Nested files
with open('source.txt', 'r') as src:
    with open('dest.txt', 'w') as dst:
        dst.write(src.read())
```

## File Operations with `with`

```python
# Reading
with open('data.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Writing
with open('output.txt', 'w') as f:
    f.write('Hello\n')
    f.write('World\n')

# Appending
with open('log.txt', 'a') as f:
    f.write('New log entry\n')

# Read and modify
with open('data.txt', 'r+') as f:
    content = f.read()
    modified = content.replace('old', 'new')
    f.seek(0)
    f.write(modified)
```

## Multiple Files

```python
# Process input file and write to output
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        upper_line = line.upper()
        outfile.write(upper_line)

# Copy file
with open('source.txt', 'r') as src, open('backup.txt', 'w') as dst:
    dst.write(src.read())

# Process multiple input files
with open('data1.txt', 'r') as f1, open('data2.txt', 'r') as f2, open('combined.txt', 'w') as out:
    out.write(f1.read())
    out.write('\n')
    out.write(f2.read())
```

## Exception Handling with `with`

```python
# with statement handles errors gracefully
try:
    with open('data.txt', 'r') as f:
        content = f.read()
        # Even if error happens here, file closes
        number = int(content)  # Might raise ValueError
except FileNotFoundError:
    print('File not found')
except ValueError:
    print('Invalid content')
# File is guaranteed to be closed

# Manual close approach is error-prone
try:
    f = open('data.txt', 'r')
    content = f.read()
    number = int(content)
except (FileNotFoundError, ValueError) as e:
    print(f'Error: {e}')
finally:
    f.close()  # Must remember to close
```

## Real Examples

```python
# Example 1: Count lines in file
with open('poem.txt', 'r') as f:
    line_count = sum(1 for _ in f)
print(f'Total lines: {line_count}')

# Example 2: Filter and save data
with open('raw_data.txt', 'r') as input_file:
    lines = [line for line in input_file if 'important' in line]

with open('filtered_data.txt', 'w') as output_file:
    output_file.writelines(lines)

# Example 3: Process and combine files
with open('data1.txt', 'r') as f1, open('data2.txt', 'r') as f2:
    content1 = f1.read()
    content2 = f2.read()

with open('combined.txt', 'w') as output:
    output.write('=== File 1 ===\n')
    output.write(content1)
    output.write('\n=== File 2 ===\n')
    output.write(content2)

# Example 4: Transform and save
import csv

with open('input.csv', 'r') as infile, open('output.csv', 'w') as outfile:
    for line in infile:
        parts = line.strip().split(',')
        # Transform data
        transformed = ','.join(part.upper() for part in parts)
        outfile.write(f'{transformed}\n')

# Example 5: Safe file editing (read-modify-write)
import shutil

# Backup original
shutil.copy('data.txt', 'data.txt.bak')

# Edit file
with open('data.txt', 'r') as input_file, open('data_temp.txt', 'w') as temp_file:
    for line in input_file:
        modified_line = line.replace('old_value', 'new_value')
        temp_file.write(modified_line)

# Replace original with modified
import os
os.replace('data_temp.txt', 'data.txt')
```

## How Context Managers Work

```python
# Context managers use __enter__ and __exit__ methods
class MyContextManager:
    def __enter__(self):
        print('Entering context')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting context')
        # Clean up resources here
        return False  # Don't suppress exceptions

# Use it
with MyContextManager() as cm:
    print('Inside context')

# Output:
# Entering context
# Inside context
# Exiting context

# Files implement this protocol
# open().__enter__() returns the file object
# open().__exit__() closes the file
```

## Exercises by Bloom Level

- **Remember**: Write a `with` statement for opening a file.
- **Understand**: Why does `with` guarantee file closure?
- **Apply**: Use `with` for multiple file operations.
- **Analyze**: What happens if error occurs inside `with` block?
- **Create**: Build programs that safely process multiple files.

## Common Errors with Example Code

### Error 1: Not using `with` statement
```python
# WRONG: File might not close if error occurs
f = open('data.txt', 'r')
content = f.read()
if len(content) > 1000:
    raise ValueError('File too large')
f.close()  # Skipped if error occurs!

# CORRECT: Use with
with open('data.txt', 'r') as f:
    content = f.read()
    if len(content) > 1000:
        raise ValueError('File too large')
# File guaranteed to close even with error
```

### Error 2: Trying to use file after `with` block
```python
# WRONG: Using file object outside with block
with open('data.txt', 'r') as f:
    data = f.read()

f.write('more data')  # ValueError: I/O operation on closed file

# CORRECT: Use data inside with block
with open('data.txt', 'r') as f:
    data = f.read()
    # Process data here

# Or store data and process later
with open('data.txt', 'r') as f:
    data = f.read()

# Now process data (file is closed, but data is stored)
result = process(data)
```

### Error 3: Forgetting `as` keyword
```python
# WRONG: Not assigning file to variable
with open('data.txt', 'r'):
    content = f.read()  # NameError: f not defined

# CORRECT: Use 'as' to assign
with open('data.txt', 'r') as f:
    content = f.read()
```

### Error 4: Multiple files with wrong syntax
```python
# WRONG: Nested with blocks are verbose
with open('input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        outfile.write(infile.read())

# BETTER: Use comma syntax
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    outfile.write(infile.read())
```

### Error 5: Exception suppression
```python
# WRONG: Trying to suppress exceptions
with open('data.txt', 'r') as f:
    content = f.read()
    number = int(content)  # ValueError not caught!

# CORRECT: Use try-except
try:
    with open('data.txt', 'r') as f:
        content = f.read()
        number = int(content)
except ValueError:
    print('Invalid content')
```

## Context Manager Advantages

| Advantage | Explanation |
|-----------|------------|
| **Auto-closes** | File closes automatically, no need for `.close()` |
| **Handles errors** | Closes even if exception occurs |
| **Readable** | Clear indentation shows scope |
| **Resource safe** | Prevents file handle leaks |
| **Supports multiple** | Can open multiple files in one statement |

## Tips
- **Always use `with`** for files (standard Python practice).
- **Never use direct `open()` without `with`**.
- Use **comma syntax** for multiple files on one line.
- Use **nested `with`** if you prefer readability over brevity.
- **Try-except works with `with`** — exceptions still bubble up.
- Context managers work for **any resource** (files, database connections, locks, etc.).

## Related Concepts
- [[Python - File IO - Opening Files]]
- [[Python - File IO - Reading Files]]
- [[Python - File IO - Writing & Appending]]
- [[Python - Error Handling - Try-Except Basics]]

## MOC
- Parent: [[Python - File IO (MOC)]]
