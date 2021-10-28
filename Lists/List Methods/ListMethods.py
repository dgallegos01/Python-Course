# adding, removing and checking existant items in a list
numbers = [5,2,1,7,4]
numbers.append(20) # this will add 20 to the end of a list
print(numbers)
numbers.insert(0, 10) # this will add 10 to index 0
print(numbers)
numbers.remove(5) # this will remove 5 from the list
print(numbers) 
numbers.clear() # this will remover everything from the list (nothing goes in the parenthesis)
print(numbers)
numbers = [5,2,1,7,4]
numbers.pop() # this will remove the last value in the list
print(numbers) # removes 4
print(numbers.index(1)) # this will print the index of the value
print(50 in numbers) # will check to see if a value is in the list using boolean
numbers = [5,2,1,5,7,4]
print(numbers.count(5)) # will check to see how many copies of a value are in the list
print(numbers.sort()) # will print 'none'. has to be independant before calling to print

numbers = [5,2,1,5,7,4]
numbers.sort() # sorts the list in assending order
print(numbers) 

numbers = [5,2,1,5,7,4]
numbers.sort() # sorts the list in assending order
numbers.reverse() # sorts the list in decending order
print(numbers) 

numbers = [5,2,1,5,7,4]
numbers2 = numbers.copy() # creates an independant copy of the list
numbers.append(10)
print(numbers)
print(numbers2)

# to print items in a list without printing the list, type this:
print(*numbers) # include a '*'
# to join numbers or letter, do this:
print(''.join(numbers))