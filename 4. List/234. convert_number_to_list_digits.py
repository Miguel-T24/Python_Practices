# 243. Write a python program to convert a given nnumber (integer) to a list of digits



def digitize(n):
    n = list(str(n))
    return list(map(int,n))

print(digitize(123))
print(digitize(1347823))