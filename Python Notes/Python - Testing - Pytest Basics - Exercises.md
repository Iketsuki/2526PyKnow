---
tags: [python, exercises, testing, pytest]
difficulty: Beginner
---

# Python - Testing - Pytest Basics — Exercises

See concept: [[Python - Testing - Pytest Basics]]
GitHub link: [Python - Testing - Pytest Basics](./Python%20-%20Testing%20-%20Pytest%20Basics.md)

## Quick syntax fixes

1) Broken: test function missing `assert`
```python
# Broken
def test_add():
    add(1,2) == 3
```
<details><summary>Answer</summary>

```python
# Fixed
def test_add():
    assert add(1,2) == 3
```
Explanation: Use `assert` in pytest tests.
</details>

2) Broken: test file not named properly
```text
# Broken
file name: testadd.py
```
<details><summary>Answer</summary>

```text
# Fixed
file name: test_add.py
```
Explanation: Pytest discovers files named `test_*.py` or `*_test.py`.
</details>

3) Broken: using print instead of assert
```python
# Broken
def test_true():
    print(True)
```
<details><summary>Answer</summary>

```python
# Fixed
def test_true():
    assert True
```
Explanation: Tests must `assert` conditions, not print.
</details>

---

## Easy

a) Write a simple test that checks `add_one(2) == 3` using `assert`.

Starter code:
```python
def add_one(n):
    return n + 1
# TODO: write test function using assert
```
<details><summary>Answer</summary>

```python
def add_one(n):
    return n + 1

def test_add_one():
    assert add_one(2) == 3
```
Explanation: Write a test function starting with `test_` and use `assert`.
</details>

b) Test that `square(3) == 9`.

Starter code:
```python
def square(n):
    return n * n
# TODO: add test
```
<details><summary>Answer</summary>

```python
def square(n):
    return n * n

def test_square():
    assert square(3) == 9
```
Explanation: Simple function test using pytest style.
</details>

---

## Medium

a) Use a fixture to provide a sample list to tests.

Starter code:
```python
import pytest

@pytest.fixture
def sample():
    # TODO: return [1,2,3]
    pass

def test_len(sample):
    assert len(sample) == 3
```
<details><summary>Answer</summary>

```python
import pytest

@pytest.fixture
def sample():
    return [1, 2, 3]

def test_len(sample):
    assert len(sample) == 3
```
Explanation: Fixtures return data for tests to use.
</details>

b) Parametrize a test for `add_one` with inputs 1,2,3.

Starter code:
```python
import pytest

def add_one(n):
    return n + 1

@pytest.mark.parametrize('n,expect', [(1,2),(2,3),(3,4)])
def test_add(n, expect):
    # TODO: assert add_one(n) == expect
    pass
```
<details><summary>Answer</summary>

```python
import pytest

def add_one(n):
    return n + 1

@pytest.mark.parametrize('n,expect', [(1,2),(2,3),(3,4)])
def test_add(n, expect):
    assert add_one(n) == expect
```
Explanation: Use `parametrize` to run multiple cases in one test.
</details>

---

## Hard

Write a test that checks a function raises `ValueError` for bad input using `pytest.raises`.

Starter code:
```python
def bad(x):
    if x < 0:
        raise ValueError('neg')
    return x

# TODO: write test using pytest.raises
```
<details><summary>Answer</summary>

```python
import pytest

def bad(x):
    if x < 0:
        raise ValueError('neg')
    return x

def test_bad():
    with pytest.raises(ValueError):
        bad(-1)
```
Explanation: `pytest.raises` checks that code raises the expected exception.
</details>
