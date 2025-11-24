---
tags: [python, functions, scope, closures, lifetime]
moc: [[Python - Functions (MOC)]]
difficulty: Intermediate
bloom_level: Understand
learning_objectives:
  - "Remember: what variable lifetime means."
  - "Understand: when variables are created and destroyed."
  - "Apply: use closures to create function factories."
  - "Analyze: how closures capture variables."
---

# Python - Functions - Variable Lifetime & Closures

## Concept
**Variable lifetime** — When a variable is created and destroyed. Local variables exist only during function execution. **Closures** — Functions that "remember" variables from their enclosing scope, even after the outer function ends.

## Variable Lifetime Basics

```python
def create_list():
    items = [1, 2, 3]  # Created when function starts
    print(items)       # Use variable
    # Deleted when function ends

create_list()  # [1, 2, 3]
# print(items)  # NameError! items no longer exists

# But objects can persist if returned
def return_list():
    items = [1, 2, 3]
    return items

my_list = return_list()  # items deleted, but list still exists
print(my_list)  # [1, 2, 3] (referenced by my_list)
```

## Function Parameters (Passed Values)

```python
def greet(name):
    # 'name' is local to this function
    name = name.upper()
    print(f'Hello, {name}')

greet('alice')  # Hello, ALICE

# Original variable unchanged
x = 'alice'
greet(x)
print(x)  # 'alice' (unchanged)
```

## Closures: Functions That Remember Variables

```python
def make_counter():
    '''Create a function that counts'''
    count = 0  # Captured in closure
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3

# 'count' is "closed over" - captured by inner function
```

## Multiple Closures with Separate State

```python
def make_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 1 (separate counter)
print(counter1())  # 3
```

## Mutable Objects (Lists, Dicts)

```python
def modify_list(items):
    items.append(4)  # Modifies original!

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4] - changed!

# Why? Lists are mutable, passed by reference

# To avoid modifying:
def modify_list_safe(items):
    items = items.copy()  # Make a copy
    items.append(4)

my_list = [1, 2, 3]
modify_list_safe(my_list)
print(my_list)  # [1, 2, 3] - unchanged
```

## Real-World: Counter Closure

```python
def make_counter(start=0):
    '''Create a function that counts from start'''
    count = start
    
    def get_count():
        return count
    
    def increment(by=1):
        nonlocal count
        count += by
        return count
    
    def reset():
        nonlocal count
        count = start
        return count
    
    # Return multiple functions sharing state
    return {
        'get': get_count,
        'inc': increment,
        'reset': reset
    }

counter = make_counter(100)
print(counter['get']())  # 100
print(counter['inc'](5))  # 105
print(counter['get']())  # 105
print(counter['reset']())  # 100
```

## Real-World: List Accumulator

```python
def make_accumulator():
    '''Create a function that accumulates values'''
    values = []
    
    def add(value):
        values.append(value)
        return values.copy()  # Return copy
    
    return add

acc = make_accumulator()
print(acc(1))  # [1]
print(acc(2))  # [1, 2]
print(acc(3))  # [1, 2, 3]
```

## Scope Best Practices

```python
# AVOID: Global variables (hard to track)
count = 0

def increment():
    global count
    count += 1

# PREFER: Functions that return values
def increment_with_return(count):
    return count + 1

x = 0
x = increment_with_return(x)

# PREFER: Closures for state (encapsulation)
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
```

## Common Errors with Example Code

### Error 1: Forgetting nonlocal in closures
```python
# WRONG: Creates local variable instead of capturing
def make_counter():
    count = 0
    
    def increment():
        count += 1  # UnboundLocalError!
        return count
    
    return increment

# counter = make_counter()
# counter()  # Error!

# CORRECT: Use nonlocal
def make_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter = make_counter()
print(counter())  # 1
```

### Error 2: Modifying mutable arguments unexpectedly
```python
# WRONG: Modifying list argument affects original
def append_item(items, item):
    items.append(item)  # Modifies the original list!

my_list = [1, 2]
append_item(my_list, 3)
print(my_list)  # [1, 2, 3] - changed!

# CORRECT: If you don't want to modify, copy first
def append_item_safe(items, item):
    items = items.copy()
    items.append(item)
    return items

my_list = [1, 2]
result = append_item_safe(my_list, 3)
print(my_list)  # [1, 2] - unchanged
print(result)   # [1, 2, 3] - new list
```

### Error 3: Closure capturing loop variable
```python
# WRONG: All closures capture the same loop variable
functions = []

for i in range(3):
    def func():
        return i  # All capture final i (2)
    functions.append(func)

print(functions[0]())  # 2 (not 0!)
print(functions[1]())  # 2 (not 1!)
print(functions[2]())  # 2

# CORRECT: Capture with default parameter
functions = []

for i in range(3):
    def func(x=i):  # Captures current i value
        return x
    functions.append(func)

print(functions[0]())  # 0
print(functions[1]())  # 1
print(functions[2]())  # 2
```

### Error 4: Variables created in if blocks
```python
# WRONG: Assuming if-block creates a scope
def process():
    if True:
        x = 100
    
    print(x)  # Works! x is still available (no block scope)

process()  # 100

# CORRECT: Remember Python has function scope, not block scope
def process():
    if condition := True:
        x = 100
    
    # x is available here (function scope, not block scope)
    print(x)  # Works
```

### Error 5: Assuming mutable default arguments are fresh
```python
# WRONG: Mutable defaults are shared across calls
def add_to_list(item, items=[]):
    items.append(item)
    return items

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [1, 2] - not fresh!
print(add_to_list(3))  # [1, 2, 3]

# CORRECT: Use None and create new list
def add_to_list(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [2] - fresh list
print(add_to_list(3))  # [3] - fresh list
```

## Exercises by Bloom Level

- **Remember**: What happens to local variables when a function ends?
- **Understand**: How do closures "remember" variables?
- **Apply**: Create a counter closure that increments and decrements.
- **Analyze**: Trace how a closure captures variables from its enclosing scope.
- **Create**: Build a function factory that creates multiple independent closures.

## Related Concepts
- [[Python - Functions - Scope & Variables]] — Scope and variable visibility
- [[Python - Functions - Definition Basics]]
- [[Python - Functions - Parameters & Return Values]]
- [[Python - Functions - Lambda Functions]]

## MOC
- Parent: [[Python - Functions (MOC)]]
