---
tags: [python, exercises, math]
difficulty: Beginner
---

# Python - Math - Absolute Values & Roots — Exercises

See concept: [[Python - Math - Absolute Values & Roots]]
GitHub link: [Python - Math - Absolute Values & Roots](./Python%20-%20Math%20-%20Absolute%20Values%20%26%20Roots.md)

## Quick syntax fixes

1) Broken: using sqrt without import
```python
print(sqrt(4))
```
<details><summary>Answer</summary>

```python
import math
print(math.sqrt(4))
```
Explanation: import math to use sqrt.
</details>

2) Broken: negative inside sqrt
```python
import math
print(math.sqrt(-1))
```
<details><summary>Answer</summary>

```python
import math
print(abs(-1))
```
Explanation: sqrt of negative is invalid; use abs for absolute value.
</details>

3) Broken: using pow for square root incorrectly
```python
print(pow(4, 1/2))
```
<details><summary>Answer</summary>

```python
print(4 ** 0.5)
```
Explanation: power operator can compute roots; use ** 0.5.
</details>

---

## Easy

a) Print absolute value of -5.

Starter code:
```python
# TODO: print abs of -5
pass
```
<details><summary>Answer</summary>

```python
print(abs(-5))
```
Explanation: `abs()` returns absolute value.
</details>

b) Compute square root of 9 using power operator.

Starter code:
```python
# TODO: sqrt of 9
pass
```
<details><summary>Answer</summary>

```python
print(9 ** 0.5)
```
Explanation: exponent 0.5 gives square root.
</details>

---

## Medium

a) Read a number and print its absolute value.

Starter code:
```python
# TODO: read and print abs
pass
```
<details><summary>Answer</summary>

```python
n = int(input())
print(abs(n))
```
Explanation: convert input then call abs.
</details>

b) Use math.sqrt to compute root of positive float input.

Starter code:
```python
import math
# TODO: read float and print sqrt
pass
```
<details><summary>Answer</summary>

```python
import math
n = float(input())
print(math.sqrt(n))
```
Explanation: convert to float before sqrt.
</details>

---

## Hard

Write a function that returns the Euclidean distance between two 2D points.

Starter code:
```python
import math
def dist(a, b):
    # TODO: compute sqrt((x2-x1)**2 + (y2-y1)**2)
    pass

print(dist((0,0),(3,4)))
```
<details><summary>Answer</summary>

```python
import math
def dist(a, b):
    return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)

print(dist((0,0),(3,4)))
```
Explanation: use square difference sum and sqrt.
</details>
