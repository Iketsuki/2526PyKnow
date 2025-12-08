### Task ID: UA1053
### Task Title: Initialize List with * Operator

-----

### 📚 Quick Lesson

**Concept:**
You can quickly create a list with repeated elements using the `*` operator. Example:
```python
arr = [0] * 5
print(arr)  # prints [0, 0, 0, 0, 0]
```

-----

### 🖥️ Main Statement

**Story:**
Write a program that asks the user for a number $n$, creates a list of $n$ zeros, and prints the list.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 100$).

**Output:**
Print a list of $n$ zeros.

**Sample Tests:**
Input:
```
5
```
Output:
```
[0, 0, 0, 0, 0]
```

Input:
```
1
```
Output:
```
[0]
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: create a list of n zeros and print it

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
