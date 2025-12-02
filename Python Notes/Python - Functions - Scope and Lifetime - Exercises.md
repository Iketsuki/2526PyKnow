---
tags: [python, exercises, functions, lifetime]
difficulty: Beginner
---

# Python - Functions - Scope and Lifetime — Exercises

See concept: [[Python - Functions - Scope and Lifetime]]
GitHub link: [Python - Functions - Scope and Lifetime](./Python%20-%20Functions%20-%20Scope%20and%20Lifetime.md)

## Quick syntax fixes

1) Broken: assuming variable lives after function without return
```python
# Broken
def f():
    a = 1
f()
print(a)
```
<details><summary>Answer</summary>

```python
# Fixed
def f():
    a = 1
    return a
a = f()
print(a)
```
Explanation: Return values if you need them outside function.
</details>

2) Broken: expecting local to persist across calls
```python
# Broken
def f():
    x = 0
    x += 1
    print(x)
f()
f()
```
<details><summary>Answer</summary>

```python
# Fixed
def f(x=[0]):
    x[0] += 1
    print(x[0])
f()
f()
```
Explanation: Mutable defaults persist; better use closures for state.
</details>

3) Broken: accessing variable before assignment in loop scope
```python
# Broken
for i in range(3):
    pass
print(i)
```
<details><summary>Answer</summary>

```python
# Fixed
for i in range(3):
    pass
print(i)
```
Explanation: Loop variables are available after loop in Python.
</details>

---

## Easy

a) Show that a variable created inside `if` block exists after the block.

Starter code:
```python
if True:
    x = 5
print(x)
```
<details><summary>Answer</summary>

```python
if True:
    x = 5
print(x)  # 5
```
Explanation: Blocks do not create new scope at module level.
</details>

b) Show that variable inside function is not visible outside.

Starter code:
```python
def f():
    y = 2
f()
try:
    print(y)
except NameError:
    print('no')
```
<details><summary>Answer</summary>

```python
def f():
    y = 2
f()
try:
    print(y)
except NameError:
    print('no')  # prints 'no'
```
Explanation: Function locals are not in global namespace.
</details>

---

## Medium

a) Demonstrate that default argument is evaluated once by showing list default behavior.

Starter code:
```python
def f(lst=[]):
    lst.append(1)
    return lst
print(f())
print(f())
```
<details><summary>Answer</summary>

```python
def f(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst
print(f())
print(f())
```
Explanation: Use None sentinel to avoid shared mutable default.
</details>

b) Show lifetime of a closure variable across calls.

Starter code:
```python
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
c = make_counter()
print(c())
print(c())
```
<details><summary>Answer</summary>

```python
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
c = make_counter()
print(c())
print(c())
```
Explanation: Closure remembers outer variables between calls.
</details>

---

## Hard

Write a function that returns two functions: one to add and one to get current value.

Starter code:
```python
def make_pair():
    # TODO: return (add, get) functions sharing same state
    pass
add, get = make_pair()
add(2)
print(get())
```
<details><summary>Answer</summary>

```python
def make_pair():
    value = 0
    def add(n):
        nonlocal value
        value += n
    def get():
        return value
    return add, get
add, get = make_pair()
add(2)
print(get())
```
Explanation: Multiple inner functions can share the same closed-over state.
</details>
