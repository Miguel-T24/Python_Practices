# 72. Write a python prohgram to remove all character except a specified character from a given string

def remove_char(string, char):
    return "".join(list(filter(lambda x:x==char, string)))

print("Original String: Hola mundo",)
print("Remove all except 'o': {}".format(remove_char("Hola mundo", "o")))
