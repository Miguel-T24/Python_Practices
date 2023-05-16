# 103. Write a python prphram to replace each character of a word of length five and more with a hash character(#).

string = "Count the lowercase letters in the said list of words"

result = " ".join(map(lambda x:(x,'#'*len(x))[len(x)>4], string.split(" ")))
print(result)