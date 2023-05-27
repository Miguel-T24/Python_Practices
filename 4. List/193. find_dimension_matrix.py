# 193. Write a python program to find the dimension of a given matrix

def dimension(m):
    return len(m),len(m[0])

print(dimension([[1, 2], [2, 4]]))
print(dimension([[0, 1, 2], [2, 4, 5]]))
print(dimension([[0, 1, 2], [2, 4, 5], [2, 3, 4]]))