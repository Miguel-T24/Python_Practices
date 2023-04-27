# 32. Write a python program to check whether a given stirng contains a capital letter, a lower case letter, a number and minimum lenggth usign lambda

def check_string(str1):
    messg = [
    lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case character.',
    lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case character.',
    lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',
    lambda str1: len(str1) >= 7                 or 'String length should be atleast 8.',]
    result = [x for x in [i(str1) for i in messg] if x != True]
    if not result:
        result.append('Valid string.')
    return result    
s = input("Input the string: ")
print(check_string(s))