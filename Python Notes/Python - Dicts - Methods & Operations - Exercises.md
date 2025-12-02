---
tags: [python, exercises, dicts]
difficulty: Beginner
---

# Exercises — Dicts: Methods & Operations

See concept: [[Python - Dicts - Methods & Operations]]

GitHub link: [Python - Dicts - Methods & Operations](./Python%20-%20Dicts%20-%20Methods%20%26%20Operations.md)

### Quick syntax fixes

1) Using update wrong:
```python
d1 = {'a':1}
d2 = {'b':2}
d1.update
```
<details><summary>Answer</summary>

```python
d1 = {'a':1}
d2 = {'b':2}
d1.update(d2)
```
Explanation: Call `update()` with the dict to merge.
</details>

2) Wrong pop syntax:
```python
d = {'a':1}
d.pop()
```
<details><summary>Answer</summary>

```python
d = {'a':1}
val = d.pop('a')
```
Explanation: `pop` requires the key; it returns the removed value.
</details>

3) Clear usage missing parentheses:
```python
d = {'a':1}
d.clear
```
<details><summary>Answer</summary>

```python
d = {'a':1}
d.clear()
```
Explanation: Methods need `()` to be called.
</details>

---

## Easy

### a) Update a dict with one pair and print

Input example:
```text
city
Paris
```

Output example:
```text
{'city': 'Paris'}
```

Starter code:
```python
base = {}
key_name = input()    # key to add
value_text = input()   # value to add
# TODO: update base with this pair and print base
```

<details><summary>Answer</summary>

```python
base = {}
key_name = input()
value_text = input()
base.update({key_name: value_text})
print(base)
```
Explanation: `update` merges key/value pairs into the dict.
</details>

### b) Use pop with default

Input example:
```text
age
```

Output example:
```text
None
{'name': 'Ana'}
```

Starter code:
```python
d = {'name': 'Ana'}
key_to_pop = input()  # key to remove
# TODO: pop the key with default None and print value and dict
```

<details><summary>Answer</summary>

```python
d = {'name': 'Ana'}
key_to_pop = input()
val = d.pop(key_to_pop, None)
print(val)
print(d)
```
Explanation: Provide a default to avoid KeyError if key missing.
</details>

---

## Medium

### a) Merge two small dicts

Input example:
```text
Tom
10
```

Output example:
```text
{'name': 'Tom', 'age': '10'}
```

Starter code:
```python
d1 = {'name': input()}  # name value
d2 = {'age': input()}   # age value
# TODO: merge d2 into d1 and print d1
```

<details><summary>Answer</summary>

```python
d1 = {'name': input()}
d2 = {'age': input()}
d1.update(d2)
print(d1)
```
Explanation: `update()` adds keys from d2 into d1.
</details>

### b) Clear the dict when command 'clear' given

Input example:
```text
clear
```

Output example:
```text
{}
```

Starter code:
```python
d = {'a':1, 'b':2}
cmd = input()  # command from user
# TODO: if cmd == 'clear' then clear d and print it
```

<details><summary>Answer</summary>

```python
d = {'a':1, 'b':2}
cmd = input()
if cmd == 'clear':
    d.clear()
print(d)
```
Explanation: `clear()` empties the dictionary.
</details>

---

## Hard

### Single: Build a dict from two lists (keys and values)

Input example:
```text
k1
k2
v1
v2
```

Output example:
```text
{'k1': 'v1', 'k2': 'v2'}
```

Starter code:
```python
k1 = input()
k2 = input()
v1 = input()
v2 = input()
keys = [k1, k2]
values = [v1, v2]
# TODO: create a dict mapping keys[i] -> values[i] and print it
```

<details><summary>Answer</summary>

```python
k1 = input()
k2 = input()
v1 = input()
v2 = input()
keys = [k1, k2]
values = [v1, v2]
res = {}
for i in range(len(keys)):
    res[keys[i]] = values[i]
print(res)
```
Explanation: Use a simple index loop to pair keys and values.
</details>
