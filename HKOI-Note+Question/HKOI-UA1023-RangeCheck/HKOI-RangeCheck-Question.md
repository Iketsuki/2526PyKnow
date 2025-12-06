### Task ID: UA1023
### Task Title: In or Out?

-----

### 📚 Quick Lesson

**Concept:**
You can combine conditions using `and`, `or`, and `not`:
- `and`: True if both sides are true
- `or`: True if at least one side is true
- `not`: True if the condition is false

Example:
```python
age = 15
if age >= 13 and age <= 19:
    print("Teenager!")
```

-----

### 🖥️ Main Statement

**Story:**
Given an integer, print `In range` if it is between 10 and 20 (inclusive), otherwise print `Out of range`.

**Input:**
The first line contains an integer $n$ ($-1000 \leq n \leq 1000$).

**Output:**
Print `In range` if $10 \leq n \leq 20$, otherwise print `Out of range`.

**Constraints:**
- $-1000 \leq n \leq 1000$

**Sample Tests:**
Input:
```
15
```
Output:
```
In range
```

Input:
```
9
```
Output:
```
Out of range
```

Input:
```
20
```
Output:
```
In range
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: use and/or/not to check if n is in range

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
