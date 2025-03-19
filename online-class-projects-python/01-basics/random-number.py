import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    
    print(f" \t 10 Random numnbers between the range of 1 to 100 ")

    # print ten random number in a range to 1 to 100
    for i in range(10):
        random_number = random.randint(1 , 100 + 1)
        print(f"{random_number} " , end=' ')

if __name__ == '__main__':
    main()
