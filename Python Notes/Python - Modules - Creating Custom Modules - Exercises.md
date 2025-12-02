---
tags: [python, exercises, modules, custom]
difficulty: Beginner
---

# Python - Modules - Creating Custom Modules — Exercises

See concept: [[Python - Modules - Creating Custom Modules]]
GitHub link: [Python - Modules - Creating Custom Modules](./Python%20-%20Modules%20-%20Creating%20Custom%20Modules.md)

## Quick syntax fixes

1) Broken: module not found because file missing
```python
import mytool
```
<details><summary>Answer</summary>

Place `mytool.py` in the same folder or add its folder to `PYTHONPATH`.

Explanation: Python finds modules on the import path.
</details>

2) Broken: naming a script same as module
```python
# file named random.py
import random
```
<details><summary>Answer</summary>

Rename your script to avoid shadowing the standard library module.

Explanation: name conflicts hide standard modules.
</details>

3) Broken: forgetting to save file before import
```python
# edit mymod.py but not saved
import mymod
```
<details><summary>Answer</summary>

Save the module file before importing in another script.

Explanation: Python loads files from disk at import time.
</details>

---

## Easy

a) Create `mymodule.py` with `def greet(name):` returning a greeting. Import and call it.

Starter code (mymodule.py):
```python
def greet(name):
    return 'Hi ' + name
```
Starter use:
```python
# TODO: import greet and print greet('Sam')
pass
```
<details><summary>Answer</summary>

```python
from mymodule import greet
print(greet('Sam'))
```
Explanation: simple custom module usage.
</details>

b) Show `if __name__ == '__main__'` guard in a module with a simple `main()`.

Starter code:
```python
def main():
    print('run')

# TODO: add guard
pass
```
<details><summary>Answer</summary>

```python
def main():
    print('run')

if __name__ == '__main__':
    main()
```
Explanation: allows module to be run or imported.
</details>

---

## Medium

a) Make a package folder `tools` with `__init__.py` and a module `tools/utils.py` with `def add(a,b)`. Show import from package root.

Starter prompt:
```text
# file layout and import example
```
<details><summary>Answer</summary>

Layout:
```
tools/
  __init__.py
  utils.py  # defines add
```
Import:
```python
from tools.utils import add
```
Explanation: packages group related modules.
</details>

b) Explain why `__init__` can be used to expose a simple API (one sentence).

Starter prompt:
```text
# one sentence
```
<details><summary>Answer</summary>

`__init__` can import selected names so `from pkg import name` is simpler.

Explanation: it creates a clean package-level API.
</details>

---

## Hard

Write a small module `mathhelp.py` with `def mul(a,b)` and a script that imports it and prints `mul(2,4)`.

Starter code (mathhelp.py):
```python
def mul(a,b):
    # TODO
    pass
```
Starter use:
```python
from mathhelp import mul
print(mul(2,4))
```
<details><summary>Answer</summary>

mathhelp.py:
```python
def mul(a,b):
    return a * b
```
use script:
```python
from mathhelp import mul
print(mul(2,4))
```
Explanation: demonstrates creating and using a custom module.
</details>
