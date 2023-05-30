# 278. Write a python program to sum the missing numbers in a given lists of integers

ef test(nums):
    max_num = max(nums)
    min_num = min(nums)
    return (max_num+min_num)*(max_num-min_num+1)//2 - sum(nums)
    
nums = [0, 3, 4, 7, 9]
print("Original list:")
print(nums)