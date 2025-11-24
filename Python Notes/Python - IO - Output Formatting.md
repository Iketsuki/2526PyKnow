---
tags: [python, io, formatting]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: f-strings and basic string formatting."
  - "Understand: when to use f-strings vs concatenation."
  - "Apply: format output with variables and expressions."
---

# Python - IO - Output Formatting

## Concept
Format output cleanly using f-strings (modern Python) or string concatenation. F-strings let you embed expressions inside curly braces.

## Example Code
```python
name = 'Jordan'
age = 16

# F-string (recommended)
print(f'Hello {name}, you are {age} years old.')

# String concatenation (older style)
print('Hello ' + name + ', you are ' + str(age) + ' years old.')
```

## Exercises by Bloom Level
- Remember: Write an f-string with one variable.
- Understand: Why are f-strings cleaner than concatenation?
- Apply: Format a sentence with 3 variables using an f-string.
- Analyze: What happens if you put an expression in `{}`? (e.g., `{age + 1}`)
- Create: Write a function that takes name and score and returns a formatted message.

## Common Errors with Example Code

1) Forgetting the `f` before the string → Regular string, not f-string

WRONG
name = 'Alice'
age = 16
message = 'Hello {name}, you are {age} years old.'
print(message)  # Hello {name}, you are {age} years old. (not replaced!)

CORRECT
name = 'Alice'
age = 16
message = f'Hello {name}, you are {age} years old.'
print(message)  # Hello Alice, you are 16 years old.

2) Mixing quote styles inside f-string → Use different quote styles carefully

WRONG
name = "Alice"
# Using same quotes inside causes issues:
message = f"She said "hello""  # SyntaxError!

CORRECT
name = "Alice"
# Mix quote types:
message = f"She said 'hello'"
print(message)  # She said 'hello'

# Or use backslash escape:
message2 = f"She said \"hello\""
print(message2)  # She said "hello"

3) Trying to use variables in regular strings → Variables aren't replaced without f

WRONG
name = 'Bob'
age = 15
# Concatenation is tedious:
message = 'Name: ' + name + ', Age: ' + str(age)

CORRECT
name = 'Bob'
age = 15
# F-string is cleaner:
message = f'Name: {name}, Age: {age}'
print(message)  # Name: Bob, Age: 15

## Related Concepts
- [[Python - IO - Print Basics]]
- [[Python - Strings - Basics]]

## MOC
- Parent: [[Python - IO (MOC)]]
