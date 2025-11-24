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

## Common Errors
- Forgetting the `f` before the string.
- Mixing quote styles inside the f-string.

## Related Concepts
- [[Python - IO - Print Basics]]
- [[Python - Strings - Basics]]

## MOC
- Parent: [[Python - IO (MOC)]]
