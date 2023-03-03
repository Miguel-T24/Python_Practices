# 33. Write a python program to sum three given integers. However, if two values are equal, the sum will be zero

def suma(n1,n2,n3):
    if n1 == n2 or n2==n3 or n1 == n3:
        return 0
    else:
        return n1 + n2
    
print(suma(2,2,2))
print(suma(10,2,5))