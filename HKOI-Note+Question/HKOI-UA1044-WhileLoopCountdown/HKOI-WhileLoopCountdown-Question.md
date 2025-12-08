### Task ID: UA1044
### Task Title: While Loop Countdown

-----

### 📚 Quick Lesson

**Concept:**
A `while` loop can count down by decreasing the variable each time. Example:
```python
n = 5
count = n
while count >= 0:
    print(count)
    count -= 1
```
This prints numbers from 5 down to 0.

-----

### 🖥️ Main Statement

**Story:**
Write a program that counts down from the number entered by the user to 1, using a `while` loop.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 100$).

**Output:**
Print numbers from $n$ down to 1, each on a new line.

**Constraints:**
- $1 \leq n \leq 100$

**Sample Tests:**
Input:
```
3
```
Output:
```
3
2
1
```

Input:
```
1
```
Output:
```
1
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: use a while loop to count down from n to 1

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
