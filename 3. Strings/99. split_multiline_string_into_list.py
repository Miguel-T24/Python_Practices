# 99. Write a python program to split a multi-line string into a list of lines

string = """This
is a
multiline
string"""

result = string.split("\n")

print("Original:\n{}".format(string))
print("Result:\n{}".format(result))
