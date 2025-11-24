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

## Concept
**Functions** take input (**parameters**) and return output (**return value**). Structure: `def name(params): ... return result`.

## Basic Function

```python
# Define function
def greet(name):
    message = f'Hello, {name}!'
    return message

# Call function
result = greet('Alice')
print(result)  # Hello, Alice!
```

## Function with Multiple Parameters

```python
def add(a, b):
    total = a + b
    return total

result = add(5, 3)
print(result)  # 8
```

## Function with No Parameters

```python
def get_password():
    return 'super_secret'

password = get_password()
print(password)
```

## Function with No Return Value

```python
def print_welcome():
    print('Welcome!')
    # No return statement

print_welcome()  # Prints: Welcome!
# Returns None if you don't explicitly return
```

## Real-World: Grade Checker

```python
def check_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

print(check_grade(85))  # B
print(check_grade(92))  # A
print(check_grade(65))  # F
```

## Real-World: Discount Calculator

```python
def apply_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

original = 50
discounted = apply_discount(original, 20)  # 20% off
print(f'${discounted:.2f}')  # $40.00
```

## Return Multiple Values (As Tuple)

```python
def divide_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder  # Return tuple

q, r = divide_with_remainder(17, 5)
print(f'{q} remainder {r}')  # 3 remainder 2
```

## Optional Parameters (Defaults)

```python
# Parameter with default value
def greet_with_title(name, title='Friend'):
    return f'Hello, {title} {name}!'

print(greet_with_title('Alice'))  # Hello, Friend Alice!
print(greet_with_title('Bob', 'Dr.'))  # Hello, Dr. Bob!
```

## Parameters vs Arguments

```python
# Parameters (in definition)
def add(a, b):  # 'a' and 'b' are parameters
    return a + b

# Arguments (in call)
result = add(5, 3)  # 5 and 3 are arguments
```

## Scope: Local vs Global

```python
x = 10  # Global variable

def modify():
    x = 20  # Local variable (inside function)
    return x

print(modify())  # 20 (inside function)
print(x)  # 10 (outside function, unchanged)
```

## Real-World: Input Validator

```python
def is_valid_age(age):
    if age < 0:
        return False
    if age > 120:
        return False
    return True

print(is_valid_age(15))  # True
print(is_valid_age(-5))  # False
```

## Early Return (Exit Function)

```python
def check_password(password):
    if len(password) < 8:
        return False  # Return early
    
    if password == 'password':
        return False  # Return early
    
    return True  # Only reaches here if above passes

print(check_password('abc'))  # False
print(check_password('safe123'))  # True
```

## Exercises by Bloom Level
- Remember: What does `return` do?
- Understand: Difference between parameter and argument?
- Apply: Write function to convert temperature.
- Analyze: Trace function with multiple returns.
- Create: Build score calculator with custom formula.

## Common Errors with Example Code

1) Forgetting parentheses when calling → Accesses function object, doesn't run it

WRONG
def greet(name):
    return f'Hello, {name}!'

result = greet  # Forgot () - this is the function itself!
print(result)  # <function greet at 0x...> (not "Hello"!)

CORRECT
def greet(name):
    return f'Hello, {name}!'

result = greet('Alice')  # () calls the function
print(result)  # Hello, Alice!

2) Not returning a value → Function returns None by default

WRONG
def add(a, b):
    total = a + b
    # Forgot return statement!

result = add(5, 3)
print(result)  # None (oops!)

CORRECT
def add(a, b):
    total = a + b
    return total

result = add(5, 3)
print(result)  # 8

3) Confusing order of parameters → Parameters must match call order

WRONG
def create_profile(name, age):
    return f'{name} is {age}'

# Wrong order - parameters switched!
profile = create_profile(25, 'Bob')
print(profile)  # 25 is Bob (nonsense!)

CORRECT
def create_profile(name, age):
    return f'{name} is {age}'

# Correct order matches definition
profile = create_profile('Bob', 25)
print(profile)  # Bob is 25

## Related Concepts
- [[Python - Functions - Default Parameters & Keywords]]
- [[Python - Functions - Lambda Functions]]
- [[Python - Conditionals - If-Else Basics]]

## MOC
- Parent: [[Python - Functions (MOC)]]
