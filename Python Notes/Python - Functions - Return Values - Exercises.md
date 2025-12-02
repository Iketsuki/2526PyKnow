---
tags: [python, exercises, functions, return-values]
difficulty: Beginner
---

# Python - Functions - Return Values — Exercises

See concept: [[Python - Functions - Return Values]]
GitHub link: [Python - Functions - Return Values](./Python%20-%20Functions%20-%20Return%20Values.md)

## Quick syntax fixes

1) Broken: returning nothing
```python
# Broken
def f():
    x=1
print(f())
```
<details><summary>Answer</summary>

```python
# Fixed
def f():
    x = 1
    return x
print(f())
```
Explanation: Use return to pass a value back.
</details>

2) Broken: forgetting parentheses when calling function
```python
# Broken
def g():
    return 2
print(g)
```
<details><summary>Answer</summary>

```python
# Fixed
def g():
    return 2
print(g())
```
Explanation: Call the function with `()` to get return value.
</details>

3) Broken: returning mutable default accidentally reused
```python
# Broken
def f(lst=[]):
    lst.append(1)
    return lst
print(f())
print(f())
```
<details><summary>Answer</summary>

```python
# Fixed
def f(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst
print(f())
print(f())
```
Explanation: Avoid mutable defaults for safety.
</details>

---

## Easy

a) Return the sum of two numbers from a function and print it.

Starter code:
```python
def s(a,b):
    # TODO: return a+b
    pass
print(s(2,3))
```
<details><summary>Answer</summary>

```python
def s(a,b):
    return a + b
print(s(2,3))
```
Explanation: Simple return of arithmetic result.
</details>

b) Write a function that returns True if a number is even.

Starter code:
```python
def is_even(n):
    # TODO: return True if even
    pass
print(is_even(4))
```
<details><summary>Answer</summary>

```python
def is_even(n):
    return n % 2 == 0
print(is_even(4))
```
Explanation: Return boolean values from functions.
</details>

---

## Medium

a) Return a list of first n squares from a function.

Starter code:
```python
def squares(n):
    # TODO: return list of squares
    pass
print(squares(3))
```
<details><summary>Answer</summary>

```python
def squares(n):
    return [i*i for i in range(1, n+1)]
print(squares(3))
```
Explanation: Functions can return collections.
</details>

b) Return None explicitly from a function when no value is needed.

Starter code:
```python
def do_nothing():
    # TODO: return None explicitly
    pass
print(do_nothing())
```
<details><summary>Answer</summary>

```python
def do_nothing():
    return None
print(do_nothing())
```
Explanation: `None` is a valid return value.
</details>

---

## Hard

Write a function that returns another function which returns a constant value.

Starter code:
```python
def const_maker(v):
    # TODO: return function that returns v
    pass
f = const_maker(10)
print(f())
```
<details><summary>Answer</summary>

```python
def const_maker(v):
    def inner():
        return v
    return inner
f = const_maker(10)
print(f())
```
Explanation: Functions can create and return other functions.
</details>
