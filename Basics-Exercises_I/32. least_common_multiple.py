# 32. write a python program to find the least common multiple of two positive integers

def lcm(n1,n2):
    if(n1 > n2):
        z = n1
    else:
        z = n2
    while(True):
        if( (z % n1 ==0) and (z%n2 ==0)):
            nlcm = z
            break
        z+=1
    return nlcm


print(lcm(4,6))
print(lcm(15,17))