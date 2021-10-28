# we will learn how to use classes in python
# classes are used to define new types. they are very important not just to python but to programming in general
# simple types are the methods we have used so far
"""
example:
Numbers
Strings
Booleans
Lists
Dictionaries
"""
# classes are used to make complex types like defining objects
# we use them to model real concepts
# it is also similar to making a function
# example:
class Point: # unlike functions or variable, we capitalize the name of our class. we don't use underscores to separate words either, only capitalize every word
    def move(self): # this is a methed not a function
        print("move")
    def draw(self):
        print("draw")


# now we can make an instance of an object
# *an object is an instance of a class
point1 = Point() # we set the class to the variable or object
point1.draw() # here we are able to call the class via the '.' method and grab the method within the class
# when we run the program, the output should be "draw"

point1.x = 10 # this is an attribute
print(point1.x)

point2 = Point() # this is a new object that is set to the class
point2.x = 1 # this creates a new attribute to that object
print(point2.x)