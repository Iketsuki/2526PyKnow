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

## What is a Loop?

A **loop** repeats code multiple times. Instead of writing the same code 5 times, write it once and loop it 5 times.

## For Loops - When You Know the Count

Use **for** when you know how many times to repeat.

```python
# Repeat 5 times
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Loop through a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry

# Loop through a word
word = 'hello'
for letter in word:
    print(letter)
# Output: h, e, l, l, o
```

## While Loops - When You Don't Know the Count

Use **while** when you repeat until something happens.

```python
# Keep asking until user says no
answer = 'yes'
while answer == 'yes':
    print('Playing...')
    answer = input('Play again? (yes/no): ')

# Countdown from 5
count = 5
while count > 0:
    print(count)
    count = count - 1
print('Blastoff!')
```

## For vs While - Which One?

**Use FOR if:**
- You have a list
- You know exactly how many times
- You're going through each item

**Use WHILE if:**
- You don't know when to stop
- You repeat until something happens
- You're waiting for user input

## Real-World: For Loop Examples

**Greet 5 Friends**
```python
for i in range(5):
    print(f'Hello friend {i+1}')
```

Output:
```
Hello friend 1
Hello friend 2
Hello friend 3
Hello friend 4
Hello friend 5
```

**Check Homework Scores**
```python
scores = [85, 90, 78, 88]
for score in scores:
    if score >= 80:
        print(f'{score} - Good!')
```

## Real-World: While Loop Examples

**Get Valid Number**
```python
while True:
    num = input('Enter 1-10: ')
    if num.isdigit() and 1 <= int(num) <= 10:
        print(f'You chose {num}')
        break  # Exit the loop
    else:
        print('Invalid! Try again')
```

**Game Loop**
```python
score = 0
playing = 'yes'

while playing == 'yes':
    score = score + 10
    print(f'Score: {score}')
    playing = input('Play again? (yes/no): ')

print(f'Final score: {score}')
```

## Comparison

| For Loop | While Loop |
|----------|-----------|
| Use with lists | Use with conditions |
| Know the count | Don't know the count |
| `for item in list:` | `while condition:` |
| Good for processing items | Good for user input |

## Real-World Comparison

**FOR - Print Each Name (known list)**
```python
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(name)
```

**WHILE - Keep Asking Until Exit (unknown count)**
```python
while True:
    name = input('What is your name? ')
    print(f'Hello {name}!')
    again = input('Play again? (yes/no): ')
    if again != 'yes':
        break
```
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

## Common Errors with Example Code

1) Creating an infinite while loop (condition never becomes false)

WRONG
```python
count = 0
while count < 5:
    print(count)
    # Forgot count += 1 (never increments)
```

CORRECT
```python
count = 0
while count < 5:
    print(count)
    count += 1  # Increment to eventually exit
```

2) Off-by-one error with range (including wrong end value)

WRONG
```python
for i in range(5):
    print(i)
# Prints 0, 1, 2, 3, 4 (not 1-5)
```

CORRECT
```python
for i in range(1, 6):  # Start at 1, end before 6
    print(i)  # 1, 2, 3, 4, 5
```

3) Modifying loop variable in a for loop (confusion about iteration)

WRONG
```python
for i in range(5):
    print(i)
    i = 10  # Doesn't affect the loop (i resets)
```

CORRECT
```python
# For loops reassign the variable each iteration
# To control the loop, use while with manual increment
count = 0
while count < 5:
    print(count)
    count += 1
```

Short tips:
- Use `for` when you know the sequence in advance.
- Use `while` when the count is unknown or condition-based.
- Always increment the counter in a while loop.
- Remember `range(n)` is 0 to n-1, not 1 to n.

## Related Concepts
- [[Python - Loops - Loop Control (Break & Continue)]]
- [[Python - Loops - Enumerate & Zip]]
- [[Python - Conditionals - If-Else Basics]]

## MOC
- Parent: [[Python - Loops (MOC)]]
