# 186. Write a python prohgram to convert a given list of tuples to a list of string

lt = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]

result = list(map(lambda x:" ".join(x),lt))

print(result)