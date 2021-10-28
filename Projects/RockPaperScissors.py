import random

play = True
game_items = ['rock', 'paper', 'scissors']
r = 'rock'
p = 'paper'
s = 'scissors'

print("Hello and welcome to the game, Rock, Paper, Scissors")
print("your job is to win against the computer now play!")

while play:
    yourTurn = input("Pick r, p, or s: ")
    if yourTurn == 'r':
        print(f"you chose {r}")
    elif yourTurn == 'p':
        print(f"you chose {p}")
    elif yourTurn == 's':
        print(f"you chose {s}")
    else:
        print("Not a choice. try again")
    computerTurn = random.choice(game_items)
    print(f"The computer chose {computerTurn}")

    if yourTurn == "r" and computerTurn == 'paper':
        print("Paper beats rock")
        question = input("The computer wins! play again? y/n ")
        if question == 'y':
            print("Okay, here we go again")
            play = True
        else:
            print("Okay, see you next time!")
            play = False
    elif yourTurn == 'p' and computerTurn == 'scissors':
        print("Scissors beats paper")
        question = input("The computer wins! play again? y/n ")
        if question == 'y':
            print("Okay, here we go again")
            play = True
        else:
            print("Okay, see you next time!")
            play = False
    elif yourTurn == 's' and computerTurn == 'rock':
        print("Rock beats scissors")
        question = input("The computer wins! play again? y/n ")
        if question == 'y':
            print("Okay, here we go again")
            play = True
        else:
            print("Okay, see you next time!")
            play = False
    elif yourTurn == 'r' and computerTurn == 'scissors':
        print("Rock beats scissors")
        question = input("You Win! play again? y/n ")
        if question == 'y':
            print("Okay, here we go again")
            play = True
        else:
            print("Okay, see you next time!")
            play = False
    elif yourTurn == 'p' and computerTurn == 'rock':
        print("Paper beats rock")
        question = input("You Win! play again? y/n ")
        if question == 'y':
            print("Okay, here we go again")
            play = True
        else:
            print("Okay, see you next time!")
            play = False
    elif yourTurn == 's' and computerTurn == 'paper':
        print("Scissors beats paper")
        question = input("You Win! play again? y/n ")
        if question == 'y':
            print("Okay, here we go again")
            play = True
        else:
            print("Okay, see you next time!")
            play = False
    else:
        question = input("Its a draw! play again? y/n ")
        if question == 'y':
            print("Okay, here we go again")
            play = True
        else:
            print("Okay, see you next time!")
            play = False