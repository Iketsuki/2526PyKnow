---
tags: [python, exercises, modules]
difficulty: Beginner
---

# Exercises — Modules: Importing Basics

See concept: [[Python - Modules - Importing Basics]]

GitHub link: [Python - Modules - Importing Basics](./Python%20-%20Modules%20-%20Importing%20Basics.md)

### Quick syntax fixes

1) Wrong `from` syntax:
```python
from math import
sqrt
```
<details><summary>Answer</summary>

```python
from math import sqrt
```
Explanation: Keep import on one line for a single name.
</details>

2) Using alias incorrectly:
```python
import math as
m
```
<details><summary>Answer</summary>

```python
import math as m
```
Explanation: Alias must be on same line as import.
</details>

3) Importing nonexistent name:
```python
from random import choicee
```
<details><summary>Answer</summary>

```python
# Correct name is 'choice'
from random import choice
```
Explanation: Use the correct function name provided by the module.
</details>

---

## Easy

### a) Import sqrt directly and use it

Input example:
```text
16
```

Output example:
```text
4.0
```

Starter code:
```python
n = int(input())  # n is the number
# TODO: import sqrt from math and print sqrt(n)
```

<details><summary>Answer</summary>

```python
from math import sqrt
n = int(input())
print(sqrt(n))
```
Explanation: `from math import sqrt` allows calling `sqrt` directly.
</details>

### b) Import choice as alias

Starter code:
```python
# TODO: import random.choice as rc and use rc to pick from a list
```

<details><summary>Answer</summary>

```python
from random import choice as rc
print(rc(['red', 'blue']))
```
Explanation: Aliasing shortens long module.function paths for convenience.
</details>

---

## Medium

### a) Import multiple names

Starter code:
```python
# TODO: from math import pi, sqrt and print pi and sqrt(4)
```

<details><summary>Answer</summary>

```python
from math import pi, sqrt
print(pi)
print(sqrt(4))
```
Explanation: Import several names separated by commas.
</details>

### b) Use full module path

Input example:
```text
2
```

Output example:
```text
4
```

Starter code:
```python
n = int(input())
# TODO: import math and print math.pow(n,2)
```

<details><summary>Answer</summary>

```python
import math
n = int(input())
print(math.pow(n, 2))
```
Explanation: Use the module name to call functions inside it.
</details>

---

## Hard

### Single: Explain relative import concept (conceptual)

Instruction:
- Very short explanation for learners: a relative import uses a dot like `from . import helper` when files are inside a package folder. This is advanced; only explain simply.

<details><summary>Answer</summary>

```text
Relative imports let files in the same package import each other using a leading dot, e.g., `from .helper import greet`. For beginners, understand modules as files you can import.
```
Explanation: Keep explanation short and conceptual.
</details>
