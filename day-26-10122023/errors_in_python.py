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


# ZeroDivisionError
# print(5 / 0) # ZeroDivisionError: division by zero - Uncomment this line to see the error


# ImportError
# from hello import hello   # Uncomment this line to see the error 

# KeyboardInterrupt
# while True:           #   Uncomment this line to see the error
#     print ("press ctrl + c or ctrl +z to stop") # Uncomment this line to see the error

# AttributeError          
# print("Hello".age)  # Uncomment this line to see the error


# AssertionError
# assert 5 < 3          # Uncomment this line to see the error

# # EOFError
# input("Enter your name: ")

# FileNotFoundError
# print(open("hello.txt"))          # Uncomment this line to see the error



list_variable = [1,2,3,4,5,'hello']




# 

class PythonClass:

    variable_1 = None
    variable_2 = None

    def meth_1():
        pass 


class Robot:

    def __init__(self,location):
        self.location = location
        self.__greet()

    def __greet(self):
        print ("Hello There!!! ")

    def anti_theft_mode(self):
        print ("Anti theft activated for ", self.location)

    def servant_mode(self,instrucion):
        pass 

sunil_robot = Robot("Sunil address")
kiran_robot = Robot("Kiran addresss")
joh_robot = Robot("Joh address")

sunil_robot.anti_theft_mode()
kiran_robot.anti_theft_mode()
joh_robot.anti_theft_mode()



class_1 = PythonClass()
# class_1.variable_3            # Uncomment this line to see the AttributeError

class_2 = PythonClass()
class_3 = PythonClass()


list_variable = [12,3,4]
# list_variable.append()      # Uncomment to see the TypeError




# ModuleNotFoundError
# import hello          # Uncomment this line to see the error


# import calculator       # Uncomment this line to see the error ModulenotfoundError


# from Calc import add, sub, div # Uncomment this line to see the ImportError

