---
tags: [python, exercises, loops, for, while]
difficulty: Beginner
---

# Python - Loops - For vs While — Exercises

See concept: [[Python - Loops - For vs While]]
GitHub link: [Python - Loops - For vs While](./Python%20-%20Loops%20-%20For%20vs%20While.md)

## Quick syntax fixes

1) Broken: using `while` without updating variable
```python
i = 0
while i < 3:
    print(i)
```
<details><summary>Answer</summary>

```python
i = 0
while i < 3:
    print(i)
    i += 1
```
Explanation: increment loop variable to avoid infinite loop.
</details>

2) Broken: using `for` with wrong range end
```python
for i in range(3):
    print(i)
```
<details><summary>Answer</summary>

This prints 0,1,2. Use `range(1,4)` to print 1..3.

Explanation: `range` end is exclusive.
</details>

3) Broken: using `break` outside loop
```python
break
```
<details><summary>Answer</summary>

`break` must be inside a loop; it stops the loop immediately.

Explanation: place `break` in `for` or `while` body.
</details>

---

## Easy

a) Print numbers 1 to 5 using `for` loop.

Starter code:
```python
# TODO: for i in range(1,6): print i
pass
```
<details><summary>Answer</summary>

```python
for i in range(1, 6):
    print(i)
```
Explanation: `range(1,6)` gives 1..5.
</details>

b) Use `while` to print numbers 1 to 5.

Starter code:
```python
 i = 1
# TODO: while i <=5: print and increment
pass
```
<details><summary>Answer</summary>

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```
Explanation: `while` repeats using a condition.
</details>

---

## Medium

a) Use `for` to sum numbers from 1 to n and print result.

Starter code:
```python
n = int(input())
# TODO: sum 1..n and print
pass
```
<details><summary>Answer</summary>

```python
n = int(input())
total = 0
for i in range(1, n+1):
    total += i
print(total)
```
Explanation: use loop and accumulate.
</details>

b) Use `while` to read numbers until user enters 0, summing them.

Starter code:
```python
# TODO: read ints until 0 and sum
pass
```
<details><summary>Answer</summary>

```python
total = 0
while True:
    n = int(input())
    if n == 0:
        break
    total += n
print(total)
```
Explanation: `break` exits the loop on condition.
</details>

---

## Hard

When is `for` generally better than `while`? Write a one-line answer.

Starter prompt:
```text
# one line
```
<details><summary>Answer</summary>

`for` is better when you have a known number of iterations or iterate over a collection.

Explanation: `for` expresses iteration intent clearly.
</details>
