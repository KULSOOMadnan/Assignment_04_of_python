# Write a program which asks the user what their favorite animal is,
# and then always responds with "My favorite animal is also ___!" 

def main():
   user = input('What is your favorite animal? ')
   print(f'My favorite animal is also {user}!')



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()