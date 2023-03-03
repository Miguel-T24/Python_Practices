# 34. Write a python program to sum two given integers. however, if the sum is between 15 and 20 it will return 20.

def suma(n1,n2):
    if (n1+n2) >= 15 and (n1+n2) <= 20:
        return 20
    else:
        return n1+n2
    
print(suma(15,3))
print(suma(20,20))