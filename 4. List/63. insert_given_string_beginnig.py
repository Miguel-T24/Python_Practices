# 63. Write a python program to insert a given string at the beginning of all items in a list

lista = [1,2,3,4]
string = "emp"

result = list(map(lambda x:string+str(x), lista))

print(result)

# second way
print(["emp{}".format(i) for i in lista])