# 40. Write a python prohram to split a given into specified sized chicks using the itertools module

from itertools import islice
def split_list(lst, n):
    lst = iter(lst)
    result = iter(lambda: tuple(islice(lst, n)), ())
    return list(result)

nums = [12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
print("Original list:")
print(nums)
n = 3
print("\nSplit the said list into equal size",n)
print(split_list(nums,n))