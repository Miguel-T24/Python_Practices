# 10. Write python program to find the list of words that are longer than n from a given list of words

words = ["Hola" , "Mundo" , "hi" ,"a"]
result = []
for i in words:
    if(len(i) > 2):
        result.append(i)

print(result)
