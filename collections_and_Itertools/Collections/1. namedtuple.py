# Collections 

"""
- namedtuple() : factory function for creating tuple subclasses with named fields
- deque: list-like container with fast append and pop on either end
- chainMap: dict-like class for creating a single view of multiple mappings
- Counter: dict subclass for counting hashable objects
- orderedDict: dict subclass that remembers the order entries were added.  
- defaultDict: dict subclass that calls a factory function to supply missing values

"""

print("nametuple")
print("Standard tuple:")
bob = "Bob",30,"Male"
jane = "Jane",29,"Female"
print("Representation Bob:",bob)
print("Jane Age: ",jane[1])

for i in [bob,jane]:
    print("Name: {} - Age: {} - Gender: {}".format(*i))

# Name: bob - Age: 30 - Gender: Male
# Name: Jane - Age: 29 - Gender: Female

print("\n"+"*"*40+"\n")
# ****************************************

import collections
Person = collections.namedtuple("Person", 'name age') # creating tuple with name

bob = Person(name = "Bob", age = 30)
print("Representation bob: {}".format(bob))
# Representation bob: Person(name='bob',age=30)

jane = Person(name = 'jane', age = 29) # Representation of jane
print("Jane age: {}".format(jane.age))
# Jane age: 29

for i in [bob,jane]:
    print("Name: {} - Age: {}".format(*i))
# Name: bob - Age: 30
# Name: jane - Age: 29

# Invalid names
# Person = collections.namedtuple("Person", "name class age") # Error because class is not valid

# We can't put invalid names
Person = collections.namedtuple("Person", "name class age" , rename = True)
Person1 = collections.namedtuple("Person1","name age age", rename = True)
print(Person._fields) # _1 class
print(Person1._fields)# _2 dulicates field

# Special attribute
Person = collections.namedtuple("Person",'name age')
bob = Person(name = "bob", age = 30)
print("Representation: {}".format(bob)) # Represetation: Person(name="bob",age=30)
print("Fields: {}".format(bob._fields)) # Fields: ('name','age')

# We can convert to instance OrderDict using _asdict()
Person = collections.namedtuple("Person", 'name age')

bob = Person(name = 'bob', age = 30)
print("Representation: {}".format(bob)) # Person(name='bob', age='30')
print("As Dictionary: {}".format(bob._asdict())) # As Dictionary: {'name':'bob','age':30}


# Replace()
Person = collections.namedtuple("Person" , "name age")
bob = Person(name = "Bob", age = 30)
print("Before: {}".format(bob)) # Person('name':'bob', age=30)
bob2 = bob._replace(name = "Robert")
print("After: {}".format(bob2)) # Person(name:'Robert',age=30)
print("Same?? : ", bob is bob2) # False