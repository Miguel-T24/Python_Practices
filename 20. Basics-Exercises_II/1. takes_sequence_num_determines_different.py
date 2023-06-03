# 1. Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

l = [1,5,7,9]
l1 = [2,4,5,5,7,9]
def test(l):
    for i in l:
        if(l.count(i)>1):
            return False
    return True
    
print(test(l)) # True
print(test(l1)) # False
