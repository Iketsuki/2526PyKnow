---
tags: [python, modules, random, math]
moc: [[Python - Modules (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: random and math module functions."
  - "Understand: when to use each function."
  - "Apply: use modules in programs."
---

# Python - Modules - Random & Math Modules

## Concept
**random module** — generate random numbers/choices. **math module** — mathematical functions. Both are in standard library.

## Random Module

### Generate Random Numbers

```python
import random

# Random float 0.0 to 1.0
num = random.random()
print(num)  # e.g., 0.73847

# Random integer in range
roll = random.randint(1, 6)  # 1-6 inclusive
print(roll)  # e.g., 4

# Random from range
num = random.randrange(0, 100, 5)  # 0, 5, 10, ... 95
print(num)  # e.g., 45
```

### Choose from List

```python
import random

items = ['apple', 'banana', 'cherry']

# Choose one random item
choice = random.choice(items)
print(choice)  # e.g., 'banana'

# Choose multiple without replacement
sample = random.sample(items, 2)
print(sample)  # e.g., ['cherry', 'apple']

# Shuffle list in place
items_copy = items.copy()
random.shuffle(items_copy)
print(items_copy)  # e.g., ['banana', 'apple', 'cherry']
```

## Math Module

### Basic Functions

```python
import math

# Power
print(math.pow(2, 3))  # 8.0 (2 to power 3)

# Square root
print(math.sqrt(16))  # 4.0

# Absolute value
print(math.fabs(-5))  # 5.0

# Ceiling and floor
print(math.ceil(3.2))  # 4
print(math.floor(3.8))  # 3
```

### Constants

```python
import math

# Pi
print(math.pi)  # 3.14159...
circumference = 2 * math.pi * 5  # radius 5
print(circumference)

# Euler's number
print(math.e)  # 2.71828...
```

### Trigonometry & Logarithm

```python
import math

# Trigonometric functions (radians)
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))  # 1.0

# Convert degrees to radians
angle_deg = 90
angle_rad = math.radians(angle_deg)
print(math.sin(angle_rad))  # 1.0

# Logarithm
print(math.log(10))  # Natural logarithm
print(math.log10(100))  # Base 10
```

## Real-World: Dice Game

```python
import random

def roll_dice(num_dice=1):
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return sum(rolls)

print(f'1 die: {roll_dice(1)}')  # e.g., 4
print(f'2 dice: {roll_dice(2)}')  # e.g., 7
print(f'3 dice: {roll_dice(3)}')  # e.g., 12
```

## Real-World: Quiz Scrambler

```python
import random

questions = [
    ('2+2', '4'),
    ('3*4', '12'),
    ('10-5', '5'),
    ('20/4', '5')
]

# Shuffle order
random.shuffle(questions)

for i, (q, answer) in enumerate(questions, 1):
    user_ans = input(f'{i}. {q} = ')
    if user_ans == answer:
        print('Correct!')
    else:
        print(f'Wrong. Answer: {answer}')
```

## Real-World: Circle Calculator

```python
import math

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

radius = 5
print(f'Area: {circle_area(radius):.2f}')  # 78.50
print(f'Circumference: {circle_circumference(radius):.2f}')  # 31.42
```

## Real-World: Random Selection

```python
import random

# Choose random student to present
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
presenter = random.choice(students)
print(f'Presenter: {presenter}')

# Choose 3 random teams
random.shuffle(students)
team1 = students[:2]
team2 = students[2:]
print(f'Team 1: {team1}')
print(f'Team 2: {team2}')
```

## Random Seed (Reproducible)

```python
import random

# Set seed for reproducible results
random.seed(42)

# Every time you set seed 42, same sequence
print(random.randint(1, 100))  # Always 82
print(random.randint(1, 100))  # Always 78

random.seed(42)
print(random.randint(1, 100))  # Again 82
```

## Common Functions Quick Reference

| Function | Purpose |
|----------|---------|
| `random.random()` | Float 0.0-1.0 |
| `random.randint(a, b)` | Integer a-b inclusive |
| `random.choice(list)` | Random item |
| `random.sample(list, k)` | k random items |
| `random.shuffle(list)` | Randomize list in place |
| `math.sqrt(x)` | Square root |
| `math.ceil(x)` | Round up |
| `math.floor(x)` | Round down |
| `math.pi` | Pi constant |

## Exercises by Bloom Level
- Remember: What does `random.choice()` do?
- Understand: Why use `random.seed()`?
- Apply: Create dice game with random rolls.
- Analyze: Compare `random.randint()` vs `random.choice()`.
- Create: Build random quiz generator.

## Common Errors
- Forgetting `import`: must do before using.
- Math functions use radians, not degrees.
- `random.shuffle()` modifies list, doesn't return new one.

## Related Concepts
- [[Python - Variables & Types - Type Conversion]]
- [[Python - Lists - Common Patterns]]
- [[Python - Math - Geometry & Shapes]]

## MOC
- Parent: [[Python - Modules (MOC)]]
