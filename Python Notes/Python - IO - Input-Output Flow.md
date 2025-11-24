---
tags: [python, io, flow]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: order of input and output."
  - "Understand: how user interaction flows in a program."
  - "Apply: build a small interactive dialog."
---

# Python - IO - Input-Output Flow

## Concept
Understand how a program flows: ask a question (output), wait for input, process, then show a result (output). This back-and-forth is the foundation of interactive programs.

## Example Code
```python
# Ask → Wait → Process → Display
print('Welcome to the Quiz!')
answer = input('What is 2 + 2? ')
result = int(answer)
if result == 4:
    print('Correct!')
else:
    print('Wrong. The answer is 4.')
```

## Exercises by Bloom Level
- Remember: Trace the order of execution in a simple program.
- Understand: Why does `input()` block the program?
- Apply: Write a program that asks 2 questions and gives different responses.
- Analyze: Redesign a multi-step input flow to be clearer.
- Create: Build a mini-dialog that guides the user through several inputs.

## Tips
- Use clear prompts so the user knows what to enter.
- Organize steps logically: ask all input first, then display results, or alternate as needed.

## Common Errors with Example Code

1) Converting input without validation (ValueError)

WRONG
```python
answer = input('What is 2 + 2? ')
result = int(answer)  # crashes if user types 'four' or leaves blank
```

CORRECT
```python
while True:
  try:
    answer = input('What is 2 + 2? ')
    result = int(answer)
    break
  except ValueError:
    print('Please enter a whole number (e.g. 4)')
print('You entered', result)
```

2) Not prompting clearly (user confusion / empty inputs)

WRONG
```python
name = input('Name: ')  # unclear: maybe first and last needed
```

CORRECT
```python
name = input('Enter your full name (first and last): ').strip()
if not name:
  name = 'Guest'
```

3) Writing to files without using context manager (file not closed / data loss)

WRONG
```python
f = open('out.txt', 'w')
f.write('Hello')
# forgot f.close()
```

CORRECT
```python
with open('out.txt', 'w', encoding='utf-8') as f:
  f.write('Hello')
# file closed automatically
```

## MOC
- Parent: [[Python - IO (MOC)]]
