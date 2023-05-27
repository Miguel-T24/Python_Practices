# 200. Write a python program to pair consecutive elements of a given list

l = [1, 2, 3, 4, 5, 6]

r = [[l[x],l[x+1]] for x in range(len(l)-1)]

print(r)