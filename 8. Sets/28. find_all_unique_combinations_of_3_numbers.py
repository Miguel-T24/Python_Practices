# 28. Write a python rprogram to find all the unique combinations of 3 nu,mnbers from a given list of numbers. adding up to a target number

def find_combinations_of_three(nums, target_val):
    nums = list(set(nums))
    result = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            complement = target_val - nums[i] - nums[j]
            if complement in nums[:i] + nums[j+1:]:
                result.add(tuple(sorted((nums[i], nums[j], complement))))
    return list(result)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_val = 12
print("Original list of numbers:")
print(nums)
print("Target value:",target_val)
print("Combine three numbers whose sum equal to a target number:")
print(find_combinations_of_three(nums, target_val))
target_val = 17
print("\nOriginal list of numbers:")
print(nums)
print("Target value:",target_val)
print("Combine three numbers whose sum equal to a target number:")
print(find_combinations_of_three(nums, target_val))