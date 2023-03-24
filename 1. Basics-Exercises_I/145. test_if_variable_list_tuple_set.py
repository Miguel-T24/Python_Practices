# 145. Write a python program to test if a variable is a list tuple or set

def check_list_tuple_set(var):
    if(isinstance(var,list)):
        return "Is List"
    if(isinstance(var,tuple)):
        return "Is a Tuple"
    if(isinstance(var,set)):
        return "Is Set"
    
print(check_list_tuple_set([1,2,3]))
print(check_list_tuple_set((1,2,3)))
print(check_list_tuple_set({1,2,3}))