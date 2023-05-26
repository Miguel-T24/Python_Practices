# 9. Write a python fucntion to find the maximum sum sub-sequence in a list. Return Subsequence

def max_sum_subsequence(arr):
    n = len(arr)
    dp = [0 for i in range(n)]
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(arr[i], dp[i-1] + arr[i])
    return max(dp)

nums =  [1,2,3]
print("Original lists:")
print(nums)