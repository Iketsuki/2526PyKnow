---
tags: [python, file-io, writing, appending]
moc: [[Python - File IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `.write()` and `.writelines()` syntax."
  - "Understand: `'w'` overwrites vs `'a'` appends behavior."
  - "Apply: save and update data in files."
  - "Analyze: when to use different write modes and methods."
  - "Create: programs that log data and save user input."
---

# Python - File IO - Writing & Appending

## Concept
Write to files using:
- **`.write(string)`** — Write string to file
- **`.writelines(list)`** — Write list of strings
- **`'w'` mode** — Overwrite (replaces all)
- **`'a'` mode** — Append (adds to end)

## Writing Files (Overwrite Mode)

```python
# .write() overwrites existing content
with open('data.txt', 'w') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')

# File now contains:
# Line 1
# Line 2

# Opening again in 'w' mode erases previous content
with open('data.txt', 'w') as f:
    f.write('New content\n')

# File now contains only:
# New content
```

## Writing Multiple Lines

```python
# .writelines() writes a list of strings
lines = ['First\n', 'Second\n', 'Third\n']

with open('output.txt', 'w') as f:
    f.writelines(lines)

# File contains:
# First
# Second
# Third

# Note: writelines() doesn't add newlines!
lines = ['First', 'Second', 'Third']
with open('output.txt', 'w') as f:
    f.writelines(lines)
# File contains: FirstSecondThird (all on one line!)
```

## Appending to Files

```python
# 'a' mode appends to existing file
with open('log.txt', 'a') as f:
    f.write('First log entry\n')

# File contains:
# First log entry

# Append again (doesn't erase)
with open('log.txt', 'a') as f:
    f.write('Second log entry\n')

# File now contains:
# First log entry
# Second log entry
```

## Formatting Output

```python
# Write formatted strings
name = 'Alice'
score = 95

with open('result.txt', 'w') as f:
    f.write(f'Name: {name}\n')
    f.write(f'Score: {score}\n')

# Write with join() (efficient)
lines = ['Name: Alice\n', 'Score: 95\n']
with open('result.txt', 'w') as f:
    f.write(''.join(lines))

# Write with custom formatting
students = [('Alice', 90), ('Bob', 85), ('Charlie', 92)]

with open('grades.txt', 'w') as f:
    for name, grade in students:
        f.write(f'{name:10} {grade:3}\n')
```

## Real Examples

```python
# Example 1: Save user input to file
with open('notes.txt', 'a') as f:
    note = input('Enter a note: ')
    f.write(f'{note}\n')

# Example 2: Create a simple log file
import datetime

with open('activity.log', 'a') as f:
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(f'[{timestamp}] Program started\n')

# Example 3: Convert and save data
temperatures = [72.5, 75.3, 74.1, 76.8]

with open('temps.txt', 'w') as f:
    for i, temp in enumerate(temperatures, 1):
        f.write(f'Day {i}: {temp}°F\n')

# Example 4: Generate report
results = {
    'Total Tests': 10,
    'Passed': 8,
    'Failed': 2,
    'Pass Rate': '80%'
}

with open('report.txt', 'w') as f:
    f.write('=' * 40 + '\n')
    f.write('TEST REPORT\n')
    f.write('=' * 40 + '\n')
    for key, value in results.items():
        f.write(f'{key}: {value}\n')

# Example 5: Append to existing file with header protection
import os

filename = 'data.csv'
needs_header = not os.path.exists(filename)

mode = 'a'  # Append

with open(filename, mode) as f:
    if needs_header:
        f.write('Name,Age,City\n')
    
    f.write('Alice,25,NYC\n')
    f.write('Bob,30,LA\n')
```

## File Writing Methods Comparison

| Method | What It Does | Best For |
|--------|------------|----------|
| `.write(str)` | Write one string | Single values, formatted strings |
| `.writelines(list)` | Write list of strings | Multiple strings, but add `\n` manually |
| Multiple `.write()` calls | Write several times | Building output incrementally |
| `f.write(''.join(list))` | Write joined list | Efficient, avoids many calls |

## Exercises by Bloom Level

- **Remember**: Call `.write()` and `.writelines()`.
- **Understand**: What's the difference between `'w'` and `'a'` modes?
- **Apply**: Save user input or processed data to a file.
- **Analyze**: When should you overwrite vs append?
- **Create**: Build a log program or data saver.

## Common Errors with Example Code

### Error 1: Using 'w' when you want to append
```python
# WRONG: Accidentally overwriting existing data
with open('log.txt', 'w') as f:
    f.write('Entry 1\n')

with open('log.txt', 'w') as f:  # Oops! Erased Entry 1
    f.write('Entry 2\n')

# File contains only "Entry 2\n"

# CORRECT: Use 'a' to append
with open('log.txt', 'a') as f:
    f.write('Entry 1\n')

with open('log.txt', 'a') as f:
    f.write('Entry 2\n')

# File contains both entries
```

### Error 2: Forgetting newlines
```python
# WRONG: Lines run together
with open('output.txt', 'w') as f:
    f.write('Line 1')
    f.write('Line 2')
    f.write('Line 3')

# File contents: "Line 1Line 2Line 3" (all on one line!)

# CORRECT: Include \n
with open('output.txt', 'w') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')
    f.write('Line 3\n')

# File contents:
# Line 1
# Line 2
# Line 3
```

### Error 3: writelines() doesn't add newlines automatically
```python
# WRONG: Expecting automatic newlines
lines = ['apple', 'banana', 'cherry']

with open('fruits.txt', 'w') as f:
    f.writelines(lines)

# File contents: "applebananaclerry" (no newlines!)

# CORRECT: Add \n to each line first
lines = ['apple\n', 'banana\n', 'cherry\n']

with open('fruits.txt', 'w') as f:
    f.writelines(lines)

# OR: Use a loop with write()
with open('fruits.txt', 'w') as f:
    for fruit in lines:
        f.write(f'{fruit}\n')
```

### Error 4: Not checking file permissions
```python
# WRONG: Assuming you can write
with open('/root/protected.txt', 'w') as f:  # PermissionError!
    f.write('data')

# CORRECT: Handle permission errors
try:
    with open('output.txt', 'w') as f:
        f.write('data')
except PermissionError:
    print('Cannot write to this location')
```

### Error 5: Trying to read and write simultaneously
```python
# WRONG: Opening in 'w' mode then trying to read
with open('data.txt', 'w') as f:
    f.write('data')
    content = f.read()  # Error! Can't read in write mode

# CORRECT: Use 'w+' or separate operations
with open('data.txt', 'w+') as f:
    f.write('data')
    f.seek(0)  # Go back to start
    content = f.read()
    print(content)  # 'data'

# OR: Use separate file opens
with open('data.txt', 'w') as f:
    f.write('data')

with open('data.txt', 'r') as f:
    content = f.read()
```

## Tips
- **Always include `\n`** when writing lines.
- Use **`'w'`** to create new or replace files.
- Use **`'a'`** to add data to existing files.
- Use **`.write()`** for single strings, control output exactly.
- Use **`.writelines()`** only if strings already have `\n`.
- Use **`f.write(''.join(list))`** for efficient batch writing.
- **Test overwrites** — make sure you really want 'w' mode!

## Related Concepts
- [[Python - File IO - Opening Files]]
- [[Python - File IO - Reading Files]]
- [[Python - File IO - Context Managers]]
- [[Python - Strings - String Methods]]

## MOC
- Parent: [[Python - File IO (MOC)]]
