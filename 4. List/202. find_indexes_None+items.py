# 202. Write a python program to find the indexes of all None items in a given list

l = [1, None, 5, 4, None, 0, None, None]

# way 1 list comprenhension
r = [x for x in range(len(l)) if l[x]==None]
print(r)

# way 2 map
r = list(filter(lambda x:l[x]==None,range(len(l))))
print(r)