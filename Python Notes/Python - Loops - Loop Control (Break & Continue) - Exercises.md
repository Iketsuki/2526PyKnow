---
tags: [python, exercises, loops]
difficulty: Beginner
---

# Python - Loops - Loop Control (Break & Continue) — Exercises

See concept: [[Python - Loops - Loop Control (Break & Continue)]]
GitHub link: [Python - Loops - Loop Control (Break & Continue)](./Python%20-%20Loops%20-%20Loop%20Control%20(Break%20%26%20Continue).md)

## Quick syntax fixes

1) Broken: missing break to stop loop
```python
while True:
    print('hi')
```
<details><summary>Answer</summary>

```python
while True:
    print('hi')
    break
```
Explanation: `break` exits the loop.
</details>

2) Broken: continue used outside loop
```python
continue
```
<details><summary>Answer</summary>

```python
for i in range(1):
    continue
```
Explanation: `continue` must be inside a loop to skip to next iteration.
</details>

3) Broken: break in try block without loop
```python
try:
    break
except:
    pass
```
<details><summary>Answer</summary>

```python
for _ in range(1):
    try:
        break
    except:
        pass
```
Explanation: break must appear in loop context; try can be inside loop.
</details>

---

## Easy

a) Loop numbers 1..5 and break when number is 3.

Starter code:
```python
# TODO: break when 3
pass
```
<details><summary>Answer</summary>

```python
for i in range(1,6):
    if i == 3:
        break
    print(i)
```
Explanation: loop stops when condition met.
</details>

b) Use continue to skip printing even numbers.

Starter code:
```python
# TODO: skip even numbers
pass
```
<details><summary>Answer</summary>

```python
for i in range(1,6):
    if i % 2 == 0:
        continue
    print(i)
```
Explanation: continue skips to next iteration.
</details>

---

## Medium

a) Read numbers until 0, skip negative numbers, stop on 999.

Starter code:
```python
# TODO: use loop with break and continue
pass
```
<details><summary>Answer</summary>

```python
while True:
    n = int(input())
    if n == 999:
        break
    if n < 0:
        continue
    if n == 0:
        break
    print(n)
```
Explanation: combine break and continue for control.
</details>

b) Use for/else with break to detect if a value found.

Starter code:
```python
lst = [1,2,3]
# TODO: print 'found' or 'not found'
pass
```
<details><summary>Answer</summary>

```python
lst = [1,2,3]
for x in lst:
    if x == 4:
        print('found')
        break
else:
    print('not found')
```
Explanation: for/else runs else when loop not broken.
</details>

---

## Hard

Write a loop that reads lines and stops when a blank line is entered, ignoring empty lines at start.

Starter code:
```python
# TODO: read until first blank after data
pass
```
<details><summary>Answer</summary>

```python
started = False
while True:
    line = input()
    if line == '' and started:
        break
    if line != '':
        started = True
        print(line)
```
Explanation: track start, then break on subsequent blank.
</details>
