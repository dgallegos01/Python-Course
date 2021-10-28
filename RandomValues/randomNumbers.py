# Remember, python already has built-in modules
# to see what modules there are, Google 'python 3 module index'
# we will be working with the module for generating random numbers
# if you want to see all the python modules, go to: C:\Python38\Lib

import random # the module is called 'random'

for i in range(3):
    print(random.random()) # here we are printing a random value between 0 and 1

for i in range(3):
    print(random.randint(10, 20)) # this will print random integers between 10 and 20

# now we will generate random names:
names = ['John', 'Marry', 'bob', 'Darrius']
name = random.choice(names) # this will randomly generate a name from the list
print(name)
# *the output of these examples will be different every time you run the program
