# Dictionaries are used to store information that go as key valued pairs
#example: name: John. 'name' is a key and 'john' is a value
# here is a dictionary:
customer = { # each key can have a string, number, boolean, list, tuple, etc.
    "name": "John Smith", 
    "age": 30,
    "is_varified": True
} # Every key is unique and cannot be duplucated. having multiple 'age' is not allowed
print(customer["name"]) # will print the value of that key
# print(customer["birthdate"]) will not work because the key does not exist
# *keys are case sensative. Here is a way around that:
print(customer.get("Name"))
print(customer.get("birthdate")) # this will print 'none' insead of an error
print(customer.get("birthdate", "Jan 1 1980")) # this will add the value to the key
customer["name"] = "Jack Smith" # this will update the value for the key specified
print(customer["name"])

customer["birth_date"] = "Feb 1, 1990" # this will add a new key
print(customer["birth_date"]) 