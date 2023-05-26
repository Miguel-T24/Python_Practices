# 6. Write a python function to check if a list is a palindrome or not. Return true otherwiese false

def palindrome(list1):
    return list1==list(list1[::-1])

lista = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]
print("{}\nis Palindrome:\n{}".format(lista,palindrome(lista)))
lista = [1, 2, 2, 1]
print("{}\nis Palindrome:\n{}".format(lista,palindrome(lista)))
lista = ['Red', 'Green', 'Blue']
print("{}\nis Palindrome:\n{}".format(lista,palindrome(lista)))
lista = ['Red', 'Green', 'Red']
print("{}\nis Palindrome:\n{}".format(lista,palindrome(lista)))
