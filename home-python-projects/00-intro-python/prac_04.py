# Write a program to solve this age-related riddle!

# anton, beth, chen, drew, and Ethan are all friends. Their ages are as follows:

# anton is 21 years old.
anton = 21

# beth is 6  years  older than anton.
beth = anton + 6

# chen is 20  years  older than beth.
chen = beth + 20


# Drew is as old as Chen's age plus Anton's age.
drew = chen + anton


# Ethan is the same age as Chen.
ethan = chen


def main():
    print(f"\nAnton is {anton} years Old\n")
    print(f"beth is {beth} years Old\n")
    print(f"chen is {chen} years Old\n")
    print(f"drew is {drew} years Old\n")
    print(f"Ethan is {ethan} years Old\n")


# This provided line is requir years Old ed at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
