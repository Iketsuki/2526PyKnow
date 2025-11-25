---
tags: [python, testing]
moc: [[Python - Testing (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: assert statements and basic unittest structure."
  - "Understand: why tests improve code reliability."
  - "Apply: write simple unit tests for functions."
---

# Python - Testing - Writing simple tests

## Concept
Intro to writing simple tests using `assert` and the `unittest` module. Start small: test pure functions with clear inputs and outputs.

## Example
```python
# function to test
def add(a, b):
    return a + b

# simple test using assert
assert add(2, 3) == 5

# basic unittest example
import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

if __name__ == '__main__':
    unittest.main()
```

## Common Errors with Example Code

1) Testing non-deterministic output without seeding random → flaky tests

WRONG
import random

def rand():
    return random.randint(1, 10)

assert rand() == 5  # flaky

CORRECT
import random
random.seed(0)
assert rand() == rand()  # deterministic when seeded

2) Testing stateful code without isolating state

WRONG
cache = {}
def add_to_cache(k, v):
    cache[k] = v

# Tests may interfere with each other

CORRECT
# Reset or inject dependencies for isolated tests
cache = {}

3) Not asserting expected exceptions

WRONG
try:
    bad_call()
except:
    pass  # test silently passes even if wrong exception

CORRECT
import pytest
with pytest.raises(ValueError):
    bad_call()

## Atomic testing notes (quick links)

This file is an overview — learners should read short, focused notes for each tool:

- [[Python - Testing - Unittest Basics]] — structure tests with the standard library
- [[Python - Testing - Pytest Basics]] — write simple, powerful tests with pytest

## Related Concepts
- [[Python - Debugging - Exception Handling]]
- [[Python - Performance - Big O basics]]

## MOC
- Parent: [[Python Fundamentals (MOC)]]
