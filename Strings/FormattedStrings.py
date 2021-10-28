# Formatted Strings are used to dynamically generate text with variables
# Here is the standard string method: 
first = 'John'
last = 'Smith'
# we want to print "John [Smith] is a coder"
message = first + ' [' + last + '] is a coder' # we do this with concatination
print(message)
# Not an ideal method because the text gets more complicated
# Here is the Formatted Method:
msg = f'{first} [{last}] is a coder' # Here we are defining placeholders in our string
print(msg)
# This method is easier for the coder to read