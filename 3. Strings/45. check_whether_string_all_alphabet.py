# 46. Write a python program to check whether a string contains all letter of the alphabet

def if_all_alphabet(string):
    set_string = set(filter(lambda x:x.isalpha(), string))
    set_string = set(map(lambda x:x.lower(), set_string))
    
    return len(set_string) == 26

print(if_all_alphabet('The quick brown fox jumps over the lazy dog'))
print(if_all_alphabet('The quick brown fox jumps over the lazy cat'))