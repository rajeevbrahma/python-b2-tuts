""" Exercise to add user details to a dictionary """

# Write a function which takes integer as input then create a dictionary with keys as numbers from 1 to n and values as square of the keys

def create_dictionary(n):
    dictionary = {}
    for i in range(1,n+1):
        dictionary[i] = i**2
    return dictionary

print(create_dictionary(5))

def create_dictionary_2(n):
    dictionary = {}
    for i in range(1,n+1):
        dictionary.update({i:i**2})
    return dictionary

print(create_dictionary_2(5))

def create_dictionary_3(n):
    dictionary = {}
    for i in range(1,n+1):
        dictionary.setdefault(i,i**2)
    return dictionary

print(create_dictionary_3(5))

