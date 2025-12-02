---
tags: [python, exercises, lists]
difficulty: Beginner
---

# Exercises — Lists: Indexing & Access

See concept: [[Python - Lists - Indexing & Access]]

GitHub link: [Python - Lists - Indexing & Access](./Python%20-%20Lists%20-%20Indexing%20%26%20Access.md)

### Quick syntax fixes

1) Using wrong index type:
```python
items = ['a','b']
print(items['0'])
```
<details><summary>Answer</summary>

```python
items = ['a','b']
print(items[0])
```
Explanation: Indices must be integers, not strings.
</details>

2) Off-by-one error shown as empty access:
```python
arr = [1,2,3]
print(arr[3])
```
<details><summary>Answer</summary>

```python
arr = [1,2,3]
print(arr[2])
```
Explanation: Last index is `len(list)-1` (here 2).
</details>

3) Negative index confusion:
```python
s = ['x','y','z']
print(s[-4])
```
<details><summary>Answer</summary>

```python
s = ['x','y','z']
print(s[-1])
```
Explanation: `-1` is last item; -4 is out of range here.
</details>

---

## Easy

### a) Print second item

Input example:
```text
red
blue
green
```

Output example:
```text
blue
```

Starter code:
```python
first_item = input()
second_item = input()
third_item = input()
colors = [first_item, second_item, third_item]  # colors is the list of inputs
# TODO: print the second item from the list
```

<details><summary>Answer</summary>

```python
first_item = input()
second_item = input()
third_item = input()
colors = [first_item, second_item, third_item]
print(colors[1])
```
Explanation: Lists are zero-indexed so index 1 is the second item.
</details>

### b) Print last item

Input example:
```text
one
two
three
```

Output example:
```text
three
```

Starter code:
```python
a = input()
b = input()
c = input()
items = [a, b, c]
# TODO: print the last item using a negative index
```

<details><summary>Answer</summary>

```python
a = input()
b = input()
c = input()
items = [a, b, c]
print(items[-1])
```
Explanation: Use index `-1` to access the last element.
</details>

---

## Medium

### a) Swap first and last items and print list

Input example:
```text
A
B
C
```

Output example:
```text
['C', 'B', 'A']
```

Starter code:
```python
x = input()  # first item
y = input()  # second item
z = input()  # third item
lst = [x, y, z]
# TODO: swap first and last items then print lst
```

<details><summary>Answer</summary>

```python
x = input()
y = input()
z = input()
lst = [x, y, z]
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)
```
Explanation: Use tuple assignment to swap list elements simply.
</details>

### b) Print third item or 'No item' if missing

Input example:
```text
apple
banana
```

Output example:
```text
No item
```

Starter code:
```python
items = [input(), input()]  # may have only two items
# TODO: print third item if exists else print 'No item'
```

<details><summary>Answer</summary>

```python
items = [input(), input()]
if len(items) >= 3:
    print(items[2])
else:
    print('No item')
```
Explanation: Check length before accessing to avoid IndexError.
</details>

---

## Hard

### Single: Replace middle item with 'X' and print

Input example:
```text
1
2
3
4
5
```

Output example:
```text
['1', '2', 'X', '4', '5']
```

Starter code:
```python
n = int(input())  # number of items
items = [input() for _ in range(n)]  # read n items (strings ok)
# TODO: replace the middle item (index n//2) with 'X' then print items
```

<details><summary>Answer</summary>

```python
n = int(input())
items = [input() for _ in range(n)]
mid = n // 2
items[mid] = 'X'
print(items)
```
Explanation: Use integer division to find middle index and assign new value.
</details>
