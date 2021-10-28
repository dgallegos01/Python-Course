# Unpacking is a very powerful tool in python
coordinates = (1,2,3)
coordinates[0] * coordinates[1] * coordinates[2] # This can be siplified
# we can define each part:
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
x * y * z # This can be simplified even further
# this is unpacking:
x, y, z = coordinates # each value in the tuple will be assigned to each variable(x,y,z)
print(x) # will print 1
print(y) # will print 2
print(z) # will print 3

# this will also work with lists
coordinates = [1,2,3]
x, y, z = coordinates 
print(x) 
print(y) 
print(z) 