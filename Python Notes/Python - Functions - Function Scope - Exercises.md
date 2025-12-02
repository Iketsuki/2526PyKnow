---
tags: [python, exercises, functions, scope]
difficulty: Beginner
---

# Python - Functions - Function Scope — Exercises

See concept: [[Python - Functions - Function Scope]]
GitHub link: [Python - Functions - Function Scope](./Python%20-%20Functions%20-%20Function%20Scope.md)

## Quick syntax fixes

1) Broken: using a variable defined inside function outside
```python
# Broken
def f():
    x = 1
f()
print(x)
```
<details><summary>Answer</summary>

```python
# Fixed
def f():
    x = 1
    return x
x = f()
print(x)
```
Explanation: Return local values to use them outside function.
</details>

2) Broken: assigning to global name inside function without return
```python
# Broken
count = 0
def inc():
    count = count + 1
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
Explanation: Pass values and return new ones instead of changing globals.
</details>

3) Broken: trying to read a local before assignment
```python
# Broken
def f():
    print(a)
    a = 1
f()
```
<details><summary>Answer</summary>

```python
# Fixed
def f():
    a = 1
    print(a)
f()
```
Explanation: Assign before use inside the same function.
</details>

---

## Easy

a) Write a function `say_hi()` that returns 'hi' and print the returned value.

Starter code:
```python
def say_hi():
    # TODO: return 'hi'
    pass
v = say_hi()
print(v)
```
<details><summary>Answer</summary>

```python
def say_hi():
    return 'hi'
v = say_hi()
print(v)
```
Explanation: Functions return values to the caller.
</details>

b) Make function `add_one(n)` that returns n+1 and show result.

Starter code:
```python
def add_one(n):
    # TODO: return n + 1
    pass
print(add_one(4))
```
<details><summary>Answer</summary>

```python
def add_one(n):
    return n + 1
print(add_one(4))
```
Explanation: Use parameter and return new value.
</details>

---

## Medium

a) Show that local `x` does not change global `x` by example.

Starter code:
```python
x = 5
def f():
    x = 2
    return x
print(x)
print(f())
```
<details><summary>Answer</summary>

```python
x = 5
def f():
    x = 2
    return x
print(x)    # prints 5
print(f())  # prints 2
```
Explanation: Function locals are separate from globals.
</details>

b) Write `set_global()` that returns new value and assign it to global variable.

Starter code:
```python
val = 1
def set_global(v):
    # TODO: return v
    pass
val = set_global(5)
print(val)
```
<details><summary>Answer</summary>

```python
val = 1
def set_global(v):
    return v
val = set_global(5)
print(val)
```
Explanation: Reassign global variable from function return.
</details>

---

## Hard

Create a function that defines a local variable then returns another function that can read that local (closure).

Starter code:
```python
def make_reader():
    # TODO: create local and return inner that reads it
    pass
r = make_reader()
print(r())
```
<details><summary>Answer</summary>

```python
def make_reader():
    local_value = 9
    def inner():
        return local_value
    return inner
r = make_reader()
print(r())  # 9
```
Explanation: Inner function closes over outer local variables.
</details>
