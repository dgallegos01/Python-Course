# practicing if statements
# we will translate these statements to if/else statements
""" 
if it's hot
    It's a hot day
    Drink plenty of water
otherwise if it's cold
    It's a cold day
    Wear warm clothes
otherwise
    It's a lovely day
"""
is_hot = True # the condition changes depending if this is true or false
is_cold = True
if is_hot:
    print("It's a hot day") # anything indented here will execute if is_hot is true
    print("Drink plenty of water")
elif is_cold: # short for else/if   
     print("It's a cold day") # anything indented here will execute if is_cold is true
     print("Wear warm clothes")
else:
    print("It's a lovely day") # prints if is_hot and is_cold are false
print("Enjoy your day") # will always print unless there is no else or else/if statement

