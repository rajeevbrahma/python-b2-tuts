""" Dictionary methods """

# Dictionary methods
# clear() - Removes all the elements from the dictionary
# copy() - Returns a copy of the dictionary
# fromkeys() - Returns a dictionary with the specified keys and value
# get() - Returns the value of the specified key
# items() - Returns a list containing a tuple for each key value pair


# Dictionary intialization
#1 . Using curly braces
example_dictionary = {
    "name":"John",
    "age":23,
    "country":"UK"
}

#2. Using dict() function
example_dictionary_2 = dict(name="John",age=23,country="UK")

# print (example_dictionary)
# print (example_dictionary_2)

john_details = {
    "name":"John",
    "age":23,
    "country":"UK"
}

john_details_2 = dict(name="John",age=23,country="UK")

print (john_details)
print (john_details_2)

#Creating a default dictionary 
# {"name":None,"age":None,"country":None}

dictionary_keys = ("name","age","country")

john_details_3 = dict.fromkeys(dictionary_keys) # By default the value is None
print (john_details_3)

# day 25 - 11/10/2020


# Access a dictionary element
print (john_details["age"])
print (john_details["country"])
print (john_details.get("age"))

# Access a dictionary element when it is not present
# print (john_details["address"]) # This will throw key error
print (john_details.get("address")) # This will return None

# Access a dictionary element which is not present and return a default value
print (john_details.get("address","Not Present"))

# Access a dictionary element which is list
john_details_4 = {
    "name":"John",
    "age":23,
    "country":"UK",
    "address":["# 342","City","State"]
}

print (john_details_4["address"][0])

# # try to perform some operations on list 

# Access a dictionary element which is dictionary
john_details_5 = {
    "name":"John",
    "age":23,
    "country":"UK",
    "address":{
        "house_number":"#342",
        "city":"City",
        "state":"State"
    }
}

print (john_details_5["address"]["state"])

# items() - Returns a list containing a tuple for each key value pair
print (john_details.items())
# dict_items([('name', 'John'), ('age', 23), ('country', 'UK')])

# keys() - Returns a list containing the dictionary's keys
print (john_details.keys())
# dict_keys(['name', 'age', 'country'])

# values() - Returns a list of all the values in the dictionary
print (john_details.values())

# pop() - Removes the element with the specified key
print (john_details.pop("name"))
print (john_details)

# popitem() - Removes the last inserted key-value pair
print (john_details.popitem())
print (john_details)

# update() - Updates the dictionary with the specified key-value pairs
john_details["name"] = "John"
john_details["country"] = "UK"
john_details["age"] = 24

print (john_details)
# {'age': 24, 'name': 'John', 'country': 'UK'}

john_details.update({"address":{
        "house_number":"#342",
        "city":"City",
        "state":"State"
    }})

print (john_details)
# {
#     'age': 24, 
#     'name': 'John', 
#     'country': 'UK', 
#     'address': {
#         'house_number': '#342', 
#         'city': 'City', 
#         'state': 'State'
#         }
# }


# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print (john_details.setdefault("contact",2347923874))
print (john_details)
print (john_details.setdefault("contact",25755843))
print (john_details)

# clear() - Removes all the elements from the dictionary
john_details.clear()
print (john_details)
john_details.setdefault("name","John")
john_details["age"] = 25
john_details["country"] = "UK"
john_details.update({
    "address":{
        'house_number': '#342', 
        'city': 'City', 
        'state': 'State'
    },
    "contact":2384792374
})

print (john_details)

john_details_copy = john_details
print (john_details_copy)

print (id(john_details_copy),id(john_details))

john_details_copy_2 = john_details.copy()
print (john_details_copy_2)

print (id(john_details_copy_2), id(john_details))

john_details.update({"temp":"temp"})
print ("ORIGINAL DICTIONARY ",john_details)
print ("COPIED DICTIONARY USING '=' ",john_details_copy)

# ORIGINAL DICTIONARY  {'name': 'John', 'age': 25, 'country': 'UK', 'address': {'house_number': '#342', 'city': 'City', 'state': 'State'}, 'contact': 2384792374, 'temp': 'temp'}

# COPIED DICTIONARY USING '='  {'name': 'John', 'age': 25, 'country': 'UK', 'address': {'house_number': '#342', 'city': 'City', 'state': 'State'}, 'contact': 2384792374, 'temp': 'temp'}

print ("COPIED DICTIONARY USING '.copy' ",john_details_copy_2)
# COPIED DICTIONARY USING '.copy'  {'name': 'John', 'age': 25, 'country': 'UK', 'address': {'house_number': '#342', 'city': 'City', 'state': 'State'}, 'contact': 2384792374}


# Exercise dictionary 

#1. write a function whichh accepts 3 user inputs for following labels and populate
# the collected values in a dictionary
# First name
# Last name
# bank account number 
# balance

# [
#     {
#         "first_name":None,
#         "last_name":None,
#         "account_number":None,
#         "balance":None
#     },
#     {},
#     {}
# ]
print ("\n\n")
def user_info_collection_func(user_number):  # function definition
    """ function to collect user information """
    user_info_collection = []
    for user in range(user_number):
        print ("Collecting user - ",user)
        # actual logic 
        # 1. collect user info
        # 2. put that in a dictionary
        # 3. add that dictionary in a list
        data_dictionary = {}
        data_dictionary["first_name"] = input("Enter your first name : ")
        data_dictionary.update({"last_name":input("Enter your last name ")})
        data_dictionary.setdefault("account_number",input("Enter your account number"))
        data_dictionary["balance"] = input("Enter your balance ")
        print (data_dictionary)
        user_info_collection.append(data_dictionary)
    print ("End of collection\n")
    print ("Here is your User collection",user_info_collection)

user_info_collection_func(2)     # function call 3
# user_info_collection_func(5)   # funcation call 5
# user_info_collection_func(6)    # function call 6

# Here is your User collection 
# [
#     {
#         'first_name': 'John', 
#         'last_name': 'Lenon', 
#         'account_number': '23846', 
#         'balance': '2389'
#     }, 
#     {
#         'first_name': 'Mark', 
#         'last_name': 'Anthony', 
#         'account_number': '237923', 
#         'balance': '23723'
#     }
# ]





