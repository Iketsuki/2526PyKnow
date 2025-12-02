# Python - Exercises - Loops - For Loop Basics

See concept: [[Python - Loops - For Loop Basics]]

Easy:
- a) Print each letter in `name = 'Amy'` on its own line.

  Output:
  A
  m
  y

  <details>
  <summary>Answer (a)</summary>

  ```python
  name = 'Amy'
  for ch in name:
      print(ch)
  ```

  Explanation: `for` loops go over each item in a sequence.
  </details>

- b) Print numbers 1 to 3 using a `for` loop.

  Output:
  1
  2
  3

  <details>
  <summary>Answer (b)</summary>

  ```python
  for i in range(1, 4):
      print(i)
  ```

  Explanation: `range(1, 4)` gives 1,2,3.
  </details>

Medium:
- a) Given a list `[2,4,6]`, print each number multiplied by 2.

  Output:
  4
  8
  12

  <details>
  <summary>Answer (a)</summary>

  ```python
  nums = [2, 4, 6]
  for n in nums:
      print(n * 2)
  ```

  Explanation: Multiply inside the loop for each item.
  </details>

- b) Given a list of names, print `Hello <name>` for each.

  Input: `['May','Ted']`
  Output:
  Hello May
  Hello Ted

  <details>
  <summary>Answer (b)</summary>

  ```python
  names = ['May', 'Ted']
  for name in names:
      print('Hello', name)
  ```

  Explanation: Use the loop variable to show each name.
  </details>

Hard:
- Create a list of squares for 1..5 using a loop (store in a list then print list).

  Output:
  [1, 4, 9, 16, 25]

  <details>
  <summary>Answer</summary>

  ```python
  squares = []
  for i in range(1, 6):
      squares.append(i * i)
  print(squares)
  ```

  Explanation: Build the list inside the loop with `.append()`.
  </details>
