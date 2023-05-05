# 79. Write a python program to find the samllest and largest words in a given string

def smallest_largest_words(string):
    string = string.split(" ")
    smallest = string[0]
    largest = ""
    for i in string:
        smallest = (smallest,i)[len(i)<len(smallest)]
        largest = (largest,i)[len(i)>len(largest)]

    return (smallest,largest)

string = "Write a Java program to sort an array of given integers using Quick sort Algorithm."
small, large = smallest_largest_words(string)

print("Original Word: {}".format(string))
print("Smallest Word: {}\nLargest Word: {}".format(small, large))
