---
tags: [python, exercises, dicts]
difficulty: Beginner
---

# Exercises — Dicts: Creation & Initialization

See concept: [[Python - Dicts - Creation & Initialization]]

### Quick syntax fixes

1) Make a dict not a list:
```python
a = [('x',1), ('y',2)]
```
<details><summary>Answer</summary>

```python
a = {'x':1, 'y':2}
```
Explanation: Use `{}` with key:value pairs for dicts.
</details>

2) Missing colon between key and value:
```python
d = {'a' 1}
```
<details><summary>Answer</summary>

```python
d = {'a': 1}
```
Explanation: Use `:` between key and value.
</details>

3) Accessing key like attribute:
```python
print(d.a)
```
<details><summary>Answer</summary>

```python
print(d['a'])
```
Explanation: Use `dict[key]` to get values.
</details>

---

## Easy

### a) Create a dict from two inputs and print a value

Input example:
```text
color
blue
```

Output example:
```text
blue
```

Starter code:
```python
k = input()
v = input()
# TODO: make a dict with k:v and print the value for k
```

<details><summary>Answer</summary>

```python
k = input()
v = input()
d = {k: v}
print(d[k])
```
Explanation: Create a dict and use the key to get its value.
</details>

### b) Make a dict with two fixed pairs and print keys

Output example:
```text
['name', 'age']
```

Starter code:
```python
d = {'name': 'Ana', 'age': '7'}
# TODO: print the list of keys
```

<details><summary>Answer</summary>

```python
d = {'name': 'Ana', 'age': '7'}
print(list(d.keys()))
```
Explanation: `keys()` gives a view; `list()` shows keys plainly.
</details>

---

## Medium

### a) Read 3 pairs (key then value) and print dict

Input example:
```text
a
1
b
2
c
3
```

Output example:
```text
{'a': '1', 'b': '2', 'c': '3'}
```

Starter code:
```python
d = {}
# TODO: read three key/value pairs and store
```

<details><summary>Answer</summary>

```python
d = {}
for _ in range(3):
    k = input()
    v = input()
    d[k] = v
print(d)
```
Explanation: Assign `d[k] = v` for each pair.
</details>

### b) Check if key exists

Input example:
```text
age
```

Suppose `d = {'name': 'Ana', 'age': '7'}`

Output example:
```text
Yes
```

Starter code:
```python
d = {'name': 'Ana', 'age': '7'}
k = input()
# TODO: print 'Yes' if k in d else 'No'
```

<details><summary>Answer</summary>

```python
d = {'name': 'Ana', 'age': '7'}
k = input()
if k in d:
    print('Yes')
else:
    print('No')
```
Explanation: Use `in` to test key membership.
</details>

---

## Hard

### Single: Merge two small dicts and print result

Example:
```text
# dict1: name->Tom
# dict2: age->10
```

Output example:
```text
{'name': 'Tom', 'age': '10'}
```

Starter code:
```python
d1 = {'name': input()}
d2 = {'age': input()}
# TODO: merge and print
```

<details><summary>Answer</summary>

```python
d1 = {'name': input()}
d2 = {'age': input()}
# simple merge for beginners:
d1.update(d2)
print(d1)
```
Explanation: `update()` adds keys from `d2` into `d1`.
</details>
