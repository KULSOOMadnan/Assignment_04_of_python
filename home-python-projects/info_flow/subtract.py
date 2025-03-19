def subtract_seven(num):
    num = num - 7
    return num

def main():
    num : int = 15
    subtract = subtract_seven(num)
    if subtract == 0:
        print('After subtracting seven, the result is zero.')
    else:
        print(f'After subtracting seven, the result is {subtract}.')
        
main()
 