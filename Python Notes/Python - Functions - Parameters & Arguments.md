---
tags: [python, functions, parameters]
moc: [[Python - Functions (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: parameter syntax."
  - "Understand: how parameters work."
  - "Apply: pass data to functions."
---

# Python - Functions - Parameters & Arguments

## Concept
Parameters are names in the function definition. Arguments are values passed when calling the function.

## Example Code
```python
def add(a, b):          # a, b are parameters
    return a + b

result = add(3, 5)      # 3, 5 are arguments
```

## Exercises by Bloom Level
- Remember: Write a function with parameters.
- Understand: Difference between parameter and argument?
- Apply: Write a function that takes 3 parameters.
- Analyze: What if you pass the wrong number of arguments?
- Create: Build a function library with various parameters.

## Common Errors with Example Code

1) Passing the wrong number of arguments (TypeError)

WRONG
```python
def add(a, b):
    return a + b

result = add(5)  # TypeError: missing 1 required positional argument: 'b'
```

CORRECT
```python
def add(a, b):
    return a + b

result = add(5, 3)  # Pass both arguments
print(result)  # 8
```

2) Confusing parameter names with variable names (NameError)

WRONG
```python
def greet(name):
    print('Hello,', person)  # person is not defined, should be 'name'

greet('Alice')
```

CORRECT
```python
def greet(name):
    print('Hello,', name)  # Use the parameter name

greet('Alice')
```

3) Not passing enough arguments when function expects them

WRONG
```python
def add(a, b, c):
    return a + b + c

result = add(1, 2)  # Missing third argument
```

CORRECT
```python
def add(a, b, c):
    return a + b + c

result = add(1, 2, 3)  # All 3 arguments provided
print(result)  # 6
```

Short tips:
- Match the number of arguments to the number of parameters.
- Use parameter names correctly inside the function.
- Use function names + parentheses to call: `func(args)`.

## Related Concepts
- [[Python - Functions - Return Values]]

## MOC
- Parent: [[Python - Functions (MOC)]]
