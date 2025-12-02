# Python - Exercises - IO - Input Basics

See concept: [[Python - IO - Input Basics]]

Easy:
- a) Ask the user for their name and print: `Hello, <name>!`.

  Input (user types): Alice
  Output:
  Hello, Alice!

  <details>
  <summary>Answer (a)</summary>

  ```python
  name = input('Enter your name: ')
  print('Hello,', name + '!')
  ```

  Explanation: `input()` reads text from the user. Use `print()` to show a greeting.
  </details>

- b) Ask for a number and print `You entered: <number>`.

  Input: 5
  Output:
  You entered: 5

  <details>
  <summary>Answer (b)</summary>

  ```python
  num = input('Enter a number: ')
  print('You entered:', num)
  ```

  Explanation: `input()` returns a string. If you need a number for math, convert with `int()`.
  </details>

Medium:
- a) Ask for a name and age. Print `Name: <name> Age next year: <age+1>`.

  Input:
  name: Ben
  age: 7

  Output:
  Name: Ben Age next year: 8

  <details>
  <summary>Answer (a)</summary>

  ```python
  name = input('Name: ')
  age = int(input('Age: '))
  print('Name:', name, 'Age next year:', age + 1)
  ```

  Explanation: Convert the age string to an integer with `int()` before adding 1.
  </details>

- b) Read two numbers and print their sum.

  Input:
  3
  4
  Output:
  Sum: 7

  <details>
  <summary>Answer (b)</summary>

  ```python
  a = int(input())
  b = int(input())
  print('Sum:', a + b)
  ```

  Explanation: Use `int()` to convert input strings to numbers so you can add them.
  </details>

Hard:
- Write a program that asks for three test scores (0-100) and prints the average rounded to 1 decimal place.

  Input:
  80
  90
  70
  Output:
  Average: 80.0

  <details>
  <summary>Answer</summary>

  ```python
  s1 = float(input('Score 1: '))
  s2 = float(input('Score 2: '))
  s3 = float(input('Score 3: '))
  avg = (s1 + s2 + s3) / 3
  print('Average:', round(avg, 1))
  ```

  Explanation: Use `float()` for decimal safety, compute the mean, then `round()` to 1 decimal.
  </details>
