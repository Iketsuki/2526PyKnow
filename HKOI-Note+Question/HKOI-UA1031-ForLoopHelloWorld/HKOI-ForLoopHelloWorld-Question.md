### Task ID: UA1031
### Task Title: Hello World Looper

-----

### 📚 Quick Lesson

**Concept:**
A `for` loop lets you repeat actions a set number of times. Example:
```python
for i in range(5):
    print("Hello World")
```
This prints "Hello World" five times.

-----

### 🖥️ Main Statement

**Story:**
Write a program that prints "Hello World" a number of times specified by the user.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 100$), the number of times to print.

**Output:**
Print "Hello World" $n$ times, each on a new line.

**Constraints:**
- $1 \leq n \leq 100$

**Sample Tests:**
Input:
```
3
```
Output:
```
Hello World
Hello World
Hello World
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: use a for loop to print Hello World n times

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
