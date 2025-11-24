---
tags: [python, io, error-handling]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: common IO errors (ValueError, FileNotFoundError)."
  - "Understand: when errors occur in IO."
  - "Apply: handle IO errors gracefully."
---

# Python - IO - Error Handling in Input/Output

## Concept
Handle errors when reading input or files using `try-except`. Common errors: `ValueError` (bad number), `FileNotFoundError` (missing file), `IOError` (file access).

## Handling Bad Input

```python
# Problem: user enters "hello" when expecting a number
try:
    age = int(input('Age: '))
except ValueError:
    print('Please enter a valid number.')
    age = 0  # Default value
```

## Handling File Errors

```python
# Problem: file doesn't exist
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found. Creating a new one.')
    with open('data.txt', 'w') as f:
        f.write('Initial content')
```

## Robust Input Loop

```python
# Keep asking until valid
while True:
    try:
        score = int(input('Score (0-100): '))
        if not (0 <= score <= 100):
            print('Score must be 0-100.')
            continue
        break
    except ValueError:
        print('Please enter a number.')
```

## Exercises by Bloom Level
- Remember: Write a try-except for input.
- Understand: What causes ValueError in input?
- Apply: Handle file and input errors.
- Analyze: When use try-except vs validation?
- Create: Build robust input with error recovery.

## Related Concepts
- [[Python - Debugging - Try-Except Basics]]
- [[Python - IO - Input Validation]]
- [[Python - File IO - Opening Files]]

## Common Errors with Example Code

Below are common mistakes when handling IO and how to fix them. Each example shows a WRONG (buggy) snippet and a CORRECT fix.

1) Wrong type from input (ValueError)

WRONG
```python
# expecting an int but not handling bad input
age = int(input('Age: '))
print('Next year you will be', age + 1)
```

CORRECT
```python
while True:
    try:
        age = int(input('Age: '))
        break
    except ValueError:
        print('Please enter a whole number for age.')
print('Next year you will be', age + 1)
```

2) File not found when opening for read (FileNotFoundError)

WRONG
```python
# this crashes if file is missing
with open('config.txt', 'r') as f:
    cfg = f.read()
```

CORRECT
```python
try:
    with open('config.txt', 'r') as f:
        cfg = f.read()
except FileNotFoundError:
    print('config.txt not found — using defaults')
    cfg = ''
```

3) Catching everything with a bare except (hides bugs)

WRONG
```python
try:
    # several IO operations
    data = open('data.txt').read()
    value = int(data)
except:
    print('Something went wrong')
```

CORRECT
```python
try:
    with open('data.txt', 'r', encoding='utf-8') as f:
        data = f.read()
    value = int(data)
except FileNotFoundError:
    print('data.txt missing — create or provide the file')
except ValueError:
    print('data.txt does not contain a valid integer')
```

Short notes:
- Always catch specific exceptions you expect.
- Validate user input before conversion.
- Use context managers (with) to ensure files close.

## MOC
- Parent: [[Python - IO (MOC)]]
