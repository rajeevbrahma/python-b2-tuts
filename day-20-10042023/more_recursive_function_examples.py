""" Recursive functions examples """
# Squares of numbers in reverse order from the given number
def print_squares_of_numbers_in_reverse_order(number):
    """ recursive example"""
    print (number**2)
    if number > 1:
        number -= 1
        print_squares_of_numbers_in_reverse_order(number)
GIVEN_INPUT = 10
print_squares_of_numbers_in_reverse_order(GIVEN_INPUT)


# Factorial of a given number
def factorial_of_a_number(number):
    """ factorial of a number """
    if number>1:
        return number * factorial_of_a_number(number-1)
    return 1

# Factorial of a given number version 2
factorial_result = 1
def factorial_of_a_number_2(factorial_result_at_every_instance,number):
    """ factorial of a number 2   """
    global factorial_result
    factorial_result_at_every_instance *= number
    factorial_result = factorial_result_at_every_instance
    if number>1:
        factorial_of_a_number_2(factorial_result_at_every_instance,number-1)

factorial_result_at_every_instance = 1 
factorial_of_a_number_2(factorial_result_at_every_instance,5)
print (factorial_result)

# # Factorial of a given number version 3 - printing 
# def factorial_of_a_number_3(factorial_result,number):
#     """ factorial of a number 2   """
#     factorial_result *= number
#     if (number>1):
#         factorial_of_a_number_3(factorial_result,number-1)
#     return factorial_result

# factorial_result = 1 
# print (factorial_of_a_number_3(factorial_result,5))



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


def produce_even_numbers_2(start_number,end_number):
    """ produce even numbers """
    print (start_number)
    if (start_number<end_number):
        start_number += 2
        produce_even_numbers_2(start_number,end_number)


end_number = 10
start_number = 2
print (produce_even_numbers_2(start_number,end_number))

