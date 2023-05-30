# 276. Write a python program to find the largest oddd number in a given lists of integers

l = [0, 9, 2, 4, 5, 6]
l.sort(reverse=True)
print(l)
r = next(filter(lambda x:x%2==1,l))
print(r)