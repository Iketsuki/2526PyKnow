import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
odd_sum = 0
even_product = 1
has_even = False
for i in range(1, n+1):
    if i % 2 == 1:
        odd_sum += i
    else:
        even_product *= i
        has_even = True
if not has_even:
    even_product = 0
print(odd_sum)
print(even_product)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
