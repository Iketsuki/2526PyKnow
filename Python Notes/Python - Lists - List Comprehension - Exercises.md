---
tags: [python, exercises, lists]
difficulty: Beginner
---

# Exercises — Lists: List Comprehension (Simple)

See concept: [[Python - Lists - List Comprehension]]

GitHub link: [Python - Lists - List Comprehension](./Python%20-%20Lists%20-%20List%20Comprehension.md)

### Quick syntax fixes

1) Missing brackets in comprehension:
```python
squares = x*x for x in range(3)
```
<details><summary>Answer</summary>

```python
squares = [x*x for x in range(3)]
```
Explanation: Comprehensions must be inside `[]` for lists.
</details>

2) Using wrong variable in expression:
```python
nums = [1,2,3]
res = [n*2 for x in nums]
```
<details><summary>Answer</summary>

```python
nums = [1,2,3]
res = [n*2 for n in nums]
```
Explanation: Use the same loop variable in expression and loop.
</details>

3) Forgetting to convert input strings if needed:
```python
n = int(input())
items = [input() for _ in range(n)]
nums = [int(x) for x in items]
```
<details><summary>Answer</summary>

```python
n = int(input())
items = [input() for _ in range(n)]
nums = [int(x) for x in items]
```
Explanation: This example is fine; show correct pattern — convert strings inside comprehension.
</details>

---

## Easy

### a) Make squares with comprehension

Input example:
```text
3
```

Output example:
```text
[0, 1, 4]
```

Starter code:
```python
n = int(input())  # n is the number of items
# TODO: create a list of squares 0..n-1 and print it
```

<details><summary>Answer</summary>

```python
n = int(input())
res = [i*i for i in range(n)]
print(res)
```
Explanation: Simple comprehension used to create a list of squares.
</details>

### b) Double numbers

Input example:
```text
2
3
4
```

Output example:
```text
[4, 6, 8]
```

Starter code:
```python
nums = [int(input()), int(input()), int(input())]
# TODO: use comprehension to make a new list with each value doubled
```

<details><summary>Answer</summary>

```python
nums = [int(input()), int(input()), int(input())]
print([x*2 for x in nums])
```
Explanation: Comprehension is shown here but keep it simple for learners.
</details>

---

## Medium

### a) Filter even numbers

Input example:
```text
1
2
3
4
```

Output example:
```text
[2, 4]
```

Starter code:
```python
nums = [int(input()), int(input()), int(input()), int(input())]
# TODO: use a comprehension to produce only even numbers and print them
```

<details><summary>Answer</summary>

```python
nums = [int(input()), int(input()), int(input()), int(input())]
print([x for x in nums if x % 2 == 0])
```
Explanation: Include the `if` clause to filter; keep examples short and clear.
</details>

### b) Convert words to uppercase

Input example:
```text
one
two
three
```

Output example:
```text
['ONE', 'TWO', 'THREE']
```

Starter code:
```python
w1 = input()
w2 = input()
w3 = input()
words = [w1, w2, w3]
# TODO: make a comprehension that uppercases each word and print result
```

<details><summary>Answer</summary>

```python
w1 = input()
w2 = input()
w3 = input()
words = [w1, w2, w3]
print([w.upper() for w in words])
```
Explanation: Use `.upper()` inside comprehension to transform strings.
</details>

---

## Hard

### Single: Create pairs (value,index) using comprehension

Input example:
```text
5
6
7
```

Output example:
```text
[('5', 0), ('6', 1), ('7', 2)]
```

Starter code:
```python
vals = [input(), input(), input()]
# TODO: create a list of tuples (value, index) using a comprehension and print it
```

<details><summary>Answer</summary>

```python
vals = [input(), input(), input()]
print([(vals[i], i) for i in range(len(vals))])
```
Explanation: Use `range(len(...))` to pair each item with its index; this keeps the comprehension explicit for beginners.
</details>
