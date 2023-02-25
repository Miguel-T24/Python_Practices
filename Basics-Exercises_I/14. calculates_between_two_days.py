# 14. Write a python program to calculate the number of days between two dates

from datetime import date

result  = (date(2014,7,11) - date(2014,7,2)).days
print("between 2/7/2014 and 11/7/2014 are {} days".format(result))