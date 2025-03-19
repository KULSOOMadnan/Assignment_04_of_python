import random

def main():
    # the numbe that er are trying to guess
    random_number = random.randint(1, 99)
    
    print('I am guessing a number between 1 and 99. Can you guess it?')
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    # True if guess is not equal to secret number
    while guess != random_number:
        if guess < random_number:
            print("Too low!")
        else:
            print("Too high!")
        guess = int(input("Enter a guess: "))
        
    print(f"Congrates You guess it {random_number}!")    
        
        
main()