# 13. Write a python program that accepts a sequence of comma separeted 4 digit binary numbers as its input. The program will print the numbers that are divisible by 5 in a comma separated

digits = ' 0100,0011,1010,1001,1100,1001'
digits = digits.split(",")

for i in digits:
    if(int(i,2)%5==0):
        print(i);break

