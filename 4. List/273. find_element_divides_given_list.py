# 273. Write a Python program to find an element that divides a given list of integers with the same sum value.

def test(nums):
	for i, x in enumerate(nums[1:-1]):
		if sum(nums[:i+1]) == sum(nums[i+2:]):
			return nums[i+1]
	return "No such element!"
nums = [0, 9, 2, 4, 5, 6]
print("Original list:")
print(nums)
print("Element that devides the said list of integers with the same sum value:\n", test(nums))