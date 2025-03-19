'''Ask the user for two numbers, one at a time,
and then print the result of dividing the first number by 
the second and also the remainder of the division.'''

def main ():
    print('\nThis program will divide two numbers and return the result and the remainder\n')
    divident = int(input('Enter the integer to be divided   :'))
    divisor = int(input('Enter the  interger to divided by :'))
    
    quotient = divident // divisor
    remainder = divisor % divisor 
    
    print(f'The result of dividing {divident} by {divisor} is {quotient}')
    print(f'The remainder is {remainder}') 
    
    
if __name__ == "__main__":
    main()