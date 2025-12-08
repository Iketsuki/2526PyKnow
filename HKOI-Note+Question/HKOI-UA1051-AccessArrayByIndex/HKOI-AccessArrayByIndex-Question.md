### Task ID: UA1051
### Task Title: Access Array Element by Index

-----

### 📚 Quick Lesson

**Concept:**
You can access elements in a list by their index. **List indices start from 0.**
Example:
```python
arr = [10, 20, 30, 40, 50]
print(arr[2])  # prints 30
```

-----

### 🖥️ Main Statement

**Story:**
Given a list `[10, 20, 30, 40, 50]`, write a program that asks the user for an index and prints the element at that index.

**Input:**
The first line contains an integer $i$ ($0 \leq i \leq 4$).

**Output:**
Print the element at index $i$ of the list `[10, 20, 30, 40, 50]`.

**Sample Tests:**
Input:
```
2
```
Output:
```
30
```

Input:
```
0
```
Output:
```
10
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

arr = [10, 20, 30, 40, 50]
i = int(input())
# TODO: print the element at index i

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
