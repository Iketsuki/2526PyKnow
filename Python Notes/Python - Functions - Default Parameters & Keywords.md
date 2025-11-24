---
tags: [python, functions, parameters]
moc: [[Python - Functions (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: default parameter syntax."
  - "Understand: keyword arguments."
  - "Apply: use defaults and keywords in calls."
---

# Python - Functions - Default Parameters & Keyword Arguments

## Concept
**Default parameters** — parameters with pre-set values. **Keyword arguments** — pass arguments by name, not order.

## Default Parameters

```python
# Without default
def greet(name):
    return f'Hello, {name}!'

# With default
def greet_friendly(name='Friend'):
    return f'Hello, {name}!'

print(greet_friendly())  # Hello, Friend!
print(greet_friendly('Alice'))  # Hello, Alice!
```

## Multiple Defaults

```python
def create_profile(name, age=18, city='Unknown'):
    return f'{name}, {age} years old, from {city}'

print(create_profile('Alice'))  # Alice, 18 years old, from Unknown
print(create_profile('Bob', 25))  # Bob, 25 years old, from Unknown
print(create_profile('Charlie', 30, 'NYC'))  # Charlie, 30 years old, from NYC
```

## Keyword Arguments (Named Arguments)

```python
def build_url(scheme, host, port=80, path=''):
    return f'{scheme}://{host}:{port}{path}'

# Positional arguments
print(build_url('http', 'example.com'))  # http://example.com:80

# Keyword arguments (can reorder!)
print(build_url(host='example.com', scheme='https', port=443))
# https://example.com:443

# Mix positional and keyword
print(build_url('http', 'example.com', path='/about'))
# http://example.com:80/about
```

## Real-World: Recipe Function

```python
def make_pizza(size='medium', crust='normal', toppings='cheese'):
    return f'{size} {crust} crust pizza with {toppings}'

# Use defaults
print(make_pizza())  # medium normal crust pizza with cheese

# Override some
print(make_pizza(size='large'))  # large normal crust pizza with cheese

# Override with keywords (any order!)
print(make_pizza(toppings='pepperoni', size='small'))
# small normal crust pizza with pepperoni
```

## Real-World: Game Settings

```python
def create_game(difficulty='normal', sounds=True, graphics='high'):
    settings = f'Difficulty: {difficulty}, Sounds: {sounds}, Graphics: {graphics}'
    return settings

# Quick game
print(create_game())

# Hard mode
print(create_game(difficulty='hard'))

# Custom settings
print(create_game(difficulty='easy', sounds=False))
```

## Why Use Defaults?

```python
# Without defaults: must specify everything
def draw_rect_old(x, y, width, height, color, fill):
    pass

# Too many arguments for simple cases
draw_rect_old(10, 10, 50, 50, 'red', True)

# With defaults: cleaner code for common cases
def draw_rect(x, y, width=50, height=50, color='black', fill=True):
    pass

# Can use defaults for simple case
draw_rect(10, 10)  # Uses all defaults

# Override only what matters
draw_rect(10, 10, color='red', fill=False)
```

## Keyword-Only Arguments (Advanced)

```python
# Arguments after * must be keywords
def power(base, exponent=2, *, verbose=False):
    result = base ** exponent
    if verbose:
        print(f'{base} to power {exponent} = {result}')
    return result

print(power(2, 3, verbose=True))  # 2 to power 3 = 8
# power(2, 3, True)  # ERROR: can't pass verbose as positional
```

## Real-World: Configuration

```python
def connect_database(
    host='localhost',
    port=5432,
    username='admin',
    password='',
    database='mydb',
    timeout=30,
    debug=False
):
    config = {
        'host': host,
        'port': port,
        'user': username,
        'password': password,
        'db': database,
        'timeout': timeout,
        'debug': debug
    }
    return config

# Simple connection
print(connect_database())

# Custom connection with keywords
print(connect_database(
    host='remote.com',
    username='alice',
    debug=True
))
```

## Order Rule: Positional Before Keywords

```python
# RIGHT: positional first, then keywords
def greet(greeting, name, punctuation='!'):
    return f'{greeting}, {name}{punctuation}'

print(greet('Hi', 'Alice'))  # Hi, Alice!
print(greet('Hey', 'Bob', '?'))  # Hey, Bob?

# WRONG: keyword before positional
# print(greet(greeting='Hi', 'Alice'))  # SyntaxError!
```

## Default with List/Dict (Pitfall)

```python
# WRONG: mutable default changes across calls!
def add_item_wrong(item, items=[]):
    items.append(item)
    return items

print(add_item_wrong('a'))  # ['a']
print(add_item_wrong('b'))  # ['a', 'b'] — unexpected!

# RIGHT: use None and create new
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item('a'))  # ['a']
print(add_item('b'))  # ['b'] — correct!
```

## Exercises by Bloom Level
- Remember: What's a default parameter?
- Understand: When use keyword arguments?
- Apply: Add defaults to function for flexibility.
- Analyze: Compare positional vs keyword calls.
- Create: Build configuration function with many defaults.

## Common Errors
- Non-default after default: `def f(a=5, b):` is error.
- Passing keyword as positional: `f(greeting='Hi', 'Alice')` is error.
- Mutable defaults: lists/dicts in defaults are shared!

## Related Concepts
- [[Python - Functions - Parameters & Return Values]]
- [[Python - Functions - Lambda Functions]]
- [[Python - Variables & Types - Scope]]

## MOC
- Parent: [[Python - Functions (MOC)]]
