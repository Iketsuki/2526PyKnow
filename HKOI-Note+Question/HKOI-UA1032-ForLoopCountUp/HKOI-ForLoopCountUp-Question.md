### Task ID: UA1032
### Task Title: Computer Learns to Count Up

-----

### 📚 Quick Lesson

**Concept:**
A `for` loop can be used to count up from a starting number to an ending number. Example:
```python
for i in range(1, 6):
    print(i)
```
This prints numbers from 1 to 5.

-----

### 🖥️ Main Statement

**Story:**
Write a program that prints numbers from 1 up to the number entered by the user.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 100$).

**Output:**
Print the numbers from 1 to $n$, each on a new line.

**Constraints:**
- $1 \leq n \leq 100$

**Sample Tests:**
Input:
```
5
```
Output:
```
1
2
3
4
5
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: use a for loop to print numbers from 1 to n

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
