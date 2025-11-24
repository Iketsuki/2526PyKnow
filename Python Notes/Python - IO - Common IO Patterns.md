---
tags: [python, io, patterns]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: common IO patterns."
  - "Understand: when to use loops with input."
  - "Apply: implement patterns like "ask multiple times" or "ask until valid"."
---

# Python - IO - Common IO Patterns

## Concept
Recognize and use recurring patterns: asking repeatedly, validating input, reading multiple lines, etc.

## Example Code
```python
# Pattern: Ask until valid input
while True:
    age_str = input('Enter your age: ')
    try:
        age = int(age_str)
        if age >= 0:
            break
    except ValueError:
        pass
    print('Invalid, try again.')

# Pattern: Collect multiple inputs
names = []
for i in range(3):
    name = input(f'Enter name {i+1}: ')
    names.append(name)
print('Names:', names)
```

## Exercises by Bloom Level
- Remember: Write the "ask until valid" pattern.
- Understand: Why use a loop for repeated input?
- Apply: Build a program that asks for numbers until the user enters -1.
- Analyze: Compare loop vs recursion for repeated input.
- Create: Make a program that validates and stores 5 user inputs.
 
## Common Errors with Example Code

### Error 1: Not validating user input
```python
# WRONG: Trusting input blindly
value = int(input('Enter number: '))  # ValueError if not number

# CORRECT: Validate or use try-except
while True:
    try:
        value = int(input('Enter number: '))
        break
    except ValueError:
        print('Please enter a valid integer')
```

### Error 2: Infinite input loops without exit
```python
# WRONG: No clear exit, user trapped
while True:
    cmd = input('> ')
    # No break condition

# CORRECT: Provide exit option
while True:
    cmd = input('> ')
    if cmd in ('q', 'quit', 'exit'):
        break
```

### Error 3: Using recursion for repeated prompting (stack risk)
```python
# WRONG: Recursive prompts can overflow
def ask():
    val = input('Enter: ')
    if not valid(val):
        ask()  # recursion

# CORRECT: Use loops for repeated prompts
def ask():
    while True:
        val = input('Enter: ')
        if valid(val):
            return val
```

### Error 4: Not trimming whitespace from input
```python
# WRONG: Compare without stripping
choice = input('Yes/No: ')
if choice == 'Yes':
    pass  # Fails for ' Yes '\n'

# CORRECT: Strip and normalize
choice = input('Yes/No: ').strip().lower()
if choice == 'yes':
    pass
```

### Error 5: Blocking long operations in prompt loop
```python
# WRONG: Long blocking tasks prevent responsive prompt
while True:
    cmd = input('> ')
    if cmd == 'process':
        long_running_task()  # Blocks prompt

# CORRECT: Offload long tasks to background thread/process
import threading
def run_task():
    long_running_task()

while True:
    cmd = input('> ')
    if cmd == 'process':
        threading.Thread(target=run_task).start()
```

## MOC
- Parent: [[Python - IO (MOC)]]
