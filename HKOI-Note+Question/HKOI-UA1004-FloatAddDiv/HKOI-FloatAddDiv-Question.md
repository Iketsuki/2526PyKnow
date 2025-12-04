### Task ID: UA1004
### Task Title: Add and Divide (Float)

-----

### 📚 Quick Lesson

**Concept:**
To read a decimal number (float), use `float(input())`. You can do math with floats just like with integers. To show a result, store it in a variable before printing.

**Example:**
If the user types `4.0`, you can add 3 and divide by 2:
```python
number = float(input())
result = (number + 3) / 2
print(result)
```

-----

### 🖥️ Main Statement

**Story:**
Read a single decimal number from the input. Add 3 to it, then divide the sum by 2. Print the result. Store the result in a variable before printing.

**Input:**
The first line contains a decimal number $X$.

**Output:**
Print $(X + 3) / 2$ on a single line.

**Constraints:**
$0.0 \leq X \leq 100.0$

## **Sample Tests:** 
| Input | Output | 
|---|---|
| 4.0 | 3.5 |
| 10.0 | 6.5 |

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# Step 1: Read a decimal number from input and store it in variable 'number'
number = # TODO: fill in the code to read a float

# Step 2: Add 3 to the number and store in 'sum_value'
sum_value = # TODO: fill in the code to add 3

# Step 3: Divide the sum by 2 and store in 'result'
result = # TODO: fill in the code to divide sum_value by 2

# Step 4: Print the result
print(result)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
