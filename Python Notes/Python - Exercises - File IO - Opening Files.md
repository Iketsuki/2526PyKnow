# Python - Exercises - File IO - Opening Files

See concept: [[Python - File IO - Opening Files]]

Easy:
- a) Open a file `data.txt` for writing and write `Hello` then close it.

  Expected file contents after run:
  Hello

  <details>
  <summary>Answer (a)</summary>

  ```python
  f = open('data.txt', 'w')
  f.write('Hello')
  f.close()
  ```

  Explanation: `'w'` mode creates or truncates the file. `close()` saves and frees the file.
  </details>

- b) Open a file `data.txt` for reading and print its contents.

  If `data.txt` contains `Hello` then output:
  Hello

  <details>
  <summary>Answer (b)</summary>

  ```python
  f = open('data.txt', 'r')
  print(f.read())
  f.close()
  ```

  Explanation: `'r'` reads the file. `read()` returns the whole text.
  </details>

Medium:
- a) Use `with` to write `Line1` to `log.txt`.

  File after run:
  Line1

  <details>
  <summary>Answer (a)</summary>

  ```python
  with open('log.txt', 'w') as f:
      f.write('Line1')
  ```

  Explanation: `with` ensures the file is closed automatically.
  </details>

- b) Read the first line from `log.txt` and print it.

  If file contains `Line1\nLine2` then output:
  Line1

  <details>
  <summary>Answer (b)</summary>

  ```python
  with open('log.txt', 'r') as f:
      first = f.readline().rstrip('\n')
      print(first)
  ```

  Explanation: `readline()` reads one line; `rstrip()` removes the trailing newline.
  </details>

Hard:
- Write a function `count_lines(path)` that returns the number of lines in a file.

  If `sample.txt` has 3 lines, output:
  3

  <details>
  <summary>Answer</summary>

  ```python
  def count_lines(path):
      count = 0
      with open(path, 'r') as f:
          for _ in f:
              count += 1
      return count

  print(count_lines('sample.txt'))
  ```

  Explanation: Iterate the file object line by line and count rows. `with` keeps it safe.
  </details>
