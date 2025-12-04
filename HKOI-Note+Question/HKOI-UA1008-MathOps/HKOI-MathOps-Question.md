### Task ID: UA1007
### Task Title: Math Operators (** // %)

-----

### 📚 Quick Lesson

**Concept:**
Python has special math symbols:
- `**` for exponentiation (power)
- `//` for integer division (quotient)
- `%` for modulo (remainder)

**Example:**
```python
number = 5
print(number ** 2)  # Shows: 25
print(number // 2)  # Shows: 2
print(number % 2)   # Shows: 1
```

-----

### 🖥️ Main Statement

**Story:**
Read an integer from input. Print its square, its integer division by 3, and its remainder when divided by 3, each on a new line.

**Input:**
The first line contains an integer $N$.

**Output:**
Print $N^2$, $N // 3$, and $N \% 3$ each on a single line.

**Constraints:**
$0 \leq N \leq 100$

## **Sample Tests:** 
| Input | Output | 
|---|---|
| 5 | 25\n1\n2 |
| 9 | 81\n3\n0 |

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# Step 1: Read an integer from input and store it in variable N
N = # TODO: fill in the code to read an integer

# Step 2: Calculate the square and store in variable square
square = # TODO: fill in the code for N squared

# Step 3: Calculate integer division by 3 and store in variable quotient
quotient = # TODO: fill in the code for N // 3

# Step 4: Calculate remainder when divided by 3 and store in variable remainder
remainder = # TODO: fill in the code for N % 3

# Step 5: Print each result on a new line
print(square)
print(quotient)
print(remainder)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
