# looking at a matrix
matrix = [
    [1,2,3], 
    [4,5,6],
    [7,8,9]   # this is a 2D list
]
matrix[0][1] = 20 # this modifies the 2 in the list
print(matrix[0][1]) # the 0 accesses the first list and the 1 gets the value 2

# using a for loop to iterate over all items in the list
for row in matrix:
    for item in row:
        print(item) # will print every item in the list