# 11. Write a python program to remove characters that have odd index values in a given string.

string = "Este"
result = ""
for i in range(len(string)):
    if(i%2==0 or i==0):
        result = result + string[i]

print(result)