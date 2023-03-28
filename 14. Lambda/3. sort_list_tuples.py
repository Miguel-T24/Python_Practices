# 3. Write a python program to sort a list of tuplesusging lambda

tupla  = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

tupla.sort(key = lambda x:x[1])

print(tupla)