"""
Define a new type called 'Person'.
This type should have a 'name' attribute and
a 'talk()' method """

class Person(object):
    def __init__(self, name): # 'self' will reference 'john' and 'name will be 'John Smith'
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}") # this is a formatted string


john = Person("John Smith") # this name will be set in the constructor
print(john.name) 
john.talk()

bob = Person("Bob Smith") # we created a new object
bob.talk()        
# *each object is a different instance of a 'Person' class