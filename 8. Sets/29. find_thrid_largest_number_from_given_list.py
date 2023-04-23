# 29. Write a python program to find the thrid largest number from given list of number. use the python set data tuype

def third_largest(nums):
    nums = set(nums)
    if len(nums) < 3:
        return None
    nums = list(nums)
    nums.sort(reverse=True)
    return nums[2]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list of numbers:")
print(nums)
print("Third largest number of the said list of numbers:")
print(third_largest(nums))