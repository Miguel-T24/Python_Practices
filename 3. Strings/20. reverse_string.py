# 20. Write a python program to reverse a string ifits length is multiple of 4

def reversee(string):
    return (string , string[::-1])[len(string) % 4 == 0]

print(reversee('abcd'))
print(reversee('Python'))
