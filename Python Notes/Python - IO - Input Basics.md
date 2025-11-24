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

## Common Errors with Example Code

1) Forgetting `input()` returns a string (type errors)

WRONG
```python
age = input('Age: ')
next_age = age + 1  # TypeError: can only concatenate str (not "int") to str
```

CORRECT
```python
age = int(input('Age: '))
next_age = age + 1
print(next_age)
```

2) Assuming input is clean (whitespace, wrong types)

WRONG
```python
name = input('Name: ')
if name == 'Alice':  # fails if user types 'Alice ' with space
    print('Welcome!')
```

CORRECT
```python
name = input('Name: ').strip().lower()
if name == 'alice':
    print('Welcome!')
```

3) Not validating numeric input (ValueError)

WRONG
```python
score = int(input('Score: '))  # crashes if user types 'high'
print(score)
```

CORRECT
```python
while True:
    try:
        score = int(input('Score: '))
        break
    except ValueError:
        print('Please enter a number')
```

Short tips:
- Always convert `input()` result to the type you need.
- Use `.strip()` and `.lower()` for string comparison.
- Validate and re-prompt if input is invalid.

## Related Concepts
- [[Python - IO - Print Basics]]
- [[Python - IO - Output Formatting]]

## MOC
- Parent: [[Python - IO (MOC)]]
