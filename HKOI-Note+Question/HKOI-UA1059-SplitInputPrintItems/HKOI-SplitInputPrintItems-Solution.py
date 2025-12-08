import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
arr = input().split()
for i in range(len(arr)):
    print(arr[i])
# Alternative:
# for x in arr:
#     print(x)
print(len(arr))

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
