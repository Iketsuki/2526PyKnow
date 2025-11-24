---
tags: [python, io, output-targets]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: print can target console, files, or format strings."
  - "Understand: different output destinations."
  - "Apply: print to console vs files."
---

# Python - IO - Output Targets (Screen vs File vs Strings)

## Concept
Print to the console with `print()`, to files with `.write()`, or build strings with `f''` for later use.

## Output to Console (Screen)

```python
print('Simple output')
print('Name:', 'Alice', sep=' | ')
print('A', 'B', 'C', end='')  # No newline
```

## Output to File

```python
# Write to file (overwrites)
with open('output.txt', 'w') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')

# Append to file
with open('output.txt', 'a') as f:
    f.write('Line 3\n')
```

## Build Strings (for later use)

```python
# F-string stores in variable
message = f'Hello, Alice. You are 15 years old.'
print(message)

# Build with concatenation
result = 'Sum: ' + str(5 + 3)
print(result)

# Build with join (efficient for many strings)
parts = ['Item 1', 'Item 2', 'Item 3']
output = ', '.join(parts)
print(output)
```

## Exercises by Bloom Level
- Remember: Use `sep` and `end` in print.
- Understand: When use file vs console?
- Apply: Write data to a file.
- Analyze: Compare string building methods.
- Create: Build formatted output that saves to file.

## Related Concepts
- [[Python - IO - Print Basics]]
- [[Python - File IO - Writing & Appending]]
- [[Python - Strings - String Formatting]]

## MOC
- Parent: [[Python - IO (MOC)]]
