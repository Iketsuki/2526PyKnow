### Task ID: UA1029P
### Task Title: Bus Fare Calculator

-----

### 🖥️ Main Statement

**Story:**
Given age and distance, calculate the bus fare using the following rules:
- If age < 12, fare = distance × 0.5
- If age >= 65, fare = distance × 0.7
- Otherwise, fare = distance × 1.0
Print the fare.

**Input:**
The first line contains an integer $a$ ($0 \leq a \leq 120$), the age.
The second line contains a float $d$ ($0 < d \leq 100$), the distance in km.

**Output:**
Print the fare (as a float).

**Constraints:**
- $0 \leq a \leq 120$
- $0 < d \leq 100$

**Sample Tests:**
Input:
```
10
5
```
Output:
```
2.5
```

Input:
```
70
10
```
Output:
```
7.0
```

Input:
```
30
8
```
Output:
```
8.0
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

a = int(input())
d = 
# TODO: calculate fare using branching

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
