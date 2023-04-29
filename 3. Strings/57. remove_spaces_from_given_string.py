# 57. Wrte a python program to remove spaces from a gicen string

def remove_spaces(string):
    string = string.split(" ")
    return "".join(string).strip()
string = "    Hola mundo como estan    "

print("Function:",remove_spaces(string))
print("Original:",string)
print("rstrip:",string.rstrip()+"!")
print("strip:",string.strip()+"!")
print("Replace:",string.replace(" ",""))