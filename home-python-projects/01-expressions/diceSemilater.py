"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""
import random


# NO OF SLIDES FOR DICE 
NUM_SLIDES = 6 

def roll_dice():
    """ Simulate two dice and Pint there result """
    dic1 = random.randint(1, NUM_SLIDES)
    dic2 = random.randint(1, NUM_SLIDES)
    total = dic1 + dic2
    print("Rolled Dice: ", dic1, "and", dic2, "Total:", total)
    
def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))
    



if __name__ == "__main__":
    main()
 