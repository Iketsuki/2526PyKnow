---
tags: [python, strings, slicing]
moc: [[Python - Strings (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: slicing syntax [start:stop:step]."
  - "Understand: negative indices, step values."
  - "Apply: extract substrings, reverse strings."
---

# Python - Strings - Slicing

## Concept
**String slicing** — Extract parts of a string using `[start:stop:step]`. Strings are immutable sequences where each character has an index.

## Basic Slicing

```python
text = 'Python'
#      0123456

# Index 0-3
print(text[0:3])  # Pyt
print(text[2:5])  # tho
print(text[1:4])  # yth

# From beginning
print(text[:3])   # Pyt

# To end
print(text[2:])   # thon

# Entire string
print(text[:])    # Python
```

## Negative Indices

```python
text = 'Python'
#      0123456
#      -6-5-4-3-2-1

# Count from end
print(text[-1])    # n (last character)
print(text[-2])    # o (second-to-last)
print(text[-3:])   # hon (last 3 characters)
print(text[:-1])   # Pytho (everything except last)
print(text[:-2])   # Pyth (everything except last 2)

# From negative to positive
print(text[-4:-1])  # tho
```

## Step (Every Nth Character)

```python
text = 'Python'

# Every character (step=1, default)
print(text[::1])   # Python

# Every 2nd character
print(text[::2])   # Pto

# Every 3rd character
print(text[::3])   # Pho

# With start and stop
print(text[1:5:2])  # yh (characters at index 1, 3)
print(text[0:6:2])  # Pto
```

## Reverse String

```python
text = 'Python'

# Reverse with step=-1
print(text[::-1])  # nohtyP

# Every 2nd character in reverse
print(text[::-2])  # nhy

# Reverse specific portion
print(text[5:1:-1])  # nohty
```

## Practical Examples

```python
# Extract domain from email
email = 'alice@example.com'
domain = email[email.index('@')+1:]
print(domain)  # example.com

# Extract file extension
filename = 'photo.jpg'
extension = filename[-4:]
print(extension)  # .jpg

# Get initials
name = 'Alice Marie Johnson'
initials = name[0] + name[6] + name[13]
print(initials)  # AMJ

# More elegant: split instead
initials = ''.join([word[0] for word in name.split()])
print(initials)  # AMJ
```

## Common Patterns

```python
text = 'Hello World'

# First 5 characters
first_five = text[:5]  # Hello

# Last 5 characters
last_five = text[-5:]  # World

# Everything except first and last
middle = text[1:-1]  # ello Worl

# Skip first word
skip_hello = text[6:]  # World

# Remove whitespace (not slicing, but useful)
no_space = text.replace(' ', '')  # HelloWorld

# Palindrome check
is_palindrome = text == text[::-1]
```

## Slicing with Variables

```python
def get_middle_word(phrase):
    '''Extract middle word from 3-word phrase'''
    words = phrase.split()
    return words[1] if len(words) >= 2 else None

print(get_middle_word('Hello World Today'))  # World

# Character slicing in function
def remove_first_last(text):
    '''Remove first and last character'''
    return text[1:-1] if len(text) > 2 else text

print(remove_first_last('Hello'))  # ell
```

## Safe Slicing (No Errors)

```python
text = 'Hi'

# These don't error, just return empty or partial
print(text[0:100])  # Hi (doesn't go past end)
print(text[5:10])   # '' (empty string)
print(text[-100:])  # Hi (doesn't go past start)

# Slicing is safe even for out-of-bounds indices!
# But indexing isn't:
print(text[100])  # IndexError!
```

## Real-World: Parse Commands

```python
command = '/help search'

# Check command format
if command.startswith('/'):
    cmd = command[1:].split()
    action = cmd[0]
    args = cmd[1:] if len(cmd) > 1 else []
    
    print(f'Action: {action}')  # help
    print(f'Args: {args}')  # ['search']
```

## Real-World: Validate Input

```python
def is_valid_code(code):
    '''Check if code is 4 alphanumeric characters'''
    # Remove spaces, get first 4 chars
    code = code.replace(' ', '')
    code = code[:4]
    return len(code) == 4 and code.isalnum()

print(is_valid_code('AB12'))  # True
print(is_valid_code('A B 1 2'))  # True (space removed)
print(is_valid_code('AB'))  # False
```

## Real-World: Extract Coordinates

```python
# Parse simple format: "x,y"
def parse_coordinates(coord_str):
    '''Parse "10,20" into (10, 20)'''
    comma_index = coord_str.index(',')
    x = int(coord_str[:comma_index])
    y = int(coord_str[comma_index+1:])
    return (x, y)

coords = parse_coordinates('10,20')
print(coords)  # (10, 20)

# Better with split:
x, y = coord_str.split(',')
x, y = int(x), int(y)
```

## Reference: Slicing Syntax

```python
string[start:stop:step]

# Default values:
string[:]        # start=0, stop=len, step=1
string[2:]       # from index 2 to end
string[:4]       # from start to index 4
string[1:5]      # from index 1 to 5
string[::2]      # every 2nd character
string[::-1]     # reverse
string[start:stop]    # from start to stop (step=1)
string[start:stop:step]  # with custom step
```

## Exercises by Bloom Level
- Remember: What does `text[2:5]` do?
- Understand: How are negative indices different from positive?
- Apply: Extract filename and extension from full path.
- Analyze: Compare `text[::-1]` vs `reversed(text)`.
- Create: Build string parser that extracts email domain.

## Common Errors
- Off-by-one: `text[0:3]` is indices 0,1,2 (not including 3).
- Forgetting slicing is safe: Won't error for `text[0:1000]`.
- Confusing `text[-1]` (last char) with `text[:-1]` (all but last).

## Related Concepts
- [[Python - Strings - Basics]]
- [[Python - Strings - String Methods]]
- [[Python - Lists - Indexing & Edge Cases]]
- [[Python - Lists - Slicing Patterns]]

## MOC
- Parent: [[Python - Strings (MOC)]]
