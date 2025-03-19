def main():
    # Get the 3 side lengths of the triangle
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))


    # Calculate perimeter
    perimeter = side1 + side2 + side3

    # Print result
    print(f"The perimeter of the triangle is {perimeter}")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
