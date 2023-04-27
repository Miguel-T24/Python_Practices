# 49. Write a python program to count the occurrences of items in a given list using lambda

nums = [3,4,5,8,0,3,8,5,0,3,1,5,2,3,4,2]

result = dict(map(lambda x: (x,list(nums).count(x)) ,nums))
print(result)