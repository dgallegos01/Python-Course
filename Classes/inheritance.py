# Inheritance is a mechanism for reusing code. Other programming languages support this
# this keeps you from having to make classes with the same methods
# Don't Repeat Yourself(DRY)
# example:
"""
class Dog:
    def walk(self):
        print("walk")


class Cat:
    def walk(self):
        print("walk")
"""

# now we will make a class that includes two different types
# example 2:
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal): # now the 'Dog' class inherits the methods of the 'Mammal' class
    def bark(self): # we can still add methods to the 'Dog' class as needed
        print("bark")


class Cat(Mammal): # we can make multiple classes that inerit the 'Mammal' class
    pass # Python does not like emply classes so put 'pass' if there is now other methods to add to that class


dog1 = Dog() # we create a variable for our type
dog1.walk() # we can then print the method which is 'walk'
dog1.bark() # we print the method 'bark'
