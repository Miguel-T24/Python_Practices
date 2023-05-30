# 261. Write a python program to move the specified number of elements to the end of the given list

from collections import deque

def move_end(l,n):
    l = deque(l)
    if(n<1):
        return list(l)
    else:
        l.rotate(-n)
    return list(l)
print([4, 5, 6, 7, 8, 1, 2, 3])
print(move_end([4, 5, 6, 7, 8, 1, 2, 3],2))

print([1, 2, 3, 4, 5, 6, 7, 8])
print(move_end([1, 2, 3, 4, 5, 6, 7, 8],-3))
print(move_end([1, 2, 3, 4, 5, 6, 7, 8],-0))

print([8, 1, 2, 3, 4, 5, 6, 7])
print(move_end([8, 1, 2, 3, 4, 5, 6, 7],2))