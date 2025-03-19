def get_user_info():
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address : str = input("What is your email address?: ")
    
    return first_name, last_name, email_address

def main():
    user_info = get_user_info()
    print('Here is the details you intered : -> ' , user_info )
    
main()

