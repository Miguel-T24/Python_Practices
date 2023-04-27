# 43. Write a python program to crate the multiplication table (from 1 to 10) of a number

num = int(input("Enter number: "))

for i in range(0,11):
    print("{} x {} = {}".format(num,i,num*i))
    