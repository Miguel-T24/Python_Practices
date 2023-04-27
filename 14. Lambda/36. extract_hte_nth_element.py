# 36. Write a python to extract the nth element form a given list of tuples using lambda

def extract_nth(lista,n):
    return list(map(lambda x:x[n],lista))

students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
print(extract_nth(students, 2))
