# 3. Write a python function that findas all the permutations of the members of a list

def permutations(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    result = []
    for i in range(len(nums)):
        m = nums[i]
        rem_list = nums[:i] + nums[i+1:]
        for p in permutations(rem_list):
            result.append([m] + p)
    return result

nums = [1,2,3,4]
print("Original list:")
print(nums)