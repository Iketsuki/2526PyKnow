---
tags: [python, exercises, modules]
difficulty: Beginner
---

# Exercises — Modules: What are Modules

See concept: [[Python - Modules - What are Modules]]

GitHub link: [Python - Modules - What are Modules](./Python%20-%20Modules%20-%20What%20are%20Modules.md)

### Quick syntax fixes

1) Using `import` in wrong place:
```python
print(math.pi)
import math
```
<details><summary>Answer</summary>

```python
import math
print(math.pi)
```
Explanation: Import before using the module.
</details>

2) Wrong import name:
```python
import Maths
```
<details><summary>Answer</summary>

```python
import math
```
Explanation: Module names are lowercase; use `math`.
</details>

3) Calling module like a function:
```python
import math
math()
```
<details><summary>Answer</summary>

```python
import math
print(math.pi)
```
Explanation: Modules are namespaces, not callable functions.
</details>

---

## Easy

### a) Import math and print pi

Output example:
```text
3.141592653589793
```

Starter code:
```python
# TODO: import math and print math.pi
```

<details><summary>Answer</summary>

```python
import math
print(math.pi)
```
Explanation: `math` module provides mathematical constants.
</details>

### b) Use random to pick between two words

Input example:
```text
(no input)
```

Output example:
```text
apple
```

Starter code:
```python
# TODO: import random and print a random choice between 'apple' and 'banana'
```

<details><summary>Answer</summary>

```python
import random
print(random.choice(['apple', 'banana']))
```
Explanation: `random.choice` picks an item from a list.
</details>

---

## Medium

### a) Use math.sqrt on input number

Input example:
```text
9
```

Output example:
```text
3.0
```

Starter code:
```python
n = int(input())  # n is integer
# TODO: import math and print math.sqrt(n)
```

<details><summary>Answer</summary>

```python
import math
n = int(input())
print(math.sqrt(n))
```
Explanation: `sqrt` returns a float square root.
</details>

### b) Use random.randint to pick a number

Input example:
```text
1
3
```

Output example:
```text
2
```

Starter code:
```python
a = int(input())  # lower bound
b = int(input())  # upper bound
# TODO: import random and print random.randint(a,b)
```

<details><summary>Answer</summary>

```python
import random
a = int(input())
b = int(input())
print(random.randint(a, b))
```
Explanation: `randint` includes both endpoints.
</details>

---

## Hard

### Single: Create a small helper file (explain only)

Instruction:
- This is conceptual for beginners: explain that a module can be a file `helper.py` with a function `greet(name)` and then imported by another file.

Starter code (example only):
```python
# helper.py
# def greet(name):
#     print('Hi', name)

# main.py
# import helper
# helper.greet('Ana')
```

<details><summary>Answer</summary>

```text
Create a file named helper.py with a function greet(name) that prints a greeting. Then in another file import helper and call helper.greet('Name').
```
Explanation: Show simple pattern of making code reusable in another file.
</details>
