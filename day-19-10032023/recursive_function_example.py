""" Recursive function example """

def factorial(number):
    """ Returns the factorial of a number """
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5)) # 120



#    *****
#    ****
#    ***
#    **
#    *


def print_stars(number):
    """ Prints stars """
    if number == 0:
        return
    else:
        print("*" * number)
        print_stars(number - 1)
