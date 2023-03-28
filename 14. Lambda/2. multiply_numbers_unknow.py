# 2. Write a python rogram to create a function that takes one argument, and that argument will be mulitplied with an unkhown given number



def func_compute(n):
    return lambda x : x *n

result = func_compute(2)
print(result(15))