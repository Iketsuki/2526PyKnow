### Task ID: UA1041
### Task Title: While Loop HelloWorld

-----

### 📚 Quick Lesson

**Concept:**
A `while` loop repeats code as long as a condition is true. Example:
```python
count = 1
while count <= 5:
    print("Hello World")
    count += 1
```
This prints "Hello World" five times.

-----

### 🖥️ Main Statement

**Story:**
Write a program that prints "Hello World" $n$ times, using a `while` loop.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 100$).

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

Input:
```
1
```
Output:
```
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
# TODO: use a while loop to print "Hello World" n times

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
