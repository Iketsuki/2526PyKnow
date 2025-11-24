---
tags: [python, functions, arguments]
moc: [[Python - Functions (MOC)]]
difficulty: Intermediate
bloom_level: Apply
learning_objectives:
  - "Remember: *args and **kwargs syntax."
  - "Understand: when to use variable arguments."
  - "Apply: write flexible functions."
---

# Python - Functions - Variable Arguments (*args/**kwargs)

## Concept
**\*args** — variable number of positional arguments (tuple). **\*\*kwargs** — variable number of keyword arguments (dict).

## *args (Variable Positional Arguments)

```python
# Function accepts any number of arguments
def sum_all(*args):
    print(args)  # args is a tuple
    return sum(args)

print(sum_all(1, 2, 3))  # (1, 2, 3) → 6
print(sum_all(10, 20))  # (10, 20) → 30
print(sum_all(5))  # (5,) → 5
```

## **kwargs (Variable Keyword Arguments)

```python
# Function accepts any keyword arguments
def create_profile(**kwargs):
    print(kwargs)  # kwargs is a dict
    return kwargs

result = create_profile(name='Alice', age=15, city='NYC')
print(result)  # {'name': 'Alice', 'age': 15, 'city': 'NYC'}
```

## Combining Regular + *args

```python
# First parameter required, rest optional
def greet(greeting, *names):
    for name in names:
        print(f'{greeting}, {name}!')

greet('Hello', 'Alice', 'Bob', 'Charlie')
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

## Combining Regular + **kwargs

```python
# First parameter required, rest as keywords
def introduce(name, **details):
    print(f'{name}:')
    for key, value in details.items():
        print(f'  {key}: {value}')

introduce('Alice', age=15, city='NYC', hobby='coding')
# Output:
# Alice:
#   age: 15
#   city: NYC
#   hobby: coding
```

## Combining All Three

```python
# Required + variable + variable keywords
def build_profile(name, *hobbies, **details):
    profile = {'name': name, 'hobbies': hobbies}
    profile.update(details)
    return profile

result = build_profile(
    'Alice',
    'coding',
    'gaming',
    'reading',
    age=15,
    city='NYC'
)
print(result)
# {
#   'name': 'Alice',
#   'hobbies': ('coding', 'gaming', 'reading'),
#   'age': 15,
#   'city': 'NYC'
# }
```

## Real-World: Flexible Sum Function

```python
def add(*numbers):
    if not numbers:
        return 0
    return sum(numbers)

print(add())  # 0
print(add(5))  # 5
print(add(1, 2, 3, 4, 5))  # 15
```

## Real-World: Print with Custom Separator

```python
def print_items(*items, sep=', ', end='\n'):
    text = sep.join(str(item) for item in items)
    print(text, end=end)

print_items('apple', 'banana', 'cherry')  # apple, banana, cherry
print_items('a', 'b', 'c', sep=' | ')  # a | b | c
```

## Real-World: API Call Builder

```python
def make_api_call(endpoint, **params):
    url = f'https://api.example.com/{endpoint}'
    
    # Build query string
    query_parts = []
    for key, value in params.items():
        query_parts.append(f'{key}={value}')
    
    query_string = '&'.join(query_parts)
    return f'{url}?{query_string}'

# Usage
url = make_api_call('users', id=5, name='Alice', role='admin')
print(url)
# https://api.example.com/users?id=5&name=Alice&role=admin
```

## Unpacking Arguments

```python
# Unpack list as positional arguments
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # 6 (same as add(1, 2, 3))

# Unpack dict as keyword arguments
def greet(name, age):
    return f'{name} is {age}'

data = {'name': 'Alice', 'age': 15}
print(greet(**data))  # Alice is 15
```

## Order of Parameters

```python
# Order matters:
# 1. Regular parameters
# 2. *args
# 3. **kwargs

def function(a, b, *args, **kwargs):
    pass

# This is correct
# def function(a, *args, b, **kwargs): ✗ Wrong order
```

## Exercises by Bloom Level
- Remember: What's \*args?
- Understand: When use *args vs regular parameters?
- Apply: Write function that accepts variable arguments.
- Analyze: Compare *args unpacking vs list passing.
- Create: Build flexible API function with *args and **kwargs.

## Common Errors
- Wrong order: \*\*kwargs must come after \*args.
- Forgetting asterisks: `args` is different from `*args`.
- Not unpacking when calling: `add([1, 2])` vs `add(*[1, 2])`.

## Related Concepts
- [[Python - Functions - Parameters & Return Values]]
- [[Python - Functions - Default Parameters & Keywords]]
- [[Python - Lists - Common Patterns]]

## MOC
- Parent: [[Python - Functions (MOC)]]
