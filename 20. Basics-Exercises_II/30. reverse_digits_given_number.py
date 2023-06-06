# 30. Write a python program to reverse the digits of a given number and add them to the original. repeat this procedure if the sum is not palindrome

def sum_pal(num):
    num = str(num)
    num_pal = num[::-1]
    r = int(num) + int(num_pal)
    while True:
        if(str(r) == str(r)[::-1]):
            return r
        else:
            r = r + int(str(r)[::-1])
            
print(sum_pal(1234))
print(sum_pal(1473))