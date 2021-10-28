# taking a closer look at lists
names = ['John', 'Bob', 'Sarah', 'Mary']
print(names[0]) # will print the index of the name

names = ['John', 'Bob', 'Sarah', 'Mary']
print(names[-1]) # will print the index of the name at the end of the list

names = ['John', 'Bob', 'Sarah', 'Mary']
print(names[2:]) # will print all names after 2

names = ['John', 'Bob', 'Darrius', 'Sarah', 'Mary']
print(names[2:4]) # will print the names within 2 and 4

names = ['John', 'Bob', 'Darrius', 'Sarah', 'Mary']
print(names[:]) # will still print every name
# this does not change the original list but creates a new list

names = ['John', 'Bob', 'Darrius', 'Sarah', 'Mary']
names[0] = 'Jon' # will modify the first index of the list
print(names)
