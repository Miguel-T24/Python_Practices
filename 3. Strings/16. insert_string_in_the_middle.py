# 16. Write a python function to insert a string in the middle of a string

def insert_string_middle(middle,word):
    return middle[:2] + word + middle[2:]

print(insert_string_middle('[[]]' , 'Python'))
print(insert_string_middle('{{}}' , 'PHP'))
print(insert_string_middle('<<>>' , 'HTML'))