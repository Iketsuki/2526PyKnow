---
tags: [python, variables, types]
moc: [[Python - Variables & Types (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: basic types (int, float, str, bool)."
  - "Understand: what each type represents."
  - "Apply: choose the right type for a value."
---

# Python - Variables - Types Basics

## Concept
Python has basic types: `int` (whole numbers), `float` (decimals), `str` (text), `bool` (True/False).

## Example Code
```python
count = 5                  # int
price = 9.99             # float
name = 'Bob'             # str
is_student = True        # bool

print(type(count))       # <class 'int'>
```

## Exercises by Bloom Level
- Remember: List the four basic types.
- Understand: Which type would you use for a person's height?
- Apply: Assign a value of each type.
- Analyze: What happens when you mix types in operations? (e.g., `5 + 'hello'`)
- Create: Build a program that demonstrates each type.

## Common Errors with Example Code

1) Using the wrong type for an operation (TypeError)

WRONG
```python
count = 5
message = count + ' apples'  # TypeError: can only concatenate str (not "int") to str
```

CORRECT
```python
count = 5
message = str(count) + ' apples'  # Convert to string first
print(message)  # 5 apples
```

2) Mixing types without conversion (unexpected results)

WRONG
```python
price = 9.99
tax = 0.1
total = price + tax  # Works, but might confuse the types
print(total)  # 10.09 (float)

quantity = 3
total_price = price * quantity  # Works (int × float = float)
print(total_price)
```

CORRECT
```python
price = 9.99
quantity = 3
total = price * quantity
print(f'Total: ${total:.2f}')  # Explicitly format as currency
```

3) Assuming type from variable name (silent errors)

WRONG
```python
age = input('Age: ')
next_year_age = age + 1  # TypeError: age is a string!
```

CORRECT
```python
age = int(input('Age: '))
next_year_age = age + 1
print(next_year_age)
```

Short tips:
- Always know the type of your variables.
- Convert types explicitly when needed (int(), str(), float()).
- Use `type()` to check a variable's type.
- Remember: `input()` always returns a string.

## Related Concepts
- [[Python - Variables - Type Casting]]

## MOC
- Parent: [[Python - Variables & Types (MOC)]]
