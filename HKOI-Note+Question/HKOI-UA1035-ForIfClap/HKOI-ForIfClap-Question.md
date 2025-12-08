### Task ID: UA1035
### Task Title: Clap for Multiples of 3

-----

### 📚 Quick Lesson

**Concept:**
You can use an `if` statement inside a `for` loop to change what you print based on a condition. Example:
```python
for i in range(1, 6):
    if i % 2 == 0:
        print("even")
    else:
        print(i)
```
This prints "even" for even numbers and the number itself for odd numbers from 1 to 5.

-----

### 🖥️ Main Statement

**Story:**
Write a program that counts from 1 to the number entered by the user. If the number is divisible by 3, print "clap" instead of the number.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 100$).

**Output:**
Print numbers from 1 to $n$, but print "clap" for numbers divisible by 3.

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
2
clap
4
5
clap
7
```

Input:
```
3
```
Output:
```
1
2
clap
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: use for loop and if to print numbers or "clap"

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
