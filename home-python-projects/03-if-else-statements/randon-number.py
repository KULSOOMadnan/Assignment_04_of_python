import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
   value = random.randint(MIN_VALUE, MAX_VALUE)
   print(f'Random number between {MIN_VALUE} and {MAX_VALUE} is {value}')

if __name__ == '__main__':
    main()