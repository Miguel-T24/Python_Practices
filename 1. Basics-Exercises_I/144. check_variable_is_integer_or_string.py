# 144. Write a python program to check whether a variable is an integer or 

def check_type(variable):
    return (("No Determinado","String")[isinstance(variable,str)]
        ,"Integer")[isinstance(variable,int)]


print(check_type("Hola mundo"))
print(check_type(50))
print(check_type(12.50))