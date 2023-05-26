# 10. Write a Python a function to find the minimum sum sub-sequence in a list. Return the sub-sequence.

def minimum_sum_subsequence(lst):
    min_sum = float('inf')
    start, end = 0, 0
    curr_start, curr_sum = 0, 0
    
    for i in range(len(lst)):
        curr_sum += lst[i]
        if curr_sum < min_sum:
            min_sum = curr_sum
            start = curr_start
            end = i
        if curr_sum > 0:
            curr_sum = 0
            curr_start = i + 1
    
    return lst[start:end+1]



nums =  [1,2,6,12]
print("Original list:")
print(nums)