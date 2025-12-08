### Task ID: UA1033
### Task Title: Computer Learns to Count Odd Numbers

-----

### 📚 Quick Lesson

**Concept:**
You can use a `for` loop with a step to count odd numbers. Example:
```python
for i in range(1, 10, 2):
    print(i)
```
This prints odd numbers from 1 to 9.

-----

### 🖥️ Main Statement

**Story:**
Write a program that prints all odd numbers from 1 up to the number entered by the user (inclusive).

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 100$).

**Output:**
Print all odd numbers from 1 to $n$, each on a new line.

**Constraints:**
- $1 \leq n \leq 100$

**Sample Tests:**
Input:
```
7
```
Output:
```
1
3
5
7
```

Input:
```
8
```
Output:
```
1
3
5
7
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: use a for loop to print odd numbers from 1 to n

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
