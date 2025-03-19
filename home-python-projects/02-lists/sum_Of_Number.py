"""
Write a function that takes a list of numbers and returns the sum of those numbers. 
"""

def sum_of_numbers(numbers : list[int])-> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """

    total: int = 0
    for number in numbers:
        total += number

    return total

# There is no need to edit code beyond this point

def main()-> None:
    numbers: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_number: int = sum_of_numbers(numbers)  # Find the sum of the list
    print(sum_of_number)  # Print out the sum above
    

if __name__ == '__main__':
    main()