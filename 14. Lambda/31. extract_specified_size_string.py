# 31. Write a ptyhon program to extract a specified size of strings from a given list of string values usgin lambda

def extract_specific_length(string,l):
    return (l,list(filter(lambda x:len(x) == l , string)))

leng , lista = extract_specific_length(['Python', 'list', 'exercises', 'practice', 'solution'], 8)

print("Length: {} , List : {}".format(leng,lista))