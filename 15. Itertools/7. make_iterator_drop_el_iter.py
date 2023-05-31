# 7. Write a python program to make an iterator that drops elements from the iterable as ,ong as the elements are negative, aftterwards, it returns every elements

# way 1
l = [-1, -2, -3, 4, -10, 2, 0, 5, 12]
lr=[]
for i in l:
    if(i>0):
        break
    lr.append(i)

print(l)
print(lr)


from itertools import takewhile

nums = [-1,-2,-3,4,-10,2,0,5,12]
print(nums)
print(list(takewhile(lambda x:x<0,nums)))