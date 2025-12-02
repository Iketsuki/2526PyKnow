---
tags: [python, exercises, lists]
difficulty: Beginner
---

# Exercises — Lists: Methods & Modification

See concept: [[Python - Lists - Methods & Modification]]

GitHub link: [Python - Lists - Methods & Modification](./Python%20-%20Lists%20-%20Methods%20%26%20Modification.md)

### Quick syntax fixes

1) Using append wrong:
```python
l = [1,2]
l.append(3,4)
```
<details><summary>Answer</summary>

```python
l = [1,2]
l.append(3)
# to add multiple use extend: l.extend([3,4])
```
Explanation: `append` takes one item; `extend` adds multiple.
</details>

2) Using remove on missing item:
```python
l = [1,2]
l.remove(3)
```
<details><summary>Answer</summary>

```python
l = [1,2]
# check before remove
if 3 in l:
    l.remove(3)
```
Explanation: Removing an item not present causes ValueError; check membership first.
</details>

3) Mistaking insert arguments:
```python
l = [1,2]
l.insert(3)
```
<details><summary>Answer</summary>

```python
l = [1,2]
l.insert(1, 3)
```
Explanation: `insert(index, value)` needs both index and value.
</details>

---

## Easy

### a) Append a new value and print list

Input example:
```text
orange
```

Output example:
```text
['apple', 'banana', 'orange']
```

Starter code:
```python
fruits = ['apple', 'banana']
new_fruit = input()  # new_fruit is the value to add
# TODO: append new_fruit to fruits and print the list
```

<details><summary>Answer</summary>

```python
fruits = ['apple', 'banana']
new_fruit = input()
fruits.append(new_fruit)
print(fruits)
```
Explanation: `append` adds a single item to the end of the list.
</details>

### b) Remove an item if present

Input example:
```text
banana
```

Output example:
```text
['apple']
```

Starter code:
```python
items = ['apple', 'banana']
remove_item = input()  # remove_item is the word to remove
# TODO: remove remove_item if in items then print items
```

<details><summary>Answer</summary>

```python
items = ['apple', 'banana']
remove_item = input()
if remove_item in items:
    items.remove(remove_item)
print(items)
```
Explanation: Check membership before calling `remove`.
</details>

---

## Medium

### a) Insert item at index 1

Input example:
```text
kiwi
```

Output example:
```text
['apple', 'kiwi', 'banana']
```

Starter code:
```python
lst = ['apple', 'banana']
value = input()  # value to insert
# TODO: insert value at index 1 and print lst
```

<details><summary>Answer</summary>

```python
lst = ['apple', 'banana']
value = input()
lst.insert(1, value)
print(lst)
```
Explanation: `insert(i, v)` adds value at position i shifting others to the right.
</details>

### b) Clear the list if user says 'clear'

Input example:
```text
clear
```

Output example:
```text
[]
```

Starter code:
```python
lst = ['a','b','c']
cmd = input()  # cmd is the user command
# TODO: if cmd == 'clear' then empty the list and print it
```

<details><summary>Answer</summary>

```python
lst = ['a','b','c']
cmd = input()
if cmd == 'clear':
    lst.clear()
print(lst)
```
Explanation: `clear()` removes all items from the list.
</details>

---

## Hard

### Single: Replace all occurrences of a value with 'X'

Input example:
```text
apple
apple
banana
apple
apple
```

Output example:
```text
['X', 'X', 'banana', 'X', 'X']
```

Starter code:
```python
n = int(input())  # number of items
items = [input() for _ in range(n)]
old = input()  # old value to replace
# TODO: replace every occurrence of old in items with 'X' and print items
```

<details><summary>Answer</summary>

```python
n = int(input())
items = [input() for _ in range(n)]
old = input()
for i in range(len(items)):
    if items[i] == old:
        items[i] = 'X'
print(items)
```
Explanation: Use an index loop to replace items in place.
</details>
