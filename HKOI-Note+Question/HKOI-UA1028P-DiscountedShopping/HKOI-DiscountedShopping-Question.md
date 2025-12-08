### Task ID: UA1028P
### Task Title: Discounted Shopping Decision

-----

### 🖥️ Main Statement

**Story:**
You are shopping for an item. Given the price and discount rate, calculate the final price. If the final price is greater than 500, apply an extra 10% discount and print the new price. Otherwise, print "No extra discount" and the price.

**Input:**
The first line contains a float $p$ ($0 < p \leq 10000$), the item price.
The second line contains an integer $d$ ($0 \leq d < 100$), the discount rate in percent.

**Output:**
If extra discount is applied, print the final price (after both discounts). Otherwise, print "No extra discount" and the price (after the first discount).

**Constraints:**
- $0 < p \leq 10000$
- $0 \leq d < 100$

**Sample Tests:**
Input:
```
800
20
```
Output:
```
576.0
```

Input:
```
400
10
```
Output:
```
No extra discount
360.0
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

p = 
d = int(input())
# TODO: calculate final price, apply extra discount if needed

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
