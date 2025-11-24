---
tags: [python, strings, slicing, indexing]
moc: [[Python - Strings (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: string indexing and slicing syntax."
  - "Understand: strings are sequences; indexing rules."
  - "Apply: extract characters and substrings."
  - "Analyze: negative indices and slice parameters."
  - "Create: programs that extract and manipulate string parts."
---

# Python - Strings - String Slicing & Indexing

## Concept
Access string characters with **indexing** `s[i]` and extract substrings with **slicing** `s[start:end:step]`.

## String Indexing

```python
word = 'hello'

# Forward indexing (0-based)
print(word[0])  # 'h'
print(word[1])  # 'e'
print(word[2])  # 'l'
print(word[4])  # 'o'

# Negative indexing (from end)
print(word[-1])  # 'o' (last character)
print(word[-2])  # 'l' (second to last)
print(word[-5])  # 'h' (first character)

# Index out of range raises error
print(word[10])  # IndexError: string index out of range
```

## Basic Slicing

```python
word = 'hello'

# [start:end] — get characters from start to end-1
print(word[0:3])   # 'hel' (chars 0, 1, 2)
print(word[1:4])   # 'ell' (chars 1, 2, 3)
print(word[2:])    # 'llo' (from 2 to end)
print(word[:3])    # 'hel' (from start to 3)
print(word[:])     # 'hello' (entire string)

# Negative indices in slicing
print(word[-3:])   # 'llo' (last 3 characters)
print(word[:-1])   # 'hell' (all except last)
print(word[-4:-1]) # 'ell' (second to last 3)
```

## Slicing with Step

```python
word = 'hello'

# [start:end:step]
print(word[::2])      # 'hlo' (every 2nd character)
print(word[1::2])     # 'el' (every 2nd starting at 1)
print(word[::1])      # 'hello' (step of 1, entire string)

# Negative step (reverse)
print(word[::-1])     # 'olleh' (reverse string)
print(word[4:1:-1])   # 'oll' (reverse from 4 to 2)
print(word[-1::-1])   # 'olleh' (reverse from end)
```

## Real Examples

```python
# Example 1: Extract domain from email
email = 'user@example.com'
domain = email[email.index('@')+1:]
print(domain)  # 'example.com'

# Example 2: Extract year from date string
date = '2024-01-15'
year = date[:4]
month = date[5:7]
day = date[-2:]
print(f'{month}/{day}/{year}')  # 01/15/2024

# Example 3: Remove extension from filename
filename = 'document.pdf'
name_only = filename[:filename.index('.')]
print(name_only)  # 'document'

# Example 4: Palindrome check
word = 'racecar'
is_palindrome = word == word[::-1]
print(is_palindrome)  # True

# Example 5: First and last characters
text = 'python'
first = text[0]
last = text[-1]
middle = text[1:-1]
print(f'{first}{middle}{last}')  # 'python' (same)

# Example 6: Every other character
text = 'abcdefgh'
every_other = text[::2]
print(every_other)  # 'aceg'

# Example 7: Reverse word
word = 'hello'
reversed_word = word[::-1]
print(reversed_word)  # 'olleh'
```

## Indexing vs Slicing

```python
word = 'hello'

# Indexing returns a single character
char = word[1]
print(char)       # 'e' (string of length 1)
print(type(char)) # <class 'str'>

# Slicing returns a substring (even if one character)
substring = word[1:2]
print(substring)  # 'e' (string of length 1)
print(type(substring))  # <class 'str'>

# Slicing never raises IndexError
print(word[100:200])  # '' (empty string, not error)
```

## Exercises by Bloom Level

- **Remember**: Index the first and last character.
- **Understand**: How do negative indices work?
- **Apply**: Slice a string to extract substrings.
- **Analyze**: How to reverse a string? Extract every nth character?
- **Create**: Build program that extracts and manipulates string parts.

## Common Errors with Example Code

### Error 1: Forgetting that slicing doesn't include end index
```python
# WRONG: Expecting end index to be included
word = 'hello'
print(word[0:3])  # Expected 'hell', got 'hel'

# CORRECT: Remember end is exclusive
print(word[0:4])  # 'hell' (includes index 3)

# To include last character:
print(word[0:5])  # 'hello'
print(word[:])    # 'hello'
```

### Error 2: Confusing negative index direction
```python
# WRONG: Wrong direction for negative
word = 'hello'
print(word[-1:0])  # '' (empty)
# Expecting to go backwards, but wrong

# CORRECT: Use step=-1 or correct negative range
print(word[::-1])  # 'olleh' (reverse)
print(word[4:0:-1])  # 'oll' (backwards from 4 to 1)
```

### Error 3: Index vs slice confusion
```python
# WRONG: Using indexing when you need slicing
word = 'hello'
char = word[0]  # 'h'
print(len(char))  # 1 (still a string!)

# Thinking you can do word[0] = 'j' to change first letter
# word[0] = 'j'  # TypeError: 'str' object does not support item assignment
# Strings are immutable!

# CORRECT: Use slicing and concatenation
new_word = 'j' + word[1:]
print(new_word)  # 'jello'
```

### Error 4: Index out of range
```python
# WRONG: Trying to index beyond string length
word = 'hello'
print(word[10])  # IndexError: string index out of range

# CORRECT: Check length or use slicing
if len(word) > 10:
    print(word[10])

# Slicing is safe
print(word[10:20])  # '' (empty, no error)
```

### Error 5: Not understanding step behavior with negative indices
```python
# WRONG: Confusing step direction
word = 'hello'
print(word[4:1])  # '' (empty, forward step can't go backward)

# CORRECT: Use negative step to go backward
print(word[4:1:-1])  # 'oll' (from index 4 down to 2)
print(word[::-1])    # 'olleh' (full reverse)
```

## String Slicing Quick Reference

| Operation | Syntax | Example | Result |
|-----------|--------|---------|--------|
| First char | `s[0]` | `'hello'[0]` | `'h'` |
| Last char | `s[-1]` | `'hello'[-1]` | `'o'` |
| First N chars | `s[:N]` | `'hello'[:3]` | `'hel'` |
| Last N chars | `s[-N:]` | `'hello'[-2:]` | `'lo'` |
| Substring | `s[i:j]` | `'hello'[1:4]` | `'ell'` |
| Every Nth | `s[::N]` | `'hello'[::2]` | `'hlo'` |
| Reverse | `s[::-1]` | `'hello'[::-1]` | `'olleh'` |

## Tips
- Remember **end index is exclusive** in slicing.
- Use **negative indices** for positions from the end.
- Slicing is **safe** — it won't raise IndexError for out-of-range.
- Indexing is **not safe** — IndexError if out of range.
- Use **`[::-1]`** to reverse strings.
- Strings are **immutable** — can't modify individual characters.
- Use **concatenation** and slicing to build new strings.

## Related Concepts
- [[Python - Strings - Basics]]
- [[Python - Strings - String Methods]]
- [[Python - Lists - Slicing]]
- [[Python - Lists - Indexing & Edge Cases]]

## MOC
- Parent: [[Python - Strings (MOC)]]
