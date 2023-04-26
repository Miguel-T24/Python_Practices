# 49. Write a python program to print nested lists (each list on a new line) using the print function

colors = [['Red'], ['Green'], ['Black']]
print("\n".join(list(map(lambda x:str(x),colors))))