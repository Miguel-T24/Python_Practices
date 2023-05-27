# 204. Write a python program to check if the first digit or character of each elemetn is a list is the same

def check_first_char_same(l):
    return len(set((map(lambda x:str(x)[0],l)))) == 1

l = [1234, 122, 1984, 19372, 100]
print(check_first_char_same(l))
l = ['aabc', 'abc', 'ab', 'a']
print(check_first_char_same(l))
l = ['aabc', 'abc', 'ab', 'ha']
print(check_first_char_same(l))