---
tags: [python, exercises, functions, varargs]
difficulty: Beginner
---

# Python - Functions - Variable Arguments — Exercises

See concept: [[Python - Functions - Variable Arguments]]
GitHub link: [Python - Functions - Variable Arguments](./Python%20-%20Functions%20-%20Variable%20Arguments.md)

## Quick syntax fixes

1) Broken: wrong star usage
```python
# Broken
def f(*args, **kwargs):
    pass
f(*1)
```
<details><summary>Answer</summary>

```python
# Fixed
def f(*args, **kwargs):
    pass
f(1)
```
Explanation: `*` unpacks iterables when calling; pass plain args normally.
</details>

2) Broken: expecting dict from *args
```python
# Broken
def f(*args):
    print(args['a'])
```
<details><summary>Answer</summary>

```python
# Fixed
def f(*args, **kwargs):
    print(kwargs.get('a'))
```
Explanation: Use `kwargs` for named parameters.
</details>

3) Broken: double star for non-dict
```python
# Broken
f(**[1,2])
```
<details><summary>Answer</summary>

```python
# Fixed
f(*[1,2])
```
Explanation: `**` unpacks dicts into named args.
</details>

---

## Easy

a) Write function `sum_all(*nums)` that returns sum of all numbers.

Starter code:
```python
def sum_all(*nums):
    # TODO: return sum of nums
    pass
print(sum_all(1,2,3))
```
<details><summary>Answer</summary>

```python
def sum_all(*nums):
    return sum(nums)
print(sum_all(1,2,3))
```
Explanation: `*args` collects positional args into a tuple.
</details>

b) Write function that accepts `**info` and prints `info['name']`.

Starter code:
```python
def show(**info):
    # TODO: print name key
    pass
show(name='Ann')
```
<details><summary>Answer</summary>

```python
def show(**info):
    print(info.get('name'))
show(name='Ann')
```
Explanation: `**kwargs` collects named args into a dict.
</details>

---

## Medium

a) Combine fixed args and `*args` to build a list of all items.

Starter code:
```python
def build(first, *rest):
    # TODO: return list with first + rest
    pass
print(build(1,2,3))
```
<details><summary>Answer</summary>

```python
def build(first, *rest):
    return [first] + list(rest)
print(build(1,2,3))
```
Explanation: Mix required and variable positional args.
</details>

b) Forward `*args` and `**kwargs` from one function to another.

Starter code:
```python
def target(a,b):
    return a+b
def forward(*args, **kwargs):
    # TODO: call target with forwarded args
    pass
print(forward(2,3))
```
<details><summary>Answer</summary>

```python
def target(a,b):
    return a+b
def forward(*args, **kwargs):
    return target(*args, **kwargs)
print(forward(2,3))
```
Explanation: Use unpacking to pass arguments through.
</details>

---

## Hard

Write a decorator-style function `call_and_print(f)` that accepts any args and prints the result of calling `f` with those args.

Starter code:
```python
def call_and_print(f, *args, **kwargs):
    # TODO: call f and print return value
    pass
def add(a,b):
    return a+b
call_and_print(add, 2, 3)
```
<details><summary>Answer</summary>

```python
def call_and_print(f, *args, **kwargs):
    result = f(*args, **kwargs)
    print(result)
def add(a,b):
    return a+b
call_and_print(add, 2, 3)
```
Explanation: Use `*` and `**` to forward arguments and handle any signature.
</details>
