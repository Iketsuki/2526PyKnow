---
tags: [python, exercises, dicts]
difficulty: Beginner
---

# Exercises — Dicts: Iteration

See concept: [[Python - Dicts - Iteration]]

GitHub link: [Python - Dicts - Iteration](./Python%20-%20Dicts%20-%20Iteration.md)

### Quick syntax fixes

1) Iterating over dict returns keys, not pairs:
```python
d = {'a':1}
for x in d:
    print(x[1])
```
<details><summary>Answer</summary>

```python
d = {'a':1}
for k in d:
    print(d[k])
```
Explanation: Looping directly over dict yields keys; use them to get values.
</details>

2) Using items() incorrectly:
```python
for k,v in d:
    print(k)
```
<details><summary>Answer</summary>

```python
for k, v in d.items():
    print(k)
```
Explanation: Use `d.items()` to get (key, value) pairs.
</details>

3) Modifying dict while iterating:
```python
for k in d:
    del d[k]
```
<details><summary>Answer</summary>

```python
for k in list(d.keys()):
    del d[k]
```
Explanation: Iterate over a copy (list of keys) when modifying the dict.
</details>

---

## Easy

### a) Print all keys on separate lines

Input example:
```text
(no input)
```

Output example:
```text
name
age
```

Starter code:
```python
person = {'name': 'Ana', 'age': '7'}
# TODO: print each key on its own line
```

<details><summary>Answer</summary>

```python
person = {'name': 'Ana', 'age': '7'}
for key in person:
    print(key)
```
Explanation: Looping over the dict prints keys by default.
</details>

### b) Print key: value pairs

Output example:
```text
name: Ana
age: 7
```

Starter code:
```python
d = {'name': 'Ana', 'age': '7'}
# TODO: print each key and value in 'key: value' format
```

<details><summary>Answer</summary>

```python
d = {'name': 'Ana', 'age': '7'}
for k, v in d.items():
    print(f"{k}: {v}")
```
Explanation: `items()` gives key/value pairs for easy formatting.
</details>

---

## Medium

### a) Sum numeric values in dict

Input example:
```text
(no input)
```

Output example:
```text
6
```

Starter code:
```python
scores = {'a': 1, 'b': 2, 'c': 3}
# TODO: add up the values and print the sum
```

<details><summary>Answer</summary>

```python
scores = {'a': 1, 'b': 2, 'c': 3}
total = 0
for v in scores.values():
    total += v
print(total)
```
Explanation: Use `values()` to loop only over the values.
</details>

### b) Collect keys that have value 'yes'

Input example:
```text
(no input)
```

Output example:
```text
['q1']
```

Starter code:
```python
answers = {'q1': 'yes', 'q2': 'no', 'q3': 'no'}
# TODO: make a list of keys whose value is 'yes' and print it
```

<details><summary>Answer</summary>

```python
answers = {'q1': 'yes', 'q2': 'no', 'q3': 'no'}
found = []
for k, v in answers.items():
    if v == 'yes':
        found.append(k)
print(found)
```
Explanation: Build a list of matching keys by checking each pair.
</details>

---

## Hard

### Single: Invert a small dict (values->keys) and print

Input example:
```text
(no input)
```

Output example:
```text
{'1': 'a', '2': 'b'}
```

Starter code:
```python
original = {'a': '1', 'b': '2'}
# TODO: make a new dict where original values are keys and keys are values
```

<details><summary>Answer</summary>

```python
original = {'a': '1', 'b': '2'}
inv = {}
for k, v in original.items():
    inv[v] = k
print(inv)
```
Explanation: Loop over items and assign reversed pairs to new dict.
</details>
