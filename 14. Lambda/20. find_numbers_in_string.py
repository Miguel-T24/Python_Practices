# 20. Write a python programto find the numbers in a given string and store them in a list

string = 'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
string = string.split(" ")

result = sorted(list(filter(lambda x:(x.isnumeric() and len(x)>1), string)))

print(" ".join(result))