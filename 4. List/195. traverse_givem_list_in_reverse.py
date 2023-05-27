# 195. Write a python program to traverse a given list in revers eorder, and rorint the elements with the original index

l = ['red', 'green', 'white', 'black']
enum_l = list(enumerate(l))

for i in range(len(enum_l)-1, -1,-1):
    print(enum_l[i][0],enum_l[i][1])