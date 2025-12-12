# UB1001P - List Indexing (1-based)
# Solution

import time
start_time = time.time()

# Step 1: Read k
k = int(input())

# Step 2: Read k lines into a list
lst = []
for _ in range(k):
    lst.append(input())

# Step 3: Read i (1-based)
i = int(input())

# Step 4: Print the i-th input (1-based)
print(lst[i-1])

end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
