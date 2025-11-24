---
tags: [python, io, beginner]
moc: [[Python - 14-Day Beginner Path (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: know how to print text and read input from the user."
  - "Understand: explain when to use input and print."
  - "Apply: write a short program that asks for your name and greets you."
---

# Python - I/O - Input & Output (Day 1)

## Concept
Input/Output (I/O) is how your program talks to the user. `print()` shows text on the screen. `input()` reads text the user types.

## Example Code
```python
# Ask the user for their name and greet them
name = input('What is your name? ')  # user types their name and presses Enter
print('Hello, ' + name + '! Nice to meet you.')
```

## Exercises by Bloom Level
- Remember: What does `print()` do? What does `input()` do?
- Understand: Explain in one sentence why we use `input()` in a program.
- Apply: Modify the program to also ask the user's age and print "You are X years old".
- Analyze: What happens if you try to add numbers read by `input()`? (Hint: types)
- Evaluate: Is it better to ask all questions first then print, or print after each input? Why?
- Create: Make a tiny chat that asks name, favorite color, and prints a friendly sentence.

## Tips for 14‑year‑olds
- Try running the program often after small changes.
- If input looks empty, check you pressed Enter.

## Common Errors with Example Code

1) Forgetting to convert input to numbers → Input is always a string, can't do math on it

WRONG
age = input('How old are you? ')
next_year = age + 1  # TypeError: can only concatenate str (not "int") to str
print(f'Next year you'll be {next_year}')

CORRECT
age = input('How old are you? ')
age = int(age)  # Convert string to integer
next_year = age + 1
print(f'Next year you'll be {next_year}')

2) Input stays as a string when you add it → Concatenates instead of adding numbers

WRONG
num1 = input('First number: ')  # User types "5"
num2 = input('Second number: ')  # User types "3"
total = num1 + num2
print(f'Total: {total}')  # Prints "53" not 8!

CORRECT
num1 = int(input('First number: '))  # Convert immediately
num2 = int(input('Second number: '))
total = num1 + num2
print(f'Total: {total}')  # Prints "8"

3) Forgetting to press Enter after input prompt → Program waits indefinitely

WRONG
# If user forgets to press Enter, program hangs:
name = input('Enter your name: ')
# Program waits for user to press Enter

CORRECT
# Always remind user what to do:
name = input('Enter your name and press Enter: ')
print(f'Hello, {name}!')

# Or handle empty input:
name = input('Enter your name: ')
if name == '':
    name = 'Friend'
print(f'Hello, {name}!')

## Related Concepts
- [[Python - Variables & Types - Basic Variables (Day 2)]]

## MOC
- Beginner path: [[Python - 14-Day Beginner Path (MOC)]]
