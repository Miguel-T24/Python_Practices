# 53. Write a python program to find the first repeat character in a given string

def first_chat_repeat(string):
    for i in string:
        if(string.count(i) > 1):
            return i
    return None

print(first_chat_repeat("abcdabcd"))
print(first_chat_repeat("abcd"))