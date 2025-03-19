# Write a program that displays the terms in the Fibonacci sequence, 
# starting with Fib(0) and continuing as long as the terms are less than 10,000
# (you should store this value as a constant!).
# Thus, your program should produce the following sample run:

def main():
    MAX_TERM_VALUE : int = 10000
    first_term = 0
    second_term = 1
    
    while first_term <= 10000:
        # -- pritning the first term --
        print(first_term)
        sum_of_terms = first_term + second_term # 0 + 1 = 1
        first_term = second_term  # 0 to 1 
        second_term = sum_of_terms # 1 to 1
    #  --- end of while loop ---
       
        
main()