---
tags: [python, exercises, math, geometry]
difficulty: Beginner
---

# Python - Math - Geometry & Shapes — Exercises

See concept: [[Python - Math - Geometry & Shapes]]
GitHub link: [Python - Math - Geometry & Shapes](./Python%20-%20Math%20-%20Geometry%20%26%20Shapes.md)

## Quick syntax fixes

1) Broken: area of circle missing pi
```python
r = 2
print(r * r)
```
<details><summary>Answer</summary>

```python
import math
r = 2
print(math.pi * r * r)
```
Explanation: area = pi * r^2.
</details>

2) Broken: using degrees in math.sin directly
```python
import math
print(math.sin(90))
```
<details><summary>Answer</summary>

```python
import math
print(math.sin(math.radians(90)))
```
Explanation: math.sin expects radians.
</details>

3) Broken: wrong formula for rectangle perimeter
```python
w = 2
h = 3
print(w * h)
```
<details><summary>Answer</summary>

```python
w = 2
h = 3
print(2 * (w + h))
```
Explanation: perimeter = 2*(w+h).
</details>

---

## Easy

a) Compute area of rectangle given width and height from input.

Starter code:
```python
# TODO: read w and h and print area
pass
```
<details><summary>Answer</summary>

```python
w = int(input())
h = int(input())
print(w * h)
```
Explanation: multiply width and height.
</details>

b) Print perimeter of square when side length is given.

Starter code:
```python
# TODO: read side and print perimeter
pass
```
<details><summary>Answer</summary>

```python
s = int(input())
print(4 * s)
```
Explanation: perimeter of square is 4*side.
</details>

---

## Medium

a) Read circle radius and print area (use math.pi).

Starter code:
```python
import math
# TODO: read r and print area
pass
```
<details><summary>Answer</summary>

```python
import math
r = float(input())
print(math.pi * r * r)
```
Explanation: area uses pi and r squared.
</details>

b) Given triangle base and height, print area (0.5*base*height).

Starter code:
```python
# TODO: triangle area
pass
```
<details><summary>Answer</summary>

```python
b = float(input())
h = float(input())
print(0.5 * b * h)
```
Explanation: triangle area formula uses half base*height.
</details>

---

## Hard

Write a function that returns the distance between two 2D points (reuse prior math pattern).

Starter code:
```python
import math
def distance(p1, p2):
    # TODO: compute Euclidean distance
    pass

print(distance((0,0),(1,1)))
```
<details><summary>Answer</summary>

```python
import math
def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

print(distance((0,0),(1,1)))
```
Explanation: use Pythagorean theorem.
</details>
