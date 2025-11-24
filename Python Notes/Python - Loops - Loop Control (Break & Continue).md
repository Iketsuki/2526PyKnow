---
tags: [python, loops, control]
moc: [[Python - Loops (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: break and continue syntax."
  - "Understand: when each is used."
  - "Apply: control loop flow."
---

# Python - Loops - Loop Control (Break & Continue)

## Concept
**break** — exit loop immediately. **continue** — skip to next iteration. Both give you control over loop flow.

## Break (Exit Loop)

```python
# Exit when condition met
for i in range(10):
    if i == 5:
        break  # Exit loop
    print(i)  # 0, 1, 2, 3, 4

# While with break (user quit)
while True:
    answer = input('Continue? (yes/no): ')
    if answer == 'no':
        break  # Exit loop
    print('Continuing...')
```

## Continue (Skip Iteration)

```python
# Skip when condition met
for i in range(5):
    if i == 2:
        continue  # Skip this iteration
    print(i)  # 0, 1, 3, 4 (2 skipped)

# Skip negative numbers
for num in [1, -2, 3, -4, 5]:
    if num < 0:
        continue  # Skip negatives
    print(num)  # 1, 3, 5
```

## Real-World: Break (Search & Exit)

**Find Item (Search):**
```python
students = ['Alice', 'Bob', 'Charlie', 'David']
search = 'Charlie'
found = False

for student in students:
    if student == search:
        print(f'Found {search}!')
        found = True
        break  # No need to check rest

if not found:
    print(f'{search} not found')
```

**Game Quit:**
```python
score = 0
playing = True

while playing:
    action = input('(p)lay, (q)uit: ')
    if action == 'q':
        break  # Quit game
    score += 10

print(f'Final score: {score}')
```

## Real-World: Continue (Filter Items)

**Skip Errors:**
```python
# Process scores, skip invalid
responses = ['85', 'invalid', '90', 'bad', '88']
valid_scores = []

for response in responses:
    if response == 'invalid' or response == 'bad':
        continue  # Skip bad data
    valid_scores.append(int(response))

print(valid_scores)  # [85, 90, 88]
```

**Skip Excluded Items:**
```python
# Greet everyone except Bob
names = ['Alice', 'Bob', 'Charlie', 'David']

for name in names:
    if name == 'Bob':
        continue  # Skip Bob
    print(f'Hello {name}!')  # Greets Alice, Charlie, David
```

**Skip Even Numbers:**
```python
# Process only odd numbers
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even
    print(num)  # 1, 3, 5, 7, 9 (odds only)
```

## Combining Break & Continue

```python
# Process list, skip some, quit early
for i in range(1, 11):
    if i == 5:
        continue  # Skip 5
    if i == 8:
        break  # Quit at 8
    print(i)  # 1, 2, 3, 4, 6, 7
```

## Real-World: Number Guessing Game

```python
import random

secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input('Guess 1-10: '))
    attempts += 1
    
    if guess == secret:
        print(f'Correct! {attempts} attempts')
        break  # Won, exit
    elif guess < secret:
        print('Too low')
        continue  # Try again
    else:
        print('Too high')
        continue  # Try again

    if attempts > 5:
        print('Too many tries!')
        break  # Give up
```

## Real-World: Input Validation

```python
# Keep asking until valid
while True:
    age = input('Age (18-100): ')
    
    try:
        age = int(age)
        if age < 18:
            print('Too young')
            continue  # Ask again
        if age > 100:
            print('Too old')
            continue  # Ask again
        
        print(f'Age {age} accepted')
        break  # Valid, exit
    
    except ValueError:
        print('Not a number')
        continue  # Ask again
```

## Visual Flow

**Break:**
```
for i in range(5):
    if i == 2:
        break    ← Exits loop
    print(i)
# Output: 0 1
```

**Continue:**
```
for i in range(5):
    if i == 2:
        continue ← Skips to next
    print(i)
# Output: 0 1 3 4
```

## Exercises by Bloom Level
- Remember: What does `break` do?
- Understand: Difference between `break` and `continue`?
- Apply: Use break to find item, continue to skip.
- Analyze: Trace execution with break/continue.
- Create: Build search game (break on find, continue on invalid).

## Common Errors with Example Code

1) Forgetting to increment counter in while loop with break (infinite loop)

WRONG
```python
count = 0
while True:
    if count == 5:
        break
    print(count)
    # Forgot: count += 1
# Infinite loop!
```

CORRECT
```python
count = 0
while True:
    if count == 5:
        break
    print(count)
    count += 1  # Must increment
```

2) Using `break` in nested loop (only exits inner loop)

WRONG
```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Only exits j loop, not i!
    print(f'i={i}')  # Still prints all i values
```

CORRECT
```python
# Need a flag to exit outer loop
for i in range(3):
    found = False
    for j in range(3):
        if j == 1:
            found = True
            break
    if found:
        break
```

3) Confusing `continue` with `break` (continuing instead of exiting)

WRONG
```python
for i in range(5):
    if i == 3:
        break  # If you meant to skip, use continue!
    print(i)  # 0, 1, 2 (stops at 3)
```

CORRECT
```python
for i in range(5):
    if i == 3:
        continue  # Skip this iteration
    print(i)  # 0, 1, 2, 4 (skips 3)
```

## Related Concepts
- [[Python - Loops - For vs While]]
- [[Python - Loops - Enumerate & Zip]]
- [[Python - Conditionals - If-Else Basics]]

## MOC
- Parent: [[Python - Loops (MOC)]]
