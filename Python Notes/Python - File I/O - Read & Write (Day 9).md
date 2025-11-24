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

## Common Errors
- Forgetting file paths or writing without closing (use `with`).

## Notes for 14‑year‑olds
- Files are created in the folder where you run the script; check your folder if you can't find the file.

## MOC
- Beginner path: [[Python - 14-Day Beginner Path (MOC)]]
