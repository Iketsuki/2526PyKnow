---
tags: [python, io, menus, programs, user-interface]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: menu-driven program structure."
  - "Understand: how to organize choices and actions."
  - "Apply: build menu-based applications."
  - "Analyze: menu validation and error handling."
  - "Create: multi-level menu systems and navigation."
---

# Python - IO - Menu-Driven Programs

## Concept
Display a **menu** with options, ask user to choose, and **execute the chosen action**. Use `while` loops for continuous menus.

## Basic Menu Pattern

```python
while True:
    # 1. Display menu
    print('=== Main Menu ===')
    print('1. Option A')
    print('2. Option B')
    print('3. Quit')
    
    # 2. Get user choice
    choice = input('Enter your choice: ')
    
    # 3. Execute action
    if choice == '1':
        print('You chose Option A')
    elif choice == '2':
        print('You chose Option B')
    elif choice == '3':
        print('Goodbye!')
        break  # Exit loop
    else:
        print('Invalid choice. Try again.')
```

## Real-World Example: Game Menu

```python
def start_game():
    print('Starting new game...')

def load_game():
    print('Loading your game...')

def show_settings():
    print('Opening settings...')

while True:
    print('=== Game Menu ===')
    print('1. Start New Game')
    print('2. Load Game')
    print('3. Settings')
    print('4. Quit')
    
    choice = input('Choose an option (1-4): ')
    
    if choice == '1':
        start_game()
    elif choice == '2':
        load_game()
    elif choice == '3':
        show_settings()
    elif choice == '4':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice. Please enter 1-4.')
```

## Real-World Example: Calculator Menu

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

while True:
    print('\n=== Simple Calculator ===')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Exit')
    
    op = input('Choose operation (1-5): ')
    
    if op == '5':
        print('Goodbye!')
        break
    elif op in ['1', '2', '3', '4']:
        try:
            a = float(input('First number: '))
            b = float(input('Second number: '))
            
            if op == '1':
                result = add(a, b)
            elif op == '2':
                result = subtract(a, b)
            elif op == '3':
                result = multiply(a, b)
            elif op == '4':
                result = divide(a, b)
                if result is None:
                    print('Cannot divide by zero!')
                    continue
            
            print(f'Result: {result}')
        except ValueError:
            print('Please enter valid numbers.')
    else:
        print('Invalid option. Enter 1-5.')
```

## Menu with Submenus

```python
def show_main_menu():
    while True:
        print('\n=== Main Menu ===')
        print('1. Player')
        print('2. Game')
        print('3. Quit')
        
        choice = input('Choose: ')
        
        if choice == '1':
            show_player_menu()
        elif choice == '2':
            show_game_menu()
        elif choice == '3':
            break
        else:
            print('Invalid choice.')

def show_player_menu():
    while True:
        print('\n=== Player Menu ===')
        print('1. View Profile')
        print('2. Change Name')
        print('3. Back')
        
        choice = input('Choose: ')
        
        if choice == '1':
            print('Your profile...')
        elif choice == '2':
            print('Changing name...')
        elif choice == '3':
            break
        else:
            print('Invalid choice.')

def show_game_menu():
    while True:
        print('\n=== Game Menu ===')
        print('1. New Game')
        print('2. Load Game')
        print('3. Back')
        
        choice = input('Choose: ')
        
        if choice == '1':
            print('Starting new game...')
        elif choice == '2':
            print('Loading game...')
        elif choice == '3':
            break
        else:
            print('Invalid choice.')

show_main_menu()
```

## Real Examples

```python
# Example 1: Todo app menu
def add_todo():
    task = input('Enter task: ')
    todos.append(task)
    print('Task added!')

def view_todos():
    if not todos:
        print('No tasks.')
    else:
        for i, task in enumerate(todos, 1):
            print(f'{i}. {task}')

def delete_todo():
    view_todos()
    try:
        index = int(input('Delete which? ')) - 1
        removed = todos.pop(index)
        print(f'Deleted: {removed}')
    except (ValueError, IndexError):
        print('Invalid number.')

todos = []

while True:
    print('\n=== Todo List ===')
    print('1. Add Todo')
    print('2. View Todos')
    print('3. Delete Todo')
    print('4. Exit')
    
    choice = input('Choose: ')
    
    if choice == '1':
        add_todo()
    elif choice == '2':
        view_todos()
    elif choice == '3':
        delete_todo()
    elif choice == '4':
        break
    else:
        print('Invalid choice.')

# Example 2: Input validation with retry
def get_valid_choice(options):
    while True:
        choice = input(f'Choose ({",".join(options)}): ')
        if choice in options:
            return choice
        print('Invalid choice.')

