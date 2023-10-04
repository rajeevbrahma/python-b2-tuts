""" Function scope example """


def my_function():
    """ Prints a message """
    message = 'Hello from within the function scope!' # function local space
    print(message)

message = 'Hello from outside the function scope!' # global space
print(message)

my_function()
print(message)




def my_function_with_global():
    """ Prints a message """
    global message
    message = 'Hello from within the function scope!'
    print(message)

message = 'Hello from outside the function scope!'
print(message)

my_function_with_global()
print(message)


number_1 = 6
number_2 = 8

def multiply_with_number():
    global number_1, number_2
    number_2 = 5
    number_1 = 5
    print(number_1 * number_2)

print (number_1 * number_2)
multiply_with_number()
print (number_1 * number_2)




    