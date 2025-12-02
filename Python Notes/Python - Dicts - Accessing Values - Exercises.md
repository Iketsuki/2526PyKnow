---
tags: [python, exercises, dicts]
difficulty: Beginner
---

# Exercises — Dicts: Accessing Values

See concept: [[Python - Dicts - Accessing Values]]

GitHub link: [Python - Dicts - Accessing Values](./Python%20-%20Dicts%20-%20Accessing%20Values.md)

### Quick syntax fixes

1) Using dot access instead of bracket:
```python
d = {'x':1}
print(d.x)
```
<details><summary>Answer</summary>

```python
d = {'x':1}
print(d['x'])
```
Explanation: Use `d[key]` to access values in dicts.
</details>

2) Key error when missing:
```python
d = {}
print(d['a'])
```
<details><summary>Answer</summary>

```python
d = {}
print(d.get('a'))
```
Explanation: `get` returns `None` if key missing instead of raising an error.
</details>

3) Using get incorrectly:
```python
d = {'a':1}
print(d.get('b', None))
```
<details><summary>Answer</summary>

```python
d = {'a':1}
print(d.get('b', 'Not found'))
```
Explanation: Provide a helpful default value when using `get`.
</details>

---

## Easy

### a) Print value for key

Input example:
```text
name
Bob
```

Output example:
```text
Bob
```

Starter code:
```python
k = input()        # k is the key name
v = input()        # v is the value
my_dict = {k: v}
# TODO: print the value for key k
```

<details><summary>Answer</summary>

```python
k = input()
v = input()
my_dict = {k: v}
print(my_dict[k])
```
Explanation: Look up the value using the key.
</details>

### b) Use get to avoid key error

Input example:
```text
age
```

Output example:
```text
Not found
```

Starter code:
```python
my_dict = {'name': 'Ana'}
key_name = input()  # key to look up
# TODO: print value if exists else print 'Not found'
```

<details><summary>Answer</summary>

```python
my_dict = {'name': 'Ana'}
key_name = input()
print(my_dict.get(key_name, 'Not found'))
```
Explanation: `get` returns the default when key missing.
</details>

---

## Medium

### a) Pop a key and show it

Input example:
```text
name
```

Output example:
```text
Ana
{'age': '7'}
```

Starter code:
```python
d = {'name': 'Ana', 'age': '7'}
key_to_pop = input()  # key to remove and show
# TODO: pop the key and then print popped value and the remaining dict
```

<details><summary>Answer</summary>

```python
d = {'name': 'Ana', 'age': '7'}
key_to_pop = input()
val = d.pop(key_to_pop, None)
print(val)
print(d)
```
Explanation: `pop` removes key and returns its value; default avoids KeyError.
</details>

### b) Safely access nested-like dict (simple)

Input example:
```text
key1
```

Output example:
```text
Not found
```

Starter code:
```python
d = {'a': {'b': 'x'}}
key = input()  # first-level key to check
# TODO: print d[key]['b'] if exists else print 'Not found'
```

<details><summary>Answer</summary>

```python
d = {'a': {'b': 'x'}}
key = input()
if key in d and 'b' in d[key]:
    print(d[key]['b'])
else:
    print('Not found')
```
Explanation: Check keys step-by-step to avoid errors.
</details>

---

## Hard

### Single: Merge values from two keys into a list

Input example:
```text
k1
k2
```

Output example:
```text
['v1', 'v2']
```

Starter code:
```python
d = {'k1': 'v1', 'k2': 'v2'}
key1 = input()  # first key
key2 = input()  # second key
# TODO: make a list with values for key1 and key2 and print it
```

<details><summary>Answer</summary>

```python
d = {'k1': 'v1', 'k2': 'v2'}
key1 = input()
key2 = input()
values = [d.get(key1), d.get(key2)]
print(values)
```
Explanation: Use `get` to safely retrieve values; result may include None if missing.
</details>
