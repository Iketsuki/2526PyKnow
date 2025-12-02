---
tags: [python, exercises, dicts]
difficulty: Beginner
---

# Python - Dicts - Modification & Methods — Exercises

See concept: [[Python - Dicts - Modification & Methods]]
GitHub link: [Python - Dicts - Modification & Methods](./Python%20-%20Dicts%20-%20Modification%20%26%20Methods.md)

## Quick syntax fixes

1) Broken: assigning to dict.key instead of dict['key']
```python
data = {}
data.key = 1
```
<details><summary>Answer</summary>

```python
data = {}
data['key'] = 1
```
Explanation: Use bracket syntax to set dict items.
</details>

2) Broken: using pop without default
```python
value = d.pop('x')
```
<details><summary>Answer</summary>

```python
value = d.pop('x', None)
```
Explanation: Provide a default to avoid KeyError.
</details>

3) Broken: modifying dict while iterating keys
```python
for k in d:
    if k == 'x':
        del d[k]
```
<details><summary>Answer</summary>

```python
for k in list(d.keys()):
    if k == 'x':
        del d[k]
```
Explanation: Iterate a copy of keys when removing items.
</details>

---

## Easy

a) Add a key 'name' with value from input to an empty dict and print it.

Starter code:
```python
# TODO: read name and add to dict
pass
```
<details><summary>Answer</summary>

```python
name = input()
person = {}
person['name'] = name
print(person)
```
Explanation: Use dict assignment to store values.
</details>

b) Given dict `d` print the value for key 'a' or 'not found'.

Starter code:
```python
d = {'b':2}
# TODO: print d['a'] or 'not found'
pass
```
<details><summary>Answer</summary>

```python
d = {'b':2}
print(d.get('a', 'not found'))
```
Explanation: `get` returns default when key missing.
</details>

---

## Medium

a) Remove a key 'x' from dict safely and print removed value or 'none'.

Starter code:
```python
d = {'x':5}
# TODO: pop safely
pass
```
<details><summary>Answer</summary>

```python
d = {'x':5}
value = d.pop('x', 'none')
print(value)
```
Explanation: `pop` with default avoids KeyError.
</details>

b) Merge two dicts and print keys count.

Starter code:
```python
a = {'x':1}
b = {'y':2}
# TODO: merge and count keys
pass
```
<details><summary>Answer</summary>

```python
a = {'x':1}
b = {'y':2}
a.update(b)
print(len(a))
```
Explanation: `update` adds items from second dict.
</details>

---

## Hard

Write a function that takes a list of (name,score) pairs and returns a dict mapping name->max score.

Starter code:
```python
def best_scores(pairs):
    # TODO: build dict of max scores
    pass

print(best_scores([('a',2),('a',3)]))
```
<details><summary>Answer</summary>

```python
def best_scores(pairs):
    out = {}
    for name, score in pairs:
        if name not in out or score > out[name]:
            out[name] = score
    return out

print(best_scores([('a',2),('a',3)]))
```
Explanation: Track the maximum seen for each key.
</details>
