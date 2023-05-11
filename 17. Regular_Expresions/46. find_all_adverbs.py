# 46. Write a ptyhon program to find all advebs and their positions in a given sentence


from re import finditer

string = "Clearly, he has no excuse for such behavior."

result = finditer("\w+ly", string)

for i in result:
    print("Start: {}, End:{}, word: {}".format(i.start(),i.end(),i.group()))