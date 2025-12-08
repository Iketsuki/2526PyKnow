### Task ID: UA1060
### Task Title: Sum Calculators Needed (Split Input, For Loop)

-----

### 📚 Quick Lesson

**Concept:**
You can use `split()` to read a line of numbers, and use a for loop with `len()` to sum them. Example:
```python
arr = input().split()
sum_val = 0
for i in range(len(arr)):
    sum_val += int(arr[i])
print(sum_val)
```

-----

### 🖥️ Main Statement

**Story:**
Write a program that asks the user for the number of students $n$, then reads one line of $n$ space-separated numbers (each 0, 1, or 2) representing the number of calculators each student needs. Print the total number of calculators needed.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 100$).
The second line contains $n$ space-separated integers $c$ ($0 \leq c \leq 2$).

**Output:**
Print the total number of calculators needed.

**Sample Tests:**
Input:
```
3
1 2 0
```
Output:
```
3
```

Input:
```
5
2 2 2 2 2
```
Output:
```
10
```

Input:
```
1
0
```
Output:
```
0
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
arr = input().split()
sum_val = 0
for i in range(____):
    # TODO: add arr[i] to sum_val
    sum_val += ____
print(sum_val)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
