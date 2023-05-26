# 5. Write a python function to find the kth largest elemtn in a list

def kth_largest_el(lst, k):
    lst.sort(reverse=True)
    return lst[k-1]

nums = [1,2,4,3,5,4,6,9,2,1]
print("Original list:")
print(nums)
k = 1
for i in range(1, 11):
    print("kth largest element in the said list, when k = ",k)
    print(kth_largest_el(nums, k))
    k=k+1