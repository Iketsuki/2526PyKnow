### Task ID: UA1017P
### Task Title: Trapezium Area Calculation

-----

### 📚 Quick Lesson

**Concept:**
The area $A$ of a trapezium (trapezoid) with parallel sides of lengths $a$ and $b$, and height $h$, is given by:

$$
A = \frac{1}{2} (a + b) \times h
$$

-----

### 🖥️ Main Statement

**Story:**
You want to find the area of a trapezium. Read the values for $a$, $b$, and $h$ from the user (in that order, one per line). Then, calculate and print the area.

**Input:**
The first line contains the length of the first parallel side $a$ (a real number).
The second line contains the length of the second parallel side $b$ (a real number).
The third line contains the height $h$ (a real number).

**Output:**
Print: `The area of the trapezium is <area>`

**Constraints:**
- $0 < a \leq 1000$
- $0 < b \leq 1000$
- $0 < h \leq 1000$

**Sample Tests:**
Input:
```
10
6
5
```
Output:
```
The area of the trapezium is 40.0
```

Input:
```
3.5
2.5
4
```
Output:
```
The area of the trapezium is 12.0
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

# Step 1: Read the first parallel side
a = # TODO: read a with input()

# Step 2: Read the second parallel side
b = # TODO: read b with input()

# Step 3: Read the height
h = # TODO: read h with input()

# Step 4: Calculate the area
area = # TODO: calculate area

# Step 5: Print the area
print(# TODO: print area)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
