# Here are more string methods to use
course = 'Python for Beginners'
print(len(course)) # this will pring the number of characters in the string
# there are 20 characters in the string
# the len() function is useful for setting character limits
course.upper() # This upper() method is used for converting lowercase to uppercase
# *functions for strings are refurred to as methods
# *functions such as pring or len are general purpose functions
print(course.upper()) # will print uppercase letters. this does not change the original variable
print(course) # the original variable remains the same
print(course.lower()) # this sets all characters to lowercase
print(course.find('P')) # this finds the index of "P" which is 0. This method is case sensitive
print(course.find('Beginners')) # works with words. prints the index where the word starts
print(course.replace('Beginners', 'Absolute beginners')) # replaces words of your choosing. Also case sensative.
print(course.replace('P', 'J')) # also works with letters
print('Python' in course) # this checks to see if the word exists in the variable (boolean expression)
print(course.title()) # sets every first letter of a word to uppercase
