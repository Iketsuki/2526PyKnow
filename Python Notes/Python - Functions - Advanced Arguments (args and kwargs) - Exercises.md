---
tags: [python, exercises, functions, args, kwargs]
difficulty: Beginner
---

# Python - Functions - Advanced Arguments (args and kwargs) — Exercises

See concept: [[Python - Functions - Advanced Arguments (args and kwargs)]]
GitHub link: [Python - Functions - Advanced Arguments (args and kwargs)](./Python%20-%20Functions%20-%20Advanced%20Arguments%20(args%20and%20kwargs).md)

## Quick syntax fixes

1) Broken: using * without name
```python
def f(*):
    pass
```
<details><summary>Answer</summary>

```python
def f(*args):
    pass
```
Explanation: name the * parameter, usually `*args`.
</details>

2) Broken: mixing positional after *args
```python
def f(*args, x):
    pass
```
<details><summary>Answer</summary>

```python
def f(*args, x=0):
    pass
```
Explanation: keyword-only parameters need defaults if not provided.
</details>

3) Broken: using ** before other params
```python
def f(**kwargs, x):
    pass
```
<details><summary>Answer</summary>

```python
def f(x, **kwargs):
    pass
```
Explanation: **kwargs must come last.
</details>

---

## Easy

a) Write a function that accepts any number of numbers and returns their sum.

Starter code:
```python
def total(*numbers):
    # TODO: sum numbers
    pass

print(total(1,2,3))
```
<details><summary>Answer</summary>

```python
def total(*numbers):
    return sum(numbers)

print(total(1,2,3))
```
Explanation: `*numbers` makes a tuple of args.
</details>

b) Write a function that accepts keywords and prints a value for key 'name' or 'none'.

Starter code:
```python
def show(**kwargs):
    # TODO: print name or none
    pass

show(name='Ann')
```
<details><summary>Answer</summary>

```python
def show(**kwargs):
    print(kwargs.get('name','none'))

show(name='Ann')
```
Explanation: `**kwargs` is a dict of keyword args.
</details>

---

## Medium

a) Combine positional list and extra args into one list inside function.

Starter code:
```python
def combine(base, *extras):
    # TODO: return combined list
    pass

print(combine([1], 2,3))
```
<details><summary>Answer</summary>

```python
def combine(base, *extras):
    return base + list(extras)

print(combine([1], 2,3))
```
Explanation: convert extras tuple to list and add.
</details>

b) Accept kwargs and return a dict with defaults for missing keys.

Starter code:
```python
def with_defaults(**kwargs):
    # TODO: ensure keys 'a' and 'b' exist
    pass

print(with_defaults(a=1))
```
<details><summary>Answer</summary>

```python
def with_defaults(**kwargs):
    return {'a': kwargs.get('a',0), 'b': kwargs.get('b',0)}

print(with_defaults(a=1))
```
Explanation: use get to supply defaults.
</details>

---

## Hard

Write a function that takes positional args and keyword args and returns a tuple (args_sum, keys_sorted).

Starter code:
```python
def analyze(*args, **kwargs):
    # TODO: sum args and return sorted keys of kwargs
    pass

print(analyze(1,2,x=3,y=4))
```
<details><summary>Answer</summary>

```python
def analyze(*args, **kwargs):
    return (sum(args), sorted(kwargs.keys()))

print(analyze(1,2,x=3,y=4))
```
Explanation: use sum for args and sorted on kwargs keys.
</details>
