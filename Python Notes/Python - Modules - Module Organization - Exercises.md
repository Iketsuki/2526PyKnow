---
tags: [python, exercises, modules, organization]
difficulty: Beginner
---

# Python - Modules - Module Organization — Exercises

See concept: [[Python - Modules - Module Organization]]
GitHub link: [Python - Modules - Module Organization](./Python%20-%20Modules%20-%20Module%20Organization.md)

## Quick syntax fixes

1) Broken: importing wrong path
```python
from package.module import func
```
<details><summary>Answer</summary>

Ensure `package` is on `PYTHONPATH` or the working folder; use relative imports inside packages.

Explanation: import paths must match package layout.

2) Broken: missing `__init__.py` (older guides)
```text
my_pkg/
  mod.py
```
<details><summary>Answer</summary>

Add `__init__.py` to make the folder a package on some systems.

Explanation: protects compatibility with older Python versions.
</details>

3) Broken: circular import example
```python
# a.py
from b import hello

def hi():
    print('hi')
```
<details><summary>Answer</summary>

Delay import: move `from b import hello` inside a function to avoid circular import at module load time.

Explanation: local imports reduce load-time cycles.
</details>

---

## Summary of Changes
The following files were successfully edited:
c:\Users\t350\gh\2526PyKnow\Python Notes\Python - Modules - Module Organization - Exercises.md
## Easy

a) Describe in one short line what a module is.

Starter prompt:
```text
# Type one short sentence
```
<details><summary>Answer</summary>

A module is a file with Python code that you can import into other code.

Explanation: keeps code organized and reusable.
</details>

b) Show a simple `from mymod import greet` and call it (assume `mymod.py` has `greet`).

Starter code:
```python
# TODO: import and call greet
pass
```
<details><summary>Answer</summary>

```python
from mymod import greet
greet()
```
Explanation: `from module import name` brings function directly.
</details>

---

## Medium

a) Create a small package structure (describe files) and show how to import `pkg.a.func`.

Starter prompt:
```text
# One-line file layout and import example
```
<details><summary>Answer</summary>

Layout:
```
pkg/
  __init__.py
  a.py  # defines def func(): ...
```
Import:
```python
from pkg.a import func
```
Explanation: package folders group modules.
</details>

b) Why put code into small modules (short answer)?

Starter prompt:
```text
# One sentence
```
<details><summary>Answer</summary>

Small modules keep code focused and easier to test and reuse.

Explanation: single-purpose files are simpler to manage.
</details>

---

## Hard

Write a tiny module `greet.py` with `def hello(name):` and show a small script that imports and uses it.

Starter code (greet.py):
```python
def hello(name):
    # TODO: return greeting string
    pass
```
Starter code (use):
```python
from greet import hello
print(hello('Ann'))
```
<details><summary>Answer</summary>

greet.py:
```python
def hello(name):
    return 'Hello ' + name
```
use script:
```python
from greet import hello
print(hello('Ann'))
```
Explanation: modules expose functions to other scripts.
</details>
