---
tags: [python, strings, methods]
moc: [[Python - Strings (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: common string methods."
  - "Understand: what each method does."
  - "Apply: use methods to process text."
---

# Python - Strings - String Methods

## Concept
**Methods** — actions on strings. Main ones: `upper()`, `lower()`, `strip()`, `replace()`, `split()`, `join()`, `find()`, `count()`.

## Case Conversion

```python
text = 'Hello World'

print(text.upper())  # HELLO WORLD
print(text.lower())  # hello world
print(text.title())  # Hello World

# Useful for case-insensitive comparison
if text.lower() == 'hello world':
    print('Match!')
```

## Whitespace Handling

```python
text = '  Hello  '

print(text.strip())  # 'Hello' (remove both sides)
print(text.lstrip())  # 'Hello  ' (remove left)
print(text.rstrip())  # '  Hello' (remove right)

# Real-world: clean user input
name = input('Name: ').strip()  # Remove accidental spaces
```

## Finding & Replacing

```python
text = 'Hello World'

# Find position
pos = text.find('World')
print(pos)  # 6 (index where 'World' starts)

pos = text.find('xyz')
print(pos)  # -1 (not found)

# Replace
new_text = text.replace('World', 'Python')
print(new_text)  # Hello Python

# Replace only first occurrence
text2 = 'banana'
print(text2.replace('a', 'o', 1))  # bonana (only 1 'a')
```

## Splitting & Joining

```python
# Split string into list
text = 'apple,banana,cherry'
fruits = text.split(',')
print(fruits)  # ['apple', 'banana', 'cherry']

# Default splits on whitespace
sentence = 'Hello my dear friend'
words = sentence.split()
print(words)  # ['Hello', 'my', 'dear', 'friend']

# Join list into string
items = ['apple', 'banana', 'cherry']
text = ', '.join(items)
print(text)  # apple, banana, cherry
```

## Counting

```python
text = 'banana'

count = text.count('a')
print(count)  # 3

sentence = 'The quick brown fox'
count = sentence.count('the', 0, 10)  # Count in range
print(count)  # 0 (case-sensitive)
```

## Checking Content

```python
text = 'Hello123'

print(text.isalpha())  # False (has numbers)
print(text.isdigit())  # False (has letters)
print(text.isalnum())  # True (only letters and numbers)

# Check if starts/ends with
filename = 'photo.jpg'
if filename.endswith('.jpg'):
    print('Image file')

if filename.startswith('photo'):
    print('Photo file')
```

## Real-World: Text Processing

```python
# Process user input (emails)
email = '  ALICE@EXAMPLE.COM  '
email = email.strip().lower()
print(email)  # alice@example.com

# Parse CSV line
line = 'Alice,15,NYC'
parts = line.split(',')
name, age, city = parts
print(f'{name} is {age} years old')
```

## Real-World: Text Cleaning

```python
# Clean noisy data
messy = '   hello   world   '
clean = messy.strip().replace('   ', ' ')
print(clean)  # hello world

# Or use split/join combo
words = messy.split()
clean = ' '.join(words)
print(clean)  # hello world
```

## Real-World: Building CSV

```python
# Create CSV from data
students = [('Alice', 15, 'A'), ('Bob', 14, 'B'), ('Charlie', 15, 'A')]

csv_lines = []
for name, age, grade in students:
    line = ','.join([name, str(age), grade])
    csv_lines.append(line)

csv_text = '\n'.join(csv_lines)
print(csv_text)
# Output:
# Alice,15,A
# Bob,14,B
# Charlie,15,A
```

## Method Chaining

```python
text = '  HELLO WORLD  '

# Chain multiple methods
result = text.strip().lower().replace('world', 'python')
print(result)  # hello python

# Same as:
text = text.strip()
text = text.lower()
text = text.replace('world', 'python')
print(text)  # hello python
```

## Exercises by Bloom Level
- Remember: What does `.upper()` do?
- Understand: Why use `.strip()` on user input?
- Apply: Use `.split()` to parse CSV.
- Analyze: Compare `.replace()` vs `.find()`.
- Create: Build text cleaner (strip, lowercase, replace).

## Common Errors
- Forgetting strings immutable: `text.lower()` doesn't change `text`.
- Case-sensitive: `'Hello' != 'hello'`.
- Off-by-one in find: returns index, not count.

## Related Concepts
- [[Python - Strings - Basics]]
- [[Python - Strings - String Formatting]]
- [[Python - Lists - Common Patterns]]

## MOC
- Parent: [[Python - Strings (MOC)]]
