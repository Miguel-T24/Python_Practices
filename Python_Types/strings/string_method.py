#Upper
print("1. Upper")
message = "Python is fun"
print(message.upper()) # PYTHON IS FUN

# swapcase()
print("\n2. Swapcase")
message = "PyThOn Is fUn"
print(message.swapcase()) # pYtHoN iS FuN

# Lower
print("\n3. Lower")
message = "PYTHON IS FUN"
print(message.lower()) # python is fun

# partition
print("\n4. partition")
string = "python is fun"
print(string.partition('is ')) # ('python', 'is' , 'fun')
print(string.partition('not ')) # ('python is fun','','')
string = "Python is fun, isn't it"
print(string.partition('is')) # ('Python ','is',' ,fun isn't it')

# replace
print("\n5. replace")
string = "cold, cold heart"
print(string.replace('cold', 'hurt')) # hurt, hurt heart
# Only two occurence
song = 'Let it be, let it be, let it be, let it be'
print(song.replace('let',"don't let", 2))

# find
print("\n6. find")
message = "python is a fun programming language"
print(message.index('fun')) #12

# rstring
print("\n7. rstrip")
string = 'this is good  '
print(string.rstrip()) # this is good
print(string.rstrip('sid oo')) #this is g

# split()
print("\n8. split")
string = "Toyota-Mazda-Range Rover-Subaru-Nissan"
print(string.split("-")) # ['Toyota','Mazda', 'Range Rover', 'Subaru', 'Nissan']
print(string.split("-",2)) # ['Toyota', 'Mazda','Range Rover-Subaru-Nissan']

# startwith
print("\n9. startWith")
message = "Python is fun"
print(message.startswith("Python")) # True
print(message.startswith("Hola")) # False


# isnumeric
print("\n10 isnumeric")
pin = '523'
print(pin.isnumeric()) # True
pin = 'abc'
print(pin.isnumeric()) # False
pin = '1a2b3c'
print(pin.isnumeric()) # False

#  index
print("\n11. index")
text = "python is fun"
print(text.index("is")) # 7
print(text.index("python is")) # 0
print(text.index("fun",5,13)) # 10
print(text.index("python" , 5)) #Error