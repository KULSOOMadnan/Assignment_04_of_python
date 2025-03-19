
user_number : int = int(input('Give me number i will print its divisor:  '))
list_range : range = range(1 , user_number + 1)
divisor : list[int] = []

for n in list_range:
    if user_number % n == 0:
        divisor.append(n)

print(f'List of "{user_number}" divisor is here ⬇️ ')
print(divisor)
        


