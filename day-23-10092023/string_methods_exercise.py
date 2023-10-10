# Write a function to accept input from the user (from command line) and do the following:
# data to be taken from the user
    # First Name
    # Last Name
    # Age
    # Occupation

# 1. Print all the inputs from the user
# 2. Print the type of the each input
# 3. Give me individual length and total length of the first name and last name
# 4. Print the input in upper case of first name and last name
# 5. Print the input in lower case of first name and last name
# 7. Print the input in capitalized case of first name and last name 
# 9. Print the input in strip case
# 10.Use join to add the first name and last name with a space in between and store in a variable called full_name
# 11. Print the input in split case
# 12. Check if age is digit/ decimal or not
# 13 find the index of the letter of your choice in the first name


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
occupation = input("Enter your occupation: ")

print("First Name: ", first_name)
print("Last Name: ", last_name)
print("Age: ", age)
print("Occupation: ", occupation)

print("Type of First Name: ", type(first_name))
print("Type of Last Name: ", type(last_name))
print("Type of Age: ", type(age))
print("Type of Occupation: ", type(occupation))

print("Length of First Name: ", len(first_name))
print("Length of Last Name: ", len(last_name))
print("Total Length of First Name and Last Name: ", len(first_name) + len(last_name))

print("Upper Case of First Name: ", first_name.upper())
print("Upper Case of Last Name: ", last_name.upper())

print("Lower Case of First Name: ", first_name.lower())
print("Lower Case of Last Name: ", last_name.lower())

print("Capitalized Case of First Name: ", first_name.capitalize())
print("Capitalized Case of Last Name: ", last_name.capitalize())

print("Strip Case of First Name: ", first_name.strip())
print("Strip Case of Last Name: ", last_name.strip())

full_name = " ".join([first_name, last_name])
print("Full Name: ", full_name)

print("Split Case of Full Name: ", full_name.split())

