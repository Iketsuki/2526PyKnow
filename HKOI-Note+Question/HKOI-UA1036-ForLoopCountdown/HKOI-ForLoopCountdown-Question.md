### Task ID: UA1036
### Task Title: Countdown to Happy New Year

-----

### 📚 Quick Lesson

**Concept:**
A `for` loop can count down by using a negative step. Example:
```python
for i in range(5, -1, -1):
    print(i)
```
This prints numbers from 5 down to 0.

-----

### 🖥️ Main Statement

**Story:**
Write a program that counts down from the number entered by the user to 1, then prints "Happy New Year!".

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 100$).

**Output:**
Print numbers from $n$ down to 1, each on a new line. After the countdown, print "Happy New Year!".

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
Happy New Year!
```

Input:
```
1
```
Output:
```
1
Happy New Year!
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: use a for loop to count down from n to 1, then print Happy New Year!

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
