---
tags: [python, io, validation]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: input validation checks."
  - "Understand: why validate user input."
  - "Apply: ensure data is correct before using."
---

# Python - IO - Input Validation

## Concept
Check that user input is valid before using it (correct type, in range, not empty). Use try-except and conditionals.

## Real-World Example: Age Validation

```python
while True:
    try:
        age = int(input('How old are you? '))
        if age < 0 or age > 120:
            print('Please enter a realistic age.')
            continue
        break
    except ValueError:
        print('Please enter a number.')

print(f'You are {age} years old.')
```

## Real-World Example: Choice Validation

```python
valid_choices = ['rock', 'paper', 'scissors']

while True:
    choice = input('Choose rock, paper, or scissors: ').lower()
    if choice in valid_choices:
        print(f'You chose {choice}!')
        break
    else:
        print(f'Invalid choice. Choose from {valid_choices}')
```

## Real-World Example: Password Strength

```python
while True:
    password = input('Enter a password: ')
    if len(password) < 6:
        print('Password must be at least 6 characters.')
    elif not any(c.isdigit() for c in password):
        print('Password must contain at least one number.')
    else:
        print('Password is strong!')
        break
```

## Real-World Example: Non-Empty Input

```python
while True:
    name = input('What is your name? ').strip()
    if not name:
        print('Name cannot be empty.')
        continue
    break

print(f'Hello, {name}!')
```

## Common Errors with Example Code

### Error 1: Not handling ValueError when converting input
```python
# WRONG: No try-except for type conversion
age = int(input('Enter your age: '))  # Crashes if user enters 'abc'

# CORRECT: Use try-except
while True:
    try:
        age = int(input('Enter your age: '))
        break
    except ValueError:
        print('Please enter a valid number.')

print(f'You are {age} years old.')
```

### Error 2: Forgetting .strip() on input
```python
# WRONG: Extra spaces cause validation to fail
name = input('Enter name: ')
if not name:  # User enters '   ' (spaces)
    print('Empty')  # Doesn't print (spaces aren't empty!)

# CORRECT: Use .strip() to remove whitespace
name = input('Enter name: ').strip()
if not name:
    print('Empty')  # Now prints for spaces only
```

### Error 3: Case-sensitive string comparisons
```python
# WRONG: Case-sensitive check
choice = input('Enter yes or no: ')
if choice == 'yes':
    print('You said yes')
# User enters 'YES' → doesn't match!

# CORRECT: Use .lower() for case-insensitive
choice = input('Enter yes or no: ').lower()
if choice == 'yes':
    print('You said yes')  # Works for 'YES', 'Yes', 'yes'
```

### Error 4: Validating without showing acceptable values
```python
# WRONG: Error message doesn't explain what's valid
choice = input('Enter your choice: ')
if choice not in ['rock', 'paper', 'scissors']:
    print('Invalid choice.')  # User doesn't know what's valid!

# CORRECT: Tell user valid options
valid = ['rock', 'paper', 'scissors']
choice = input(f'Enter your choice {valid}: ').lower()
if choice not in valid:
    print(f'Invalid choice. Must be one of {valid}.')
```

### Error 5: Not re-prompting on validation failure
```python
# WRONG: Single attempt, then continues
age_str = input('Enter your age: ')
try:
    age = int(age_str)
except ValueError:
    print('Invalid age')
# Program continues even if conversion failed!

# CORRECT: Loop until valid
while True:
    try:
        age = int(input('Enter your age: '))
        if 0 <= age <= 120:
            break
        else:
            print('Please enter a realistic age (0-120).')
    except ValueError:
        print('Please enter a number.')

print(f'You are {age} years old.')
```

## Exercises by Bloom Level

- **Remember**: Write a simple range check. Write a try-except for int().
- **Understand**: Why is validation important?
- **Apply**: Validate age, name, choice input.
- **Analyze**: When use try-except vs if-checks?
- **Create**: Build a form with multiple validation rules.

## Tips
- Use `.strip()` to remove extra spaces.
- Use try-except for type conversion (int, float).
- Use `.lower()` for case-insensitive comparisons.
- Use `while True:` with `break` for re-prompting.
- Always tell users what's valid.

## Related Concepts
- [[Python - IO - Input-Output Flow]]
- [[Python - Debugging - Try-Except Basics]]
- [[Python - Loops - For Loop Basics]]

## MOC
- Parent: [[Python - IO (MOC)]]
