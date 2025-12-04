### Task ID: UA1008
### Task Title: Simple Math Problems

-----

### 📚 Quick Lesson

**Concept:**
You can use `+`, `-`, `*`, `/` to do basic math in Python. Each operator does what you expect: add, subtract, multiply, divide.

**Example:**
```python
# Add
print(3 + 2)  # Shows: 5
# Subtract
print(7 - 4)  # Shows: 3
# Multiply
print(6 * 2)  # Shows: 12
# Divide
print(8 / 2)  # Shows: 4.0
```

-----

### 🖥️ Main Statement

**Story:**
Read two numbers from input. Print their sum, difference, product, and quotient (division result) each on a new line.

**Input:**
The first line contains an integer $A$.
The second line contains an integer $B$.

**Output:**
Print $A + B$, $A - B$, $A * B$, and $A / B$ (as a float) each on a single line.

**Constraints:**
$1 \leq A, B \leq 100$

## **Sample Tests:** 
Input:
```
7
3
```
Output:
```
10
4
21
2.3333333333333335
```

Input:
```
12
4
```
Output:
```
16
8
48
3.0
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# Step 1: Read two integers from input and store in A and B
A = # TODO: fill in the code to read first integer
B = # TODO: fill in the code to read second integer

# Step 2: Calculate sum, difference, product, and quotient
sum_value = # TODO: fill in the code for A + B
diff_value = # TODO: fill in the code for A - B
prod_value = # TODO: fill in the code for A * B
quot_value = # TODO: fill in the code for A / B

# Step 3: Print each result on a new line
print(sum_value)
print(diff_value)
print(prod_value)
print(quot_value)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
