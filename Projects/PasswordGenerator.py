import random

print("Hello, welcome to Password Generator")
print("How many letters and numbers would you like your password to be?")

How_many_letters = int(input("Letters: "))
How_many_numbers = int(input("Numbers: "))

y = How_many_letters
z = How_many_numbers

password = []

for letters in range(y):
    rand_letters = random.choice(["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    password.append(rand_letters)

for numbers in range(z):
       rand_num = random.choice(['0','1','2','3','4','5','6','7','8','9'])
       password.append(rand_num)

NewPassword = ''.join(password).title()

print(f"Here is your new password: {NewPassword}")