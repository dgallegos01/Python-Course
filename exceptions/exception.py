# we are going to learn how to handle errors in python
# example:
"""
age = int(input('Age: '))
print(age)
"""
# *if you type anything other than an integer, you will get an error
# * you will get a 'ValueError' and the program will crash
# this is how we handle errors:
try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value') # this is an exception. it prevents our program from crashing
# *Instead of crashing, we catch the error and control the output

# example 2:
"""
try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid value')
"""
# If we input 0, then we will get a 'ZeroDivisionError'
# Here is how we handle it:
try:
    age = int(input('Age2: '))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')