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

# Access a dictionary element
john_details["age"]




# # To create a dictionary with the following keys default value as None
# example_dictionary_3 = dict.fromkeys(("name","age","country"))
# print (example_dictionary_3)


# print (example_dictionary.get("name"))
# print (example_dictionary.get("age"))
# print (example_dictionary.get("country"))

# print (example_dictionary.items())

# print (example_dictionary.keys())

# print (example_dictionary.values())

# print (example_dictionary.pop("name"))
# print (example_dictionary)

# print (example_dictionary.popitem())
# print (example_dictionary)

# example_dictionary.update({"name":"John"})
# print (example_dictionary)

# example_dictionary.update({"name":"John","age":23})
# print (example_dictionary)

# example_dictionary.update({"name":"John","age":23,"country":"UK"})
# print (example_dictionary)

# example_dictionary.setdefault("name","John")
# print (example_dictionary)

# example_dictionary.clear()

# print (example_dictionary)

# example_dictionary = {
#     "name":"John",
#     "age":23,
#     "country":"UK"
# }

# example_dictionary_2 = example_dictionary.copy()
# print (example_dictionary_2)

# example_dictionary_2.clear()
# print (example_dictionary_2)

# example_dictionary_2 = example_dictionary
# print (example_dictionary_2)


