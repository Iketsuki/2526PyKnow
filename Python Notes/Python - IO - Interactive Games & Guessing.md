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

## Related Concepts
- [[Python - Loops - For Loop Basics]]
- [[Python - Conditionals - If-Else Basics]]
- [[Python - Modules - Common Modules (random-math-etc)]]

## MOC
- Parent: [[Python - IO (MOC)]]
