# 8. Write a python function that takes a list and return a new list with distinct elements from the first list

def distinct(lista):
    result = []
    result.append(lista[0])

    for i in range(1,len(lista)):
        if(lista[i] not in result):
            result.append(lista[i])
    
    return result


print(distinct([1,2,3,4,4,4,5,6,7]))