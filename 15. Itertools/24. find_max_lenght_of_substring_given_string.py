# 24. write a python program to find the maximum length of a substring in a given string where all the characters of the substring are the same. Use the istertools module to solve the problem

from itertools import groupby

str1 = "aaabbccddeeeee"

str2 = groupby(str1)

r = list(map(lambda x:(x[0],list(x[1])), str2))
print(r)


# r = []
# for i,j in str2:
#     r.append((i,list(j)))

r = max(r,key=lambda x:x[1])
print(r[0] , len(r[1]))