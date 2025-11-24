---
tags: [python, functions, advanced-arguments, args, kwargs]
moc: [[Python - Functions (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: `*args` and `**kwargs` syntax."
  - "Understand: flexible argument collection and unpacking."
  - "Apply: create functions with variable arguments."
  - "Analyze: order of parameters, when to use each pattern."
  - "Create: utility functions and decorators with flexible arguments."
---

# Python - Functions - Advanced Arguments (args and kwargs)

## Concept
- **`*args`** — Collect extra positional arguments as a tuple
- **`**kwargs`** — Collect keyword arguments as a dictionary
- Allow functions to accept variable number of arguments

## Using *args (Variable Positional Arguments)

```python
# Function accepts any number of positional arguments
def print_all(*args):
    print(f'Args: {args}')  # args is a tuple
    for arg in args:
        print(arg)

print_all(1, 2, 3)  # Works
# Output:
# Args: (1, 2, 3)
# 1
# 2
# 3

print_all()  # Works with zero arguments
# Args: ()

print_all('hello')  # Works with one argument
# Args: ('hello',)
```

## Using **kwargs (Variable Keyword Arguments)

```python
# Function accepts any number of keyword arguments
def config(**kwargs):
    print(f'Kwargs: {kwargs}')  # kwargs is a dict
    for key, value in kwargs.items():
        print(f'{key} = {value}')

config(name='Alice', age=15, city='NYC')
# Output:
# Kwargs: {'name': 'Alice', 'age': 15, 'city': 'NYC'}
# name = Alice
# age = 15
# city = NYC

config()  # Works with no keyword arguments
# Kwargs: {}
```

## Combining Arguments

```python
# Regular parameters, then *args, then **kwargs
def complete_function(required, optional=10, *args, **kwargs):
    print(f'Required: {required}')
    print(f'Optional: {optional}')
    print(f'Extra positional: {args}')
    print(f'Extra keyword: {kwargs}')

complete_function(1)
# Required: 1
# Optional: 10
# Extra positional: ()
# Extra keyword: {}

complete_function(1, 2, 3, 4, name='Alice', city='NYC')
# Required: 1
# Optional: 2
# Extra positional: (3, 4)
# Extra keyword: {'name': 'Alice', 'city': 'NYC'}
```

## Unpacking with * and **

```python
# Unpack list as arguments
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # Unpacks to add(1, 2, 3)
print(result)  # 6

# Unpack dict as keyword arguments
def greet(name, age, city):
    print(f'{name}, {age}, from {city}')

person = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
greet(**person)  # Unpacks to greet(name='Alice', age=25, city='NYC')
```

## Real Examples

```python
# Example 1: Flexible print function
def smart_print(*args, sep=' ', **kwargs):
    print(sep.join(str(arg) for arg in args), **kwargs)

smart_print(1, 2, 3)  # 1 2 3
smart_print(1, 2, 3, sep='-')  # 1-2-3
smart_print(1, 2, 3, sep='-', end='!\n')  # 1-2-3!

# Example 2: Build a menu function
def menu(*options):
    for i, option in enumerate(options, 1):
        print(f'{i}. {option}')
    choice = int(input('Choose: '))
    return options[choice - 1]

selected = menu('Load', 'Save', 'Exit')

# Example 3: Configuration builder
def create_config(name, **options):
    config = {'name': name}
    config.update(options)
    return config

my_config = create_config('Database', host='localhost', port=5432, user='admin')
print(my_config)
# {'name': 'Database', 'host': 'localhost', 'port': 5432, 'user': 'admin'}

# Example 4: Wrapper function
def log_call(func, *args, **kwargs):
    print(f'Calling {func.__name__}')
    result = func(*args, **kwargs)
    print(f'Returned {result}')
    return result

def add(a, b):
    return a + b

log_call(add, 5, 3)

# Example 5: Merge multiple dicts
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5}
merged = merge_dicts(d1, d2, d3)
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

## Parameter Order Rules

When defining a function, parameters must be in this order:
1. Regular parameters
2. Parameters with defaults
3. `*args`
4. Keyword-only parameters (after `*`)
5. `**kwargs`

```python
# CORRECT order
def function(a, b=2, *args, debug=False, **kwargs):
    pass

# WRONG order (would be syntax error)
# def function(debug=False, a, *args, **kwargs): pass
```

## Real-World Patterns

```python
# Pattern 1: Decorator with flexible arguments
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Took {end - start:.2f} seconds')
        return result
    return wrapper

@timer
def slow_function(x):
    import time
    time.sleep(x)

slow_function(1)

# Pattern 2: Method overloading simulation
def function(*args):
    if len(args) == 1:
        # Handle one argument
        return args[0] * 2
    elif len(args) == 2:
        # Handle two arguments
        return args[0] + args[1]
    else:
        raise ValueError('Expected 1 or 2 arguments')

print(function(5))     # 10
print(function(5, 3))  # 8
```

## Exercises by Bloom Level

- **Remember**: Write function with `*args` and `**kwargs`.
- **Understand**: How does unpacking work? When to use each?
- **Apply**: Create flexible functions with variable arguments.
- **Analyze**: How do `*args` and `**kwargs` interact with other parameters?
- **Create**: Build wrapper functions, decorators, or utility functions.

## Common Errors with Example Code

### Error 1: Forgetting *args is a tuple, not separate parameters
```python
# WRONG: Thinking *args unpacks automatically
def add(*args):
    return args[0] + args[1] + args[2]  # What if only 2 args given?

add(1, 2)  # IndexError!

# CORRECT: Handle variable length
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

add(1, 2)  # 3
add(1, 2, 3, 4)  # 10
```

### Error 2: Wrong parameter order
```python
# WRONG: *args before default parameter
def function(a, *args, b=10):  # This is actually valid! b becomes keyword-only
    pass

# VERY WRONG: Default before *args
# def function(a, b=10, *args): pass  # Syntax error!

# CORRECT: Regular params, defaults, *args, **kwargs
def function(a, b=2, *args, debug=False, **kwargs):
    pass
```

### Error 3: Not unpacking when needed
```python
# WRONG: Passing list as single argument
numbers = [1, 2, 3]
def add(a, b, c):
    return a + b + c

result = add(numbers)  # TypeError: add() missing 2 required positional arguments

# CORRECT: Unpack with *
result = add(*numbers)  # Unpacks to add(1, 2, 3)
print(result)  # 6
```

### Error 4: Confusing kwargs keys with parameter names
```python
# WRONG: Assuming kwargs auto-matches parameters
def greet(name):
    print(f'Hello, {name}')

greet(**{'person': 'Alice'})  # TypeError: unexpected keyword argument 'person'

# CORRECT: Keys must match parameter names
greet(**{'name': 'Alice'})  # Works
# Or:
greet(name='Alice')
```

### Error 5: Mutating kwargs or args unexpectedly
```python
# WRONG: Modifying args/kwargs changes the tuple/dict
def process(*args):
    args[0] = 100  # TypeError: 'tuple' object does not support item assignment

# WRONG: Modifying mutable objects in kwargs
def update(initial, **kwargs):
    items = initial
    items.update(kwargs)  # Modifies original!
    return items

config = {'debug': False}
result = update(config, verbose=True)
print(config)  # {'debug': False, 'verbose': True} - changed!

# CORRECT: Make a copy
def update(initial, **kwargs):
    items = initial.copy()  # Copy first
    items.update(kwargs)
    return items

config = {'debug': False}
result = update(config, verbose=True)
print(config)  # {'debug': False} - unchanged
```

## Naming Convention
- **`args`** — Standard name for `*args` (not required, but conventional)
- **`kwargs`** — Standard name for `**kwargs` (not required, but conventional)
- **Alternative names**: `*values`, `**options`, etc. are valid but less common

## Tips
- Use **`*args`** when function needs any number of positional arguments.
- Use **`**kwargs`** when function needs configuration/options.
- Remember **order**: regulars → defaults → `*args` → `**kwargs`.
- Use **`*list` and `**dict`** to unpack when calling functions.
- **`args` is a tuple** (immutable), **`kwargs` is a dict** (mutable).
- **Don't mutate** `args` or objects in `kwargs` unexpectedly.

## Related Concepts
- [[Python - Functions - Definition Basics]]
- [[Python - Functions - Default Parameters & Keywords]]
- [[Python - Functions - Function Scope]]
- [[Python - Lists - Unpacking]]

## MOC
- Parent: [[Python - Functions (MOC)]]
