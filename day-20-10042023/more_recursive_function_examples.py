
# 10,9,.....1

# def recursive_func_example():
#     recursive_func_example()

def print_squares_of_numbers_in_reverse_order(number):
    """ recursive example"""
    print (number**2)
    if (number > 1):
        number -= 1
        print_squares_of_numbers_in_reverse_order(number)

print_squares_of_numbers_in_reverse_order(10)


# for i in range(10,0,-1):
#     print (i**2)


# factorial of number 

def factorial_of_a_number(number):
    """ factorial of a number """
    if (number>1):
        return number + factorial_of_a_number(number-1)
    return 1


# 3*2*3*4*5
print (factorial_of_a_number(10))
    # """
    #     [5*4*3*2*1] factorial

    #     [5+4+3+2+3] # cummulative addition
    
    # """



# 3. define a recursive function to produce sum of all numbers from that number till 1

# define a recursive function to produce even numbers from the given till 1

# 10,8,6,4,2



def produce_even_numbers(number):
    """ produce even numbers """
    print (number)
    if (number<10):
        number+=2
        produce_even_numbers(number)

# print (produce_even_numbers(2))


