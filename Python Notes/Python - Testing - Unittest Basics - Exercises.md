---
tags: [python, exercises, testing, unittest]
difficulty: Beginner
---

# Python - Testing - Unittest Basics — Exercises

See concept: [[Python - Testing - Unittest Basics]]
GitHub link: [Python - Testing - Unittest Basics](./Python%20-%20Testing%20-%20Unittest%20Basics.md)

## Quick syntax fixes

1) Broken: forgetting to import `unittest`
```python
# Broken
class MyTest(unittest.TestCase):
    pass
```
<details><summary>Answer</summary>

```python
# Fixed
import unittest

class MyTest(unittest.TestCase):
    pass
```
Explanation: Import unittest before using it.
</details>

2) Broken: test method not starting with `test_`
```python
# Broken
def check_sum(self):
    self.assertEqual(1+1, 2)
```
<details><summary>Answer</summary>

```python
# Fixed
def test_check_sum(self):
    self.assertEqual(1+1, 2)
```
Explanation: Unittest discovers methods starting with `test_`.
</details>

3) Broken: using assert instead of self.assertEqual in unittest
```python
# Broken
def test_add(self):
    assert add(1,2) == 3
```
<details><summary>Answer</summary>

```python
# Fixed
def test_add(self):
    self.assertEqual(add(1,2), 3)
```
Explanation: Use unittest assertion methods inside TestCase.
</details>

---

## Easy

a) Write a `unittest.TestCase` with one test that checks `add_one(2)` equals 3.

Starter code:
```python
import unittest

def add_one(n):
    return n + 1

class TestMath(unittest.TestCase):
    # TODO: add test method
    pass

if __name__ == '__main__':
    unittest.main()
```
<details><summary>Answer</summary>

```python
import unittest

def add_one(n):
    return n + 1

class TestMath(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(add_one(2), 3)

if __name__ == '__main__':
    unittest.main()
```
Explanation: Use a TestCase and assertEqual.
</details>

b) Run a simple test that checks `square(3) == 9` using unittest.

Starter code:
```python
import unittest

def square(n):
    return n * n

class TestSquare(unittest.TestCase):
    # TODO: add test
    pass

if __name__ == '__main__':
    unittest.main()
```
<details><summary>Answer</summary>

```python
import unittest

def square(n):
    return n * n

class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(3), 9)

if __name__ == '__main__':
    unittest.main()
```
Explanation: Write test methods inside TestCase class.
</details>

---

## Medium

a) Use `setUp` to create shared data for tests.

Starter code:
```python
import unittest

class T(unittest.TestCase):
    def setUp(self):
        # TODO: create self.data = [1,2,3]
        pass
    def test_len(self):
        self.assertEqual(len(self.data), 3)

if __name__ == '__main__':
    unittest.main()
```
<details><summary>Answer</summary>

```python
import unittest

class T(unittest.TestCase):
    def setUp(self):
        self.data = [1,2,3]
    def test_len(self):
        self.assertEqual(len(self.data), 3)

if __name__ == '__main__':
    unittest.main()
```
Explanation: `setUp` runs before each test to prepare data.
</details>

b) Test that a function raises `ValueError` using `assertRaises`.

Starter code:
```python
import unittest

def bad(x):
    if x < 0:
        raise ValueError
    return x

class T(unittest.TestCase):
    def test_bad(self):
        # TODO: use assertRaises
        pass

if __name__ == '__main__':
    unittest.main()
```
<details><summary>Answer</summary>

```python
import unittest

def bad(x):
    if x < 0:
        raise ValueError
    return x

class T(unittest.TestCase):
    def test_bad(self):
        with self.assertRaises(ValueError):
            bad(-1)

if __name__ == '__main__':
    unittest.main()
```
Explanation: `assertRaises` checks exceptions in unittest.
</details>

---

## Hard

Write tests that run multiple cases using a loop inside a test method.

Starter code:
```python
import unittest

def add_one(n):
    return n + 1

class T(unittest.TestCase):
    def test_many(self):
        # TODO: test add_one for 1..3
        pass

if __name__ == '__main__':
    unittest.main()
```
<details><summary>Answer</summary>

```python
import unittest

def add_one(n):
    return n + 1

class T(unittest.TestCase):
    def test_many(self):
        for i, expect in [(1,2),(2,3),(3,4)]:
            self.assertEqual(add_one(i), expect)

if __name__ == '__main__':
    unittest.main()
```
Explanation: Loop inside test to check multiple cases.
</details>
