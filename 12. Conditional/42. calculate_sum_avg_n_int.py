# 42. Write a ptyhon program to calculate the sum and average of n integer numebrs (input from the usar). ionput 0 to finish

num = 0
lista = []
while True:
    num = int(input("Give me a number: "))
    if(num!=0):
        lista.append(num)
    else:
        break

print("the sum of numbers entered is {}".format(sum(lista)))
print("The average of number entered is {}".format(sum(lista)/len(lista)))