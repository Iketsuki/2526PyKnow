---
tags: [python, io, interactive]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: interactive program flow."
  - "Understand: how to engage users."
  - "Apply: build a simple interactive game or quiz."
---

# Python - IO - Interactive Games & Guessing

## Concept
Build interactive programs where the user guesses or plays. Use loops, conditionals, and input to create engagement.

## Real-World Example: Simple Guessing Game

```python
import random

# Computer picks a number
secret = random.randint(1, 10)
print('I am thinking of a number between 1 and 10.')

# User guesses
while True:
    guess = int(input('What is your guess? '))
    if guess == secret:
        print('You got it! You win!')
        break
    elif guess < secret:
        print('Too low. Try again.')
    else:
        print('Too high. Try again.')
```

## Real-World Example: Quiz Game

```python
questions = [
    {'question': 'What is 2 + 2?', 'answer': 4},
    {'question': 'What is the capital of France?', 'answer': 'Paris'},
]

score = 0
for q in questions:
    answer = input(q['question'] + ' ')
    if answer == str(q['answer']):
        score += 1
        print('Correct!')
    else:
        print(f'Wrong. The answer is {q["answer"]}')

print(f'Final score: {score}/{len(questions)}')
```

## Exercises by Bloom Level
- Remember: Write a simple guessing program.
- Understand: Why use `while True`?
- Apply: Add hints to the guessing game.
- Analyze: How to prevent invalid input?
- Create: Build a multi-round game with scoring.

## Common Errors with Example Code

1) Not handling invalid input in interactive games (TypeError / ValueError)

WRONG
```python
import random
secret = random.randint(1, 10)
guess = int(input('Guess: '))  # Crashes if user types 'five'
if guess == secret:
    print('Correct!')
```

CORRECT
```python
import random
secret = random.randint(1, 10)
while True:
    try:
        guess = int(input('Guess: '))
        if guess == secret:
            print('Correct!')
            break
        else:
            print('Try again')
    except ValueError:
        print('Please enter a number')
```

2) Infinite loop without proper exit condition

WRONG
```python
score = 0
while True:
    answer = input('Question: ')
    if answer == 'correct':
        score += 1
    # No way to exit the loop!
```

CORRECT
```python
score = 0
rounds = 3
for i in range(rounds):
    answer = input(f'Question {i+1}: ')
    if answer == 'correct':
        score += 1
print(f'Final score: {score}/{rounds}')
```

3) Not validating user choices (silent failures or incorrect game flow)

WRONG
```python
choice = input('Rock, paper, or scissors? ')
if choice == 'rock':
    print('You chose rock')
# User types 'Rock' or 'ROCK' - doesn't match!
```

CORRECT
```python
valid_choices = ['rock', 'paper', 'scissors']
while True:
    choice = input(f'Choose from {valid_choices}: ').lower().strip()
    if choice in valid_choices:
        break
    print('Invalid choice')
print(f'You chose {choice}')
```

Short tips:
- Wrap numeric input in try-except to catch non-numbers.
- Always validate user input before using it.
- Use loops to keep asking until valid input is given.
- Use `.lower().strip()` for case-insensitive, clean input.

## Related Concepts
- [[Python - Loops - For Loop Basics]]
- [[Python - Conditionals - If-Else Basics]]
- [[Python - Modules - Common Modules (random-math-etc)]]

## MOC
- Parent: [[Python - IO (MOC)]]
