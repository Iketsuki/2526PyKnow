---
tags: [python, exercises, testing]
difficulty: Beginner
---

# Exercises — Testing: Writing simple tests

See concept: [[Python - Testing - Writing simple tests]]

GitHub link: [Python - Testing - Writing simple tests](./Python%20-%20Testing%20-%20Writing%20simple%20tests.md)

### Quick syntax fixes

1) Wrong `assert` usage:
```python
def add(a, b):
    return a + b
assert add(2,3) = 5
```
<details><summary>Answer</summary>

```python
def add(a, b):
    return a + b
assert add(2, 3) == 5
```
Explanation: Use `==` to compare values in an assert.
</details>

2) Forgetting to call the function in test:
```python
def double(x):
    return x * 2
assert double == 6
```
<details><summary>Answer</summary>

```python
def double(x):
    return x * 2
assert double(3) == 6
```
Explanation: Call the function with parentheses to get its return value.
</details>

3) Test expecting wrong type:
```python
def greet(name):
    return 'Hi ' + name
assert greet('Ana') == None
```
<details><summary>Answer</summary>

```python
def greet(name):
    return 'Hi ' + name
assert greet('Ana') == 'Hi Ana'
```
Explanation: Make sure expected value matches the function return type.
</details>

---

## Easy

### a) Write `add` function and test it

Input example:
```text
(no stdin input)
```

Output example (what the test would check):
```text
Test passes if no AssertionError
```

Starter code:
```python
# TODO: write function add(x, y) that returns x + y
# simple test (do not change):
# assert add(2, 3) == 5
```

<details><summary>Answer</summary>

```python
def add(x, y):
    return x + y
# test
assert add(2, 3) == 5
```
Explanation: Return the sum; the assert will pass when add works.
</details>

### b) Write `double` and test

Input example:
```text
(no stdin input)
```

Output example:
```text
Test passes if no AssertionError
```

Starter code:
```python
# TODO: write function double(n) that returns n*2
# test example: assert double(4) == 8
```

<details><summary>Answer</summary>

```python
def double(n):
    return n * 2
# test
assert double(4) == 8
```
Explanation: Simple multiplication and assert to check correctness.
</details>

---

## Medium

### a) Test function that returns True/False

Input example:
```text
(no stdin input)
```

Output example:
```text
Test passes if no AssertionError
```

Starter code:
```python
# TODO: write is_even(n) that returns True when n is even else False
# test example: assert is_even(4) is True
```

<details><summary>Answer</summary>

```python
def is_even(n):
    return n % 2 == 0
# test
assert is_even(4) is True
assert is_even(3) is False
```
Explanation: Use modulo to determine evenness; tests check both cases.
</details>

### b) Test with simple exception handling (show expected test)

Input example:
```text
(no stdin input)
```

Output example:
```text
Test passes if ValueError is raised for bad input
```

Starter code:
```python
# TODO: write to_int(s) that returns int(s) but raises ValueError if not numeric
# test example:
# try:
#     to_int('x')
#     assert False  # should not reach here
# except ValueError:
#     assert True
```

<details><summary>Answer</summary>

```python
def to_int(s):
    return int(s)
# test
try:
    to_int('x')
    assert False
except ValueError:
    assert True
```
Explanation: Demonstrates how a test checks that errors are raised for bad input.
</details>

---

## Hard

### Single: Write a small function and a set of asserts

Input example:
```text
(no stdin input)
```

Output example:
```text
All tests pass (no AssertionError)
```

Starter code:
```python
# TODO: write function first_and_last(lst) that returns (first, last) from a list
# tests (do not change):
# assert first_and_last([1,2,3]) == (1,3)
# assert first_and_last(['a','b']) == ('a','b')
```

<details><summary>Answer</summary>

```python
def first_and_last(lst):
    return (lst[0], lst[-1])
# tests
assert first_and_last([1,2,3]) == (1,3)
assert first_and_last(['a','b']) == ('a','b')
```
Explanation: Use indexing to grab first and last elements; tests check two cases.
</details>
