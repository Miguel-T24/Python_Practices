# 5. Write a python program to get a single string from two given strings, separated by space and swap the first twot character of each string

def function_string(str1, str2):
    return str2[0:-1] + str1[-1] + " " + str1[0:-1] + str2[-1]

print(function_string("abc" , "xyz"))

