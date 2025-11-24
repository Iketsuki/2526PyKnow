---
tags: [python, strings, formatting]
moc: [[Python - Strings (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: f-string syntax."
  - "Understand: different formatting methods."
  - "Apply: format strings for output."
---

# Python - Strings - String Formatting

## Concept
**Formatting** — insert variables into strings. Methods: f-strings (modern), `.format()`, `%` (old).

## F-Strings (Best Way)

```python
name = 'Alice'
age = 15

# Basic f-string
message = f'Hello {name}, you are {age}'
print(message)  # Hello Alice, you are 15

# Expressions inside
print(f'Next year: {age + 1}')  # Next year: 16

# Method calls
text = 'hello'
print(f'Uppercase: {text.upper()}')  # Uppercase: HELLO
```

## Formatting Numbers

```python
price = 19.567

# Round to 2 decimals
print(f'Price: ${price:.2f}')  # Price: $19.57

# Thousands separator
large = 1000000
print(f'Population: {large:,}')  # Population: 1,000,000

# Percentage
score = 0.85
print(f'Score: {score:.1%}')  # Score: 85.0%
```

## Alignment & Padding

```python
# Left align
print(f'{"Alice":<10} = 90')  # Alice      = 90

# Right align
print(f'{"Alice":>10} = 90')  #      Alice = 90

# Center
print(f'{"Alice":^10} = 90')  #   Alice    = 90

# Pad with zeros
num = 42
print(f'{num:05d}')  # 00042
```

## Format Method (Older)

```python
name = 'Bob'
age = 16

# Using .format()
message = 'Hello {}, you are {}'.format(name, age)
print(message)  # Hello Bob, you are 16

# Named arguments
message = 'Hello {name}, you are {age}'.format(name=name, age=age)
print(message)
```

## Percent Formatting (Old Style)

```python
# Not recommended, but you'll see it
name = 'Charlie'
age = 17

message = 'Hello %s, you are %d' % (name, age)
print(message)  # Hello Charlie, you are 17
```

## Real-World: Report Formatting

```python
students = [
    ('Alice', 90, 95),
    ('Bob', 85, 88),
    ('Charlie', 92, 90)
]

print('Name       Math  English')
print('-' * 25)

for name, math, english in students:
    print(f'{name:<10} {math:>4}  {english:>7}')

# Output:
# Name       Math  English
# -------------------------
# Alice        90       95
# Bob          85       88
# Charlie      92       90
```

## Real-World: Price Display

```python
items = [
    ('Apple', 1.50),
    ('Banana', 0.75),
    ('Orange', 2.25)
]

print('Item          Price')
print('-' * 20)

for item, price in items:
    print(f'{item:<12} ${price:.2f}')

# Output:
# Item          Price
# --------------------
# Apple        $1.50
# Banana       $0.75
# Orange       $2.25
```

## Combining Strings

```python
# Multiple f-strings
first = 'Hello'
second = 'World'
combined = f'{first} {second}!'
print(combined)  # Hello World!

# Using join (for many items)
words = ['Python', 'is', 'awesome']
message = ' '.join(words)
print(message)  # Python is awesome
```

## Exercises by Bloom Level
- Remember: What syntax for f-strings?
- Understand: How to format decimals?
- Apply: Create formatted table.
- Analyze: Compare f-string vs .format().
- Create: Build report with aligned columns.

## Common Errors
- Forgetting `f` before string: `'Hello {x}'` won't work (need `f'...'`).
- Wrong format specifier: `{x:.2}` should be `{x:.2f}`.
- Nested quotes: Use different quotes `f"{x's}"` or escape.

## Related Concepts
- [[Python - Strings - Basics]]
- [[Python - Strings - String Methods]]
- [[Python - IO - Output Formatting]]

## MOC
- Parent: [[Python - Strings (MOC)]]
