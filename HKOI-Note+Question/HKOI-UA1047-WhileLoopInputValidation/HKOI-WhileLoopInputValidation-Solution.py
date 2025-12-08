import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

while True:
    n = int(input())
    if 1 <= n <= 100:
        print(f"Accepted: {n}")
        break
    else:
        print("Invalid input. Try again.")

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
