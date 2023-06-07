# 33. Write a python program to compute the digit number of the sum of two given integers

def compute_sum_digit(n1,n2):
    return len(str(n1+n2))

print(compute_sum_digit(6,8))
print(compute_sum_digit(7,3))
print(compute_sum_digit(5,4))