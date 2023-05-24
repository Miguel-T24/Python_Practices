# 153. Write a python program to check if a given element occurs at least n times in a list

lista = [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]

def check_el_at_least(lista,el,occ):
    return lista.count(el)>occ-1

print("3 occurs at least 4 times? {}".format(lista.count(3)>4-1))
print("3 occurs at least 4 times? {}".format(check_el_at_least(lista,0,5)))
print("3 occurs at least 4 times? {}".format(check_el_at_least(lista,8,3)))
