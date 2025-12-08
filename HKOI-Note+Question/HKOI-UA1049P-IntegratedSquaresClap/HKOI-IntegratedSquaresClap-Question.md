### Task ID: UA1049P
### Task Title: Squares and Clap for Multiples of 4

-----

### 📚 Quick Lesson

**Concepts Combined:**
- Generating square numbers with a while loop
- Using if statements for conditional output

-----

### 🖥️ Main Statement

**Story:**
Write a program that prints all square numbers (1, 4, 9, ...) less than or equal to the number entered by the user. If the square number is a multiple of 4, print "clap" instead of the number.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 1000$).

**Output:**
Print all square numbers less than or equal to $n$, each on a new line. If the square number is a multiple of 4, print "clap" instead.

**Constraints:**
- $1 \leq n \leq 1000$

**Sample Tests:**
Input:
```
20
```
Output:
```
1
clap
9
16
```

Input:
```
4
```
Output:
```
1
clap
```

Input:
```
10
```
Output:
```
1
clap
9
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: print squares, "clap" for multiples of 4

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
