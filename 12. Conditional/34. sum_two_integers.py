# 34. Write a python program to sum two integers. However, if the sum is between 15 and 20 it will return 20

def sum_two(a,b):
    return (a+b,20)[a+b>14 and a+b < 21]

print(sum_two(14,2))
print(sum_two(14,7))