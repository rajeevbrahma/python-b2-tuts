""" Different errors in python """

# SyntaxError
# print("Hello World)

print ("Hello World")

def hello():
    print("Hello World")

# print ("Hello World")

# if True:
#     print("Hello World")
#     print ("Hello World")
#     print (1)
#     print (2323)
# else:
#     print("Hello World")
#     print ("Hello World")
#     print (1)
#     print (2323)

# for i in range(10):
#     print (i)


# IndentationError
# def hello():                                                          Uncomment this line to see the error
# print("Hello World")  # IndentationError: expected an indented block - Uncomment this line to see the error

# NameError
print(hello())

# Function names / Variable Names

# print (hello_world()) # trying to call a function that is not defined yet - Uncommnet this line to see the error
# print (hello_world) # trying to call a variable that is not defined yet - Uncomment this line to see the error

# TypeError
# When you are trying to operate on a variable with a different type
print (5+5) # 10
print ("5"+"5") # 55
print ([1,2]+[3,4]) # [1, 2, 3, 4]
# print ([1,2] + 5) # TypeError: can only concatenate list (not "int") to list - Uncomment this line to see the error
# print(5 + "Hello") # TypeError: unsupported operand type(s) for +: 'int' and 'str' - Uncomment this line to see the error

# ValueError
print (int("5")) # 5
# print (int("hello")) - Uncomment this line to see the error

# IndexError
# List Data types
list_variable = [1,2,3,4,5]
print (list_variable[0]) # 1
# print (list_variable[9]) # IndexError: list index out of range - Uncomment this line to see the error


# KeyError
# Dictionary data types
dictionary_variable = {"name": "John"}
print (dictionary_variable["name"]) # John
# print (dictionary_variable["address"]) # KeyError: 'address' - Uncomment this line to see the error


# # ZeroDivisionError
# print(5 / 0) # ZeroDivisionError: division by zero - Uncomment this line to see the error


# # ModuleNotFoundError
# import hello

# # ImportError
# from hello import hello

# # KeyboardInterrupt
# while True:
#     pass



# # AssertionError
# # assert 5 < 3

# # AttributeError
# # print("Hello".age)

# # EOFError
# input("Enter your name: ")

# # FileNotFoundError
# # print(open("hello.txt"))
