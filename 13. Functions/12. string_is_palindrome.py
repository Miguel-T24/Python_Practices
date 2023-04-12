# 12. Write a python function that checks whether a passed string is a palindrome or not

def palindrome(string):
    return (string == string[-1::-1])

print(palindrome("ana"))
print(palindrome("hola"))