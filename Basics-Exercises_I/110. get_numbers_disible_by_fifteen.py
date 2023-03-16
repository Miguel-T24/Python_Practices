# 110. Write a python program to get numbers divisible by fifteen from a list using an anonymous function

num_list = num_list = [45, 55, 60, 37, 100, 105, 220]

func_lambda = filter(lambda x : (x%15 ==0) , num_list)
print(func_lambda)


lista = list(func_lambda)
print(lista)