# 33. write a python program to count float values in a mixed list using lambda

lista = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
result = list(filter(lambda x:isinstance(x,float),lista))
print("Original List: {}\nList of float: {}\nlength: {}".format(lista,result, len(result)))
