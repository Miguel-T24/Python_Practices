# 6. Write a python script to generate and print a dictionary that contanis a number (between 1 and n) in the form (x, x*x)


def generateN(n):
    dic = {}
    for i in range(1,n+1):
        dic[i] = i*i
    return dic


print(generateN(5))
