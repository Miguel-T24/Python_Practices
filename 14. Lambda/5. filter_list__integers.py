# 5. Write a python program to filter a list of integers

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_odd = list(filter(lambda x : x%2 != 0 , lista))
lista_even = list(filter(lambda x :x%2 ==0,lista))

print("Odd list:",lista_odd)
print("Even list:",lista_even)