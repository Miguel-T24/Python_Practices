# 207. Write a python program to find the common tuples between two given lists

l1 = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
l2 = [('red', 'green'), ('orange', 'pink')]

l = l1 if len(l1)<len(l2) else l2
g = l1 if len(l1)>len(l2) else l2

r = list(filter(lambda x:x in g,l))
print(r)