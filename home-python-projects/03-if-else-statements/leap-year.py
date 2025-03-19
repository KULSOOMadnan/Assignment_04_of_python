# Write a program that reads a year from the user
# and tells whether a given year is a leap year or not.

def leap_year():
    year = int(input('Enter a year to check if it is a leap year: '))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('The year ' + str(year) + ' is a leap year')
            else:
                print('The year ' + str(year) + ' is not a leap year')
        else:
            print('The year ' + str(year) + ' is a leap year')

    else:
        print('The year ' + str(year) + ' is not a leap year')


leap_year()
