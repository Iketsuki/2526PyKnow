---
tags: [python, file-io, reading, writing, beginner]
moc: [[Python - File I/O (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: open(), read(), write() syntax."
  - "Understand: what files are and how Python reads/writes them."
  - "Apply: write programs that save and load data."
---

# Python - File I/O - Read & Write (Day 9)

## What is a File?

A **file** is like a notebook where a computer stores information. Your program can:
- **Write** (save) information to a file
- **Read** (load) information from a file

Files are stored on your computer's hard drive. When you close the program, the file stays there.

## Opening a File

Before you read or write, you must **open** the file first.

```python
# Open a file to read
file = open('names.txt', 'r')

# Open a file to write (creates new or replaces old)
file = open('names.txt', 'w')

# When done, close the file
file.close()
```

The second part (`'r'` or `'w'`) tells Python what you want to do:
- `'r'` = read (look at the file)
- `'w'` = write (create or replace the file)
- `'a'` = append (add to the end)

## Reading a Whole File

```python
# Open file to read
file = open('names.txt', 'r')

# Read everything
content = file.read()
print(content)

# Close the file
file.close()
```

The `.read()` method gives you all the text as one big string.

## Reading Line by Line

```python
# Open file
file = open('names.txt', 'r')

# Read each line
for line in file:
    print(line)

# Close the file
file.close()
```

Each `line` includes the text plus a newline character `\n` at the end.

## Writing to a File

```python
# Open file to write (creates new file)
file = open('names.txt', 'w')

# Write text
file.write('Alice\n')
file.write('Bob\n')
file.write('Charlie\n')

# Close file
file.close()
```

**Important:** `write()` doesn't add a newline automatically. Use `\n` to go to the next line.

## Reading and Printing

Here's a program that reads a file and prints each line:

```python
# Open file
file = open('scores.txt', 'r')

# Read and print
for line in file:
    print(line)

# Close file
file.close()
```

If your file has:
```
Alice: 95
Bob: 87
Charlie: 92
```

It prints:
```
Alice: 95
Bob: 87
Charlie: 92
```

## Writing and Saving

Here's a program that saves names to a file:

```python
# Create list of names
names = ['Alice', 'Bob', 'Charlie']

# Open file to write
file = open('names.txt', 'w')

# Write each name
for name in names:
    file.write(name + '\n')

# Close file
file.close()

print('Saved!')
```

This creates a file with three lines (one name each).

## The Safe Way: Using `with`

**Better way to read/write files:**

```python
# Read safely
with open('names.txt', 'r') as file:
    content = file.read()
    print(content)
# File closes automatically!

# Write safely
with open('names.txt', 'w') as file:
    file.write('Alice\n')
    file.write('Bob\n')
# File closes automatically!
```

The `with` statement closes the file automatically. You don't need `.close()`.

## Real-World: Save Scores

```python
# Get scores from user
scores = []
for i in range(3):
    score = input(f'Score {i+1}: ')
    scores.append(score + '\n')

# Save to file
with open('scores.txt', 'w') as file:
    for score in scores:
        file.write(score)

print('Scores saved!')
```

## Real-World: Load and Print

```python
# Load scores from file
with open('scores.txt', 'r') as file:
    for line in file:
        print(line)
```

## Common Errors with Example Code

1) Forgetting to close the file

WRONG
```python
file = open('data.txt', 'r')
content = file.read()
print(content)
# File never closes! Wastes memory
```

CORRECT
```python
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)
# Closes automatically
```

2) Trying to read a file that doesn't exist

WRONG
```python
file = open('missing.txt', 'r')
# Error: FileNotFoundError
```

CORRECT
```python
try:
    with open('missing.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('File not found')
```

3) Writing when you want to add to a file

WRONG
```python
with open('names.txt', 'w') as file:
    file.write('Diana\n')
# Erases old names! Creates new file
```

CORRECT - Use 'a' to add
```python
with open('names.txt', 'a') as file:
    file.write('Diana\n')
# Keeps old names, adds Diana
```

## Tips
- Use **`with` statement** to safely open/close files
- Use **`'r'` to read**, **`'w'` to write**, **`'a'` to append**
- Always add **`\n`** after text to go to next line
- Use **`for line in file:`** to read line by line

## Related Concepts
- [[Python - File IO - Opening Files]]
- [[Python - File IO - Reading Files]]
- [[Python - File IO - Writing & Appending]]
- [[Python - Debugging - Try-Except Basics]]

## MOC
- Parent: [[Python - File I/O (MOC)]]
