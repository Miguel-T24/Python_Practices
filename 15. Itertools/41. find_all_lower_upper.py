# 41. Write a python program to find all lower andupper mixed case comibinations f a given string

from itertools import combinations

str1 = 'abc'
l_str = len(str1)
str1 += "".join([x.lower() if x.isupper() else x.upper() for x in str1])
print(str1)
str2 = list(combinations(str1,l_str))

r = []
for i in str2:
    r.append("".join(i))
print(r)