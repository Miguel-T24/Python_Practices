# 85. Write a python program to convert a given bytearray to a hexadecimal string

byte_array = [111, 12, 45, 67, 109]

result = "".join(map(lambda x : hex(x), byte_array))
result = result.replace("x","")

print(result)