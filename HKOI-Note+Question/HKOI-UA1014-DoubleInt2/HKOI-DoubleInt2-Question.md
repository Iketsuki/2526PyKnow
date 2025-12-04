### Task ID: UA1014
### Task Title: Double the Integer 2

-----

### 📚 Quick Lesson

**Concept:**
To read an integer from input, use `int()`. To join numbers and text, use `str()` to convert numbers to strings before printing.

```python
# Example: Multiply by 3
x = int(input())
result = x * 3
print(str(x) + "*3=" + str(result))
```

-----

### 🖥️ Main Statement

**Story:**
Read an integer from input. Print the result of doubling it in the format: `x*2=y`.

**Input:**
The first line contains an integer $x$.

**Output:**
Print one line: $x*2=y$, where $y$ is $x$ doubled.

**Sample Tests:**
Input:
```
5
```
Output:
```
5*2=10
```

Input:
```
-7
```
Output:
```
-7*2=-14
```

Input:
```
0
```
Output:
```
0*2=0
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# Step 1: Read an integer from input
x = # TODO: read integer

# Step 2: Double the value
result = # TODO: double x

# Step 3: Print in the format x*2=y
print(# TODO: print x*2=result using str())

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
