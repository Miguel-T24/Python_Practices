# 112. Write a pythn program to calculate the sum of two numbers given as string. Return the result in the same string representation

def sum_two_num(n1,n2):
    if(n1=="" or n2 ==""):
        return "Error!!!"
    else:
        return str(int(n1) + int(n2))

print(sum_two_num("234242342341", "2432342342"))
print(sum_two_num("", "2432342342"))
print(sum_two_num("1000", "0"))
print(sum_two_num("1000", "10"))