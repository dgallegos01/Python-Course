# we will make a dice game
import random


class Dice: # we make a dice class
    def roll(self): # we make a method called 'roll'
        first = random.randint(1, 6) 
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())