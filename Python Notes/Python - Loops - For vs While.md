---
tags: [python, loops, for, while]
moc: [[Python - Loops (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: for vs while syntax."
  - "Understand: when to use each."
  - "Apply: choose right loop type."
---

# Python - Loops - For vs While

## Concept
**For loops** — iterate over a known sequence (list, range, string). **While loops** — repeat while condition is true (unknown count).

## For Loops (Known Count)

```python
# Loop through range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Loop through list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Loop through string
word = 'hello'
for letter in word:
    print(letter)  # h, e, l, l, o
```

## While Loops (Unknown Count)

```python
# Repeat until condition is false
count = 0
while count < 5:
    print(count)
    count += 1  # Increment

# Loop until user quits
while True:
    answer = input('Continue? (yes/no): ')
    if answer == 'no':
        break  # Exit loop
```

## Real-World: When to Use Each

**For — Known Iterations:**
```python
# Greet 5 friends (known count)
for i in range(5):
    print(f'Hello friend {i+1}')

# Process quiz scores (known list)
scores = [85, 90, 78, 88]
for score in scores:
    if score >= 80:
        print(f'{score} — Pass!')
```

**While — Unknown Iterations:**
```python
# Get valid input (unknown how many tries)
while True:
    num = input('Enter number 1-10: ')
    try:
        num = int(num)
        if 1 <= num <= 10:
            print(f'You chose {num}')
            break
    except:
        print('Invalid! Try again')

# Countdown (known but might skip)
time = 10
while time > 0:
    print(time)
    time -= 1
    if time == 5:
        print('Halfway!')
```

## Comparison

| Feature | For | While |
|---------|-----|-------|
| Use When | Known sequence | Condition-based |
| Count | Pre-determined | Unknown |
| Best For | Lists, ranges | User input, validation |
| Common Error | Off-by-one | Infinite loop |

## Real-World Game Loop

```python
# Game with while (unknown when user quits)
score = 0
playing = True

while playing:
    action = input('Play again? (yes/no): ')
    if action == 'no':
        playing = False
    else:
        score += 10
        print(f'Score: {score}')

print(f'Final score: {score}')
```

## Real-World: Process Multiple Items

```python
# For loop (known list)
tasks = ['homework', 'dishes', 'laundry']

for task in tasks:
    print(f'Doing {task}...')
    print(f'Finished {task}!')

# While loop would need manual index
tasks = ['homework', 'dishes', 'laundry']
index = 0

while index < len(tasks):
    task = tasks[index]
    print(f'Doing {task}...')
    index += 1  # Must increment manually!
```

## Exercises by Bloom Level
- Remember: Which loop uses `range()`?
- Understand: Why use while for user input?
- Apply: Write for loop over list, while for validation.
- Analyze: Compare nested for vs nested while.
- Create: Build a quiz game (for questions, while validation).

## Common Errors
- Infinite while loop: condition never becomes false.
- For loop off-by-one: `range(5)` is 0-4, not 1-5.
- Forgetting to increment in while: loop never ends.

## Related Concepts
- [[Python - Loops - Loop Control (Break & Continue)]]
- [[Python - Loops - Enumerate & Zip]]
- [[Python - Conditionals - If-Else Basics]]

## MOC
- Parent: [[Python - Loops (MOC)]]
