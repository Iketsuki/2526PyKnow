---
tags: [python, exercises, loops]
difficulty: Beginner
---

# Exercises — Loops: Range Function

See concept: [[Python - Loops - Range Function]]

### Quick syntax fixes

1) Wrong range order:
```python
for i in range(5, 1):
    print(i)
```
<details><summary>Answer</summary>

```python
for i in range(1, 5):
    print(i)
```
Explanation: `range(start, stop)` needs start < stop to list increasing numbers.
</details>

2) Missing step example:
```python
for i in range(0,10,):
    print(i)
```
<details><summary>Answer</summary>

```python
for i in range(0,10,1):
    print(i)
```
Explanation: If you include a comma for step, provide a step value. Often omit it for default step 1.
</details>

3) Using range on string directly:
```python
for i in range('abc'):
    print(i)
```
<details><summary>Answer</summary>

```python
for ch in 'abc':
    print(ch)
```
Explanation: Iterate over string characters directly.
</details>

---

## Easy

### a) Print numbers 0..2

Output example:
```text
0
1
2
```

Starter code:
```python
# TODO: use range to print 0,1,2 each on new line
```

<details><summary>Answer</summary>

```python
for i in range(3):
    print(i)
```
Explanation: `range(3)` gives 0..2.
</details>

### b) Use range to print even numbers 2,4,6

Output example:
```text
2
4
6
```

Starter code:
```python
# TODO: use range with step to print 2,4,6
```

<details><summary>Answer</summary>

```python
for i in range(2, 7, 2):
    print(i)
```
Explanation: `range(start, stop, step)` controls step size.
</details>

---

## Medium

### a) Print 3 numbers starting at a from input

Input example:
```text
5
```

Output example:
```text
5
6
7
```

Starter code:
```python
a = int(input())
# TODO: print a, a+1, a+2 using range
```

<details><summary>Answer</summary>

```python
a = int(input())
for i in range(a, a+3):
    print(i)
```
Explanation: Use range with computed end.
</details>

### b) Show indexes of list using range

Input example:
```text
apple
banana
```

Output example:
```text
0
1
```

Starter code:
```python
items = [input(), input()]
# TODO: print indices using range
```

<details><summary>Answer</summary>

```python
items = [input(), input()]
for i in range(len(items)):
    print(i)
```
Explanation: `range(len(...))` gives indices.
</details>

---

## Hard

### Single: Print numbers from n down to 1

Input example:
```text
4
```

Output example:
```text
4
3
2
1
```

Starter code:
```python
n = int(input())
# TODO: use range with negative step to count down
```

<details><summary>Answer</summary>

```python
n = int(input())
for i in range(n, 0, -1):
    print(i)
```
Explanation: Use a negative step to count down.
</details>
