---
tags: [python, exercises, functions]
difficulty: Beginner
---

# Exercises — Functions: Definition Basics

See concept: [[Python - Functions - Definition Basics]]

### Quick syntax fixes

1) Missing colon after def:
```python
def say_hello()
    print('Hi')
```
<details><summary>Answer</summary>

```python
def say_hello():
    print('Hi')
```
Explanation: Add `:` after function header and indent body.
</details>

2) Wrong function call syntax:
```python
def f():
    return 1
print f()
```
<details><summary>Answer</summary>

```python
def f():
    return 1
print(f())
```
Explanation: Calls need parentheses in Python 3.
</details>

3) Indentation error:
```python
def f():
print('x')
```
<details><summary>Answer</summary>

```python
def f():
    print('x')
```
Explanation: Function body must be indented.
</details>

---

## Easy

### a) Define a function that prints Hello

Input example:
```text
(no input)
```

Output example:
```text
Hello
```

Starter code:
```python
# TODO: write function say_hello and call it
```

<details><summary>Answer</summary>

```python
def say_hello():
    print('Hello')

say_hello()
```
Explanation: Define the function then call it.
</details>

### b) Function that returns double

Input example:
```text
3
```

Output example:
```text
6
```

Starter code:
```python
n = int(input())
# TODO: write a function double(x) that returns x*2, then print double(n)
```

<details><summary>Answer</summary>

```python
def double(x):
    return x * 2

n = int(input())
print(double(n))
```
Explanation: Use `return` to give value back from function.
</details>

---

## Medium

### a) Function that greets a name

Input example:
```text
Lily
```

Output example:
```text
Hi Lily
```

Starter code:
```python
name = input()
# TODO: write greet(name) that prints 'Hi <name>' and call it
```

<details><summary>Answer</summary>

```python
def greet(name):
    print('Hi', name)

name = input()
greet(name)
```
Explanation: Pass the input to the function and print inside.
</details>

### b) Function that adds two numbers

Input example:
```text
2
5
```

Output example:
```text
7
```

Starter code:
```python
a = int(input())
b = int(input())
# TODO: write add(x,y) returning sum, then print add(a,b)
```

<details><summary>Answer</summary>

```python
def add(x, y):
    return x + y

a = int(input())
b = int(input())
print(add(a, b))
```
Explanation: Functions can return values to use later.
</details>

---

## Hard

### Single: Function that returns the longer of two words

Input example:
```text
cat
doggy
```

Output example:
```text
doggy
```

Starter code:
```python
a = input()
b = input()
# TODO: write longer(x,y) and print the result
```

<details><summary>Answer</summary>

```python
def longer(x, y):
    if len(x) >= len(y):
        return x
    else:
        return y

a = input()
b = input()
print(longer(a, b))
```
Explanation: Use `len()` to compare string lengths and return the correct word.
</details>
