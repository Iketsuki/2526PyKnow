---
tags: [python, exercises, lists, loops]
difficulty: Beginner
---

# Exercises — Lists: Iteration & Looping

See concept: [[Python - Lists - Iteration & Looping]]

### Quick syntax fixes

1) Wrong for syntax:
```python
for i in range(5)
    print(i)
```
<details><summary>Answer</summary>

```python
for i in range(5):
    print(i)
```
Explanation: Add colon after `for` and indent the body.
</details>

2) Using range with a list:
```python
for x in range([1,2,3]):
    print(x)
```
<details><summary>Answer</summary>

```python
for x in [1,2,3]:
    print(x)
```
Explanation: Iterate directly over the list or use `range(len(list))`.
</details>

3) Missing colon in if inside loop:
```python
for x in [1,2]:
    if x > 1
        print(x)
```
<details><summary>Answer</summary>

```python
for x in [1,2]:
    if x > 1:
        print(x)
```
Explanation: Add colon after `if`.
</details>

---

## Easy

### a) Print each item of a list on its own line

Input example:
```text
red
blue
green
```

Output example:
```text
red
blue
green
```

Starter code:
```python
items = [input(), input(), input()]
# TODO: print each item on its own line using a loop
```

<details><summary>Answer</summary>

```python
items = [input(), input(), input()]
for it in items:
    print(it)
```
Explanation: Use `for` to iterate over elements.
</details>

### b) Sum numbers in a list

Input example:
```text
1
2
3
```

Output example:
```text
6
```

Starter code:
```python
nums = [int(input()), int(input()), int(input())]
# TODO: compute and print sum
```

<details><summary>Answer</summary>

```python
nums = [int(input()), int(input()), int(input())]
total = 0
for n in nums:
    total += n
print(total)
```
Explanation: Use a loop to add each number to `total`.
</details>

---

## Medium

### a) Count how many items equal 'yes'

Input example:
```text
yes
no
yes
```

Output example:
```text
2
```

Starter code:
```python
items = [input(), input(), input()]
# TODO: count how many items are 'yes'
```

<details><summary>Answer</summary>

```python
items = [input(), input(), input()]
count = 0
for it in items:
    if it == 'yes':
        count += 1
print(count)
```
Explanation: Increment count when condition is true.
</details>

### b) Print items with their index

Input example:
```text
apple
banana
```

Output example:
```text
0: apple
1: banana
```

Starter code:
```python
items = [input(), input()]
# TODO: use a loop to print index and item
```

<details><summary>Answer</summary>

```python
items = [input(), input()]
for i in range(len(items)):
    print(f"{i}: {items[i]}")
```
Explanation: Use `range(len(...))` to get indices.
</details>

---

## Hard

### Single: Remove duplicates while keeping order

Input example:
```text
apple
banana
apple
banana
```

Output example:
```text
['apple', 'banana']
```

Starter code:
```python
items = [input(), input(), input(), input()]
# TODO: make a new list with duplicates removed, keep first order
```

<details><summary>Answer</summary>

```python
items = [input(), input(), input(), input()]
seen = []
for it in items:
    if it not in seen:
        seen.append(it)
print(seen)
```
Explanation: Use a `seen` list and append only new items.
</details>
