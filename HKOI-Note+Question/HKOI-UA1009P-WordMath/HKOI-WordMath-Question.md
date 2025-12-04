### Task ID: UA1009P
### Task Title: Word Problem — Math Operators

-----

| Symbol | Operation         | Example      |
|--------|-------------------|--------------|
| +      | Addition          | 3 + 2 = 5    |
| -      | Subtraction       | 7 - 4 = 3    |
| *      | Multiplication    | 6 * 2 = 12   |
| /      | Division          | 8 / 2 = 4.0  |
| //     | Integer Division  | 7 // 3 = 2   |
| %      | Modulo (Remainder)| 7 % 3 = 1    |
| **     | Exponentiation    | 2 ** 3 = 8   |

-----

### 🖥️ Main Statement

**Story:**
Amy has $A$ apples. She gives $B$ apples to her friend. She then buys $C$ more apples. How many apples does Amy have now?

**Input:**
The first line contains an integer $A$ (initial apples).
The second line contains an integer $B$ (apples given away).
The third line contains an integer $C$ (apples bought).

**Output:**
Print the number of apples Amy has at the end.

**Constraints:**
$0 \leq B \leq A \leq 100$
$0 \leq C \leq 100$

## **Sample Tests:**
Input:
```
10
3
5
```
Output:
```
12
```

Input:
```
20
5
0
```
Output:
```
15
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

A = # TODO: read initial apples
B = # TODO: read apples given away
C = # TODO: read apples bought

# TODO: calculate final apples
final_apples = # TODO: fill in the math

print(final_apples)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
