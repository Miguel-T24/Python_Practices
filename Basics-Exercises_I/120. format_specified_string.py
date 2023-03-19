# 120. Write a python program to format specified string and limit the length of a string

string = '1234567890'

print("Original String:", string)
print("%.6s" %string)
print("%.9s" %string)
print("%.10s" %string)

print("\n")

print("{:.6}".format(string))
print("{}".format(string[0:6]))


