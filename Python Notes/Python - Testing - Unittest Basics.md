---
tags: [python, testing, unittest]
moc: [[Python - Testing (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: unittest.TestCase structure."
  - "Understand: setUp/tearDown and assertion methods."
  - "Apply: write small unittest test cases."
---

# Python - Testing - Unittest Basics

## Concept
The built-in `unittest` framework organizes tests as classes inheriting from `unittest.TestCase`. Use `setUp`/`tearDown` for shared fixtures and assertion helpers like `assertEqual`.

## Example
```python
import unittest

from mymodule import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

if __name__ == '__main__':
    unittest.main()
```

## Common Errors with Example Code
1) Not naming tests correctly — `unittest` discovers methods starting with `test_`

WRONG
class T(unittest.TestCase):
    def check_add(self):
        self.assertEqual(add(2,3), 5)

CORRECT
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

2) Shared state across tests (mutating globals)

WRONG
cache = {}

class TestCache(unittest.TestCase):
    def test_a(self):
        cache['x'] = 1
    def test_b(self):
        self.assertEqual(cache.get('x'), None)  # flaky

CORRECT
class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = {}
    def test_a(self):
        self.cache['x'] = 1

## Related Concepts
- [[Python - Testing - Writing simple tests]]
- [[Python - Testing - Pytest Basics]]

## MOC
- Parent: [[Python - Testing (MOC)]]
