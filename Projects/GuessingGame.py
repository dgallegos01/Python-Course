import random

play = True

while play:

    guessNum = int(input("guess a number between 1 and 10: "))

    if guessNum >= 1 and guessNum <= 10:
        num = random.randint(1, 10)
        if num == guessNum:
            print(f"{num} is correct!")
            question = input("whould you like to play again? y/n ")
            if question == 'y':
                print("Okay here we go again!")
                play = True
            else:
                print("Okay see you again next time!")
                play = False
        else:
            print(f"{guessNum} is incorrect!")
            print(f"The correct answer is {num}")
            question = input("whould you like to play again? y/n ")
            if question == 'y':
                print("Okay here we go again!")
                play = True
            else:
                print("Okay see you again next time!")
                play = False
        
    else:
        print("not in range")