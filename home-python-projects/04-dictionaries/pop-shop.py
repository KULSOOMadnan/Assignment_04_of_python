def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = input(f'How many "{fruit_name}"  do you want to buy ? which price is {fruits[fruit_name]} :')
        total_cost += price * float(amount_bought)
        print("Your total is $" + str(total_cost))
        
        
        
main()
        
    