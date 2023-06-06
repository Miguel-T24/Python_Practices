# 25. write a python program to find the digits that are missing from a given mobile number

mob_num = [9,8,3,2,2,0,9,7,6,3]
num = [1,2,3,4,5,6,7,8,9,0]
mob_num = set(mob_num)

missing = set(num).difference(mob_num)
print(list(missing))
