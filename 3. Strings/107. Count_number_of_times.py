# 1077. Write a ptyhon prohram that takes two string. Count the number of times each string contains the same three letters at the same index

def test(text1, text2):
           ctr = 0
           for i in range(len(text1) - 2):
                       if text1[i:i+3] == text2[i:i+3]:
                                   ctr += 1
           return ctr
text1 ="Red"
text2 ="RedGreen"
print("Original strings:", text1,text2)
print("Check said two strings contain three letters at the same index:")
print(test(text1, text2))