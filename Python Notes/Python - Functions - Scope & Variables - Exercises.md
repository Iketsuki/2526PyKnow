---
tags: [python, exercises, functions, scope, variables]
difficulty: Beginner
---

# Python - Functions - Scope & Variables — Exercises

See concept: [[Python - Functions - Scope & Variables]]
GitHub link: [Python - Functions - Scope & Variables](./Python%20-%20Functions%20-%20Scope%20%26%20Variables.md)

## Quick syntax fixes

1) Broken: modifying global without return
```python
# Broken
count = 0
def inc():
    count += 1
inc()
print(count)
```
<details><summary>Answer</summary>

```python
# Fixed
count = 0
def inc(c):
    return c + 1
count = inc(count)
print(count)
```
Explanation: Avoid changing globals in-place from functions.
</details>

2) Broken: reading uninitialized local
```python
# Broken
def f():
    print(val)
    val = 1
f()
```
<details><summary>Answer</summary>

```python
# Fixed
def f():
    val = 1
    print(val)
f()
```
Explanation: Assign before using inside same function.
</details>

3) Broken: accidental global creation
```python
# Broken
def make():
    y = 5
make()
print(y)
```
<details><summary>Answer</summary>

```python
# Fixed
def make():
    return 5
y = make()
print(y)
```
Explanation: Return values instead of relying on globals.
</details>

---

## Easy

a) Show that a local variable does not change a global variable.

Starter code:
```python
value = 10
def f():
    value = 5
    return value
print(value)
print(f())
```
<details><summary>Answer</summary>

```python
value = 10
def f():
    value = 5
    return value
print(value)   # 10
print(f())     # 5
```
Explanation: Local names shadow global names inside functions.
</details>

b) Create function `inc_by(x, n)` that returns x+n.

Starter code:
```python
def inc_by(x, n):
    # TODO: return x + n
    pass
print(inc_by(2,3))
```
<details><summary>Answer</summary>

```python
def inc_by(x, n):
    return x + n
print(inc_by(2,3))
```
Explanation: Use parameters and return to avoid globals.
</details>

---

## Medium

a) Demonstrate using `global` keyword to modify a variable defined outside function.

Starter code:
```python
cnt = 0
def add_one():
    # TODO: use global to increment cnt
    pass
add_one()
print(cnt)
```
<details><summary>Answer</summary>

```python
cnt = 0
def add_one():
    global cnt
    cnt += 1
add_one()
print(cnt)
```
Explanation: `global` allows changing module-level variables.
</details>

b) Show how to use nonlocal to modify an outer variable in nested function.

Starter code:
```python
def outer():
    x = 1
    def inner():
        # TODO: increase x using nonlocal
        pass
    inner()
    return x
print(outer())
```
<details><summary>Answer</summary>

```python
def outer():
    x = 1
    def inner():
        nonlocal x
        x += 1
    inner()
    return x
print(outer())  # 2
```
Explanation: `nonlocal` changes variable in nearest outer scope.
</details>

---

## Hard

Write a function that returns a counter function; each call to counter increases value.

Starter code:
```python
def make_counter():
    # TODO: return function that increments and returns count
    pass
c = make_counter()
print(c())
print(c())
```
<details><summary>Answer</summary>

```python
def make_counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner
c = make_counter()
print(c())
print(c())
```
Explanation: Use closure + `nonlocal` to remember state between calls.
</details>
