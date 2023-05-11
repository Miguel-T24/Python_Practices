# 37. Write a python program to convert snake-case stirng to camel-case string

def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('python_exercises'))