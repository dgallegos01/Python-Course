# calculating our birth year
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2020 - int(birth_year)
print(type(age))
print(age)
# this program will not work unless you use int()
# type() will show the class of the variable