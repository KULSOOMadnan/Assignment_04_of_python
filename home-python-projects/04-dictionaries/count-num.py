def user_number ():
    user_numbers = []
    while True:
        
        user_input = input("Enter a number or press (Enter) to quit: ")
        if user_input == "":
            break
        
        int_input = int(user_input)
        user_numbers.append(int_input)
    return user_numbers


def count_numbers_in_list(num_list):
    """
    Create an empty dictionary.
    Loop over the list of numbers. 
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """
    num_dict = {}
    for num in num_list:
        
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict
    
    
def print_counts(num_dict):
    """
    Loop over the dictionary and print out each key and its value.
    """
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")

    
def main():
    numbers = user_number()
    num_dict = count_numbers_in_list(numbers)
    print(print_counts(num_dict))
   
    
main()


