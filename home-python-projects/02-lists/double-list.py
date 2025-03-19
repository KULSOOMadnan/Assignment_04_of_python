
def double_list(numbers : list[int])-> list[int]:
    """
    Takes in a list of numbers and returns a new list with each number doubled.
    """
    doubled_numbers : list[int] = []
    for number in numbers:
        doubled_numbers.append(number * 2 )
    return doubled_numbers
        

def main():
    # This is the original list
    numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers
    doubled_numbers: list[int] = double_list(numbers)
    print(doubled_numbers)

    # for i in range(len(numbers)):  # Loop through the indices of the list
    #     elem_at_index = numbers[i]  # Get the element at index i in the numbers list
    #     numbers[i] = elem_at_index * 2 
    #     print(numbers[i])# Set the element at index i to be equal to the previous element times 2

    # print(numbers)
    
  


if __name__ == '__main__':
    main()