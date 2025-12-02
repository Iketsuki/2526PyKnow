---
tags: [python, exercises, variables, scope]
difficulty: Beginner
---

# Python - Variables & Types - Scope — Exercises

See concept: [[Python - Variables & Types - Scope]]
GitHub link: [Python - Variables & Types - Scope](./Python%20-%20Variables%20%26%20Types%20-%20Scope.md)

## Quick syntax fixes

1) Broken: using local variable outside function
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

2) Broken: modifying global without return
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
Explanation: Avoid modifying globals directly; return new value.
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
Explanation: Assign returned value to a variable at module level.
</details>

---

## Easy

a) Write a function that returns 10, assign it to a variable and print.

Starter code:
```python
def give_ten():
    # TODO: return 10
    pass
v = give_ten()
print(v)
```
<details><summary>Answer</summary>

```python
def give_ten():
    return 10
v = give_ten()
print(v)
```
Explanation: Return values are for passing data out of functions.
</details>

b) Fix code so function increments a number and the change is visible outside.

Starter code:
```python
count = 1
def inc():
    count = count + 1
inc()
print(count)
```
<details><summary>Answer</summary>

```python
count = 1
def inc(c):
    return c + 1
count = inc(count)
print(count)
```
Explanation: Return new value and assign it to the global variable.
</details>

---

## Medium

a) Use a global variable correctly by returning new value from function.

Starter code:
```python
total = 0
def add(n):
    # TODO: return total + n without using global keyword
    pass
total = add(5)
print(total)
```
<details><summary>Answer</summary>

```python
total = 0
def add(n):
    return total + n
total = add(5)
print(total)
```
Explanation: Use return to avoid global side-effects.
</details>

b) Explain local vs global with a short code sample (fill the TODOs).

Starter code:
```python
value = 2
def f():
    value = 3
    return value
print(value)
print(f())
```
<details><summary>Answer</summary>

```python
value = 2
def f():
    value = 3
    return value
print(value)  # prints 2 - global value
print(f())    # prints 3 - local value
```
Explanation: Local variables inside function do not change global ones.
</details>

---

## Hard

Write a function that uses an outer variable from a closure and returns a function that adds to that outer value.

Starter code:
```python
def make_adder(x):
    # TODO: return a function that adds x to its input
    pass
add5 = make_adder(5)
print(add5(2))  # expect 7
```
<details><summary>Answer</summary>

```python
def make_adder(x):
    def inner(y):
        return x + y
    return inner
add5 = make_adder(5)
print(add5(2))  # prints 7
```
Explanation: Inner function closes over `x` from outer scope.
</details>
