import random

NUM_OF_SLIDES = 6

def roll_dice():
     # Setting a seed is useful for debugging (uncomment the line below to do so!)
    # random.seed(1)
    
    # Roll die
    die1: int = random.randint(1, NUM_OF_SLIDES)
    die2: int = random.randint(1, NUM_OF_SLIDES)
    
    # Get their total
    total: int = die1 + die2
    
    # Print out the results
    print("Dice have", NUM_OF_SLIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)



if __name__ == '__main__':
    roll_dice()