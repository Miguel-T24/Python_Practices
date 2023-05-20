# 13 .Write a python program to rotate a deque object a specified number (positive) of times

import collections

nums = collections.deque((2,4,6,8,10))
print("Deque Before Rotation: \n{}".format(nums))
nums.rotate(1)
print("Deque after 1 negative rotation\n{}".format(nums))
nums.rotate(2)
print("Deque after 2 positive rotations:\n{}".format(nums))
