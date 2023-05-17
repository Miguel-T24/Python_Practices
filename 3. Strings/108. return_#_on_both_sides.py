# 108. Write a python program that takes a stirng and reutrn # on both sides of each element, which are not vowels

def test(text):
    return "".join([el, '-' + el + '-'][el not in "AEIOUaeiou"] for el in text)
text ="Green"
print("Original string:", text)
print("Insert Hash elements on both side of each element, which are not vowels:")
print(test(text))