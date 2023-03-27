# 5. Write a python function to calculare the facotrial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial(n):
    fact = n
    if(n==0):
        fact = 1
    else:
        for i in range(n,1,-1):
            fact *= (i-1)
    return fact

print(factorial(4))
print(factorial(5))
print(factorial(0))