# 39. write a python program to compute the future value of the specified principal amount, rate of interest, and number of years

amount = 10000
int = 3.5
years = 7

future_value = amount * ( (1+(0.01*int))** years)
print(type(future_value))
print("{:.4f}".format(future_value))