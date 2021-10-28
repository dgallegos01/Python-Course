""" make a program that will output this F shape
xxxxx
xx
xxxxx
xx
xx
"""
numbers = [5,2,5,2,2] # this is one way to do it
for x_count in numbers:
    print('x' * x_count) # other programming languages do not support this method

numbers = [5,2,5,2,2] # this is another way to do it
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)