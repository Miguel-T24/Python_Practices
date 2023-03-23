# 7, Write a python script to print dictionary where the keys are numbers between 1 and 15 (beth included) and tha values are the square of the keys

dic = {}

for i in range(1,16):
    dic[i] = i * i

print(dic)