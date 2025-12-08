### Task ID: UA1026P
### Task Title: Age Group Classifier

-----

### 🖥️ Main Statement

**Story:**
Given a person's age, print their age group: "Child" (<13), "Teenager" (13–19), "Adult" (20–64), or "Senior" (65+).

**Input:**
The first line contains an integer $a$ ($0 \leq a \leq 120$), the age.

**Output:**
Print the age group.

**Constraints:**
- $0 \leq a \leq 120$

**Sample Tests:**
Input:
```
10
```
Output:
```
Child
```

Input:
```
15
```
Output:
```
Teenager
```

Input:
```
30
```
Output:
```
Adult
```

Input:
```
70
```
Output:
```
Senior
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

a = int(input())
# TODO: print age group using if-elif-else

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
