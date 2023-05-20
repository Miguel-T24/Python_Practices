# 12. Write a python program to count the numebr of times a specific element appears in a deque object

import collections

nums = collections.deque((2,9,0,8,2,4,0,9,2,4,8,2,0,4,2,3,4,0))

print("Number of 2 in the sequence: {}".format(nums.count(2)))
print("Number of 4 in the sequence: {}".format(nums.count(4)))

