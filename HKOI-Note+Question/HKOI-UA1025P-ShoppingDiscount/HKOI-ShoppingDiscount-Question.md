### Task ID: UA1025P
### Task Title: Shopping Discount Detector

-----

### 📚 Quick Lesson

**Concept:**
To calculate a discounted price:
- Discounted price = price × (1 - discount_rate / 100)

Example:
```python
price = 200
rate = 20
final = price * (1 - rate / 100)
print(final)  # 160.0
```

-----

### 🖥️ Main Statement

**Story:**
You are shopping for an item. Given the price and discount rate, calculate the final price. If the final price is greater than 100, print "Expensive". Otherwise, print "Affordable".

**Input:**
The first line contains a float $p$ ($0 < p \leq 10000$), the item price.
The second line contains an integer $d$ ($0 \leq d < 100$), the discount rate in percent.

**Output:**
Print the final price (as a float), then on the next line print either "Expensive" or "Affordable".

**Constraints:**
- $0 < p \leq 10000$
- $0 \leq d < 100$

**Sample Tests:**
Input:
```
200
20
```
Output:
```
160.0
Expensive
```

Input:
```
80
10
```
Output:
```
72.0
Affordable
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

p = float(input())
d = int(input())
# TODO: calculate final price and print affordability

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
