### Task ID: UA1003
### Task Title: Double the Number

-----

### 📚 Quick Lesson

**Concept:**
To read a number from the user, use `input()`. To do math, you must convert the input to an integer using `int()`. You can then multiply or add numbers as needed.

**Example:**
If the user types `5`, you can double it by writing:
```python
number = int(input())
print(number * 2)
```

-----

### 🖥️ Main Statement

**Story:**
Read a single integer from the input. Print double its value.

**Input:**
The first line contains an integer $N$.

**Output:**
Print $2 \times N$ on a single line.

**Constraints:**
$1 \leq N \leq 100$

## **Sample Tests:** 
| Input | Output | 
|---|---|
| 5 | 10 |
| 42 | 84 |

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# Step 1: Read an integer from input and store it in variable N
N = # TODO: fill in the code to read an integer

# Step 2: Calculate double the value and store in variable result
result = # TODO: fill in the code to double N

# Step 3: Print the result
print(result)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
