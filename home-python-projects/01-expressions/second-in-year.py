"""
Use Python to calculate the number of seconds in a year,
and tell the user what the result is in a nice
print statement that looks like this (of course the value 5 
should be the calculated number instead):
"""

#  constent 
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():

    num_of_Sec_in_year = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN 
    print("\n---Number of Seconds in a Year---")
    
    print(f"There are {num_of_Sec_in_year} in a Year ")


if __name__ == '__main__':
    main()