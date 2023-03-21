# 133. Write a ptyhon program to calculate the time runs (difference between start and current time of a program)

import time

start = time.time()
input1 = input("Enter: ") 
print(input1)
end = time.time()

print(end - start)