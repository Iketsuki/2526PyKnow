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

## What is a Function?

A **function** is a reusable block of code that does one thing.

Think of a function like a recipe:
- **Recipe:** "Mix flour and water, then bake"
- **Function:** A block of code that always does the same thing

## Making a Function with `def`

Use `def` to create a function:

```python
def say_hello():
    print('Hello!')
```

## Calling a Function

Write the function name with `()` to run it:

```python
def say_hello():
    print('Hello!')

say_hello()  # Run the function
say_hello()  # Run it again
```

Output:
```
Hello!
Hello!
```

## Why Use Functions?

**Without functions** - you repeat code:
```python
print('Hello Alice!')
print('Hello Bob!')
print('Hello Charlie!')
```

**With functions** - write once, use many times:
```python
def greet():
    print('Hello!')

greet()  # Use it 3 times
greet()
greet()
```

## Real-World Examples

**Simple Function**
```python
def play_sound():
    print('Beep!')

play_sound()
play_sound()
```

**Greeting Function**
```python
def say_goodbye():
    print('See you later!')

say_goodbye()
```

**Game Function**
```python
def start_game():
    print('Welcome to the game!')
    print('Let us begin...')

start_game()
```

## Exercises by Bloom Level

- **Remember:** Write a function that prints your name.
- **Understand:** Why is a function better than copying code?
- **Apply:** Create a function that prints 3 lines.
- **Create:** Make a function that does something fun.

## Common Errors with Example Code

1) Forgetting `def` keyword

WRONG
```python
say_hello():
    print('Hello!')
```

CORRECT
```python
def say_hello():
    print('Hello!')

say_hello()
```

2) Forgetting parentheses `()` when calling

WRONG
```python
def say_hello():
    print('Hello!')

say_hello  # Nothing happens!
```

CORRECT
```python
def say_hello():
    print('Hello!')

say_hello()  # With () it runs
```

3) Forgetting the colon `:`

WRONG
```python
def say_hello()
    print('Hello!')
```

CORRECT
```python
def say_hello():
    print('Hello!')
```

4) Not indenting inside the function

WRONG
```python
def say_hello():
print('Hello!')  # Should be indented
```

CORRECT
```python
def say_hello():
    print('Hello!')  # Indented
```

## Tips
- Use **`def name():`** to define a function
- **Indent** the code inside the function
- Use **`name()`** with parentheses to call it
- A function does nothing until you **call it**

## Related Concepts
- [[Python - Functions - Parameters & Return Values]]
- [[Python - Functions - Lambda (Anonymous Functions)]]

## MOC
- Parent: [[Python - Functions (MOC)]]

## MOC
- Parent: [[Python - Functions (MOC)]]
