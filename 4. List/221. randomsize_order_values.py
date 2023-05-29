# 221. Write a python program to randomize the order of the values of a list, returning a new list.

from random import choice

def randomaize(l):
    # return list(map(lambda x:l.pop(l.index(choice(l))), range(len(l))))
    return [l.pop(l.index(choice(l))) for i in range(len(l))]

l = [1, 2, 3, 4, 5, 6]
print(l)
print(randomaize(l))
