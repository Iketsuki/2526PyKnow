---
tags: [python, exercises, lists]
difficulty: Beginner
---

# Exercises — Lists: Creation & Initialization

See concept: [[Python - Lists - Creation & Initialization]]

### Quick syntax fixes

1) Use brackets for list:
```python
x = 1, 2, 3
```
<details><summary>Answer</summary>

```python
x = [1, 2, 3]
```
Explanation: Use `[]` to make a list.
</details>

2) Wrong commas:
```python
x = [1 2 3]
```
<details><summary>Answer</summary>

```python
x = [1, 2, 3]
```
Explanation: Separate items with commas.
</details>

3) Empty list creation error:
```python
x = ()
```
<details><summary>Answer</summary>

```python
x = []
```
Explanation: `()` makes a tuple; use `[]` for a list.
</details>

---

## Easy

### a) Create a list of three names and print the second

Input example:
```text
Anna
Ben
Cara
```

Output example:
```text
Ben
```

Starter code:
```python
# Read three names and store in a list
names = [input(), input(), input()]
# TODO: print the second name
```

<details><summary>Answer</summary>

```python
names = [input(), input(), input()]
print(names[1])
```
Explanation: Lists are zero-indexed; index 1 is the second item.
</details>

### b) Make a list of numbers and print length

Input example:
```text
2
4
6
```

Output example:
```text
3
```

Starter code:
```python
nums = [input(), input(), input()]
# TODO: print how many items are in the list
```

<details><summary>Answer</summary>

```python
nums = [input(), input(), input()]
print(len(nums))
```
Explanation: Use `len()` to get list length.
</details>

---

## Medium

### a) Read n names, print first and last

Input example:
```text
3
Amy
Bo
Cal
```

Output example:
```text
Amy
Cal
```

Starter code:
```python
n = int(input())
# TODO: read n names into a list and print first and last on separate lines
```

<details><summary>Answer</summary>

```python
n = int(input())
names = [input() for _ in range(n)]
print(names[0])
print(names[-1])
```
Explanation: Use list comprehension and negative index for last.
</details>

### b) Add an item to a list and print it

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
# read one fruit and add
f = input()
# TODO: add f to fruits and print the list
```

<details><summary>Answer</summary>

```python
fruits = ['apple', 'banana']
f = input()
fruits.append(f)
print(fruits)
```
Explanation: Use `append` to add an item.
</details>

---

## Hard

### Single: Read numbers and print their reversed list

Input example:
```text
4
1
2
3
4
```

Output example:
```text
['4', '3', '2', '1']
```

Starter code:
```python
n = int(input())
# TODO: read n items into a list and print the reversed list (strings are OK)
```

<details><summary>Answer</summary>

```python
n = int(input())
nums = [input() for _ in range(n)]
nums.reverse()
print(nums)
```
Explanation: `reverse()` changes the list order in place.
</details>
