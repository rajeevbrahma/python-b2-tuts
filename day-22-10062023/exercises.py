# collect name and display
# collect name and store in a list
# collect name, bank_code, account_number
# collect above bank details for multiple people

account_users = []

# def collect_user_info():
#     user = None
#     global account_users
#     while (user != ""):
#         user = input("Please enter your name here - ")
#         account_users += [user]
    
# collect_user_info()
# print (account_users)


# account_users = []

# def collect_user_info():
#     add_more = "Y"
#     global account_users
#     while (add_more != "N"):
#         user_data = {"name":None,"account_number":None,"balance":None,"password":None}
#         user_data["name"] = input("Please enter your name here - ")
#         user_data["account_number"] = input("Please enter your account number here - ")
#         user_data["balance"] = input("Please enter your balance here - ")
#         user_data["password"] = input("Please enter your password here - ")
#         account_users += [user_data]
#         add_more = input("Do you want to add more Y / N")
        
    
# collect_user_info()
# print (account_users)


# write a function which collects information from user and store them in the dictionary
# with his accountnumber as key



account_user_details = {}


#function definition
def collect_user_info():
    """ function to collect user information """
    i =0
    while i<3:          # 3 times
        data = {}
        data["name"] = input("Enter your name")
        data["balance"] = input("Enter your balance")
        data["password"] = input("Enter password")
        account_number = input("Account number")
        account_user_details[account_number] = data
        i+=1
        print (account_user_details)
    
    i = 0
    while i<3:         # infinite times
        data = {}
        data["name"] = input("Enter your name")
        data["balance"] = input("Enter your balance")
        data["password"] = input("Enter password")
        account_number = input("Account number")
        account_user_details[account_number] = data
        print (account_user_details)

    # # FOR CUSTOMER 1
    
    #     data = {}  # initialized an empty dictionary
    #     print (data)
    #     data["name"] = input("Enter your name") # populating my empty dictionary with name as key and input 
    #     # from the user a value associate to it.
    #     print (data)
    #     data["balance"] = input("Enter your balance")
    #     print (data)
    #     data["password"] = input("Enter password")
    #     print (data)
    #     account_number = input("Account number")
    #     account_user_details[account_number] = data
    #     print (account_user_details)

    # print ("We have added first customer ")
    # data = {}  # initialized an empty dictionary
    
    # # FOR CUSTOMER 2
    # data["name"] = input("Enter your name") # populating my empty dictionary with name as key and input 
    # # from the user a value associate to it.
    # print (data)
    # data["balance"] = input("Enter your balance")
    # print (data)
    # data["password"] = input("Enter password")
    # print (data)
    # account_number = input("Account number")
    # account_user_details[account_number] = data
    # print ("We have added SECOND customer ")
    # print (account_user_details)
    # data = {}  # initialized an empty dictionary
    # # FOR CUSTOMER 3
    # data["name"] = input("Enter your name") # populating my empty dictionary with name as key and input 
    # # from the user a value associate to it.
    # print (data)
    # data["balance"] = input("Enter your balance")
    # print (data)
    # data["password"] = input("Enter password")
    # print (data)
    # account_number = input("Account number")
    # account_user_details[account_number] = data
    # print (account_user_details)
    



collect_user_info()

# for j in range(5):
#     print ("Hello world")

# print ("WHILE HERE ")
# i = 1
# while i <= 5:
#     print ("Hello world")
#     i += 1

{
    '1234': {
        'name': 'MArk', 
        'balance': '12390', 
        'password': '2343'
    }, 
    '1235': {
        'name': 'John', 
        'balance': '2389423', 
        'password': '2343'
    }, 
    '1236': {
        'name': 'Paul', 
        'balance': '2323908', 
        'password': '2134'
    }
}

{
    '1234': {
        'name': 'Mark',
        'balance': '2348923',
        'password': '132'
    }, 
    '1235': {
        'name': 'John',
        'balance': '283923',
        'password': '124'
    }, '1236': {
        'name': 'Paul',
        'balance': '1394823',
        'password': '289'
    }
}






