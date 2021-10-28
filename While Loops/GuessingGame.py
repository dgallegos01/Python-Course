secret_number = 9
guess_count = 0 # you can refractor variables by highlighting them, right click and select 'extract variable' the change the variable
guess_limit = 3 # it is better to define your values as variable to make your code easier to read
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('you win!')
        break # terminates the loop
else: # will execute when the while statement is false
    print('You Failed')