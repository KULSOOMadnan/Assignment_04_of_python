import random


NUM_ROUNDS = 3


def high_low_game():

    # welcome messgage
    print('\tWelcome to the High-Low Game! ')
    print(f'-' * 30)

    # Milestone 5: keep track of your score
    your_score = 0

    for i in range(NUM_ROUNDS):
        print("Round", i + 1,)

        computer_number = random.randint(1, 100)
        player_number = random.randint(1, 100)
        print("Your number is ", player_number)
        print("The computer's number is", computer_number)
        try:
            # user guess
            user_choice = input(
                "Do you think your number is higher or lower than the computer's?: ").lower()

            high_and_correct = user_choice = "higher" and player_number >= computer_number
            lower_and_correct = user_choice = "lower" and player_number <= computer_number
            if high_and_correct or lower_and_correct:
                if user_choice <= computer_number:
                    print('You were right! The computer"s number was ',
                          computer_number)
                    your_score += 1
            else:
                print("Aww, that's incorrect. The computer's number was ",
                      computer_number)

            print("Your score is now", your_score)
            print()

        except Exception as e:
            print('Error! ', "Write only lower and higher ")

        else:
            print("Your final score is", your_score)
            if your_score == NUM_ROUNDS:
                print("Wow! You played perfectly!")
            elif your_score > NUM_ROUNDS // 2:
                print("Good job, you played really well!")
            else:
                print("Better luck next time!")

            print("Thanks for playing!")


def main():
    high_low_game()


if __name__ == "__main__":
    main()
