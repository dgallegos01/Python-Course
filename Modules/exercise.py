# we will take a code from a previous exercise, give it new elements, and turn it into a module
# the module will be called utils.py
# here is the example code:
"""
numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
"""
# now we will import the module containing the function of that code
import utils # you can use this or call the function directly. either way is up to you

numbers = [3,6,2,8,4,10] # we make our list
max = utils.find_max(numbers) # we pass the variable to the function
print(max) # output should be 10

