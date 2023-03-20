# 22. Write a python program to count the number 4 in a given list

def count_4(nums):
    count = 0
    for i in nums:
        if i == 4: 
            count += 1
    print("the number 4 appears {} times".format(count))

count_4([1,2,3,4])
count_4([1,4,3,4])
count_4([4,4,3,4])

