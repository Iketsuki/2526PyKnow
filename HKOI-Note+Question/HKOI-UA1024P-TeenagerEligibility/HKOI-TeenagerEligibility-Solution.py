import time
# Start the timer (for debug only)
start_time = time.time()
####START YOUR WORK HERE####

a = int(input())
e = input()  # 'True' or 'False'
if 13 <= a <= 19 and e == 'True':
    print('Teenager and eligible')
else:
    print('Not both')

####END YOUR WORK HERE####
# Stop the timer and print duration (for debug only)
end_time = time.time()
# print(f"Debug: Time taken: {end_time - start_time} seconds")
