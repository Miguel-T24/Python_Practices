# 83. Write a python program to prnt four integer values - decimal, octal, hexadecimal (capitalized), binary - in a single line

value = int(input("Enter value: "))

print("Decimal: {}\nOctal: {}\nHexadecimal: {}\nBinary: {}".format(value, oct(value), hex(value), bin(value)))
