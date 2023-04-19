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

print("\n"+"*"*40+"\n")

import collections
Person = collections.namedtuple("Person", 'name age')

bob = Person(name = "Bob", age = 30)
print("Representation bob: {}".format(bob))

jane = Person(name = 'jane', age = 29)
print("Jane age: {}".format(jane.age))

for i in [bob,jane]:
    print("Name: {} - Age: {}".format(*i))

# Invalid names
# Person = collections.namedtuple("Person", "name class age") # Error because class is not valid

# We can mada valid names
Person = collections.namedtuple("Person", "name class age" , rename = True)
Person1 = collections.namedtuple("Person1","name age age", rename = True)
print(Person._fields) # _1 class
print(Person1._fields)# _2 dulicates field

# Special attribute

Person = collections.namedtuple("Person",'name age')
bob = Person(name = "bob", age = 30)
print("Representation: {}".format(bob))
print("Fields: {}".format(bob._fields))

# We can convert to instance OrderDict using _asdict()
Person = collections.namedtuple("Person", 'name age')

bob = Person(name = 'bob', age = 30)
print("Representation: {}".format(bob))
print("As Dictionary: {}".format(bob._asdict()))


# Replace()
Person = collections.namedtuple("Person" , "name age")
bob = Person(name = "Bob", age = 30)
print("Before: {}".format(bob))
bob2 = bob._replace(name = "Robert")
print("After: {}".format(bob2))
print("Same?? : ", bob is bob2) # False