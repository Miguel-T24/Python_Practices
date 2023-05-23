# 137. Write a python program to find the firts even and odd number in a given list of numbers

list1 =[1, 3, 5, 7, 4, 1, 6, 8]

e_active = 0
o_active = 0
even = 0
odd = 0

for i in list1:
    if(i%2==0):
        if(even==0):
            even = i
            e_active = 1
    else:
        if(odd==0):
            odd = i
            o_active = 1
    if(e_active == 1 and o_active==1):break

print("Even: {}\nOdd: {}".format(even,odd))

