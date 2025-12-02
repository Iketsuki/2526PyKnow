# Python - Exercises - Lists - Creation & Initialization

See concept: [[Python - Lists - Creation & Initialization]]

Easy:
- a) Make a list with three fruits: `['apple', 'banana', 'cherry']`. Print it.

  Output:
  ['apple', 'banana', 'cherry']

  <details>
  <summary>Answer (a)</summary>

  ```python
  fruits = ['apple', 'banana', 'cherry']
  print(fruits)
  ```

  Explanation: Use square brackets `[]` with comma-separated values to create a list.
  </details>

- b) Make an empty list and then add 'egg' using `.append()`.

  Output:
  ['egg']

  <details>
  <summary>Answer (b)</summary>

  ```python
  items = []
  items.append('egg')
  print(items)
  ```

  Explanation: Start with `[]`. `.append()` adds an item at the end.
  </details>

Medium:
- a) Create a list of three numbers and print the second item.

  Example list: `[10, 20, 30]`
  Output:
  20

  <details>
  <summary>Answer (a)</summary>

  ```python
  nums = [10, 20, 30]
  print(nums[1])  # index 1 is the second item
  ```

  Explanation: Lists use zero-based indexes; `0` is first, `1` is second.
  </details>

- b) Make a list from `range(1, 6)` and print it.

  Output:
  [1, 2, 3, 4, 5]

  <details>
  <summary>Answer (b)</summary>

  ```python
  nums = list(range(1, 6))
  print(nums)
  ```

  Explanation: `range()` makes a sequence; `list()` converts it to a list you can print.
  </details>

Hard:
- Given a list of words, make a new list with each word repeated twice.

  Input:
  ['hi', 'ok']
  Output:
  ['hihi', 'okok']

  <details>
  <summary>Answer</summary>

  ```python
  words = ['hi', 'ok']
  doubled = [w * 2 for w in words]
  print(doubled)
  ```

  Explanation: A list comprehension builds a new list quickly. `w * 2` repeats the string twice.
  </details>
