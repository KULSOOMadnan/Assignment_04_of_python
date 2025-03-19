def greet(name):
    return "Greetings " + name + "!"

def main():
    name = input('Enter Your name : ')
    user_name = greet(name)
    print(user_name)
    
main()