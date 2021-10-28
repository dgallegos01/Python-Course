# we are going to make a function that returns values
def square(number):
    return number * number # this return statement returns values to the caller of the function

result = square(3) # this is similar to 'input()', we are passing 3 to the function
print(result)
# here is a second way to print the function:
print(square(3))

# what happens when we remove 'return'?
def square(number):
    print(number * number) # if there is no 'return' Python will still give a number output but will also output null or None 

print(square(3))
# *All functions in Python will return 'None' by default unless there is a return statement
