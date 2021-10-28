# a module is basically a file with python code
# we use them to organize our code into multiple files
# we will take this piece of code and turn it into a module
# we will make a separate file called 'converters.py' and put some code into it. every file is a module
# then we will do this:
import converters # we are calling the name of the file to import and reference its code. (do not include '.py')
from converters import kg_to_lbs # here we are just calling a specific function from that module. you can use this if you don't want to reference every function from that file

kg_to_lbs(100) # this does not need 'converters.' because the sepecific function was directly imported
print(converters.kg_to_lbs(70)) # we are calling the function, passing the value '70' and printing the output