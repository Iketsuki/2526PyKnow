---
tags: [python, functions, basics]
moc: [[Python - Functions (MOC)]]
difficulty: Beginner
bloom_level: Understand
learning_objectives:
  - "Remember: function definition and call syntax."
  - "Understand: parameters and return values."
  - "Apply: write and use functions."
---

# Python - Functions - Parameters & Return Values

## What are Parameters?

**Parameters** are inputs to a function. Think of them like slots in a box.

```python
def greet(name):  # 'name' is a parameter
    print(f'Hello, {name}!')

greet('Alice')  # 'Alice' is the argument
```

Parameters are in the definition. Arguments are what you pass when calling.

## Using One Parameter

```python
def say_name(name):
    print(name)

say_name('Alice')  # Output: Alice
say_name('Bob')    # Output: Bob
```

## Using Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(5, 3)  # Output: 8
add(10, 20)  # Output: 30
```

## What is Return?

**Return** gives back a value from the function.

```python
def add(a, b):
    total = a + b
    return total  # Send back the answer

result = add(5, 3)
print(result)  # 8
```

Without `return`, you get `None`.

## Real Examples

**Grade Checker**
```python
def check_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    else:
        return 'C'

grade = check_grade(85)
print(grade)  # B
```

**Discount Calculator**
```python
def apply_discount(price, discount):
    final = price - discount
    return final

new_price = apply_discount(50, 10)
print(new_price)  # 40
```

**Double a Number**
```python
def double(number):
    return number * 2

result = double(5)
print(result)  # 10
```

## Default Parameters

You can give parameters a default value:

```python
def greet(name, greeting='Hello'):
    return f'{greeting}, {name}!'

print(greet('Alice'))  # Hello, Alice!
print(greet('Bob', 'Hi'))  # Hi, Bob!
```

## Returning Multiple Values

```python
def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

q, r = divide(17, 5)
print(q)  # 3
print(r)  # 2
```

## Exercises by Bloom Level

- **Remember:** What is a parameter?
- **Understand:** What does `return` do?
- **Apply:** Write a function that adds two numbers and returns the result.
- **Create:** Write a function that checks if a number is positive.

## Common Errors with Example Code

1) Forgetting `return`

WRONG
```python
def add(a, b):
    total = a + b
    # No return!

result = add(5, 3)
print(result)  # None
```

CORRECT
```python
def add(a, b):
    total = a + b
    return total

result = add(5, 3)
print(result)  # 8
```

2) Wrong parameter order

WRONG
```python
def create_profile(name, age):
    return f'{name} is {age}'

profile = create_profile(25, 'Bob')  # Wrong order!
print(profile)  # 25 is Bob (wrong!)
```

CORRECT
```python
def create_profile(name, age):
    return f'{name} is {age}'

profile = create_profile('Bob', 25)  # Correct order
print(profile)  # Bob is 25
```

3) Forgetting parentheses when calling

WRONG
```python
def greet(name):
    return f'Hello, {name}!'

result = greet  # No ()!
print(result)  # Shows function, not message
```

CORRECT
```python
def greet(name):
    return f'Hello, {name}!'

result = greet('Alice')  # With ()
print(result)  # Hello, Alice!
```

## Tips
- **Parameters** go in the definition
- **Arguments** go in the call
- **Return** sends back a value
- Parameters can have **default values**

## Related Concepts
- [[Python - Functions - Definition Basics]]
- [[Python - Conditionals - If-Else Basics]]

## MOC
- Parent: [[Python - Functions (MOC)]]

## MOC
- Parent: [[Python - Functions (MOC)]]
