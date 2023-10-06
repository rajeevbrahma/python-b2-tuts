
# 1. Write a fucntion which takes list as an input and returns the even number(s) from that as a list

def return_even_number_list(inp):
    """ returning even list"""
    even_number_list = []
    for list_number in inp:
        if (list_number % 2 == 0):
            even_number_list += [list_number]
    return even_number_list


input_list = [12,3,4,21,34,5,123,5,6,343]
# print (return_even_number_list(input_list))

# 2. Write a function a which takes two integers and returns the following result

    # 2,5
    # [2**1, 2**2, 2**3, 2**4, 2**5]

def return_power_of_number(base,power_range):
    """ power of a number """
    power_of_numbers_list = []
    for power in range(1,power_range+1):
        power_of_numbers_list += [base ** power]
    return power_of_numbers_list

# print(return_power_of_number(base=2,power_range=5))

# 3. Write a function which takes two integers as inputs and return product  of those two numbers

# function definition
def return_product(number1,number2):
    """ Product of two numbers """
    return number1 * number2

print ("Product of 1,2,",return_product(1,2)) # function call 
print ("Product of 3,2,",return_product(3,2)) # function call
print ("Product of 6,2,",return_product(6,2)) # function call
print ("Product of 4,5,",return_product(4,5)) # function call

# 4. Write a function which takes two arguments which are integers and return the greatest number among them

def return_greatest_number(number1,number2):
    """ return greatest number """
    if number1 > number2:
        return number1
    else:
        return number2

print (return_greatest_number(1,2))
print (return_greatest_number(5,2))
print (return_greatest_number(8,2))
print (return_greatest_number(4,23))
print (return_greatest_number(12,2))
print (return_greatest_number(4,2))
print (return_greatest_number(1,5))

# 5. Write a function which takes list and an integer as input and return the integers index in that list
# [1,2,3,4,5,6]


def get_me_index(give_list,given_number):
    """ Gives the index """
    index = 0
    for list_value in give_list:
        if (list_value == given_number):
            return index
        index +=1
    

print (get_me_index([2,23,3,5,6,2,3],5))
print (get_me_index([2,23,3,5,6,2,3],3))
print (get_me_index([2,23,3,5,6,2,3],23))
print (get_me_index([2,23,3,5,6,2,3],2))

# 7. Write a function which takes list and integer as input and return how many times a number is 
# repeated in the list

# 8.  Write a function which takes list and integer as input and return all the index positions that 
# this number is in 


# 6. Write a function which takes list as an input and returns the lenght of the list





