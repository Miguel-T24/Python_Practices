# 39. Write a python program to get the index of the first element that is greater than specified element usng the itertools module

# way 1 : without itertools
l = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]
# greater than 73
r = next(filter(lambda x:x>73,l),None)
print(l.index(r))

# way 2 : with itertools
from itertools import takewhile
def first_index(l1, n):
    return len(list(takewhile(lambda x: x[1] <= n, enumerate(l1))))


nums = [12,45,23,67,78,90,100,76,38,62,73,29,83]
print("Original list:")
print(nums)
n = 73
print("\nIndex of the first element which is greater than",n,"in the said list:")
print(first_index(nums,n))