### Task ID: UA1037P
### Task Title: FizzBuzz Counter

-----

### 🖥️ Main Statement

**Story:**
Write a program that counts from 1 to the number entered by the user.
- If the number is divisible by 3, print "Fizz".
- If the number is divisible by 5, print "Buzz".
- If the number is divisible by both 3 and 5, print "FizzBuzz".
- Otherwise, print the number.

**Input:**
The first line contains an integer $n$ ($1 \leq n \leq 100$).

**Output:**
Print the appropriate string for each number from 1 to $n$, each on a new line.

**Constraints:**
- $1 \leq n \leq 100$

**Sample Tests:**
Input:
```
5
```
Output:
```
1
2
Fizz
4
Buzz
```

Input:
```
15
```
Output:
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

**Starter Code**
Copy the code and edit it if you need.

```python
import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
# TODO: use for loop and if-elif-else to print Fizz, Buzz, FizzBuzz, or the number

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
```
