---
tags: [python, exercises, debugging, print]
difficulty: Beginner
---

# Python - Debugging - Print Debugging — Exercises

See concept: [[Python - Debugging - Print Debugging]]

GitHub link: [Python - Debugging - Print Debugging](./Python%20-%20Debugging%20-%20Print%20Debugging.md)

## Quick syntax fixes

1) Broken code: missing a print to see value
```python
# Broken
def double(n):
    return n * 2
double(3)
```
<details><summary>Answer</summary>

```python
# Fixed
def double(n):
    return n * 2
print(double(3))
```
Explanation: Print the function result to see it.
</details>

2) Broken code: helpful print missing inside a loop
```python
# Broken
for i in range(3):
    pass
```
<details><summary>Answer</summary>

```python
# Fixed
for i in range(3):
    print('loop i=', i)
```
Explanation: Print inside loop to trace iterations.
</details>

3) Broken code: not printing intermediate value
```python
# Broken
total = 0
for i in [1,2,3]:
    total += i
print(total)
```
<details><summary>Answer</summary>

```python
# Fixed (add debug prints)
total = 0
for i in [1,2,3]:
    total += i
    print('added', i, 'total now', total)
print(total)
```
Explanation: Print intermediate values to check progress.
</details>

---

## Easy

a) Add a print to show the input and output of this function.

Starter code:
```python
def add(a, b):
    return a + b
result = add(2, 3)
# TODO: print input numbers and result
```
<details><summary>Answer</summary>

```python
def add(a, b):
    return a + b
result = add(2, 3)
print('a=', 2, 'b=', 3, 'result=', result)
```
Explanation: Print inputs and outputs to trace function behavior.
</details>

b) Print the loop index each time in a loop that sums numbers.

Starter code:
```python
numbers = [4,5,6]
total = 0
for i in range(len(numbers)):
    total += numbers[i]
# TODO: print i and numbers[i] inside the loop
print(total)
```
<details><summary>Answer</summary>

```python
numbers = [4,5,6]
total = 0
for i in range(len(numbers)):
    print('i=', i, 'value=', numbers[i])
    total += numbers[i]
print(total)
```
Explanation: Printing index and value helps find logic errors.
</details>

---

## Medium

a) Use print debugging to find why this code gives 0 instead of 6.

Starter code:
```python
def multiply_list(lst):
    result = 0
    for v in lst:
        result = result * v
    return result
print(multiply_list([1,2,3]))
```
<details><summary>Answer</summary>

```python
def multiply_list(lst):
    result = 1
    for v in lst:
        print('before:', result, 'multiply by', v)
        result = result * v
        print('after:', result)
    return result
print(multiply_list([1,2,3]))
```
Explanation: Start product at 1 and use prints to trace multiplication steps.
</details>

b) Add prints to show types of elements while filtering integers from a list.

Starter code:
```python
items = [1, '2', 3]
ints = []
for it in items:
    # TODO: print item and type, then keep only ints
    pass
print(ints)
```
<details><summary>Answer</summary>

```python
items = [1, '2', 3]
ints = []
for it in items:
    print('item:', it, 'type:', type(it))
    if isinstance(it, int):
        ints.append(it)
print(ints)
```
Explanation: Print types to verify which items are ints.
</details>

---

## Hard

Use print debugging to show why a function returns wrong type and fix it.

Starter code:
```python
def join_numbers(lst):
    s = 0
    for n in lst:
        s = s + str(n)
    return s
print(join_numbers([1,2,3]))
```
<details><summary>Answer</summary>

```python
def join_numbers(lst):
    s = ''
    for n in lst:
        print('n:', n, 'type:', type(n), 's before:', s)
        s = s + str(n)
        print('s after:', s)
    return s
print(join_numbers([1,2,3]))
```
Explanation: Start `s` as an empty string and use prints to show changes.
</details>
