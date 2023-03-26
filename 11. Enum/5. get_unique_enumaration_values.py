# 5. Write a python program to get unique enumeration values


from enum import Enum

class Countries(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    India = 355
    USA = 213

for result in Countries:
    print("{:15} = {}".format(result.name,result.value))
    