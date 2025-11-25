---
tags: [python, testing, pytest]
moc: [[Python - Testing (MOC)]]
difficulty: Beginner
bloom_level: Apply
learning_objectives:
  - "Remember: simple pytest test functions and fixtures."
  - "Understand: how pytest simplifies testing."
  - "Apply: write pytest tests and use fixtures."
---

# Python - Testing - Pytest Basics

## Concept
`pytest` allows simple test functions without classes and provides rich fixtures and plugins. It's popular for concise tests.

## Example
```python
# test_add.py
from mymodule import add

def test_add():
    assert add(2, 3) == 5
```

## Fixtures
```python
import pytest

@pytest.fixture
def sample_list():
    return [1,2,3]

def test_len(sample_list):
    assert len(sample_list) == 3
```

## Common Errors
1) Not installing pytest or running wrong command

WRONG
# expecting pytest when none installed

CORRECT
# install: pip install pytest
# run: pytest -q

2) Using mutable default fixtures incorrectly

WRONG
@pytest.fixture
def cache=[]:  # bad: shared mutable default
    return cache

CORRECT
@pytest.fixture
def cache():
    return {}

## Related Concepts
- [[Python - Testing - Writing simple tests]]
- [[Python - Testing - Unittest Basics]]

## MOC
- Parent: [[Python - Testing (MOC)]]
