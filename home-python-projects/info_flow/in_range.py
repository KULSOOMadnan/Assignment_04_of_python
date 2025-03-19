def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

# Taking inputs from the user
n = int(input("Enter the number to check: "))
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

# Checking if the number is in range
answers = in_range(n, low, high)
print(f'Is the Number in range: {answers}')