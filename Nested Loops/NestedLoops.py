# Nested loops are loops inside a loop
# example with coordinates
for x in range(4): # x starts with 0
    for y in range(3): # y will print each value in range first before it goes back the the first loop  
        print(f'({x}, {y})') # for every x value, ther is a set of y values
""" output:
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
(2, 0)
(2, 1)
(2, 2)
(3, 0)
(3, 1)
(3, 2)
"""