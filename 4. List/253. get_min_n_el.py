# 253. Write a python program to get the n minimum elements from a given list of nu,,bers

def min_n_number(l,n):
    l = sorted(l)
    return [l[x] for x in range(n)]

print(min_n_number([1, 2, 3],1))
print(min_n_number([1, 2, 3],2))
print(min_n_number([-2, -3, -1, -2, -4, 0, -5],3))