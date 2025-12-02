---
tags: [python, exercises, functions]
difficulty: Beginner
---

# Python - Functions - Default Parameters & Keywords — Exercises

See concept: [[Python - Functions - Default Parameters & Keywords]]
GitHub link: [Python - Functions - Default Parameters & Keywords](./Python%20-%20Functions%20-%20Default%20Parameters%20%26%20Keywords.md)

## Quick syntax fixes

1) Broken: default after required kw-only without default
```python
def f(x, y=1, z):
    pass
```
<details><summary>Answer</summary>

```python
def f(x, z, y=1):
    pass
```
Explanation: parameters with defaults must follow required params.
</details>

2) Broken: using None default and mutable default
```python
def f(a=[]):
    a.append(1)
```
<details><summary>Answer</summary>

```python
def f(a=None):
    if a is None:
        a = []
    a.append(1)
```
Explanation: avoid mutable defaults like lists.
</details>

3) Broken: wrong keyword argument name
```python
def f(x=1):
    pass
f(y=2)
```
<details><summary>Answer</summary>

```python
def f(x=1):
    pass
f(x=2)
```
Explanation: use correct keyword names.
</details>

---

## Easy

a) Write a function with default `greet='Hi'` that prints the greeting and a name.

Starter code:
```python
def say(name, greet='Hi'):
    # TODO: print greeting and name
    pass

say('Ann')
```
<details><summary>Answer</summary>

```python
def say(name, greet='Hi'):
    print(greet, name)

say('Ann')
```
Explanation: default parameter used when not provided.
</details>

b) Call a function with a keyword argument for clarity.

Starter code:
```python
def add(a,b):
    print(a+b)
# TODO: call using keywords
pass
```
<details><summary>Answer</summary>

```python
def add(a,b):
    print(a+b)
add(a=2, b=3)
```
Explanation: keyword call names arguments explicitly.
</details>

---

## Medium

a) Write a function with a default list handled safely.

Starter code:
```python
def collect(item, bag=None):
    # TODO: append item to bag safely
    pass

collect('a')
```
<details><summary>Answer</summary>

```python
def collect(item, bag=None):
    if bag is None:
        bag = []
    bag.append(item)
    return bag

collect('a')
```
Explanation: create new list when default is None.
</details>

b) Write a function that accepts a keyword `times=1` and repeats a string.

Starter code:
```python
def repeat(s, times=1):
    # TODO: return repeated string
    pass

print(repeat('x', 3))
```
<details><summary>Answer</summary>

```python
def repeat(s, times=1):
    return s * times

print(repeat('x', 3))
```
Explanation: default used when not provided.
</details>

---

## Hard

Write a function that accepts `**kwargs` and returns a string showing keys sorted with their values.

Starter code:
```python
def show_kwargs(**kwargs):
    # TODO: return sorted keys and values
    pass

print(show_kwargs(b=2,a=1))
```
<details><summary>Answer</summary>

```python
def show_kwargs(**kwargs):
    return ','.join(f"{k}={kwargs[k]}" for k in sorted(kwargs.keys()))

print(show_kwargs(b=2,a=1))
```
Explanation: sort keys before formatting.
</details>
