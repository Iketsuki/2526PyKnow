# UA1011 - Round to Thousandths (3 Decimal Places)
# Solution

import time
start_time = time.time()

# Step 1: Read a real number from input
value = float(input())

# Step 2: Round the value to 3 decimal places
rounded = round(value, 3)

# Step 3: Print the rounded value with exactly 3 decimal places
print(f"{rounded:.3f}")

end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
