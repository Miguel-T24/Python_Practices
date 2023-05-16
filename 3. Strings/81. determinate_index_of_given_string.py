# 81. Write a python program to determine the index of a given string at which a certain substring starts. If the substring is not found in the given string return 'Not Found'

from re import search

def index_substring(string, substring):
    if (search(substring, string)):
        return search(substring,string).start()
    else:
        return "Not Found"
    
print(index_substring("Python Exercises", "Ex"))