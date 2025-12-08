### Task ID: UA1042
### Task Title: While Loop Odd Counter

-----

### 📚 Quick Lesson

**Concept:**
You can use a `while` loop to print odd numbers by incrementing by 2. Example:
```python
n = 7
count = 1
while count <= n:
    print(count)
    count += 2
```
This prints odd numbers from 1 to 7.

-----

### 🖥️ Main Statement

**Story:**
Write a program that prints all odd numbers from 1 up to the number entered by the user (inclusive), using a `while` loop.

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
# TODO: use a while loop to print odd numbers from 1 to n

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
