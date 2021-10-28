# parameters are place holders for recieving information
# they are used with functions to pass information
# example:
def greet_user(name): # this is passing the variable 'name' and declaring it with a value when the function is called. similar to: name = john
    print(f'Hi {name}!') # calling the variable when the function is executed
    print('Welcome aboard')


print('Start')
greet_user("john") # the variable 'name' will be set to 'john' 
greet_user("mary") # this will replace 'john' with 'mary' for the variable 'name'
print("Finish")
# *once you pass a variable to a function, there must be a positional arguement that goes with it. you must have a value in the parenthesis when the function is called
# *parameters and arguements are NOT the same!
# you can also pass multiple parameters in a function:
def greet_user(first_name, last_name): # we declared two variables in the function
    print(f'Hi {first_name} {last_name}!') 
    print('Welcome aboard')


print('Start')
greet_user("john", "smith") # we set two arguements when we call the function
print("Finish")


