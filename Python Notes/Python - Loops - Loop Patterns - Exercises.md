---
tags: [python, exercises, loops]
difficulty: Beginner
---

# Python - Loops - Loop Patterns — Exercises

See concept: [[Python - Loops - Loop Patterns]]
GitHub link: [Python - Loops - Loop Patterns](./Python%20-%20Loops%20-%20Loop%20Patterns.md)

## Quick syntax fixes

1) Broken: using while with wrong condition
```python
while i < 5:
    print(i)
```
<details><summary>Answer</summary>

```python
i = 0
while i < 5:
    print(i)
    i += 1
```
Explanation: initialize and update loop variable.
</details>

2) Broken: for loop with range wrong step
```python
for i in range(0,10,0):
    print(i)
```
<details><summary>Answer</summary>

```python
for i in range(0,10,1):
    print(i)
```
Explanation: step cannot be zero.
</details>

3) Broken: infinite for loop with generator misuse
```python
for i in []:
    pass
```
<details><summary>Answer</summary>

```python
for i in range(3):
    print(i)
```
Explanation: provide an iterable that yields values.
</details>

---

## Easy

a) Print numbers 0..4 using for loop.

Starter code:
```python
# TODO: for 0..4
pass
```
<details><summary>Answer</summary>

```python
for i in range(5):
    print(i)
```
Explanation: range(5) yields 0..4.
</details>

b) Use while loop to count down from 3.

Starter code:
```python
# TODO: countdown
pass
```
<details><summary>Answer</summary>

```python
i = 3
while i > 0:
    print(i)
    i -= 1
```
Explanation: update loop variable each iteration.
</details>

---

## Medium

a) Use enumerate to print index and value of list `['a','b']`.

Starter code:
```python
# TODO: enumerate
pass
```
<details><summary>Answer</summary>

```python
for i, v in enumerate(['a','b']):
    print(i, v)
```
Explanation: enumerate gives index and value.
</details>

b) Use zip to iterate two lists in parallel.

Starter code:
```python
# TODO: zip [1,2] and ['a','b']
pass
```
<details><summary>Answer</summary>

```python
for n, c in zip([1,2], ['a','b']):
    print(n, c)
```
Explanation: zip pairs elements from two iterables.
</details>

---

## Hard

Write a nested loop that prints multiplication table 1..3.

Starter code:
```python
# TODO: nested loops
pass
```
<details><summary>Answer</summary>

```python
for i in range(1,4):
    for j in range(1,4):
        print(i*j, end=' ')
    print()
```
Explanation: inner loop prints products for each i.
</details>
