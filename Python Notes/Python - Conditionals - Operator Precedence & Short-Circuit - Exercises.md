---
tags: [python, exercises, conditionals, precedence]
difficulty: Beginner
---

# Python - Conditionals - Operator Precedence & Short-Circuit — Exercises

See concept: [[Python - Conditionals - Operator Precedence & Short-Circuit]]
GitHub link: [Python - Conditionals - Operator Precedence & Short-Circuit](./Python%20-%20Conditionals%20-%20Operator%20Precedence%20%26%20Short-Circuit.md)

## Quick syntax fixes

1) Broken: misunderstanding `and` vs `&`
```python
# Broken
if a & b:
    print('ok')
```
<details><summary>Answer</summary>

```python
# Fixed
if a and b:
    print('ok')
```
Explanation: `and` is boolean operator; `&` is bitwise.
</details>

2) Broken: expecting short-circuit but function is called
```python
# Broken
def f():
    print('call')
    return True
print(False and f())
```
<details><summary>Answer</summary>

```python
# Fixed (no change needed to show behavior)
def f():
    print('call')
    return True
print(False and f())  # f() is not called because False short-circuits
```
Explanation: `and` short-circuits when left side is False.
</details>

3) Broken: wrong order of operations
```python
# Broken
if a or b and c:
    print('ok')
```
<details><summary>Answer</summary>

```python
# Fixed
if a or (b and c):
    print('ok')
```
Explanation: `and` runs before `or`; use parentheses for clarity.
</details>

---

## Easy

a) Show that `False and f()` does not call `f` by writing code that prints 'no call'.

Starter code:
```python
def f():
    print('called')
    return True
# TODO: use and with False to avoid calling f
pass
```
<details><summary>Answer</summary>

```python
def f():
    print('called')
    return True
print(False and f())
```
Explanation: Short-circuit prevents `f()` from executing.
</details>

b) Use parentheses to make `(a or b) and c` explicit and print result.

Starter code:
```python
a = True
b = False
c = True
# TODO: compute (a or b) and c and print
pass
```
<details><summary>Answer</summary>

```python
a = True
b = False
c = True
print((a or b) and c)
```
Explanation: Parentheses show grouping.
</details>

---

## Medium

a) Given `x`, print 'ok' when x is between 1 and 10 and not zero using short circuit.

Starter code:
```python
x = 5
# TODO: print True when 1<=x<=10 and x!=0
pass
```
<details><summary>Answer</summary>

```python
x = 5
print((1 <= x <= 10) and (x != 0))
```
Explanation: Combine checks with `and`.
</details>

b) Prevent calling `danger()` when `safe` is True using short-circuit.

Starter code:
```python
def danger():
    print('danger')
    return True
safe = True
# TODO: use or/and so danger() is not called when safe
pass
```
<details><summary>Answer</summary>

```python
def danger():
    print('danger')
    return True
safe = True
print(safe or danger())
```
Explanation: `or` short-circuits if left side is True.
</details>

---

## Hard

Write `choose(a,b,c)` that returns `a` if `a` truthy else `b` if `b` truthy else `c` using short-circuit operators.

Starter code:
```python
def choose(a, b, c):
    # TODO: return a or b or c
    pass
print(choose('', 'hi', 'bye'))
```
<details><summary>Answer</summary>

```python
def choose(a, b, c):
    return a or b or c
print(choose('', 'hi', 'bye'))
```
Explanation: `or` returns the first truthy value.
</details>
