""" Exception Handling in Python """

# Different Errors in Python

# ArithmeticError
# AssertionError
# TabError
# MemoryError
# TimeoutError
# UnicodeError
# RecursionError
# FileExistsError - FILE HANDLING


# -------------- Exception handling analogy with the Checkpost scenario ------------

#           check post 4  check post 1     check post 2       check post 3    
#            specalist     Drunk Drive      Seat belt           Helmet
# -->
# 1 DD        caught                    
# 2 Sbelt     caught                              
# 3 helment   caught   
# 4 nolicense caught                                               


#            check post 1     check post 2       check post 3   check post 4 
#             Drunk Drive      Seat belt           Helmet       specalist
# -->
# 1 DD        caught                    
# 2 Sbelt                       caught            
# 3 helment                                        cuaght  
# 4 nolicense                                                     caught           





#  --------- Syntax ---------

# try:
#     # try block instructions you want to look for possible exceptions / errors 
# except NameError: # This can only catch the NameErrors alone
#     # you can either quickly fix that exception if possible
# except Exception as e: # General exception and he can catch any kind of exception 
#     # either you want to get the details of exception
#     # you can either quickly fix that exception if possible
# else:
#     # This block will get executed only when you didnt catch any exceptions 
# finally:
#     # This block will always gets executed irrespective of the exceptions 
#     # Typically you can use this block to close any opened database connections / files


# Example 1 - when there is no exception
try:
    print("Hello World")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("This will always execute")


# int(input("Enter account number - ")) # user-1 - '123'  / user-2 'asdhfk'
# print ("Hello ")

# Example 2 - when there is an exception and catching the exception with the general exception type
try:
    print("Hello World")
    print(5 / 0)
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("This will always execute")

# Example 3 - when there is an exception and catching the exception with the specific exception type
try:
    print("Hello World")
    print(5 / 0)
except ZeroDivisionError:
    print("You cannot divide a number by zero")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("This will always execute")

# Example 4 - when there is an exception and catching the exception with the specific exception type
try:
    print("Hello World")
    print (hello)
except NameError:
    print("hello is not defined")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("This will always execute")

# Example 5 - Multiple Exceptions - catching the multiple exceptions with single except block
try:
    print("Hello World")
    # print (5/0)  # ZeroDivisionError - Uncomment this line to see the exception
    print (hello)  # NameError - Uncomment this line to see the exception
except (ZeroDivisionError, NameError):
    print("You cannot divide a number by zero or hello is not defined")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("This will always execute")


# catch key error 
try:
    print({"name": "John"}["age"])
except KeyError:
    print("KeyError: Key not found")

# catch value error
try:
    print(int("Hello"))
except ValueError:
    print("ValueError: Invalid value")

# catch type error
try:
    print(5 + "Hello")
except TypeError:
    print("TypeError: Invalid type")



try:
    print ("Instructions that needs monitoring")
    list_variable = [1,2,3] 
    dict_variable = {}
    dict_variable.setdefault("a","apple")   # = {"a":"apple"}
    print (list_variable)
    print (dict_variable)  

    # print (hello)  # NameError - Uncomment this line to see the exception
    # print (5/0)       # ZeroDivisionError
    # print (list_variable[4])  # IndexError     
    # print (dict_variable["b"]) # KeyError
except AttributeError:
    print ("Attribute error")
except NameError:
    print ("NameError encountered")
except ZeroDivisionError:
    print ("Zero Division error .....")
except KeyError:
    print ("Key error occured")
except Exception as e:
    print (e,type(e))
    print ("Something went wrong")
else:
    print ("Nothing weng wrong")
finally:
    print ("Always this line gets executed")

print ("\n \tLine after try exception block")


# # # Example 6 - Raising Exceptions
# # try:
# #     print("Hello World")
# #     # print (5/0)
# #     print (hello)
# # except (ZeroDivisionError, NameError):
# #     print("You cannot divide a number by zero or hello is not defined")
# #     raise
# # except:
# #     print("Something went wrong")
# # else:
# #     print("Nothing went wrong")
# # finally:
# #     print("This will always execute")















