# 21. Write a python program to print the alphabet pattern 'L'

for i in range(7):
    for j in range(5):
        if(i!=6):
            print("*")
            break
        else:
            print("*",end="")
print()