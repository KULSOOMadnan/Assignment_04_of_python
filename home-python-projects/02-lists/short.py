MAX_LENGHT = 4 


def short_list(numbers: list[int]) -> None:
    "Take a list of numbers and return a list of the first MAX_LENGHT numbers"
    while len(numbers) > MAX_LENGHT:
        del_items = numbers.pop()
        print('Removing:' , del_items )
    print('The list is now:', numbers)
        
def user_interface():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main () -> None:
    lst= user_interface()
    print('The elements of the list are: ', lst)
    short_list(lst)
    
if __name__ == '__main__':  
    main()