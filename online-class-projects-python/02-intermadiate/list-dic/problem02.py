# Initialize a List:

lst = [1 , "name" , "kulsoom" , 2 ,"Rimsha"]


def access_element(param1 , index):
    try:
         return param1[index]
    except IndexError:
        return "THIS INDEX IS OUT of RANGE"
   


# # user_index = input('Enter a index to return a element: ')
# index_no = int(user_index)
# result = access_elements(lst , index_no )
# # print(result)
    

def modifying_element(lst , index , new_val):
    try:
        modify_val = lst[index] = new_val
        print(lst)
        return modify_val
    except IndexError:
        return "THIS INDEX IS OUT of RANGE"
   


# user_index = input('Enter a index to return a element: ')
# update_val = input('Enter a values of selected  index: ')
# index_no = int(user_index)
# result = modifying_element(lst , index_no , update_val )
# print(result)
    

def slicing_list(lst , end , start):
    try:
        return lst[start : end]
    except IndexError:
        return "Invalid indexces."


# result = slicing_index(lst , start=1 , end=5)
# print(result)
        
    
def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")
    
    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modifying_element(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slicing_list(lst, start, end))
    else:
        print("Invalid operation.")

index_game()