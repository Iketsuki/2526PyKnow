import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

while True:
    n = int(input())
    if 1 <= n <= 100:
        break
    else:
        print("Invalid input. Try again.")

sum_odd = 0
count = 1
while count <= n:
    sum_odd += count
    count += 2
print(sum_odd)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
