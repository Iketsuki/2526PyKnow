### Task ID: UA1020
### Task Title: Threes Detector!

-----

### 📚 Quick Lesson

**Concept:**
Comparison operators let you compare values:
- `>` (greater than)
- `<` (less than)
- `>=` (greater than or equal to)
- `<=` (less than or equal to)
- `==` (equal to)
- `!=` (not equal to)

Example (not related to this question):
```python
age = 18
if age >= 18:
    print("You are an adult!")
```

**Review:**
The `%` operator gives the remainder after division. For example, `7 % 3` is `1` because 7 divided by 3 is 2 with a remainder of 1.

-----

### 🖥️ Main Statement

**Story:**
Given an integer, print `3` if it is divisible by 3.

**Input:**
The first line contains an integer $n$ ($-1000 \leq n \leq 1000$).

**Output:**
If $n$ is divisible by 3, print `3`.

**Constraints:**
- $-1000 \leq n \leq 1000$

**Sample Tests:**
Input:
```
9
```
Output:
```
3
```

Input:
```
8
```
Output:
```
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: print 3 if n is divisible by 3

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
