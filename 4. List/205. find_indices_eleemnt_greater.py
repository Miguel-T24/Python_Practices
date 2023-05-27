# 205. wirte a python program to find the indices of elements in a given lists that are greater than a specified value


def indices_greater_than(l,g):
    return  list(filter(lambda x:l[x]>g,range(len(l))))

l = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
print("Indices Greater Than 3000:\n{}".format(indices_greater_than(l,3000)))
l = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
print("Indices Greater Than 2000:\n{}".format(indices_greater_than(l,20000)))

