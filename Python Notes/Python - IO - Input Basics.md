---
tags: [python, io, input]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: `input()` syntax."
  - "Understand: input always returns a string."
  - "Apply: read user input and use it in a program."
---

# Python - IO - Input Basics

## Concept
`input()` pauses the program and waits for the user to type something, then returns it as a string.

## Syntax
```python
value = input(prompt_text)
```

## Example Code
```python
name = input('What is your name? ')
print('Hello, ' + name)

age_str = input('How old are you? ')
age = int(age_str)  # Convert to integer
```

## Exercises by Bloom Level
- Remember: Write an `input()` statement.
- Understand: Why is the result always a string?
- Apply: Ask the user for a number and print double it (convert to int first).
- Analyze: What happens if you try `int(input('number?'))` and the user types "hello"?
- Create: Build a small program that gathers 3 pieces of info from the user and combines them.

## Common Errors
- Forgetting that input returns a string, not a number.
- Trying to do math with string numbers without converting.

## Related Concepts
- [[Python - IO - Print Basics]]
- [[Python - IO - Output Formatting]]

## MOC
- Parent: [[Python - IO (MOC)]]
