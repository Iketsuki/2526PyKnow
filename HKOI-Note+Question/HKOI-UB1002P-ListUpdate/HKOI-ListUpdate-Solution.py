# UB1002P - List Update (1-based)
# Solution

import time
start_time = time.time()

# Step 1: Read n
n = int(input())

# Step 2: Read n numbers into a list
lst = []
for _ in range(n):
    lst.append(int(input()))

# Step 3: Read i and v
i = int(input())
v = int(input())

# Step 4: Update the i-th element (1-based)
lst[i-1] = v

# Step 5: Print the updated list
for x in lst:
    print(x)

end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
