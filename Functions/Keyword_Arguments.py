# positional arguments mean that the order of a argument(or value) matters
# keyword arguments do not have to be in order
def greet_user(first_name, last_name): 
    print(f'Hi {first_name} {last_name}!') 
    print('Welcome aboard')


print('Start')
greet_user("john", "smith") # whatever argument is first, it will belong to the first parameter declared. ex: 'john' belongs to 'first_name'
print("Finish")
# *depending on how many parameters are passed, there must always be the same amount of arguments
# example 2:
def greet_user(first_name, last_name): 
    print(f'Hi {first_name} {last_name}!') 
    print('Welcome aboard')


print('Start')
greet_user(last_name="smith", first_name="john") # these are keyword arguments. we set the arguments to the parameters they belong to
print("Finish")
# *using keyword arguments are more common with numbers and values
# example 3:
def greet_user(first_name, last_name): 
    print(f'Hi {first_name} {last_name}!') 
    print('Welcome aboard')


print('Start')
greet_user('John', 'smith') 
#ex: calc_cost(total=50, shipping=50, discount=0.1) -> its easier to see what each value represents in the code with keyword arguments
print("Finish")
# *Python does not like it when you mix keyword and positional arguments so stay consistant with what you choose
# *If you have to mix both then use keyword arguments after positional arguments
# ex: greet_user('John', last_name='smith')