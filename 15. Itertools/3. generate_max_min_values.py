# 3. Write a python to generate the maximum and minimum values of the elements of an iterable

from itertools import accumulate

def running_max_product(iters):
    return accumulate(iters, max)
#List
result = running_max_product([1,3,2,7,9,8,10,11,12,14,11,12,7])
print("Running maximum value of a list:")
for i in result:
    print(i)