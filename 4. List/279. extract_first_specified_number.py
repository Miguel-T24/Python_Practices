# 279. Write a Python program to extract the first specified number of vowels from a given string. If the specified number is less than the number of vowels present in the string then display "n is less than the number of vowels present in the string".

def extract_n_vowels(word,nv):
    vowels = list('aeiouAEIUO')
    c=0
    r=[]
    for i in word:
        if(i in vowels):
            r.append(i)
            c+=1
        if(c==nv):
            return "".join(r)
    return "n is less than number of vowels present in the string."

print("Python")
print(extract_n_vowels("Python",2))
print("Python Exercises")
print(extract_n_vowels("Python Exercises",3))
