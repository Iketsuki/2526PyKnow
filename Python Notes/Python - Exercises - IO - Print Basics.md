# Python - Exercises - IO - Print Basics

See concept: [[Python - IO - Print Basics]]

Easy:
- a) Write a `print()` statement that shows: Hello, World!

  Input: (none)
  Output:
  Hello, World!

  <details>
  <summary>Answer (a)</summary>

  ```python
  print('Hello, World!')
  ```

  Explanation: `print()` shows text on the screen. Put the text in quotes.
  </details>

- b) Print your name, age, and city on one line separated by commas.

  Example variables:
  ```python
  name = 'Tom'
  age = 9
  city = 'Seoul'
  ```
  Expected Output:
  Tom, 9, Seoul

  <details>
  <summary>Answer (b)</summary>

  ```python
  print(name, age, city, sep=', ')
  ```

  Explanation: `print()` can take many values. `sep` sets what goes between them.
  </details>

Medium:
- a) Print the numbers 1 to 5 on one line separated by `-`.

  Input: (none)
  Output:
  1-2-3-4-5

  <details>
  <summary>Answer (a)</summary>

  ```python
  print(1, 2, 3, 4, 5, sep='-')
  ```

  Explanation: `sep='-'` places `-` between each printed value.
  </details>

- b) Use `end` to print `A B C!` (no newline after `!`).

  Input: (none)
  Output:
  A B C!

  <details>
  <summary>Answer (b)</summary>

  ```python
  print('A', 'B', 'C', end='!')
  ```

  Explanation: `end` replaces the final newline with what you give (here `!`).
  </details>

Hard:
- Write a function `greet(name, age, city)` that prints: `Name: <name>, Age: <age>, City: <city>`.

  Example call:
  ```python
  greet('Lina', 10, 'Tokyo')
  ```
  Output:
  Name: Lina, Age: 10, City: Tokyo

  <details>
  <summary>Answer</summary>

  ```python
  def greet(name, age, city):
      print('Name:', name + ',', 'Age:', age + ',', 'City:', city)
  ```

  Explanation: The function takes the values and prints them. Using commas in `print()` adds spaces automatically; the `+ ','` creates the comma after values. You can also use `f"Name: {name}, Age: {age}, City: {city}"` for cleaner formatting.
  </details>
