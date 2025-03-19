def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message)
    # return message  * repeats

def main():
    message = input('Enter a message to ')
    repeat = int(input('Enter a  number of to repeat it  '))
    
    final_result=print_multiple(message , repeat)
    print(f'{final_result}')
    
main()