# 6. Write a python program to count the number of even and odd numbers in a series of numbers.


numbers = [1,2,3,4,5,6,7,8,9]
counte = 0
counto = 0
for i in numbers:
    if(i % 2 == 0):
        counte += 1
    else:
        counto += 1

print("Even : {} , Odd : {}".format(counte, counto))
