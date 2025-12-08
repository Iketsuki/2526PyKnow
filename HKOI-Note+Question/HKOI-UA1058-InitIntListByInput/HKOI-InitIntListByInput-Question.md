### Task ID: UA1058
### Task Title: Initialize Integer List by Input

-----

### 📚 Quick Lesson

**Concept:**
You can fill a list of numbers by assigning values to each index in a loop. Example:
```python
n = 3
arr = [0] * n
for i in range(n):
    arr[i] = int(input())
print(arr)
```

-----

### 🖥️ Main Statement

**Story:**
Write a program that asks the user for the number of elements, then reads that many integers (one per line) and stores them in a list. Print the list at the end.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 10$).
The next $n$ lines each contain an integer.

**Output:**
Print the list of integers.

**Sample Tests:**
Input:
```
3
1
2
3
```
Output:
```
[1, 2, 3]
```

Input:
```
2
10
20
```
Output:
```
[10, 20]
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# Step 1: create a list of n zeros
arr = [0] * n
# Step 2: fill the list using a loop
for i in range(n):
    # TODO: read an integer and store it in arr[i]
    arr[i] = ____
# Step 3: print the list
print(arr)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
