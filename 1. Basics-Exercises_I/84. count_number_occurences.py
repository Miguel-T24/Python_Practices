# 84. Write a python program to count the number of cocurrences of a specific character in a string

def counter(string , char):
    count = 0
    for i in string:
        if i == char:
            count +=1
    return count

print("The {} in {} apparence {} times.".format("\"a\"","\"Holaa Mundo\"",counter("Holaa Mundo" , "a")))



# Best Solution, and simple

character = "a"
print("The {} in {} apparence {} times".format("\"a\"" , "\"Holaa Mundo\"" , "Holaa Mundo".count("a")))

