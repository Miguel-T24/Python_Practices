# 13. Write a python program that matches a word containing 'z', not the start or end of the word

from re import search

def test(string):
    return bool(search("\w+z\w+",string))

print(test("El zorro salio corriendo")) # False
print(test("Voy a Cazar animales")) # True
print(test("Hola mundo")) # False