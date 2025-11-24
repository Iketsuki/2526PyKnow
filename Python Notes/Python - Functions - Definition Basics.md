---
tags: [python, functions, definition]
moc: [[Python - Functions (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: `def` syntax."
  - "Understand: why write functions."
  - "Apply: define and call simple functions."
---

# Python - Functions - Definition Basics

## Concept
Define reusable code with `def`. Call it by name to run the code.

## Example Code
```python
def greet():
    print('Hello!')

greet()
greet()
```

## Exercises by Bloom Level
- Remember: Write a simple function.
- Understand: Why reuse code in functions?
- Apply: Define a function with a single line.
- Analyze: When should code be in a function?
- Create: Build a program with multiple functions.

## Common Errors with Example Code

1) Defining a function but never calling it (code doesn't run)

WRONG
```python
def greet():
    print('Hello!')
# Function defined, but never called
```

CORRECT
```python
def greet():
    print('Hello!')

greet()  # Actually call the function
```

2) Forgetting parentheses when calling (referencing, not executing)

WRONG
```python
def greet():
    print('Hello!')

greet  # Just refers to function, doesn't call it
```

CORRECT
```python
def greet():
    print('Hello!')

greet()  # Parentheses execute the function
```

3) Defining a function with no body (SyntaxError)

WRONG
```python
def greet():
    # Empty, needs at least one statement
```

CORRECT
```python
def greet():
    print('Hello!')

# OR use pass as placeholder:
def placeholder():
    pass
```

Short tips:
- Use `def name():` to define a function.
- Use `name()` with parentheses to call it.
- A function does nothing until called.
- Use `pass` if you need an empty function body.

## Related Concepts
- [[Python - Functions - Parameters & Arguments]]

## MOC
- Parent: [[Python - Functions (MOC)]]
