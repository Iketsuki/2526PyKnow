# Python - Exercises - Functions - Definition Basics

See concept: [[Python - Functions - Definition Basics]]

Easy:
- a) Define a function `say_hi()` that prints `Hi!` and call it.

  Output:
  Hi!

  <details>
  <summary>Answer (a)</summary>

  ```python
  def say_hi():
      print('Hi!')

  say_hi()
  ```

  Explanation: `def` creates a function. Call it by name with parentheses.
  </details>

- b) Define `add_one(x)` that returns `x + 1`.

  Input: 4
  Output:
  5

  <details>
  <summary>Answer (b)</summary>

  ```python
  def add_one(x):
      return x + 1

  print(add_one(4))
  ```

  Explanation: `return` gives a value back to the caller.
  </details>

Medium:
- a) Write `greet(name)` that prints `Hello, <name>`.

  Input: 'Sam'
  Output:
  Hello, Sam

  <details>
  <summary>Answer (a)</summary>

  ```python
  def greet(name):
      print('Hello,', name)

  greet('Sam')
  ```

  Explanation: Functions can take parameters to use inside.
  </details>

- b) Write `is_even(n)` that returns `True` if `n` is even, else `False`.

  Input: 6
  Output:
  True

  <details>
  <summary>Answer (b)</summary>

  ```python
  def is_even(n):
      return n % 2 == 0

  print(is_even(6))
  ```

  Explanation: The function returns a boolean result from the `%` test.
  </details>

Hard:
- Write `sum_list(lst)` that returns the sum of numbers in a list.

  Input: [1,2,3]
  Output:
  6

  <details>
  <summary>Answer</summary>

  ```python
  def sum_list(lst):
      total = 0
      for x in lst:
          total += x
      return total

  print(sum_list([1, 2, 3]))
  ```

  Explanation: Use a loop to add each item into a running `total` and return it.
  </details>
