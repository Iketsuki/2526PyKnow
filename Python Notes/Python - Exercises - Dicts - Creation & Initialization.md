# Python - Exercises - Dicts - Creation & Initialization

See concept: [[Python - Dicts - Creation & Initialization]]

Easy:
- a) Make a dict for a person: `{'name': 'Ana', 'age': 8}` and print it.

  Output:
  {'name': 'Ana', 'age': 8}

  <details>
  <summary>Answer (a)</summary>

  ```python
  person = {'name': 'Ana', 'age': 8}
  print(person)
  ```

  Explanation: Curly braces `{}` create a dict. Keys map to values.
  </details>

- b) Create an empty dict and add `person['city'] = 'Osaka'`.

  Output:
  {'city': 'Osaka'}

  <details>
  <summary>Answer (b)</summary>

  ```python
  d = {}
  d['city'] = 'Osaka'
  print(d)
  ```

  Explanation: Assigning to a new key adds it to the dictionary.
  </details>

Medium:
- a) Given `scores = {'a': 10, 'b': 7}`, print `a`'s score.

  Output:
  10

  <details>
  <summary>Answer (a)</summary>

  ```python
  scores = {'a': 10, 'b': 7}
  print(scores['a'])
  ```

  Explanation: Use square brackets with the key to get a value.
  </details>

- b) Use `.get()` to read `c` from `scores`, returning 0 if missing.

  Output:
  0

  <details>
  <summary>Answer (b)</summary>

  ```python
  print(scores.get('c', 0))
  ```

  Explanation: `.get(key, default)` returns `default` when key missing.
  </details>

Hard:
- Merge two dicts `a = {'x':1}` and `b = {'y':2}` into `{'x':1,'y':2}` and print.

  Output:
  {'x': 1, 'y': 2}

  <details>
  <summary>Answer</summary>

  ```python
  a = {'x': 1}
  b = {'y': 2}
  a.update(b)
  print(a)
  ```

  Explanation: `.update()` copies keys and values from `b` into `a`. If keys overlap, `b`'s values replace `a`'s.
  </details>
