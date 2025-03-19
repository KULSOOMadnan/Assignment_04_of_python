def double(num : int):
    numb = num * 2 
    # print('parameter num  ' + str(id(num))  + '\nfunction varaible  ' + str(id(numb)))
    return numb


def main():
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()