# 35 write a python program that returns true if the two given integers values are equal or their sum of difference is 5

def checkInt(n1,n2):
    if n1 == n2 or n1 + n2 == 5 or n1-n2 ==5:
        return True
    else:
        return False
    

print(checkInt(5,5))
print(checkInt(2,3))
print(checkInt(6,1))
print(checkInt(20,30))