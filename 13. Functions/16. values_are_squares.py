# 16. Write a python function to create and print a list wherhe the values are the squares of numbers between 1 and 30

def printValues():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	print(l)
		
printValues()