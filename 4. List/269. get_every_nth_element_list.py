# 269. Write a python program to get every nth element in a given lists

def nth_elements(l,r=1):
    res = []
    for i in range(r-1,len(l),r):
        res.append(l[i])
    return res

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(l)
print(nth_elements(l,2))
print(nth_elements(l,5))
print(nth_elements(l,6))