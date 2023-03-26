# 7. Write a python program that prints each item and its corresponding type from the following list

from pprint import pprint

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for i in datalist:
    pprint("Data : {} , Type : {}".format(i,type(i)))
    
pprint(datalist)