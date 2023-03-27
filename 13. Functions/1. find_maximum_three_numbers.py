
# 1. Write a pthon function to find tha maximum of three numebrs

def maximum_three_num(n1,n2,n3):
    result = 0
    if(n1>n2 and n1>n3):
        result = n1
    if(n2>n1 and n2>n3):
        result = n2
    if(n3>n1 and n3>n2):
        result = n3

    return result
print(maximum_three_num(1,2,3))