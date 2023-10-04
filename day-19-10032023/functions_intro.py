"""
    
    Functions are a way to group code together and give it a name.
    Functions are a way to reuse code.
    Functions are a way to make your code more 
        1. readable.
        2. testable.
        3. modular.
        4. debuggable.
        5. maintainable.
    

    Syntax:
    def function_name():
        # code goes here
        # code goes here
    
    function_name() # calling the function

    function_name() # calling the function again


"""

# GLOBAL SPACE

def say_hello():
    print ("Hello")

def say_hello_with_name(name):
    #LOCAL SPACE
    """ This function prints hello world """
    print ("Hello ",name)

say_hello_with_name(name="Python") # calling the function


def square_a_number(number):
    """ This function prints square of a number """  
    print ("Square of ",number,"is",number*number)

square_a_number(5)


def product_of_two_numbers(number_1,number_2):
    """ This funtion prints product of two numbers """
    print (number_1 * number_2)

product_of_two_numbers(2,3)

# Function definition
def division_operation(divid,divis):
    """ This func prints the """
    # / -  quotient
    # % - reminder
    print ("Reminder is ",divid%divis)
    print ("Quotient is ",divid/divis)

division_operation(10,3)  # Function call with position arguments
division_operation(divis=3,divid=10) # function call with keyword arguments


# def say_hello_with_name(name):
#     """ This function prints hello world """
#     print("Hello World", name)

# say_hello_with_name("John") # calling the function


# def say_hello_with_name_and_age(name, age):
#     """ This function prints hello world """
#     print("Hello World", name, age)

# say_hello_with_name_and_age("John", 20) # calling the function

# def say_hello_with_default_name(name="Python Programmer"):
#     """ This function prints hello world """
#     print("Hello World", name)

# say_hello_with_default_name() # calling the function

# say_hello_with_default_name("Jane") # calling the function

# def function_with_return():
#     """ This function prints hello world """
#     return "Hello World"

# print(function_with_return()) # calling the function

# def function_with_return_and_name(name):
#     """ This function prints hello world """
#     return "Hello World " + name

# print(function_with_return_and_name("John")) # calling the function


# Write a function which takes a number as an input and prints if it is even or odd
    # just use above concept and control flow statement

# write a function which takes a list of random numbers as an input and prints if they are even or odd 
    # just use above concept and control flow statement & loops and list

# Write a function which takes a list of objects as an input and prints the length of the list (please dont use inbuilt function)

    # just use above concept and control flow statement,loops, list

# write a function which takes input from the user and decide if it is a number or not


# def even_or_odd(number):
#     """ Even or Odd function """
#     if number%2 == 0:
#         print (number,"is ","Even")
#     else:
#         print (number,"is ","Odd")

# even_or_odd('3')
# even_or_odd('5')
# even_or_odd('6')


def return_even_or_odd(number):
    """ Returns True when given number is Even """
    return number%2 == 0


boolean_result = return_even_or_odd(19)
if (boolean_result):
    print ("Yes it is Even")  # condition success / if block
else: 
    print ("Its Odd")         # condition failure / else block

print (return_even_or_odd(5))
print (return_even_or_odd(6))
print (return_even_or_odd(7))
print (return_even_or_odd(8))


# Write a function which takes an input from the user and returns that value
# input()


def take_user_input():
    """ Function to take user input"""
    return input("Enter something here")

take_user_input()
take_user_input()
take_user_input()


    

# return_even_or_odd(5) True / False