# 1. Write a python program to crate an Enum Object and display a member name and value

from enum import Enum
class Country (Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

print("Member Name: {}".format(Country.Albania.name))
print("Member Value: {}".format(Country.Albania.value))

