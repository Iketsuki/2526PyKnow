---
tags: [python, exercises, io, validation]
difficulty: Beginner
---

# Python - IO - Input Validation — Exercises

See concept: [[Python - IO - Input Validation]]
GitHub link: [Python - IO - Input Validation](./Python%20-%20IO%20-%20Input%20Validation.md)

## Quick syntax fixes

1) Broken: not handling ValueError
```python
# Broken
n = int(input('n: '))
```
<details><summary>Answer</summary>

```python
# Fixed
try:
    n = int(input('n: '))
except ValueError:
    n = 0
```
Explanation: Use try/except to catch conversion errors.
</details>

2) Broken: empty string check
```python
# Broken
name = input('name: ')
if name:
    print('ok')
```
<details><summary>Answer</summary>

```python
# Fixed
name = input('name: ')
if name.strip():
    print('ok')
else:
    print('no name')
```
Explanation: Use `strip()` to treat whitespace-only input as empty.
</details>

3) Broken: input out of range
```python
# Broken
choice = int(input('1-3: '))
if choice > 3:
    print('bad')
```
<details><summary>Answer</summary>

```python
# Fixed
choice = int(input('1-3: '))
if choice < 1 or choice > 3:
    print('bad')
```
Explanation: Check lower and upper bounds.
</details>

---

## Easy

a) Read input and print `bad input` if it is not an integer.

Starter code:
```python
val = input('n: ')
# TODO: print number or 'bad input'
```
<details><summary>Answer</summary>

```python
val = input('n: ')
try:
    n = int(val)
    print(n)
except ValueError:
    print('bad input')
```
Explanation: Use try/except to validate.
</details>

b) Read a name and print 'empty' if user only enters spaces.

Starter code:
```python
name = input('name: ')
# TODO: check for empty or whitespace only
```
<details><summary>Answer</summary>

```python
name = input('name: ')
if name.strip():
    print(name)
else:
    print('empty')
```
Explanation: `strip()` removes whitespace.
</details>

---

## Medium

a) Validate a menu number 1-3 and reprompt until correct.

Starter code:
```python
# TODO: ask number 1-3 until valid
```
<details><summary>Answer</summary>

```python
while True:
    try:
        choice = int(input('1-3: '))
        if 1 <= choice <= 3:
            break
        else:
            print('choose 1-3')
    except ValueError:
        print('not a number')
print('you chose', choice)
```
Explanation: Loop until valid integer in range.
</details>

b) Read float temperature and print with one decimal or 'bad' on failure.

Starter code:
```python
val = input('temp: ')
# TODO: try to convert to float and print with one decimal, else print 'bad'
```
<details><summary>Answer</summary>

```python
val = input('temp: ')
try:
    t = float(val)
    print(f'{t:.1f}')
except ValueError:
    print('bad')
```
Explanation: Use float() and format.
</details>

---

## Hard

Write `read_int(prompt, low, high)` that asks until user enters an integer in range and returns it.

Starter code:
```python
def read_int(prompt, low, high):
    # TODO: loop until valid integer in range
    pass

print(read_int('n: ', 1, 5))
```
<details><summary>Answer</summary>

```python
def read_int(prompt, low, high):
    while True:
        try:
            v = int(input(prompt))
            if low <= v <= high:
                return v
            print('out of range')
        except ValueError:
            print('not a number')

print(read_int('n: ', 1, 5))
```
Explanation: Loop and validate type and bounds.
</details>
