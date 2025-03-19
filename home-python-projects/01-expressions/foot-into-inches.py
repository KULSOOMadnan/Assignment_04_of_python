"""
An example program with constants
"""

INCHES_IN_FOOT: int = 12  # There are 12 inches for 1 foot.

def main():
    feet = float(input("Enter the number of feet: "))
    inches = feet * INCHES_IN_FOOT
    print(f"{feet} feet is {inches} inches.")

if __name__ == "__main__":
    
    main()

