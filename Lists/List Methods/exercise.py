# Write a program to remove the duplicates in a list
numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number) # this will add one of every number from the original list to the new list
print(uniques)