### Task ID: UA1018P
### Task Title: Seconds to Time (h:m:s)

-----

### 📚 Quick Lesson

**Concept:**
To convert seconds into hours, minutes, and seconds:

$$
\text{hours} = \left\lfloor \frac{\text{seconds}}{3600} \right\rfloor \\
\text{minutes} = \left\lfloor \frac{\text{seconds} \bmod 3600}{60} \right\rfloor \\
\text{seconds} = \text{seconds} \bmod 60
$$

-----

### 🖥️ Main Statement

**Story:**
You are given a number of seconds. Convert it to hours, minutes, and seconds, and print them separated by colons.

**Input:**
The first line contains an integer $n$ ($0 \leq n \leq 100000$), the number of seconds.

**Output:**
Print the time in the format: `<hours>:<minutes>:<seconds>`

**Constraints:**
- $0 \leq n \leq 100000$

**Sample Tests:**
Input:
```
3661
```
Output:
```
1:1:1
```

Input:
```
59
```
Output:
```
0:0:59
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# Step 1: Read the number of seconds
n = # TODO: read n with input()

# Step 2: Calculate hours, minutes, seconds
# TODO: calculate h, m, s

# Step 3: Print in h:m:s format
print(# TODO: print result)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
