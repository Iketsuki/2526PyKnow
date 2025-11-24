---
tags: [python, strings, immutability, mutability]
moc: [[Python - Strings (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: strings are immutable (cannot change after creation)."
  - "Understand: string methods return new strings."
  - "Apply: reassign variables to modify strings."
  - "Analyze: how immutability affects performance and use cases."
---

# Python - Strings - String Immutability

## Concept
**Immutable** — Strings cannot be changed after creation. String methods return *new* strings; you must reassign the variable to "modify" it.

## What is Immutability?

```python
text = 'hello'

# You CANNOT modify a string in-place
# text[0] = 'H'  # TypeError! str object does not support item assignment

# Instead, strings methods return NEW strings
upper_text = text.upper()  # Returns 'HELLO'
print(text)         # 'hello' (original unchanged)
print(upper_text)   # 'HELLO'

# To "change" a string, reassign
text = text.upper()
print(text)  # 'HELLO' (reassigned variable)
```

## Real Examples

```python
# Example 1: Reassigning with methods
name = 'alice'
name = name.capitalize()  # 'Alice'
print(name)

# Example 2: Building strings
text = 'hello'
text = text + ' world'  # Creates new string
print(text)  # 'hello world'

# Example 3: Replacing (returns new string)
message = 'I like cats'
message = message.replace('cats', 'dogs')
print(message)  # 'I like dogs'

# Example 4: Splitting and joining
text = 'apple,banana,cherry'
items = text.split(',')  # ['apple', 'banana', 'cherry']
result = '-'.join(items)  # 'apple-banana-cherry'
print(result)
```

## Strings vs Lists (Mutability Comparison)

```python
# Strings are IMMUTABLE
text = 'hello'
# text[0] = 'H'  # Error!

# Lists are MUTABLE
items = ['a', 'b', 'c']
items[0] = 'x'  # Works! Changes to [' x', 'b', 'c']
print(items)

# String methods return new strings
text = 'hello'
upper = text.upper()  # Returns new string 'HELLO'

# List methods modify in-place OR return new list
items = ['a', 'b', 'c']
items.append('d')  # Modifies original (no return)
items2 = items.copy()  # Returns new list
```

## Exercises by Bloom Level

- **Remember**: Why are strings immutable?
- **Understand**: What does `.upper()` return?
- **Apply**: Use methods and reassign to "modify" strings.
- **Analyze**: Compare strings with mutable lists.
- **Create**: Process and transform strings.

## Common Errors with Example Code

### Error 1: Trying to modify a string in-place
```python
# WRONG: Trying to change a character directly
text = 'hello'
text[0] = 'H'  # TypeError: str object does not support item assignment!

# CORRECT: Create new string and reassign
text = text[0].upper() + text[1:]
print(text)  # 'Hello'

# BETTER: Use string methods
text = 'hello'
text = text.capitalize()
print(text)  # 'Hello'
```

### Error 2: Forgetting to reassign after method call
```python
# WRONG: Calling method but not reassigning
name = 'alice'
name.upper()  # Returns 'ALICE' but we don't save it!
print(name)   # 'alice' (unchanged!)

# CORRECT: Reassign the result
name = name.upper()
print(name)  # 'ALICE'
```

### Error 3: Confusing string building with mutation
```python
# WRONG: Assuming += modifies in-place (it doesn't)
text = 'hello'
text += ' world'  # Actually creates NEW string and reassigns!
print(text)  # 'hello world'

# This works, but understand what's happening:
# Old: text = 'hello'
# New: text = 'hello' + ' world'  (new string created)

# For large strings, this can be inefficient
big_text = ''
for i in range(1000):
    big_text += str(i)  # Creates 1000 new strings! (slow)

# BETTER: Use list and join
parts = []
for i in range(1000):
    parts.append(str(i))
big_text = ''.join(parts)  # Creates one string (fast)
```

### Error 4: Not understanding immutability affects function behavior
```python
# WRONG: Expecting function to modify string argument
def make_upper(text):
    text = text.upper()  # Modifies LOCAL variable, not original!

my_text = 'hello'
make_upper(my_text)
print(my_text)  # 'hello' (unchanged in outer scope!)

# CORRECT: Return the modified string
def make_upper(text):
    return text.upper()

my_text = 'hello'
my_text = make_upper(my_text)
print(my_text)  # 'HELLO'
```

### Error 5: Chaining string methods without reassign
```python
# WRONG: Forgetting final reassignment
text = 'hello world'
text.replace('hello', 'goodbye').upper()  # Computes but doesn't save!
print(text)  # 'hello world' (unchanged)

# CORRECT: Reassign the final result
text = text.replace('hello', 'goodbye').upper()
print(text)  # 'GOODBYE WORLD'

# OR break into steps
text = text.replace('hello', 'goodbye')
text = text.upper()
print(text)  # 'GOODBYE WORLD'
```

## Tips
- String methods return new strings; you must reassign.
- `+=` with strings creates a new string (doesn't modify in-place).
- For efficiency with many string operations, use lists and `''.join()`.
- Remember: Strings are immutable, Lists are mutable.

## Related Concepts
- [[Python - Strings - String Slicing & Indexing]]
- [[Python - Variables - Mutability & Immutability]]
- [[Python - Strings - Basics]]

## MOC
- Parent: [[Python - Strings (MOC)]]
