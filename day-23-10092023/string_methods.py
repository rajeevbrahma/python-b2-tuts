""" String Methods """

EXAMPLE_SENTENCE_1 = "Python is very easy to learn"
EXAMPLE_SENTENCE_2 = " But you have to practice every day "
FULL_CAPITAL_SENTENCE = "PYTHON IS VERY EASY TO LEARN"
SMALL_CAPITAL_SENTENCE = "python is very easy to learn"
MIXED_CASE_SENTENCE = "PyThOn Is VeRy EaSy To LeArN"
NUMERIC_STRING = "1234567890"
print(EXAMPLE_SENTENCE_1.capitalize()) # turns the first letter of first word into upper case
print(SMALL_CAPITAL_SENTENCE.upper()) # turns all the letters into upper case
print(FULL_CAPITAL_SENTENCE.lower()) # turns all the letters into lower case
print(EXAMPLE_SENTENCE_1.title()) # turns the first letter of every word into upper case
# turns the first letter of every word into upper case and vice versa
print(MIXED_CASE_SENTENCE.swapcase())
print(EXAMPLE_SENTENCE_1.casefold()) # turns all the letters into lower case

print(EXAMPLE_SENTENCE_1.center(31)) # adds given number of spaces before the center of the string
print(EXAMPLE_SENTENCE_1.center(29,"*")) # adds given character before the center of the string
print(EXAMPLE_SENTENCE_1.ljust(35)) # adds given number of spaces at the left of the string
print(EXAMPLE_SENTENCE_1.ljust(35,"*")) # adds given character at the left of the string
print(EXAMPLE_SENTENCE_1.rjust(29)) # adds given number of spaces at the right of the string
print(EXAMPLE_SENTENCE_1.rjust(29,"*")) # adds given character at the right of the string
print(NUMERIC_STRING.zfill(29)) # adds given number of zeros at the left of the string
print(EXAMPLE_SENTENCE_1.replace("easy","super easy")) # replaces the given word with the given word
EXAMPLE_SENTENCE_3 = "Python is easy to learn and easy to code"
print(EXAMPLE_SENTENCE_3.replace("easy","super easy",1)) # replaces the given word with the given word
print(EXAMPLE_SENTENCE_3.replace("easy","super easy",2)) # replaces the given word with the given word

print (EXAMPLE_SENTENCE_1.count("i"))           # Returns the count of a char in a string
print(EXAMPLE_SENTENCE_1.startswith("P")) # returns True if the string starts with the given character
print(EXAMPLE_SENTENCE_1.endswith("n")) # returns True if the string ends with the given character
print(EXAMPLE_SENTENCE_1.isalnum()) # returns True if the string is alphanumeric
print(EXAMPLE_SENTENCE_1.isalpha()) # returns True if the string is alphabetic
print(EXAMPLE_SENTENCE_1.isdecimal()) # returns True if the string is decimal
print(NUMERIC_STRING.isdecimal()) # returns True if the string is decimal
print(EXAMPLE_SENTENCE_1.isdigit()) # returns True if the string is digit
print(NUMERIC_STRING.isdigit()) # returns True if the string is digit

print(EXAMPLE_SENTENCE_1.islower()) # returns True if the string is lower case

print (EXAMPLE_SENTENCE_1.find("t"))  # Returns the index of a char in the string
print (EXAMPLE_SENTENCE_1.index("t")) # Returns the index of a char in the string
print (EXAMPLE_SENTENCE_2.strip())   # Removes white space at begining or ending of a string 
print(" ".join(EXAMPLE_SENTENCE_1))  # joins every character with the given character (space in this example)

print (EXAMPLE_SENTENCE_1.split())   # splits the string into a list of words

#IDENTIFIER IS NOTHING BUT THE NAME OF A VARIABLE, FUNCTION, CLASS, MODULE, PACKAGE, ETC.
#IDENTIFIER RULES:
#1. IDENTIFIER CAN NOT START WITH A NUMBER
#2. IDENTIFIER CAN NOT CONTAIN SPECIAL CHARACTERS EXCEPT UNDERSCORE (_)
#3. IDENTIFIER CAN NOT BE A KEYWORD
#4. IDENTIFIER CAN NOT CONTAIN SPACE
#5. IDENTIFIER CAN NOT CONTAIN ANY SPECIAL CHARACTERS EXCEPT UNDERSCORE (_)

# isidentifier() method returns True if the string follows the above rules
# example of valid identifiers:
# variable_1
# _variable_1
# variable1

# example of invalid identifiers:
# 1variable
# variable 1
# variable-1
# variable@1

# isidentifier will check if the given string is a valid identifier or not

identifier_1 = "variable_1"
identifier_2 = "_variable_1"
identifier_3 = "variable1"
identifier_4 = "1variable"
identifier_5 = "variable 1"
identifier_6 = "variable-1"
print(identifier_1.isidentifier()) # returns True if the string is identifier
print (identifier_2.isidentifier()) # returns True if the string is identifier
print (identifier_3.isidentifier()) # returns True if the string is identifier
print (identifier_4.isidentifier()) # returns True if the string is identifier
print (identifier_5.isidentifier()) # returns True if the string is identifier
print (identifier_6.isidentifier()) # returns True if the string is identifier

# check 
given_string = " John is a software Engineer "
# get me the count of n in the above string
count_of_letter_n = given_string.count("n")
# print (count_of_letter_n)


print (given_string.replace("software", "Mechanical"))
print (given_string)
print(given_string.startswith(" "))
zero_filled_string = "1231".zfill(7)
print (zero_filled_string) 
print("abcd1234".isalnum())  # True
print("@#$^&".isalnum())  # False
print("abcd1234@#$".isalnum())  # True

