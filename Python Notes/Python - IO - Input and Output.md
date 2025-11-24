---
tags: [python, io, input-output]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: input() and print() syntax."
  - "Understand: reading strings, converting types."
  - "Apply: build interactive programs."
---

# Python - IO - Input & Output

## Concept
**Input/Output (I/O)** — `input()` reads user keyboard input (returns string), `print()` displays output to screen. Core of interactive programs.

## Basic Print

```python
# Simple output
print('Hello, World!')

# Multiple values
print('Age:', 14)
print('Score:', 95, 'out of', 100)

# Without newline
print('Loading', end='')
print('...')  # Prints on same line

# Custom separator
print('Apple', 'Banana', 'Cherry', sep=', ')
# Output: Apple, Banana, Cherry
```

## Basic Input

```python
# Read from keyboard (returns string!)
name = input('Enter your name: ')
print('Hello,', name)

# Input is always a string
age_str = input('Enter age: ')
print(f'You entered: {age_str} (type: {type(age_str).__name__})')

# Convert to number
age = int(age_str)
print(f'Next year you will be {age + 1}')
```

## Type Conversion After Input

```python
# String to integer
score_str = input('Enter score: ')  # '95'
score = int(score_str)  # 95
print(score + 5)  # Works: 100

# String to float
height_str = input('Enter height (meters): ')  # '1.75'
height = float(height_str)  # 1.75
print(f'Height: {height}')

# Multiple inputs
line = input('Enter coordinates (x,y): ')  # '10,20'
x_str, y_str = line.split(',')
x = int(x_str)
y = int(y_str)
print(f'Position: ({x}, {y})')
```

## Safe Input with Error Handling

```python
def get_integer(prompt):
    '''Safely get integer from user'''
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('Please enter a valid number')

age = get_integer('Enter age: ')
print(f'Your age: {age}')
```

## Input with Validation

```python
def get_valid_choice(prompt, options):
    '''Get user choice from list'''
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        print(f'Please enter one of: {", ".join(options)}')

response = get_valid_choice(
    'Continue? (y/n): ',
    ['y', 'n']
)
```

## Format Output

```python
name = 'Alice'
score = 95.5

# F-string (modern, recommended)
print(f'{name} scored {score}%')

# .format() method
print('{} scored {}%'.format(name, score))

# % operator (older)
print('%s scored %.1f%%' % (name, score))

# Alignment and padding
print(f'{name:>10}')  # Right-aligned, width 10
print(f'{score:>6.1f}')  # Right-aligned float, 6 width, 1 decimal
```

## Multiple Lines

```python
# Multi-line string
print('''
Welcome to the program!
1. Option 1
2. Option 2
3. Option 3
''')

# Or use \n
print('Line 1\nLine 2\nLine 3')
```

## Real-World: Quiz Program

```python
def quiz():
    '''Simple 3-question quiz'''
    score = 0
    
    questions = [
        ('What is 2 + 2? ', '4'),
        ('What is the capital of France? ', 'paris'),
        ('Is Python a snake? ', 'yes')
    ]
    
    for question, answer in questions:
        response = input(question).lower().strip()
        if response == answer:
            print('Correct!')
            score += 1
        else:
            print(f'Wrong! The answer is {answer}')
    
    print(f'\nYou scored {score}/3')

quiz()
```

## Real-World: Age Calculator

```python
def calculate_birth_year():
    '''Calculate birth year from age'''
    try:
        age = int(input('Enter your age: '))
        
        if age < 0 or age > 150:
            print('Invalid age!')
            return
        
        from datetime import datetime
        current_year = datetime.now().year
        birth_year = current_year - age
        
        print(f'You were born in {birth_year}')
    except ValueError:
        print('Please enter a valid number')

calculate_birth_year()
```

## Real-World: Simple Game

```python
def number_guessing_game():
    '''Guess a number between 1-10'''
    import random
    
    target = random.randint(1, 10)
    guesses = 0
    
    while True:
        try:
            guess = int(input('Guess (1-10): '))
            guesses += 1
            
            if guess == target:
                print(f'Correct! Found in {guesses} tries')
                break
            elif guess < target:
                print('Too low')
            else:
                print('Too high')
        except ValueError:
            print('Please enter a number')

number_guessing_game()
```

## Clear Output

```python
import os

# Clear screen (Windows: 'cls', Mac/Linux: 'clear')
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print('Clean slate!')
```

## Input/Output Summary

```python
# Output (print)
print('text')  # Print to screen
print(a, b, c)  # Multiple values
print(f'{x}')  # F-string (recommended)
print(value, end='')  # No newline

# Input (input)
response = input('prompt: ')  # Always returns string
value = int(input('number: '))  # Convert type

# Formatting
f'{value:>10}'  # Right-aligned, width 10
f'{3.14:.2f}'  # 2 decimal places
'{} {}'.format(a, b)  # .format() method
```

## Exercises by Bloom Level
- Remember: What does `input()` return?
- Understand: Why convert input to int/float?
- Apply: Build age calculator program.
- Analyze: Compare print() with print(end='').
- Create: Build interactive quiz with scoring.

## Common Errors with Example Code

Here are common mistakes when using `input()` and `print()`, with fixes.

1) Forgetting that `input()` returns a string

WRONG
```python
age = input('Enter age: ')
print(age + 5)  # TypeError: can only concatenate str (not "int") to str
```

CORRECT
```python
age = int(input('Enter age: '))  # convert explicitly after validation
print(age + 5)
```

2) Using int() improperly on floating text

WRONG
```python
value = int('3.14')  # ValueError
```

CORRECT
```python
value = float('3.14')
value = int(value)  # if you really need an int
```

3) Not stripping whitespace from input

WRONG
```python
name = input('Enter your name: ')
if name == 'Alice':
    print('Welcome Alice')
```

CORRECT
```python
name = input('Enter your name: ').strip()
if name.lower() == 'alice':
    print('Welcome Alice')
```

Short tips:
- Always validate and convert input explicitly.
- Use `strip()` and `lower()` when comparing user strings.
- Wrap conversions in try/except or re-prompt the user when invalid.

## Related Concepts
- [[Python - Variables & Types - Type Conversion]]
- [[Python - Strings - String Formatting Detailed]]
- [[Python - Debugging - Exception Handling]]
- [[Python - Functions - Definition Basics]]

## MOC
- Parent: [[Python - IO (MOC)]]
