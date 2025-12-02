---
tags: [python, exercises, modules, random, math]
difficulty: Beginner
---

# Python - Modules - Common Modules (random-math-etc) — Exercises

See concept: [[Python - Modules - Common Modules (random-math-etc)]]
GitHub link: [Python - Modules - Common Modules (random-math-etc)](./Python%20-%20Modules%20-%20Common%20Modules%20%28random-math-etc%29.md)

## Quick syntax fixes

1) Broken: forgot to import `random`
```python
print(random.randint(1, 3))
```
<details><summary>Answer</summary>

```python
import random
print(random.randint(1, 3))
```
Explanation: import the module before use.
</details>

2) Broken: using `math.sqrt` without import
```python
print(math.sqrt(9))
```
<details><summary>Answer</summary>

```python
import math
print(math.sqrt(9))
```
Explanation: `math` must be imported.
</details>

3) Broken: wrong module name
```python
import rand
print(rand.randint(1,2))
```
<details><summary>Answer</summary>

```python
import random
print(random.randint(1,2))
```
Explanation: use the correct module name `random`.
</details>

---

## Easy

a) Use `random.choice` to pick a fruit from a list and print it.

Starter code:
```python
import random
fruits = ['apple', 'banana', 'cherry']
# TODO: pick one fruit and print
pass
```
<details><summary>Answer</summary>

```python
import random
fruits = ['apple', 'banana', 'cherry']
print(random.choice(fruits))
```
Explanation: `random.choice` picks one item.
</details>

b) Use `math.pow` to compute 2^3 and print the result.

Starter code:
```python
import math
# TODO: compute 2 to the 3rd power
pass
```
<details><summary>Answer</summary>

```python
import math
print(math.pow(2, 3))
```
Explanation: `math.pow(x, y)` returns x ** y as float.
</details>

---

## Medium

a) Use `random.randint` to simulate a dice roll (1–6). Print "You rolled: <n>".

Starter code:
```python
import random
# TODO: roll dice and print
pass
```
<details><summary>Answer</summary>

```python
import random
n = random.randint(1, 6)
print('You rolled:', n)
```
Explanation: `randint(1,6)` includes both ends.
</details>

b) Use `math.sqrt` to print the square root of a number from input.

Starter code:
```python
import math
n = float(input())
# TODO: print sqrt
pass
```
<details><summary>Answer</summary>

```python
import math
n = float(input())
print(math.sqrt(n))
```
Explanation: convert input to number before using `math.sqrt`.
</details>

---

## Hard

Write a function that returns a random float between 0 and 1 multiplied by the square root of an integer input.

Starter code:
```python
import random
import math

def random_times_sqrt(n):
    # TODO: return random * sqrt(n)
    pass

print(random_times_sqrt(16))
```
<details><summary>Answer</summary>

```python
import random
import math

def random_times_sqrt(n):
    return random.random() * math.sqrt(n)

print(random_times_sqrt(16))
```
Explanation: `random.random()` gives 0≤x<1; multiply by `math.sqrt`.
</details>
