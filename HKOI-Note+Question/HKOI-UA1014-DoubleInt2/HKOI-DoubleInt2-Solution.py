# UA1014 - Double the Integer
# Solution

import time
start_time = time.time()

# Step 1: Read an integer from input
x = int(input())

# Step 2: Double the value
result = x * 2

# Step 3: Print in the format x*2=y
print(str(x) + "*2=" + str(result))

end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
