---
tags: [python, exercises, functions, parameters]
difficulty: Beginner
---

# Python - Functions - Parameters & Return Values — Exercises

See concept: [[Python - Functions - Parameters & Return Values]]
GitHub link: [Python - Functions - Parameters & Return Values](./Python%20-%20Functions%20-%20Parameters%20%26%20Return%20Values.md)

## Quick syntax fixes

1) Broken: missing return
```python
# Broken
def f(x):
    x+1
print(f(2))
```
<details><summary>Answer</summary>

```python
# Fixed
def f(x):
    return x + 1
print(f(2))
```
Explanation: Use `return` to send value back to caller.
</details>

2) Broken: wrong parameter name
```python
# Broken
def greet(name):
    print('Hi', username)
greet('Ann')
```
<details><summary>Answer</summary>

```python
# Fixed
def greet(name):
    print('Hi', name)
greet('Ann')
```
Explanation: Use correct parameter names inside function.
</details>

3) Broken: too many return values
```python
# Broken
def f():
    return 1,2
print(f())
```
<details><summary>Answer</summary>

```python
# Fixed
def f():
    return (1,2)
print(f())
```
Explanation: Returning a tuple is fine; be explicit.
</details>

---

## Easy

a) Write `mul(a,b)` that returns product and show result.

Starter code:
```python
def mul(a, b):
    # TODO: return a*b
    pass
print(mul(2,3))
```
<details><summary>Answer</summary>

```python
def mul(a, b):
    return a * b
print(mul(2,3))
```
Explanation: Functions take parameters and return values.
</details>

b) Write `greet(name='friend')` with default and print greeting.

Starter code:
```python
def greet(name='friend'):
    # TODO: return greeting string
    pass
print(greet())
```
<details><summary>Answer</summary>

```python
def greet(name='friend'):
    return 'Hello ' + name
print(greet())
```
Explanation: Use default parameter values for optional args.
</details>

---

## Medium

a) Show how multiple return values work by returning two values and unpacking them.

Starter code:
```python
def stats(a,b):
    # TODO: return sum and product
    pass
s,p = stats(2,3)
print(s,p)
```
<details><summary>Answer</summary>

```python
def stats(a,b):
    return a + b, a * b
s,p = stats(2,3)
print(s,p)
```
Explanation: Functions can return tuples which can be unpacked.
</details>

b) Write a function that takes a string, capitalizes it and returns new string.

Starter code:
```python
def make_title(s):
    # TODO: return s with first letter uppercase
    pass
print(make_title('hello'))
```
<details><summary>Answer</summary>

```python
def make_title(s):
    return s.capitalize()
print(make_title('hello'))
```
Explanation: Use string methods and return result.
</details>

---

## Hard

Write `apply_twice(f, x)` that calls function `f` on `x` two times and returns result.

Starter code:
```python
def apply_twice(f, x):
    # TODO: return f(f(x))
    pass
def inc(x):
    return x+1
print(apply_twice(inc, 3))  # 5
```
<details><summary>Answer</summary>

```python
def apply_twice(f, x):
    return f(f(x))
def inc(x):
    return x+1
print(apply_twice(inc, 3))  # 5
```
Explanation: Functions can be passed and returned; use them as values.
</details>
