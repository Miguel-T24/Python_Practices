# 208. Sum a list of numbers. Write a python program to sum the first numbers with second and divide it by 2, then sum the second with the third and divide by 2, and so on

l = [1, 2, 3, 4, 5, 6, 7]
r = list(map(lambda x:(l[x]+l[x+1])/2, range(len(l)-1)))

print(r)