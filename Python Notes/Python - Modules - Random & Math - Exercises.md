---
tags: [python, exercises, modules, random, math]
difficulty: Beginner
---

# Python - Modules - Random & Math — Exercises

See concept: [[Python - Modules - Random & Math]]
GitHub link: [Python - Modules - Random & Math](./Python%20-%20Modules%20-%20Random%20%26%20Math.md)

## Quick syntax fixes

1) Broken: calling `random()` instead of `random.random()`
```python
import random
print(random())
```
<details><summary>Answer</summary>

```python
import random
print(random.random())
```
Explanation: `random` is module; use `random.random()`.
</details>

2) Broken: mixing `math.floor` and wrong import
```python
from math import *
print(floor(3.7))
```
<details><summary>Answer</summary>

```python
import math
print(math.floor(3.7))
```
Explanation: `math.floor` works either via `math.floor` or direct import.
</details>

3) Broken: using `randint` with float bounds
```python
import random
print(random.randint(1.0, 5.0))
```
<details><summary>Answer</summary>

```python
import random
print(random.randint(1, 5))
```
Explanation: `randint` needs integer arguments.
</details>

---

## Easy

a) Print a random integer between 10 and 20.

Starter code:
```python
import random
# TODO: print random int 10..20
pass
```
<details><summary>Answer</summary>

```python
import random
print(random.randint(10, 20))
```
Explanation: `randint` includes both ends.
</details>

b) Use `math.ceil` to round 3.2 up and print.

Starter code:
```python
import math
# TODO: print ceil of 3.2
pass
```
<details><summary>Answer</summary>

```python
import math
print(math.ceil(3.2))
```
Explanation: `ceil` rounds upward.
</details>

---

## Medium

a) Generate 5 random floats between 0 and 1 and print them on one line separated by spaces.

Starter code:
```python
import random
# TODO: generate list and print
pass
```
<details><summary>Answer</summary>

```python
import random
nums = [random.random() for _ in range(5)]
print(' '.join(str(x) for x in nums))
```
Explanation: list and join convert floats to strings.
</details>

b) Read a number and print its square root rounded to 3 decimals using `math.sqrt`.

Starter code:
```python
import math
n = float(input())
# TODO: print sqrt to 3 decimals
pass
```
<details><summary>Answer</summary>

```python
import math
n = float(input())
print('{:.3f}'.format(math.sqrt(n)))
```
Explanation: format with `:.3f` for three decimals.
</details>

---

## Hard

Write a function `random_scaled(n)` that returns a random number between 0 and `sqrt(n)`.

Starter code:
```python
import random
import math

def random_scaled(n):
    # TODO
    pass

print(random_scaled(25))
```
<details><summary>Answer</summary>

```python
import random
import math

def random_scaled(n):
    return random.random() * math.sqrt(n)

print(random_scaled(25))
```
Explanation: `random.random()` * `sqrt(n)` gives 0..sqrt(n).
</details>
