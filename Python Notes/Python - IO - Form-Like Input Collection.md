---
tags: [python, io, forms]
moc: [[Python - IO (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: collecting multiple inputs in sequence."
  - "Understand: form-like data collection."
  - "Apply: gather and process user data."
---

# Python - IO - Form-Like Input Collection

## Concept
Gather multiple pieces of information from a user sequentially (like a form), then process and display.

## Real-World Example: Profile Creator

```python
print('=== Create Your Profile ===')
name = input('What is your name? ')
age = int(input('How old are you? '))
hobby = input('What is your favorite hobby? ')
color = input('What is your favorite color? ')

print('\n=== Your Profile ===')
print(f'Name: {name}')
print(f'Age: {age}')
print(f'Hobby: {hobby}')
print(f'Color: {color}')
```

## Real-World Example: Pizza Order

```python
print('=== Welcome to PizzaPlace ===')
name = input('Your name: ')
size = input('Pizza size (Small/Medium/Large): ')
toppings_str = input('Toppings (comma-separated): ')
toppings = toppings_str.split(',')

print('\n=== Your Order ===')
print(f'Customer: {name}')
print(f'Size: {size}')
print(f'Toppings: {", ".join(toppings)}')
```

## Real-World Example: School Survey

```python
print('=== Quick Survey ===')
subject = input('Your favorite subject: ')
rating = int(input('Rate school (1-10): '))
change = input('One thing you want to change: ')

if rating >= 7:
    print('You seem to enjoy school!')
else:
    print('Hope things improve!')
```

## Exercises by Bloom Level
- Remember: Collect 3 pieces of info from user.
- Understand: Why put a `print()` between input and display?
- Apply: Build a simple profile creator.
- Analyze: How to validate user input (e.g., age is positive)?
- Create: Build a multi-section form (address, contact info, etc).

## Related Concepts
- [[Python - IO - Input Basics]]
- [[Python - IO - Output Formatting]]
- [[Python - Strings - String Methods]]

## Common Errors with Example Code

Here are common mistakes when collecting multiple inputs and how to fix them.

1) Not validating numeric input (ValueError)

WRONG
```python
age = int(input('How old are you? '))  # crashes if user enters non-number
```

CORRECT
```python
while True:
  try:
    age = int(input('How old are you? '))
    if age < 0:
      print('Age cannot be negative.')
      continue
    break
  except ValueError:
    print('Please enter a whole number for age.')
```

2) Not trimming or normalizing input (extra whitespace)

WRONG
```python
toppings = input('Toppings (comma-separated): ').split(',')
# [' pepperoni', ' mushrooms']  # leading spaces remain
```

CORRECT
```python
toppings = [t.strip() for t in input('Toppings (comma-separated): ').split(',') if t.strip()]
# ['pepperoni', 'mushrooms']
```

3) Assuming inputs are non-empty (Empty strings)

WRONG
```python
name = input('Your name: ')
print('Hello,', name)  # prints 'Hello, ' if blank
```

CORRECT
```python
name = input('Your name: ').strip()
if not name:
  name = 'Guest'
print('Hello,', name)
```

Short tips:
- Always validate and sanitize user input.
- Use loops to re-prompt when input is invalid.
- Trim whitespace and handle empty fields gracefully.

## MOC
- Parent: [[Python - IO (MOC)]]
