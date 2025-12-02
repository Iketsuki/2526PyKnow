---
tags: [python, exercises, debugging, exception-info]
difficulty: Beginner
---

# Python - Debugging - Exception Info — Exercises

See concept: [[Python - Debugging - Exception Info]]
GitHub link: [Python - Debugging - Exception Info](./Python%20-%20Debugging%20-%20Exception%20Info.md)

## Quick syntax fixes

1) Broken: not printing exception message
```python
# Broken
try:
    1/0
except Exception:
    pass
```
<details><summary>Answer</summary>

```python
# Fixed
try:
    1/0
except Exception as e:
    print('error:', e)
```
Explanation: Capture exception as a variable to inspect message.
</details>

2) Broken: not using traceback to see full info
```python
# Broken
try:
    1/0
except Exception as e:
    print(e)
```
<details><summary>Answer</summary>

```python
# Fixed
import traceback
try:
    1/0
except Exception as e:
    traceback.print_exc()
```
Explanation: `traceback.print_exc()` shows stack trace for debugging.
</details>

3) Broken: swallowing exception
```python
# Broken
try:
    x = int('a')
except ValueError:
    pass
```
<details><summary>Answer</summary>

```python
# Fixed
try:
    x = int('a')
except ValueError as e:
    print('bad int:', e)
```
Explanation: Log or print exception info instead of ignoring it.
</details>

---

## Easy

a) Catch an exception and print its type and message.

Starter code:
```python
try:
    1/0
except Exception as e:
    # TODO: print type and message
    pass
```
<details><summary>Answer</summary>

```python
try:
    1/0
except Exception as e:
    print(type(e), e)
```
Explanation: `type(e)` shows the exception class.
</details>

b) Use `traceback` to print a readable stack trace for an error.

Starter code:
```python
import traceback
try:
    int('a')
except Exception:
    # TODO: print stack trace
    pass
```
<details><summary>Answer</summary>

```python
import traceback
try:
    int('a')
except Exception:
    traceback.print_exc()
```
Explanation: Stack trace helps find where an error happened.
</details>

---

## Medium

a) Log exception info to a file using `traceback.format_exc()`.

Starter code:
```python
import traceback
try:
    1/0
except Exception:
    # TODO: write traceback to 'err.log'
    pass
```
<details><summary>Answer</summary>

```python
import traceback
try:
    1/0
except Exception:
    with open('err.log', 'w') as f:
        f.write(traceback.format_exc())
```
Explanation: Save tracebacks for later inspection.
</details>

b) Extract exception message and use it in a user-friendly print statement.

Starter code:
```python
try:
    int('a')
except Exception as e:
    # TODO: print 'Error: <message>'
    pass
```
<details><summary>Answer</summary>

```python
try:
    int('a')
except Exception as e:
    print('Error:', str(e))
```
Explanation: Convert exception to string to show message.
</details>

---

## Hard

Write a function `debug_run(fn)` that runs `fn` and returns `(False, traceback)` on error or `(True, result)` on success.

Starter code:
```python
import traceback
def debug_run(fn):
    # TODO: run fn and return (True, result) or (False, traceback)
    pass
def bad():
    1/0
print(debug_run(bad))
```
<details><summary>Answer</summary>

```python
import traceback
def debug_run(fn):
    try:
        return (True, fn())
    except Exception:
        return (False, traceback.format_exc())
def bad():
    1/0
print(debug_run(bad))
```
Explanation: Return traceback text so caller can print or log it.
</details>
