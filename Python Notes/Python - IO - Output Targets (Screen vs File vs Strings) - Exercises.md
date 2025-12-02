---
tags: [python, exercises, io]
difficulty: Beginner
---

# Python - IO - Output Targets (Screen vs File vs Strings) — Exercises

See concept: [[Python - IO - Output Targets (Screen vs File vs Strings)]]
GitHub link: [Python - IO - Output Targets (Screen vs File vs Strings)](./Python%20-%20IO%20-%20Output%20Targets%20(Screen%20vs%20File%20vs%20Strings).md)

## Quick syntax fixes

1) Broken: writing to screen but meant file
```python
print('a', file='out.txt')
```
<details><summary>Answer</summary>

```python
with open('out.txt','w') as f:
    print('a', file=f)
```
Explanation: `print` can target a file object with `file=`.
</details>

2) Broken: capturing output to string incorrectly
```python
s = print('hi')
```
<details><summary>Answer</summary>

```python
import io
buf = io.StringIO()
print('hi', file=buf)
s = buf.getvalue()
```
Explanation: use StringIO to capture printed output.
</details>

3) Broken: forgetting newline when writing to file
```python
with open('out.txt','w') as f:
    f.write('a')
print(open('out.txt').read())
```
<details><summary>Answer</summary>

```python
with open('out.txt','w') as f:
    f.write('a\n')
print(open('out.txt').read())
```
Explanation: add newline when needed.
</details>

---

## Easy

a) Print a message to the console and to a file.

Starter code:
```python
# TODO: print to screen and file
pass
```
<details><summary>Answer</summary>

```python
print('hi')
with open('out.txt','w') as f:
    print('hi', file=f)
```
Explanation: print to both targets separately.
</details>

b) Capture printed text into a string and print its length.

Starter code:
```python
import io
# TODO: capture and length
pass
```
<details><summary>Answer</summary>

```python
import io
buf = io.StringIO()
print('hello', file=buf)
s = buf.getvalue()
print(len(s))
```
Explanation: StringIO stores printed output.
</details>

---

## Medium

a) Write a function that writes text to either a file or returns it as a string based on a flag.

Starter code:
```python
def output_text(text, to_file=False):
    # TODO: if to_file write out.txt else return string
    pass

print(output_text('hi'))
```
<details><summary>Answer</summary>

```python
def output_text(text, to_file=False):
    if to_file:
        with open('out.txt','w') as f:
            f.write(text)
        return None
    else:
        return text

print(output_text('hi'))
```
Explanation: conditional output targets.
</details>

b) Capture a function's print output and return it.

Starter code:
```python
import io
def f():
    print('x')
# TODO: capture f output
pass
```
<details><summary>Answer</summary>

```python
import io
def f():
    print('x')
buf = io.StringIO()
import sys
old = sys.stdout
sys.stdout = buf
f()
sys.stdout = old
print(buf.getvalue())
```
Explanation: redirect stdout to capture prints.
</details>

---

## Hard

Write a function that prints numbers to a file and returns the same text as a string.

Starter code:
```python
def write_and_return(nums):
    # TODO: write to file and return combined string
    pass

print(write_and_return([1,2]))
```
<details><summary>Answer</summary>

```python
def write_and_return(nums):
    lines = '\n'.join(str(n) for n in nums) + '\n'
    with open('out.txt','w') as f:
        f.write(lines)
    return lines

print(write_and_return([1,2]))
```
Explanation: write joined lines and return same string.
</details>