# Example 3: Menu with functions in dict
actions = {
    '1': ('Start Game', lambda: print('Starting...')),
    '2': ('Load Game', lambda: print('Loading...')),
    '3': ('Quit', None)
}

while True:
    print('\n=== Game Menu ===')
    for key, (label, _) in actions.items():
        print(f'{key}. {label}')
    
    choice = input('Choose: ')
    
    if choice in actions:
        if choice == '3':
            break
        actions[choice][1]()  # Execute function
    else:
        print('Invalid choice.')
```

## Menu Design Best Practices

```python
# ✓ GOOD: Clear, numbered, instructions
print('=== Settings ===')
print('1. Sound')
print('2. Graphics')
print('3. Back')
choice = input('Select (1-3): ')

# ✗ BAD: Unclear, no instructions
print('Sound Graphics Back')
choice = input('Choose: ')

# ✓ GOOD: Validate input
if choice in ['1', '2', '3']:
    # process
else:
    print('Invalid.')

# ✗ BAD: No validation
process(choice)  # Crashes if choice is invalid

# ✓ GOOD: Show success message
if choice == '1':
    print('Sound enabled.')

# ✗ BAD: No feedback
if choice == '1':
    enable_sound()  # No message
```

## Exercises by Bloom Level

- **Remember**: Write a 3-option menu.
- **Understand**: Why use `while True` with `break`?
- **Apply**: Build a simple menu-driven app (todo, calculator).
- **Analyze**: How to handle invalid menu choices?
- **Create**: Build multi-level menus or menu systems.

## Common Errors with Example Code

### Error 1: Infinite loop without exit
```python
# WRONG: No break condition
while True:
    choice = input('Menu: ')
    if choice == '1':
        print('Option 1')
    # No way to exit!

# CORRECT: Provide exit option
while True:
    choice = input('Menu (1-exit): ')
    if choice == '1':
        print('Option 1')
    elif choice == 'exit':
        break
```

### Error 2: String vs integer comparison
```python
# WRONG: Comparing strings to integers
choice = input('Choose 1-3: ')
if choice == 1:  # '1' != 1
    print('You chose 1')
# This never executes!

# CORRECT: Compare strings (input returns string)
if choice == '1':
    print('You chose 1')

# OR: Convert to integer
choice = int(input('Choose 1-3: '))
if choice == 1:
    print('You chose 1')
```

### Error 3: Not clearing screen between menus
```python
# WRONG: Output keeps stacking
while True:
    print('=== Menu ===')
    # After 10 iterations, lots of old menus visible

# BETTER: Use os.system('clear') or os.system('cls')
import os

while True:
    os.system('clear')  # Unix/Mac
    # os.system('cls')  # Windows
    print('=== Menu ===')
```

### Error 4: Not handling non-numeric input
```python
# WRONG: Assumes user enters number
choice = int(input('Choose 1-3: '))  # ValueError if input is 'abc'

# CORRECT: Handle errors
try:
    choice = int(input('Choose 1-3: '))
except ValueError:
    print('Please enter a number.')
    continue  # Retry
```

### Error 5: Repeating menu code instead of using functions
```python
# WRONG: Duplicate menu code
while True:
    print('=== Main ===')
    # ... lots of code ...
    
    if choice == '1':
        while True:
            print('=== Submenu ===')
            # ... lots of code ...

# CORRECT: Use functions
def main_menu():
    while True:
        print('=== Main ===')
        # ...
        if choice == '1':
            submenu()

def submenu():
    while True:
        print('=== Submenu ===')
        # ...

main_menu()
```

## Menu Structure Template

```python
# Function for each action
def action_1():
    print('Doing action 1')

def action_2():
    print('Doing action 2')

# Menu loop
while True:
    # Display
    print('\n=== Menu ===')
    print('1. Action 1')
    print('2. Action 2')
    print('3. Quit')
    
    # Get input
    choice = input('Choose: ')
    
    # Execute
    if choice == '1':
        action_1()
    elif choice == '2':
        action_2()
    elif choice == '3':
        break
    else:
        print('Invalid.')
```

## Tips
- Use **`while True` with `break`** for menu loops.
- **String comparison** for input (input() returns string).
- **Validate** before processing.
- Use **functions** for each action.
- **Clear** output or organize menus visually.
- Provide **exit option** clearly.
- **Repeat menu** after each action (loop continues).

## Related Concepts
- [[Python - IO - Input Basics]]
- [[Python - Loops - While Loop Basics]]
- [[Python - Conditionals - If-Else Basics]]

## MOC
- Parent: [[Python - IO (MOC)]]
