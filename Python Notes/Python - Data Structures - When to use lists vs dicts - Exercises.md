---
tags: [python, exercises, datastructures, lists, dicts]
difficulty: Beginner
---

# Python - Data Structures - When to use lists vs dicts — Exercises

See concept: [[Python - Data Structures - When to use lists vs dicts]]
GitHub link: [Python - Data Structures - When to use lists vs dicts](./Python%20-%20Data%20Structures%20-%20When%20to%20use%20lists%20vs%20dicts.md)

## Quick syntax fixes

1) Broken: using list like dict
```python
# Broken
names = []
print(names['bob'])
```
<details><summary>Answer</summary>

```python
# Fixed
names = {'bob': 1}
print(names['bob'])
```
Explanation: Use dict for key lookup, list for ordered items.
</details>

2) Broken: using dict like list
```python
# Broken
items = {'a':1,'b':2}
print(items[0])
```
<details><summary>Answer</summary>

```python
# Fixed
items = {'a':1,'b':2}
print(items['a'])
```
Explanation: Dict keys are not index positions.
</details>

3) Broken: append to dict
```python
# Broken
d = {}
d.append('x')
```
<details><summary>Answer</summary>

```python
# Fixed
d = {}
d['x'] = 1
```
Explanation: Use assignment to add dict keys.
</details>

---

## Easy

a) Give three fruit names in a list and print the second fruit.

Starter code:
```python
fruits = ['apple','banana','cherry']
# TODO: print second fruit
pass
```
<details><summary>Answer</summary>

```python
fruits = ['apple','banana','cherry']
print(fruits[1])
```
Explanation: Lists use zero-based indexes.
</details>

b) Create a dict for a person with keys `name` and `age` and print the age.

Starter code:
```python
person = {'name': 'Ann', 'age': 10}
# TODO: print age
pass
```
<details><summary>Answer</summary>

```python
person = {'name': 'Ann', 'age': 10}
print(person['age'])
```
Explanation: Use key lookup with dicts.
</details>

---

## Medium

a) Convert a list of pairs into a dict (pairs are [key,value]).

Starter code:
```python
pairs = [['a',1], ['b',2]]
# TODO: make dict from pairs and print
pass
```
<details><summary>Answer</summary>

```python
pairs = [['a',1], ['b',2]]
d = dict(pairs)
print(d)
```
Explanation: Use `dict()` to convert pairs into a mapping.
</details>

b) Check if a name is in a list or a dict keys and print which structure has it.

Starter code:
```python
names_list = ['Ann','Bob']
names_dict = {'Ann':1}
name = 'Bob'
# TODO: print 'list' or 'dict' or 'none'
pass
```
<details><summary>Answer</summary>

```python
names_list = ['Ann','Bob']
names_dict = {'Ann':1}
name = 'Bob'
if name in names_dict:
    print('dict')
elif name in names_list:
    print('list')
else:
    print('none')
```
Explanation: `in` works for both but checks keys for dict.
</details>

---

## Hard

Write a function that counts words from a list into a dict (word->count) and returns the dict.

Starter code:
```python
def count_words(words):
    # TODO: return dict of counts
    pass
print(count_words(['a','b','a']))
```
<details><summary>Answer</summary>

```python
def count_words(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts
print(count_words(['a','b','a']))
```
Explanation: Use dict.get to count safely.
</details>
