# 57. Write a python program to get the execution time of a python method

import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1, n+1):
        s  = s + i 
    end_time = time.time()

    return s , end_time - start_time

print("Time to sum 1 to 5 and required time to calculate is {}".format(sum_of_n_numbers(5)))