### Task ID: UA1027P
### Task Title: Ticket Eligibility Checker

-----

### 🖥️ Main Statement

**Story:**
Given age and whether the person has a disabled card, print "Eligible for 2 dollar ticket" if age is 65 or above, or has a disabled card. Otherwise, print "Regular ticket".

**Input:**
The first line contains an integer $a$ ($0 \leq a \leq 120$), the age.
The second line contains a string $d$ (`True` or `False`), whether the person has a disabled card.

**Output:**
Print the ticket type.

**Constraints:**
- $0 \leq a \leq 120$
- $d$ is either `True` or `False`

**Sample Tests:**
Input:
```
70
False
```
Output:
```
Eligible for 2 dollar ticket
```

Input:
```
40
True
```
Output:
```
Eligible for 2 dollar ticket
```

Input:
```
40
False
```
Output:
```
Regular ticket
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

a = int(input())
d = input()  # 'True' or 'False'
# TODO: check eligibility and print ticket type

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
