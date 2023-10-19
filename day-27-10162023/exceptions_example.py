""" Exceptions example """

collection_of_bank_users = [
    {
        'account_number': 23846,
        'first_name': 'John', 
        'last_name': 'Lenon',  
        'balance': '2389',
        'address': '123 Main Street',
        'products': ['savings', 'current', 'credit card', 'loan', 'mortgage', 'investment']
    },
    {
        'account_number': 237923,
        'first_name': 'Mark', 
        'last_name': 'Anthony',  
        'balance': '23723',
        'products': ['savings', 'current', 'credit card']
    }
]


# Exercise - Write instructions which takes input from the user and do the following and please handle all the
# errors that user might do

#IndexError, KeyError, ZeroDivisionErrror, TypeError, ValueError

#1. look for the username that you recieve from the command line and show the details

collection_of_users = {
    "john":{
        "age":42,  #44
        "children_names":["a",'b']
    },
    "mark":{
        "age":45,
        "children_names":["c",'d']
    }
} 

# You are actually looking for the user who is not present do you want to add me 

while True:
    user_name = input("Enter the user name whose details you want to see ")
    try:
        print (collection_of_users[user_name])
    except KeyError:
        print ("You are looking for user not present in the list, please try again...")
        # print ("You are actually looking for the user who is not present do you want to add me")
    
    try:
        age_increment_value = int(input("Please add the age that you want to add to this user ---  "))
        print (collection_of_users[user_name]['age'] + age_increment_value )
    except ValueError:
        print ("Please give age in numerics only.....")
    
    try:
        print (collection_of_users[user_name]['age'] + age_increment_value )
    except TypeError:
        print ("Error ")
    except ValueError:
        print ("Please give age in numerics only.....")
    