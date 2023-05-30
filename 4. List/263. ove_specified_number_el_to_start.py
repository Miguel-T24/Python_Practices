# 163. Write a python porgram to move the specified number of elements to the start of the given list

from collections import deque

def move_start(l,n):
    l = deque(l)
    if(n<1):
        return list(l)
    else:
        l.rotate(n)
    return list(l)

print([4, 5, 6, 7, 8, 1, 2, 3])
print(move_start([4, 5, 6, 7, 8, 1, 2, 3],2))
