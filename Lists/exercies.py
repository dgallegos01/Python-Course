# Write a program to find the largest number in a list.

numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max) # output should be 10