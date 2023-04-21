string = "hola mundo"
print("mun" in string)

def check_substring(lista, substring):
    for i in substring:
        if(i not in lista):
            return False
    return True

lista1 = [1,2,3,4,5]
print(check_substring(lista1,[2,3]))
print(check_substring(lista1,[2,7]))