# 48. Write a ptyhon program to swap commas and dots in a string

string = "32.054,23"
print("Original:",string)
string = list(string)
for i in range(len(string)):
    if(string[i]=="."):
        string[i] = ","
    elif(string[i]==","):
        string[i]="."
string = "".join(string)
print("Swap:",string)

# second way and more easy
string = "32.054,23"
print("Original:",string)
string = string.translate(str.maketrans(",.",".,"))
print("Swap 2:",string)