---
tags: [python, variables, types, functions]
moc: [[Python - Variables & Types (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: common built-in functions."
  - "Understand: type(), len(), str(), etc."
  - "Apply: use built-ins to check and convert data."
---

# Python - Variables & Types - Built-in Functions

## Concept
**Built-in functions** — Pre-made functions available without importing. Examples: `type()`, `len()`, `str()`, `int()`, `float()`, `list()`, `dict()`.

## Type Checking with type()

```python
# Check data type
x = 42
print(type(x))  # <class 'int'>

name = 'Alice'
print(type(name))  # <class 'str'>

items = [1, 2, 3]
print(type(items))  # <class 'list'>

# Using type() in logic
value = input('Enter something: ')
if type(value) == str:
    print('It is a string')
```

## Using isinstance() for Safety

```python
# isinstance() is better for type checking
value = 42

if isinstance(value, int):
    print('value is an integer')

if isinstance(value, (int, float)):
    print('value is a number')

# Works with inheritance (advanced)
if isinstance(value, object):
    print('Everything is an object in Python')
```

## Length with len()

```python
# Get length of sequences
text = 'hello'
print(len(text))  # 5

items = [1, 2, 3, 4]
print(len(items))  # 4

data = {'name': 'Bob', 'age': 14}
print(len(data))  # 2 (counts keys)

# Common pattern: check if list is empty
if len(items) > 0:
    print('List has items')

# Better: truthiness
if items:  # Empty list is falsy
    print('List has items')
```

## Type Conversion Functions

```python
# str() - convert to string
age = 14
message = 'I am ' + str(age) + ' years old'
print(message)  # I am 14 years old

# int() - convert to integer
score = int('95')  # 95
pi = int(3.14)  # 3 (truncates)

# float() - convert to float
price = float('9.99')  # 9.99
whole = float(10)  # 10.0

# bool() - convert to boolean
print(bool(1))  # True
print(bool(0))  # False
print(bool('hello'))  # True
print(bool(''))  # False
```

## Range and Sequence Creation

```python
# range() - create sequence of numbers
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(2, 5):
    print(i)  # 2, 3, 4

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# list() - convert to list
text = 'hello'
chars = list(text)  # ['h', 'e', 'l', 'l', 'o']

numbers = list(range(5))  # [0, 1, 2, 3, 4]

# tuple() - convert to tuple
items = tuple([1, 2, 3])  # (1, 2, 3)
```

## Min, Max, Sum, Abs

```python
scores = [85, 92, 78, 95, 88]

print(max(scores))  # 95
print(min(scores))  # 78
print(sum(scores))  # 438
print(len(scores))  # 5
average = sum(scores) / len(scores)  # 87.6

# Absolute value (distance from zero)
print(abs(-5))  # 5
print(abs(3.14))  # 3.14
print(abs(-42))  # 42
```

## Sorting with sorted()

```python
scores = [85, 92, 78, 95, 88]
sorted_scores = sorted(scores)
print(sorted_scores)  # [78, 85, 88, 92, 95]

# Reverse sort
reverse = sorted(scores, reverse=True)
print(reverse)  # [95, 92, 88, 85, 78]

# Sort strings
names = ['Zara', 'Alice', 'Bob']
print(sorted(names))  # ['Alice', 'Bob', 'Zara']
```

## Round, Floor, Ceil

```python
# round() - built-in
price = 3.14159
print(round(price))  # 3
print(round(price, 2))  # 3.14

# For floor/ceil, import math
import math
print(math.floor(3.9))  # 3
print(math.ceil(3.1))  # 4
```

## Real-World: Validate Grades

```python
def get_valid_grade():
    while True:
        try:
            grade = input('Enter grade (0-100): ')
            grade = int(grade)
            
            if 0 <= grade <= 100:
                return grade
            else:
                print('Grade must be 0-100')
        except ValueError:
            print(f'Invalid input: {grade}')

grade = get_valid_grade()
print(f'Your grade: {grade}')
```

## Real-World: Safe List Processing

```python
def process_scores(data):
    # Check if data is a list
    if not isinstance(data, list):
        print('Error: must be a list')
        return None
    
    if len(data) == 0:
        print('Error: list is empty')
        return None
    
    # Find min, max, average
    min_score = min(data)
    max_score = max(data)
    avg_score = sum(data) / len(data)
    
    return {
        'min': min_score,
        'max': max_score,
        'avg': round(avg_score, 2)
    }

result = process_scores([85, 92, 78, 95])
print(result)  # {'min': 78, 'max': 95, 'avg': 87.5}
```

## Real-World: Leaderboard Ranking

```python
# Game scores
scores = [45, 92, 78, 92, 55, 100]

# Get unique scores (sorted)
top_scores = sorted(set(scores), reverse=True)
print(f'Top {len(top_scores)} scores: {top_scores}')

# Find position
player_score = 92
rank = top_scores.index(player_score) + 1
print(f'Rank: {rank}')
```

## Common Built-ins Reference

```python
# Type checking
type(x)  # Returns type
isinstance(x, int)  # True/False

# Size/length
len(x)  # Length of sequence
abs(x)  # Absolute value

# Type conversion
int(x)  # To integer
str(x)  # To string
float(x)  # To float
bool(x)  # To boolean
list(x)  # To list
tuple(x)  # To tuple
dict(x)  # To dict

# Sequences
range(start, stop, step)  # Number sequence
sorted(x)  # Returns sorted list
reversed(x)  # Returns reversed

# Math
sum(x)  # Sum of elements
min(x)  # Smallest
max(x)  # Largest
round(x, decimals)  # Round number
```

## Exercises by Bloom Level
- Remember: Name 5 built-in functions.
- Understand: When would you use `isinstance()` vs `type()`?
- Apply: Use built-ins to process a list of numbers.
- Analyze: Compare safety of `int()` vs type checking.
- Create: Build input function using built-ins to validate data.

## Common Errors
- Forgetting `len()` returns count, not last index.
- `type()` vs `isinstance()` — use `isinstance()` when possible.
- `int('3.14')` crashes — convert float first.

## Related Concepts
- [[Python - Variables & Types - Type Checking]]
- [[Python - Variables & Types - Type Conversion]]
- [[Python - Conditionals - Truthiness]]
- [[Python - Debugging - Exception Handling]]

## MOC
- Parent: [[Python - Variables & Types (MOC)]]
