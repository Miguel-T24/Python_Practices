# 254. Write a python program to get the weighted average of two or more numbers

l1 = nums1 = [10, 50, 40]
l2 = nums2 = [2, 5, 3]

def sum_av(l1,l2):
    return sum(l1[x]*l2[x] for x in range(len(l1))) / sum(l2)

print(sum_av(l1,l2))

l1 = [82, 90, 76, 83]
l2 = [0.2, 0.35, 0.45, 32]
print(sum_av(l1,l2))