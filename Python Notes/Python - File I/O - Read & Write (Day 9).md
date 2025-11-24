---
tags: [python, file-io, beginner]
moc: [[Python - 14-Day Beginner Path (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: open and close files."
  - "Understand: difference between reading and writing."
  - "Apply: save a small note to a file and read it back."
---

# Python - File I/O - Read & Write (Day 9)

## Concept
File I/O lets programs save and read information from disk. Use `open()` with modes `'w'` (write) and `'r'` (read), or use `with` to auto-close.

## Example Code
```python
# Write a note to a file
with open('note.txt', 'w') as f:
    f.write('This is my first file!\n')

# Read it back
with open('note.txt', 'r') as f:
    text = f.read()
    print(text)
```

## Exercises by Bloom Level
- Remember: What does `with open(..., 'w')` do?
- Understand: Why use `with` instead of `open()` and `close()`?
- Apply: Ask the user for a line and append it to a file.
- Analyze: What happens if the file doesn't exist when reading?
- Create: Make a simple diary program that appends the date and text to a file.

## Common Errors with Example Code

1) Forgetting to use `with` statement → File not properly closed

WRONG
f = open('note.txt', 'w')
f.write('Hello')
# Forgot to close! File stays open in memory.

CORRECT
with open('note.txt', 'w') as f:
    f.write('Hello')
# Auto-closed when exiting with block

2) Writing and reading without specifying mode → Wrong mode for operation

WRONG
# Trying to read from write mode:
with open('note.txt', 'w') as f:
    text = f.read()  # ValueError: not readable

CORRECT
# Use 'r' for reading:
with open('note.txt', 'r') as f:
    text = f.read()
    print(text)

# Use 'w' for writing:
with open('note.txt', 'w') as f:
    f.write('Hello')

3) File not found when trying to read → File doesn't exist or wrong path

WRONG
with open('missing.txt', 'r') as f:
    text = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'

CORRECT
import os
filename = 'note.txt'

if os.path.exists(filename):
    with open(filename, 'r') as f:
        text = f.read()
        print(text)
else:
    print(f'File {filename} not found')

## Notes for 14‑year‑olds
- Files are created in the folder where you run the script; check your folder if you can't find the file.

## MOC
- Beginner path: [[Python - 14-Day Beginner Path (MOC)]]
