---
tags: [python, functions, scope, variables]
moc: [[Python - Functions (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: local, global, and nonlocal scope keywords."
  - "Understand: variable visibility in different scopes."
  - "Apply: use global and nonlocal keywords correctly."
  - "Analyze: trace variable lookups using LEGB rule."
---

# Python - Functions - Scope & Variables

## Concept
**Scope** — The region of code where a variable is accessible. **Local scope** (inside function), **global scope** (whole program), **nonlocal scope** (nested functions).

## Local Scope

```python
def greet():
    name = 'Alice'  # Local variable
    print(name)

greet()  # Alice

# Cannot access 'name' here
print(name)  # NameError! name is not defined
```

## Global Scope

```python
name = 'Bob'  # Global variable

def greet():
    print(name)  # Can read global

greet()  # Bob

print(name)  # Bob
```

## Global Keyword - Modifying Global Variables

```python
count = 0  # Global variable

def increment():
    global count  # Access and modify global
    count += 1
    print(f'Count: {count}')

increment()  # Count: 1
increment()  # Count: 2
print(count)  # 2 (global is changed)

# Without 'global': UnboundLocalError
def increment_bad():
    count += 1  # Error: trying to modify before assignment

# increment_bad()  # Would crash!
```

## Local Shadows Global

```python
score = 100  # Global

def update_score():
    score = 50  # Local (shadows global)
    print(f'Local: {score}')

update_score()  # Local: 50
print(f'Global: {score}')  # Global: 100

# Global is unchanged!
```

## Nested Functions & Enclosing Scope

```python
def outer():
    x = 10
    
    def inner():
        # Can see outer's variable
        print(f'Inner sees: {x}')
    
    inner()
    print(f'Outer has: {x}')

outer()
# Inner sees: 10
# Outer has: 10
```

## Nonlocal Keyword

```python
def outer():
    count = 0
    
    def increment():
        nonlocal count  # Access enclosing function's variable
        count += 1
        return count
    
    return increment

counter = outer()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3

# Each call increments the same count
```

## Scope Lookup Order (LEGB Rule)

Python looks for variables in this order:

```
1. Local - inside the function
2. Enclosing - in enclosing functions
3. Global - whole program
4. Built-in - Python built-ins
```

```python
x = 'global'

def outer():
    x = 'enclosing'
    
    def inner():
        x = 'local'
        print(x)  # Local (found first)
    
    inner()
    print(x)  # Enclosing

outer()
# local
# enclosing
print(x)  # global
```

## Real-World: Game Counter

```python
score = 0  # Global game state

def add_points(points):
    '''Add points to global score'''
    global score
    score += points
    return score

def reset_score():
    '''Reset to zero'''
    global score
    score = 0

def get_score():
    '''Return current score (no global needed)'''
    return score

add_points(10)
print(get_score())  # 10

add_points(5)
print(get_score())  # 15

reset_score()
print(get_score())  # 0
```

## Common Errors with Example Code

### Error 1: Forgetting global keyword
```python
# WRONG: UnboundLocalError
total = 0

def add_to_total(value):
    total += value  # Error: total referenced before assignment

# add_to_total(5)  # Crashes!

# CORRECT: Use global
total = 0

def add_to_total(value):
    global total
    total += value

add_to_total(5)
print(total)  # 5
```

### Error 2: Confusing local assignment with global
```python
# WRONG: Changes local, not global
price = 100

def apply_discount():
    price = 80  # Creates local variable
    print(f'Local: {price}')

apply_discount()  # Local: 80
print(f'Global: {price}')  # Global: 100 (unchanged!)

# CORRECT: Use global to modify
price = 100

def apply_discount():
    global price
    price = 80

apply_discount()
print(f'Global: {price}')  # Global: 80 (changed!)
```

### Error 3: Using global for reading (unnecessary)
```python
# WORKS but redundant: global not needed for reading
count = 5

def show_count():
    global count  # Not necessary for reading!
    print(count)

show_count()  # 5

# CORRECT: Don't use global if only reading
count = 5

def show_count():
    print(count)  # Can read without global

show_count()  # 5
```

### Error 4: Confusing nonlocal with global
```python
# WRONG: Using global inside nested function
x = 100

def outer():
    x = 50
    
    def inner():
        global x  # This refers to PROGRAM LEVEL x, not outer's x!
        x = 25
    
    inner()
    print(f'Outer sees: {x}')  # 50 (unchanged, inner modified global)

outer()
print(f'Global: {x}')  # 25

# CORRECT: Use nonlocal for enclosing function's variable
x = 100

def outer():
    x = 50
    
    def inner():
        nonlocal x  # Refers to outer's x
        x = 25
    
    inner()
    print(f'Outer sees: {x}')  # 25 (changed!)

outer()
print(f'Global: {x}')  # 100 (unchanged)
```

### Error 5: Shadowing built-ins
```python
# WRONG: Shadows built-in list function
def process_data():
    list = [1, 2, 3]  # Shadows built-in list()
    new_list = list(range(5))  # Error: list is not callable!

# process_data()  # TypeError!

# CORRECT: Use different variable name
def process_data():
    items = [1, 2, 3]  # Clear, doesn't shadow
    new_items = list(range(5))

process_data()  # Works
```

## Exercises by Bloom Level

- **Remember**: What does the `global` keyword do?
- **Understand**: What's the difference between local and global scope?
- **Apply**: Use global keyword in a game state tracker.
- **Analyze**: Trace variable lookups in nested functions using LEGB rule.
- **Create**: Build a nested function that correctly uses both nonlocal and global.

## Related Concepts
- [[Python - Functions - Scope and Lifetime]] — Variable lifetime and closures
- [[Python - Functions - Definition Basics]]
- [[Python - Functions - Parameters & Return Values]]
- [[Python - Variables & Types - Scope]]

## MOC
- Parent: [[Python - Functions (MOC)]]
