# Python - Exercises - Conditionals - If-Else Basics

See concept: [[Python - Conditionals - If-Else Basics]]

Easy:
- a) Write an `if` that prints `Yes` when `x` is 5.

  Input: x = 5
  Output:
  Yes

  <details>
  <summary>Answer (a)</summary>

  ```python
  x = 5
  if x == 5:
      print('Yes')
  ```

  Explanation: Use `==` to compare values in `if`.
  </details>

- b) Print `Even` if a number is even, otherwise print `Odd`.

  Input: 4
  Output:
  Even

  <details>
  <summary>Answer (b)</summary>

  ```python
  n = 4
  if n % 2 == 0:
      print('Even')
  else:
      print('Odd')
  ```

  Explanation: `%` gives the remainder. Even numbers have remainder 0 when divided by 2.
  </details>

Medium:
- a) Ask for age and print `Can watch PG` if age &gt;= 10, else `Wait`.

  Input: 9
  Output:
  Wait

  <details>
  <summary>Answer (a)</summary>

  ```python
  age = int(input('Age: '))
  if age >= 10:
      print('Can watch PG')
  else:
      print('Wait')
  ```

  Explanation: Use `>=` to check "greater or equal".
  </details>

- b) Given a score, print `A`, `B`, or `F` using `if`, `elif`, `else`.

  Input: 85
  Output:
  B

  <details>
  <summary>Answer (b)</summary>

  ```python
  score = int(input())
  if score >= 90:
      print('A')
  elif score >= 75:
      print('B')
  else:
      print('F')
  ```

  Explanation: `elif` checks another condition if the first is false.
  </details>

Hard:
- Write a program that reads a day name and prints `Weekend` for Saturday/Sunday, otherwise `Weekday`.

  Input: Saturday
  Output:
  Weekend

  <details>
  <summary>Answer</summary>

  ```python
  day = input().strip()
  if day == 'Saturday' or day == 'Sunday':
      print('Weekend')
  else:
      print('Weekday')
  ```

  Explanation: Use `or` to accept either weekend name. `.strip()` removes extra spaces.
  </details>
