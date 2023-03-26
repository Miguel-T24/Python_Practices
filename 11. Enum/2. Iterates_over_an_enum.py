# 2. Write a python program that iterates over an enum class and displays each memeber and their value

from enum import Enum

class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

for i in Country:
    print("{} = {}".format(i.name, i.value))