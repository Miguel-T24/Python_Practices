# 3. Write a python progra to display all the memebr names of an enum class ordered by their values

from enum import IntEnum

class Country(IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

print("Country name ordered by country code:")
for data in sorted(Country):
    print("{}".format(data.name))
    
