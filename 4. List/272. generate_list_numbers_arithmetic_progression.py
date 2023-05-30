# 272. Write a python program to generate a list of numebrs in the arithmetic progression stratting with the given positive integer and up to the specified limit

def progression(start,limit,prog):
    if(start<1):
        return "Invalid"
    r = []
    for i in range(start,limit+1,prog):
        r.append(i)
    return r

print(progression(1,15,1))
print(progression(3,36,3))
print(progression(5,25,5))
