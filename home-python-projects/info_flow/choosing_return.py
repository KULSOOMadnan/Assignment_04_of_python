ADULT_AGE = 18 

def is_adult(age : int):
    if age <= ADULT_AGE:
        return True
    
    return False

def main():
    age : str = input("Enter a age of  person : ") 
    adult_ha = is_adult(int(age))
    print(adult_ha)
    
main()