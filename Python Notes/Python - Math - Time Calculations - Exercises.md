---
tags: [python, exercises, math, time]
difficulty: Beginner
---

# Python - Math - Time Calculations — Exercises

See concept: [[Python - Math - Time Calculations]]
GitHub link: [Python - Math - Time Calculations](./Python%20-%20Math%20-%20Time%20Calculations.md)

## Quick syntax fixes

1) Broken: adding hours without converting to minutes
```python
hours = 1
print(hours + 30)
```
<details><summary>Answer</summary>

```python
hours = 1
print(hours * 60 + 30)
```
Explanation: convert hours to minutes before adding.
</details>

2) Broken: wrong modulus for seconds
```python
sec = 90
print(sec % 60)
```
<details><summary>Answer</summary>

```python
sec = 90
print(sec // 60, sec % 60)
```
Explanation: use // for minutes and % for leftover seconds.
</details>

3) Broken: formatting time with simple print
```python
h = 2
m = 3
print(h + ':' + m)
```
<details><summary>Answer</summary>

```python
h = 2
m = 3
print(f"{h}:{m:02d}")
```
Explanation: format minutes with leading zeros.
</details>

---

## Easy

a) Convert hours to minutes given input hours.

Starter code:
```python
# TODO: read hours and print minutes
pass
```
<details><summary>Answer</summary>

```python
h = int(input())
print(h * 60)
```
Explanation: multiply hours by 60.
</details>

b) Given total minutes, print hours and leftover minutes.

Starter code:
```python
# TODO: split minutes into hours and minutes
pass
```
<details><summary>Answer</summary>

```python
mins = int(input())
print(mins // 60, mins % 60)
```
Explanation: integer division and modulus split time.
</details>

---

## Medium

a) Read hh mm and add 30 minutes, print new time in hh mm.

Starter code:
```python
# TODO: add 30 minutes
pass
```
<details><summary>Answer</summary>

```python
h = int(input())
m = int(input())
total = h * 60 + m + 30
print(total // 60, total % 60)
```
Explanation: convert to minutes, add, then split.
</details>

b) Convert seconds input to hh:mm:ss format string.

Starter code:
```python
# TODO: format seconds
pass
```
<details><summary>Answer</summary>

```python
sec = int(input())
h = sec // 3600
sec = sec % 3600
m = sec // 60
s = sec % 60
print(f"{h}:{m:02d}:{s:02d}")
```
Explanation: compute hours, minutes, seconds, format with zeros.
</details>

---

## Hard

Write a function that adds two times given as (h,m) tuples and returns normalized (h,m).

Starter code:
```python
def add_times(t1, t2):
    # TODO: add and normalize
    pass

print(add_times((1,50),(0,30)))
```
<details><summary>Answer</summary>

```python
def add_times(t1, t2):
    total = (t1[0]*60 + t1[1]) + (t2[0]*60 + t2[1])
    return (total // 60, total % 60)

print(add_times((1,50),(0,30)))
```
Explanation: convert to minutes and normalize back to hours and minutes.
</details>
