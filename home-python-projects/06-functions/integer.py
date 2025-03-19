# function to take out all even numbers 
def count_even(lst : list[int] ):
    """
    take a list as a parameyer then return all the 
    even number from that list
    """
    count = 0 
    even_nub = [i for i in lst if i % 2 == 0]
    count = len(even_nub)
    print("Total Even number in the List  -> " +   str(count))
        



# getting int to make a list 
def get_user_list():
    lst = []
    user_input = input('Enter a integer to add the list or press (enter) to quit: ')
    while user_input != '':
        lst.append(int(user_input))
        user_input = input('Enter a integer to add the list or press (enter) to quit: ')
    
    return lst
    
def main():
    list_from_user =  get_user_list()
    count_even(list_from_user)

if __name__ == "__main__":
    main()
   