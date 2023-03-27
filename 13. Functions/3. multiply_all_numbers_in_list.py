# 3. Write a python function to multiply all the numbers in a list

def  multiply_list(lista):
    mul = 1
    for i in lista:
        mul *= i
    return mul

print(multiply_list([8,2,3,-1,7]))