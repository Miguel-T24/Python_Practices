# 252. Write a python program to get the n maximum elements from a given list of number

def max_val_n(l,n):
    l = sorted(l,reverse=True)
    return [l[x] for x in range(n)]

print(max_val_n([1, 2, 3],1))
print(max_val_n([1, 2, 3],2))
print(max_val_n([-2, -3, -1, -2, -4, 0, -5],3))