---
tags: [python, conditionals, truthiness]
moc: [[Python - Conditionals (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: truthy vs falsy values."
  - "Understand: which values are truthy/falsy."
  - "Apply: use truthiness in conditions."
---

# Python - Conditionals - Truthiness

## Concept
In conditions, some values are "truthy" (act like True) and others are "falsy" (act like False). Falsy: `0`, `''`, `[]`, `None`, `False`. Truthy: everything else.

## Falsy Values

```python
# All falsy values:
if False:
    print('False is falsy')

if 0:
    print('0 is falsy')  # Doesn't print

if 0.0:
    print('0.0 is falsy')  # Doesn't print

if '':
    print('Empty string is falsy')  # Doesn't print

if []:
    print('Empty list is falsy')  # Doesn't print

if ():
    print('Empty tuple is falsy')  # Doesn't print

if {}:
    print('Empty dict is falsy')  # Doesn't print

if None:
    print('None is falsy')  # Doesn't print
```

## Truthy Values

```python
# All truthy values:
if True:
    print('True is truthy')  # Prints

if 1:
    print('1 is truthy')  # Prints

if -1:
    print('-1 is truthy')  # Prints (any non-zero number)

if 'hello':
    print('Non-empty string is truthy')  # Prints

if [1, 2, 3]:
    print('Non-empty list is truthy')  # Prints

if (1, 2):
    print('Non-empty tuple is truthy')  # Prints

if {'key': 'value'}:
    print('Non-empty dict is truthy')  # Prints
```

## Practical Use: Check if Empty

```python
items = [1, 2, 3]

# OLD WAY
if len(items) > 0:
    print('Has items')

# BETTER WAY (using truthiness)
if items:
    print('Has items')

# Check if empty
if not items:
    print('No items')
```

## Check if None

```python
value = None

# Using truthiness
if not value:
    print('Value is None or falsy')

# More specific (better)
if value is None:
    print('Value is None')

# Different scenarios
if value:
    print('Value exists')
else:
    print('Value is None or falsy')
```

## Check if String Empty

```python
name = input('Name: ')

# Using truthiness
if name:
    print(f'Hello {name}')
else:
    print('Name required')

# More specific
if name == '':
    print('Name is empty')

# Best: use strip to remove spaces
if name.strip():
    print(f'Hello {name}')
```

## Real-World: Optional Input

```python
def create_profile(name, age=None, city=None):
    profile = {'name': name}
    
    if age:  # Use truthiness (works if age is 0, which is falsy!)
        profile['age'] = age
    
    # Better: explicit check for None
    if age is not None:
        profile['age'] = age
    
    if city:
        profile['city'] = city
    
    return profile

print(create_profile('Alice', 15, 'NYC'))
# {'name': 'Alice', 'age': 15, 'city': 'NYC'}
```

## Real-World: Check List Has Items

```python
scores = []

if scores:
    average = sum(scores) / len(scores)
    print(f'Average: {average}')
else:
    print('No scores yet')

# Add a score
scores.append(85)

if scores:
    average = sum(scores) / len(scores)
    print(f'Average: {average}')
```

## Real-World: Default Values

```python
# Use truthiness with 'or' for defaults
name = input('Name: ')
name = name or 'Guest'  # Use 'Guest' if name is empty

age_str = input('Age: ')
age = int(age_str) if age_str else 18  # Default 18

print(f'{name} is {age}')
```

## Caution: Zero is Falsy!

```python
# Can cause bugs:
age = 0
if age:
    print('Age is set')
else:
    print('Age not set')  # Prints! But 0 is a valid age

# Better: explicit check
if age is not None:
    print('Age is set')
```

## Using not (Negation)

```python
items = []

if not items:
    print('List is empty')

if not '':
    print('String is empty')

if not None:
    print('Value is None')

# Double negative (confusing!)
if not not [1, 2]:
    print('List is not empty')  # Just use 'if items:'
```

## Boolean Operators with Truthiness

```python
# and: True if both truthy
name = 'Alice'
age = 15

if name and age:
    print('Has both')

# or: True if either truthy
email = ''
phone = '555-1234'

if email or phone:
    print('Has contact info')

# not: Negate truthiness
password = ''

if not password:
    print('Password required')
```

## Exercises by Bloom Level
- Remember: Is empty list truthy or falsy?
- Understand: Why use `if items:` instead of `if len(items) > 0:`?
- Apply: Use truthiness to check if input is empty.
- Analyze: When is `0` valid but falsy?
- Create: Build form validator using truthiness.

## Common Errors
- Using `if x:` when `x = 0` is valid (use `if x is not None:`).
- Confusing truthiness with boolean equality.
- Not understanding that empty containers are falsy.

## Related Concepts
- [[Python - Conditionals - Boolean Logic (and-or-not)]]
- [[Python - Conditionals - Comparison Operators]]
- [[Python - Variables & Types - Type Checking]]

## MOC
- Parent: [[Python - Conditionals (MOC)]]
- Parent: [[Python - Conditionals (MOC)]]
