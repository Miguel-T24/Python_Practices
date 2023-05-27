# 185. Write a python program to convert a given decimal number to a binary list

decimal = 8
bin_l = list(bin(decimal)[2:])
print("Decimal: {}\nBinary: {}\nBinary list: {}".format(decimal,bin(decimal)[2:],bin_l))
