import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
i = 1
while i * i <= n:
    sq = i * i
    if sq % 4 == 0:
        print("clap")
    else:
        print(sq)
    i += 1

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
