# 14. Write a python program that accepts a string and caluclates the number of digits and letters 

string = "Python 3.2"
countd = 0
countl = 0

for i in string:
    if i.isdigit():
        countd+=1
    if i.isalpha():
        countl+=1

print("Original String : {}\nNumber of Digits : {}\nNumber of Letter  {}".format(string, countd,countl))

