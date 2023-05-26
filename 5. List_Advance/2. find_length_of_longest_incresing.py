# 2. Wirte a python function find the length of the longest increasing subsequence in a list

def longest_increasing_subsequence(nums):
    n = len(nums)
    arr = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                arr[i] = max(arr[i], arr[j]+1)
    return max(arr)

nums = [10,20,30,40,50,60,70,80]
print("Original list:")
print(nums)