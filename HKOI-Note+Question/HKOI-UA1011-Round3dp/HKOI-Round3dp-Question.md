### Task ID: UA1011
### Task Title: Round to Thousandths (3 Decimal Places)

-----

### 📚 Quick Lesson

**Concept:**
To round a number to the nearest thousandth (3 decimal places), use the `round()` function or string formatting. For example:

```python
value = 3.1415926
rounded = round(value, 3)  # rounded is 3.142
print(rounded)

# Or use formatting to always show 3 decimal places:
value = 2.0
print(f"{value:.3f}")  # Shows: 2.000
```

-----

### 🖥️ Main Statement

**Story:**
Read a real number from input. Print its value rounded to the nearest thousandth (3 decimal places).

**Input:**
The first line contains a real number $x$.

**Output:**
Print $x$ rounded to 3 decimal places. Always show 3 digits after the decimal point.

**Constraints:**
$-1000.0 \leq x \leq 1000.0$

## **Sample Tests:**
Input:
```
3.1415926
```
Output:
```
3.142
```

Input:
```
2.0
```
Output:
```
2.000
```

Input:
```
-0.12345
```
Output:
```
-0.123
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# Step 1: Read a real number from input
value = # TODO: fill in the code to read a float

# Step 2: Round the value to 3 decimal places
rounded = # TODO: fill in the code to round value

# Step 3: Print the rounded value with exactly 3 decimal places
print(# TODO: print rounded value with 3 decimal places)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
