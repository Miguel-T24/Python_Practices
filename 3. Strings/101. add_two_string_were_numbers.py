# 101. Write a ptyhon progarm to add two strings as if they were numbers.

def add_two_number(n1,n2):
    if (n1.isdigit() and n2.isdigit() or int(n1)<0 and int(n2)<0):
        return int(n1)+int(n2)
    else:
        return "Error in Input!" 

print(add_two_number("10","32"))
print(add_two_number("10","22.6"))
print(add_two_number("10","-200"))