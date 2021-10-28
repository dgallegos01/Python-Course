# exanples:
course = 'python for beginners' # single quotes are commonly used for basic grammer
print(course)
course = "Python's Course for Beginners" # use double quotes for sentences with apostraphies 
print(course)
course = 'Python Course for "Beginners"' # single quotes are useful when using quoted words
print(course)
course = ''' 
Dear User,

This is a string test

Thank you,
-Darrius
''' # using triple quotes allows you to write full sentences and paragraphs
print(course)
course = 'Python for Beginners' # Every letter and character is assigned a number value, starting from 0
# ex. Python = 012345, known as an "index"
print(course[0]) #select a number and it will print the corresponding letter
# There are also negative index's, starting with -1 it reads the string from right to left
print(course[-1]) # This will print the last letter of the string
print(course[0:3]) # prints all index's from 0 to 3 (excluding 3)
print(course[0:]) # prints all characters to the end of the string
print(course[1:]) # Excludes the first character
print(course[:5]) # Python assumes the starting point is 0
print(course[:]) # this will print every character in the index
# assigning a new variable
another = course[:] # a copy of our first variable
print(another) # will print the original string
# new example
name = 'Jennifer'
print(name[1:-1]) # excludes the first and last characters
