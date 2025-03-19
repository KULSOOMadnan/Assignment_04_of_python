CONSTANT = 100 

def main():
    current_value = int(input("Enter a number to double it : "))
    while current_value <= CONSTANT:
        current_value = current_value * 2 
        print(f'{current_value}')
        
main()