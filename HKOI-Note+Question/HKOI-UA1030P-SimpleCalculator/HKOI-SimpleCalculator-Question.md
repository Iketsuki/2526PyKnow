### Task ID: UA1030P
### Task Title: Simple Calculator

-----

### 📚 Quick Lesson

**Concept:**
You can use if-elif-else to select operations based on user input:
```python
op = input()  # 'add', 'sub', 'mul', 'div'
if op == 'add':
    #perform addition
```

-----

### 🖥️ Main Statement

**Story:**
Write a simple calculator. Given two numbers and an operation, print the result.

**Input:**
The first line contains a float $a$ ($-10000 \leq a \leq 10000$).
The second line contains a float $b$ ($-10000 \leq b \leq 10000$).
The third line contains a string $op$ (`add`, `sub`, `mul`, `div`).

**Output:**
Print the result of the operation.

**Constraints:**
- $-10000 \leq a, b \leq 10000$
- $op$ is one of `add`, `sub`, `mul`, `div`
- For `div`, $b \neq 0$

**Sample Tests:**
Input:
```
5
3
add
```
Output:
```
8.0
```

Input:
```
5
3
sub
```
Output:
```
2.0
```

Input:
```
5
3
mul
```
Output:
```
15.0
```

Input:
```
5
2
div
```
Output:
```
2.5
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

a = float(input())
b = float(input())
op = input()  # 'add', 'sub', 'mul', 'div'
# TODO: perform the operation and print result

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
