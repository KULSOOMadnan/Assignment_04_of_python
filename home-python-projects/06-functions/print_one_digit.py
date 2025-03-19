def print_ones_digit(num : int):
    """Prints the ones digit of the given number."""
    ones_digit = num % 10  # Get the remainder when divided by 10
    print("The ones digit is", ones_digit)
    
def main():
    number = input('Enter a number ')
    print_ones_digit(int(number))
    
main()