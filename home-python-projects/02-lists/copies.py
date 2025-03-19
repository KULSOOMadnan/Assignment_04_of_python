# fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

# Here is an example run of this program (user input in bold italics):

# Enter a message to copy: Hello world!

# List before: []

# List after: ['Hello world!', 'Hello world!', 'Hello world!']

from typing import Any

def add_three_copies(list : list[str] , data: Any ) -> None:
    for i in range(3):
        list.append(data)


def user_interface():
    message = input('Enter a message i will write it three times: ')
    lists = []
    print(f'List before: {lists}')
    add_three_copies(lists, message)
    print(f'List after: {lists}')
    

if __name__ == '__main__':
    user_interface()