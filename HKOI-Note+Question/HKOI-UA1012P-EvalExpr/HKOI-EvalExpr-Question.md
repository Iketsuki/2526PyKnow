### Task ID: UA1011P
### Task Title: Evaluate Expression (Real Numbers)

-----

| Symbol | Operation         | Example      |
|--------|-------------------|--------------|
| +      | Addition          | 3 + 2 = 5    |
| -      | Subtraction       | 7 - 4 = 3    |
| *      | Multiplication    | 6 * 2 = 12   |
| /      | Division          | 8 / 2 = 4.0  |
| **     | Exponentiation    | 2 ** 3 = 8   |

-----

### 🖥️ Main Statement

**Story:**
Given a real number $x$, calculate the value of $y$ using the formula:

$$
y = x - \frac{x^2 + 4}{2} + \frac{x^3 - 3x + 7}{3}
$$

Print the value of $y$ rounded to three decimal places.

**Input:**
The first line contains a real number $x$.

**Output:**
Print the value of $y$ rounded to three decimal places.

**Constraints:**
$-100.0 \leq x \leq 100.0$

## **Sample Tests:**
Input:
```
2.0
```
Output:
```
2.667
```

Input:
```
-1.5
```
Output:
```
-2.125
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

x = # TODO: read the real number

# TODO: calculate y using the formula
y = # TODO: fill in the formula

# TODO: print y rounded to three decimal places
print(# TODO: print y rounded to 3 decimal places)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
