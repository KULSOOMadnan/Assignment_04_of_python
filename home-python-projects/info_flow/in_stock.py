def num_in_stock(fruit):
    if fruit == "apple":
        return 5
    elif fruit == "mango":
        return 90
    elif fruit == "strawberry":
        return 40
    else:
        return 0 


def main():
    fruit = input('Enter a fruit : ')
    stocks = num_in_stock(fruit)
    if stocks == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stocks)

    
main()
    