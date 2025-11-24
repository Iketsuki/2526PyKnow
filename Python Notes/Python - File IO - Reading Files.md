---
tags: [python, file-io, reading, files]
moc: [[Python - File IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `.read()`, `.readline()`, `.readlines()` syntax."
  - "Understand: difference between read methods and when to use each."
  - "Apply: extract and process file content."
  - "Analyze: performance implications for large files."
  - "Create: programs that parse and analyze file data."
---

# Python - File IO - Reading Files

## Concept
Read files using:
- **`.read()`** — Read entire file at once
- **`.readline()`** — Read one line
- **`.readlines()`** — Read all lines as list
- **Loop** — Read line-by-line (most efficient)

## Reading Entire File at Once

```python
# .read() returns entire file as one string
with open('poem.txt', 'r') as f:
    content = f.read()
    print(content)

# Good for small files, loads entire content into memory
# Bad for large files (uses lots of memory)
```

## Reading One Line at a Time

```python
# .readline() reads one line
with open('data.txt', 'r') as f:
    line1 = f.readline()
    print(line1)  # First line (includes \n)
    
    line2 = f.readline()
    print(line2)  # Second line
    
    line3 = f.readline()
    # Returns '' when no more lines
```

## Reading All Lines as List

```python
# .readlines() reads all lines into a list
with open('data.txt', 'r') as f:
    lines = f.readlines()
    print(lines)  # ['Line 1\n', 'Line 2\n', 'Line 3\n']
    
    # Access individual lines
    print(lines[0])  # First line
    print(lines[1])  # Second line
    
    # Loop through lines
    for line in lines:
        print(line.strip())  # strip() removes \n
```

## Line-by-Line Iteration (Most Efficient)

```python
# Loop directly over file object (most efficient)
with open('data.txt', 'r') as f:
    for line in f:
        print(line.strip())  # Process one line at a time

# Better for large files (doesn't load all into memory)
# Each line is read as needed
```

## Processing Content

```python
# Example: Count words
with open('document.txt', 'r') as f:
    content = f.read()
    words = content.split()
    print(f'Total words: {len(words)}')

# Example: Find lines containing keyword
with open('log.txt', 'r') as f:
    for line in f:
        if 'ERROR' in line:
            print(line.strip())

# Example: Extract numbers from lines
with open('data.txt', 'r') as f:
    total = 0
    for line in f:
        try:
            total += float(line.strip())
        except ValueError:
            pass  # Skip non-numeric lines
    print(f'Total: {total}')
```

## Real Examples

```python
# Example 1: Read CSV-like data
with open('scores.txt', 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        name, score = parts[0], parts[1]
        print(f'{name}: {score}')

# Example 2: Read and filter large file
with open('huge_file.log', 'r') as f:
    errors = []
    for line in f:
        if 'ERROR' in line or 'CRITICAL' in line:
            errors.append(line.strip())
    print(f'Found {len(errors)} errors')

# Example 3: Read and transform content
with open('input.txt', 'r') as f:
    lines = f.readlines()

with open('output.txt', 'w') as f:
    for i, line in enumerate(lines, 1):
        f.write(f'{i}: {line}')

# Example 4: Read numbers and calculate
with open('numbers.txt', 'r') as f:
    numbers = [float(line.strip()) for line in f]
    avg = sum(numbers) / len(numbers)
    print(f'Average: {avg}')

# Example 5: Read configuration file
config = {}
with open('config.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):  # Skip comments/empty
            key, value = line.split('=')
            config[key.strip()] = value.strip()
print(config)
```

## Reading Methods Comparison

| Method | Returns | Best For | Memory |
|--------|---------|----------|--------|
| `.read()` | Entire file (string) | Small files, simple access | All in memory |
| `.readline()` | One line (string) | Reading line-by-line manually | One line |
| `.readlines()` | All lines (list) | Need indexed access | All in memory |
| `for line in f` | One line (string) | Large files, iteration | One line |

## Newlines & Stripping

```python
# Lines include trailing newline character \n
with open('data.txt', 'r') as f:
    line = f.readline()
    print(repr(line))  # Shows 'Line 1\n'
    print(line)  # Prints with visible newline
    
    # .strip() removes leading/trailing whitespace
    print(repr(line.strip()))  # Shows 'Line 1' (no \n)
    
    # .rstrip('\n') removes just newline
    print(repr(line.rstrip('\n')))  # Shows 'Line 1' (no \n)
```

## Exercises by Bloom Level

- **Remember**: Call `.read()`, `.readline()`, `.readlines()`.
- **Understand**: When to use each method?
- **Apply**: Read and process a file.
- **Analyze**: Which method for large files? Why?
- **Create**: Build program that parses and analyzes file data.

## Common Errors with Example Code

### Error 1: Forgetting newlines are included
```python
# WRONG: Not aware of \n in lines
with open('data.txt', 'r') as f:
    for line in f:
        print(line)  # Double-spaced (one from \n, one from print())

print(line)  # Line 1
            # (blank line from \n)

# CORRECT: Strip the newline
with open('data.txt', 'r') as f:
    for line in f:
        print(line.strip())  # No double spacing
```

### Error 2: Using .read() on large files
```python
# WRONG: Loading entire large file into memory
with open('huge_file.log', 'r') as f:
    content = f.read()  # Uses lots of RAM!
    for line in content.split('\n'):
        process(line)

# CORRECT: Iterate line-by-line
with open('huge_file.log', 'r') as f:
    for line in f:  # One line at a time
        process(line.strip())
```

### Error 3: Reading multiple times without resetting
```python
# WRONG: Second read returns nothing
with open('data.txt', 'r') as f:
    lines1 = f.readlines()
    lines2 = f.readlines()  # Empty list!

# CORRECT: Store result or seek(0)
with open('data.txt', 'r') as f:
    lines = f.readlines()
    # Use 'lines' twice if needed
    print(lines)
    print(lines)

# OR: Seek back to start
with open('data.txt', 'r') as f:
    lines1 = f.readlines()
    f.seek(0)  # Go back to beginning
    lines2 = f.readlines()  # Now works
```

### Error 4: Comparing line directly without stripping
```python
# WRONG: Comparison fails because of \n
with open('data.txt', 'r') as f:
    for line in f:
        if line == 'error':  # Never true (has \n: 'error\n')
            print('Found error')

# CORRECT: Strip first
with open('data.txt', 'r') as f:
    for line in f:
        if line.strip() == 'error':
            print('Found error')
```

### Error 5: Assuming specific encoding
```python
# WRONG: Default encoding might fail with special characters
with open('utf8_file.txt', 'r') as f:
    content = f.read()  # UnicodeDecodeError on non-ASCII!

# CORRECT: Specify encoding
with open('utf8_file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Or handle different encodings
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    with open('file.txt', 'r', encoding='latin-1') as f:
        content = f.read()
```

## Tips
- Use **`for line in f`** for large files (most efficient).
- Use **`.read()`** only for small files.
- Always **`.strip()`** lines to remove newlines.
- Use **`encoding='utf-8'`** for special characters.
- For CSV data, use **`csv` module** instead of manual splitting.
- For JSON data, use **`json` module** instead of manual parsing.

## Related Concepts
- [[Python - File IO - Opening Files]]
- [[Python - File IO - Writing & Appending]]
- [[Python - File IO - Context Managers]]
- [[Python - Strings - String Methods]]

## MOC
- Parent: [[Python - File IO (MOC)]]
