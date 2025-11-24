---
tags: [python, strings, basics]
moc: [[Python - Strings (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: string syntax and creation."
  - "Understand: strings are sequences."
  - "Apply: create and use strings."
---

# Python - Strings - Basics

## Concept
**Strings** — text in quotes. Can use `'single'`, `"double"`, or `'''triple'''`. Strings are sequences (like lists).

## Creating Strings

```python
# Single quotes
message = 'Hello'

# Double quotes
greeting = "Hi there"

# Triple quotes (multi-line)
poem = '''
Roses are red,
Violets are blue
'''

# Empty string
empty = ''
```

## Escaping Characters

```python
# Backslash escapes special characters
quote = 'It\'s nice'  # Escaped apostrophe
print(quote)  # It's nice

newline = 'Line 1\nLine 2'  # \n is newline
print(newline)
# Line 1
# Line 2

tab = 'Name\tAge'  # \t is tab
print(tab)  # Name	Age

backslash = 'C:\\Users\\name'  # \\ is backslash
print(backslash)  # C:\Users\name
```

## String Length

```python
name = 'Alice'
print(len(name))  # 5

empty = ''
print(len(empty))  # 0

sentence = 'Hello, World!'
print(len(sentence))  # 13 (includes space and punctuation)
```

## String Indexing (Like Lists)

```python
word = 'Python'

print(word[0])  # 'P'
print(word[1])  # 'y'
print(word[5])  # 'n'

# Negative indexing
print(word[-1])  # 'n' (last)
print(word[-2])  # 'o' (second to last)
```

## String Iteration

```python
word = 'Hi'

for letter in word:
    print(letter)
# Output:
# H
# i
```

## String Immutability (Can't Change)

```python
text = 'Hello'

# This FAILS (strings can't be changed in place)
# text[0] = 'J'  # Error!

# Instead, create new string
text = 'Jello'  # New string
print(text)
```

## Concatenation (Joining Strings)

```python
first = 'Alice'
last = 'Smith'
full_name = first + ' ' + last
print(full_name)  # Alice Smith

# Or using join (more efficient)
parts = ['Hello', 'World']
message = ' '.join(parts)
print(message)  # Hello World
```

## String Repetition

```python
star = '*'
line = star * 10
print(line)  # **********

word = 'Ha'
laugh = word * 3
print(laugh)  # HaHaHa
```

## Real-World: User Greeting

```python
name = input('Name: ')
age_str = input('Age: ')
age = int(age_str)

greeting = f'Hello {name}, you are {age} years old'
print(greeting)
```

## Real-World: Building Messages

```python
item = 'apple'
count = 5

message = f'You have {count} {item}s'
print(message)  # You have 5 apples

# Or without f-string
message = 'You have ' + str(count) + ' ' + item + 's'
print(message)  # Same output
```

## Checking String Content

```python
text = 'Hello World'

if 'Hello' in text:
    print('Found greeting')

if 'hello' in text:
    print('Found lowercase')  # Doesn't print (case-sensitive)
else:
    print('Not found')
```

## Exercises by Bloom Level
- Remember: How to create a string with apostrophe?
- Understand: Why are strings like lists?
- Apply: Create greeting with user input.
- Analyze: Difference between mutable lists and immutable strings.
- Create: Build formatted message from data.

## Common Errors
- Mismatched quotes: `'Hello"` won't work.
- Trying to change string: `text[0] = 'X'` fails.
- Forgetting newline: `\n` not just new line in code.

## Related Concepts
- [[Python - Strings - String Methods]]
- [[Python - Lists - Indexing & Edge Cases]]
- [[Python - Strings - String Formatting]]

## MOC
- Parent: [[Python - Strings (MOC)]]
