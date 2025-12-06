### Task ID: UA1020
### Task Title: Even or Odd

-----

### 📚 Quick Lesson

**Concept:**
The `if-else` statement lets you choose between two actions. For example:

```python
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

-----

### 🖥️ Main Statement

**Story:**
Given an integer, print "Even" if it is even, otherwise print "Odd".

**Input:**
The first line contains an integer $n$ ($-1000 \leq n \leq 1000$).

**Output:**
Print `Even` if $n$ is even, otherwise print `Odd`.

**Constraints:**
- $-1000 \leq n \leq 1000$

**Sample Tests:**
Input:
```
4
```
Output:
```
Even
```

Input:
```
7
```
Output:
```
Odd
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: use if-else to print Even or Odd

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
