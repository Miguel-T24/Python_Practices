# 233. Write a Python program to chunk a given list into n smaller lists.

from math import ceil

def chunk_list_into_n(nums, n):
  size = ceil(len(nums) / n)
  return list(
    map(lambda x: nums[x * size:x * size + size],
    list(range(n)))
  )
print(chunk_list_into_n([1, 2, 3, 4, 5, 6, 7], 4))  