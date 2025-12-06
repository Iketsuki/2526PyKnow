### Task ID: UA1022
### Task Title: Number Mood Detector

-----

### 📚 Quick Lesson

**Concept:**
The `if-elif-else` structure lets you check multiple conditions in order:

```python
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
```

This is useful when you have more than two possible outcomes.

-----

### 🖥️ Main Statement

**Story:**
Given an integer, print `Positive` if it is greater than 0, `Negative` if it is less than 0, or `Zero` if it is exactly 0.

**Input:**
The first line contains an integer $n$ ($-1000 \leq n \leq 1000$).

**Output:**
Print `Positive`, `Negative`, or `Zero` according to the value of $n$.

**Constraints:**
- $-1000 \leq n \leq 1000$

**Sample Tests:**
Input:
```
5
```
Output:
```
Positive
```

Input:
```
-3
```
Output:
```
Negative
```

Input:
```
0
```
Output:
```
Zero
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: use if-elif-else to print Positive, Negative, or Zero

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
