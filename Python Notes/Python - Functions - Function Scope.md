---
tags: [python, functions, scope, variables]
moc: [[Python - Functions (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: local vs global scope definitions."
  - "Understand: scope rules and variable lifetime."
  - "Apply: avoid scope-related bugs in functions."
  - "Analyze: scope shadowing and variable access patterns."
  - "Create: design functions with proper scope usage."
---

# Python - Functions - Function Scope

## Concept
**Scope** determines where variables exist and are accessible:
- **Local scope**: Variables inside a function (only exist inside)
- **Global scope**: Variables outside functions (accessible everywhere)
- **Nested scope**: Variables in outer functions (accessible in inner functions)
- **Built-in scope**: Python's built-in variables and functions

## Local vs Global Scope

```python
x = 10  # Global scope

def test():
    y = 5  # Local scope
    print(x)  # Can access global
    print(y)  # Can access local

test()
print(x)  # 10 (global exists here)
# print(y)  # Error: y not in this scope
```

## Variable Lifetime

```python
# GLOBAL: Exists for entire program
counter = 0

def increment():
    counter += 1  # Will error - need 'global'
    
# LOCAL: Created when function called, destroyed when function exits
def create_local():
    temp = 42
    print(temp)  # Works
    
create_local()
# print(temp)  # Error: temp no longer exists
```

## Modifying Global Variables

```python
count = 0

# WRONG: Trying to modify global without 'global' keyword
def increment_wrong():
    count += 1  # Error!

# CORRECT: Declare 'global' to modify
def increment_correct():
    global count
    count += 1

increment_correct()
print(count)  # 1
```

## Real Examples

```python
# Example 1: Scope shadowing (local hides global)
name = 'Global'

def test():
    name = 'Local'  # Shadows global
    print(name)  # 'Local'

test()
print(name)  # 'Global' (unchanged)

# Example 2: Nested function scope
def outer():
    x = 10
    
    def inner():
        print(x)  # Can access outer's x
    
    inner()  # 10

outer()

# Example 3: Function parameters are local
def greet(name):  # 'name' is local
    print(f'Hello, {name}')
    
greet('Alice')  # 'Alice'
# print(name)  # Error: name not defined

# Example 4: Return values to communicate between scopes
total = 0

def calculate(x, y):
    return x + y  # Return value to global scope

total = calculate(5, 3)
print(total)  # 8
```

## Scope Lookup Order (LEGB)

1. **Local**: Inside current function
2. **Enclosing**: In outer functions (for nested functions)
3. **Global**: At module level
4. **Built-in**: Python's built-in namespace

```python
x = 'global'

def outer():
    x = 'enclosing'
    
    def inner():
        x = 'local'
        print(x)  # 'local' - found in Local scope
    
    inner()
    print(x)  # 'enclosing'

outer()
print(x)  # 'global'
```

## Exercises by Bloom Level

- **Remember**: What is the difference between local and global scope?
- **Understand**: Why does modifying a global variable inside a function require the `global` keyword?
- **Apply**: Write a function that safely modifies a global variable.
- **Analyze**: Trace variable lookups in nested functions using LEGB order.
- **Create**: Design a counter program using global variables and functions.

## Common Errors with Example Code

### Error 1: Forgetting 'global' keyword when modifying global variable
```python
# WRONG: Trying to modify global without declaring it
count = 0

def increment():
    count += 1  # UnboundLocalError!

# CORRECT: Use 'global' keyword
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1
```

### Error 2: Assuming parameter modifications affect global variable
```python
# WRONG: Modifying parameter doesn't affect original
x = 10

def modify(x):
    x = 20  # Only modifies local parameter

modify(x)
print(x)  # 10 (unchanged!)

# CORRECT: Either return the value or use 'global'
x = 10

def modify():
    global x
    x = 20

modify()
print(x)  # 20
```

### Error 3: Referencing variable before assignment in local scope
```python
# WRONG: Using variable before assignment
x = 10

def test():
    print(x)  # UnboundLocalError
    x = 5  # x is local, but used before assignment

test()

# CORRECT: Read global OR create local first
x = 10

def test():
    print(x)  # 10 (uses global)

def test2():
    x = 5  # Assign first
    print(x)  # 5
```

### Error 4: Confusing local parameter names with globals
```python
# WRONG: Unclear which variable is being used
name = 'Global Name'

def greet(name):
    print(name)  # Local parameter, shadows global

greet('Alice')  # 'Alice' (parameter, not global)
print(name)  # 'Global Name' (unchanged)

# BETTER: Use different names or be explicit
person_name = 'Global Name'

def greet(name):
    print(f'Greeting: {name}')

greet('Alice')
print(person_name)  # Clear which is which
```

### Error 5: Using mutable global defaults (mutable as function argument)
```python
# WRONG: Mutable default argument modified across calls
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Why?!

# CORRECT: Use None, create new list each time
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [2]
```

## Tips
- Use **local variables** by default (safer, clearer).
- Use **global** sparingly; prefer returning values.
- Use `global` keyword only when you need to modify a global variable.
- Avoid **shadowing** (naming local variable same as global).
- For nested functions, use `nonlocal` to modify enclosing scope (not just global).

## Related Concepts
- [[Python - Variables - Scope Basics]]
- [[Python - Functions - Definition Basics]]
- [[Python - Functions - Default Parameters & Keywords]]

## MOC
- Parent: [[Python - Functions (MOC)]]
