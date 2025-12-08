import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

n = int(input())
arr = input().split()
sum_score = 0
for i in range(len(arr)):
    sum_score += int(arr[i])
avg = sum_score / len(arr)
print(avg)

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
