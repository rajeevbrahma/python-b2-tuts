random_string = "aiuysdoifpasodifuaoisdufoisudofgksjdfhasjd"

"""
"aieiaiaiaiai"
['a','i','e']
"""
"""
1. you have to define a unique character list

iterate through the string 
    in every iteration you have to check if the letter existed in the unique character list
    if not add the character to the unique character list

    for loop
    if control flow

    in operator
"""
# initialise an empty result list
unique_character_list = ['a']

# iterate through the random string
for character in random_string:
    if character not in unique_character_list:
        unique_character_list += [character]
print (unique_character_list)

# iterate through the random string
for character in random_string:
    if character in unique_character_list:
        pass
    else:
        unique_character_list += [character]
print (unique_character_list)



# 2. Instead of list store the above unique characters as a string 
# "aiuysdofpgkjh"

unique_character_list = ""
# iterate through the random string
for character in random_string:
    if character in unique_character_list:
        pass
    else:
        unique_character_list += character
print (unique_character_list)


# 3. Make a seperate list for vowels and consonants used in the above random string
# vowels in the above random string      - []
# consonants in the above random string  - []

vowel_unique_character_list = []
consonant_unique_character_list = []
# random_string = "aiuysdoifpasodifuaoisdufoisudofgksjdfhasjd"
vowels = "aeiou"
for character in random_string:
        if character in vowels and character not in vowel_unique_character_list:
            vowel_unique_character_list += [character]
        elif (character not in vowels and character not in consonant_unique_character_list):
            consonant_unique_character_list += [character]

print ("vowels in the above random string  - ",vowel_unique_character_list)
print ("consonants in the above random string -  ",consonant_unique_character_list)


# Kirans approach
vowel_unique_character_list = []
consonant_unique_character_list = []

vowels = "aeiou"
for character in random_string:
        if character in vowels:
            if character not in vowel_unique_character_list:
                vowel_unique_character_list += [character]
        else:
            if (character not in consonant_unique_character_list):
                consonant_unique_character_list += [character]

print ("vowels in the above random string  - ",vowel_unique_character_list)
print ("consonants in the above random string -  ",consonant_unique_character_list)

# 4. Generate the number dictionary till 100

number_dictionary = {}
for number in range(1,10):
    number_dictionary[number] = str(number)

print (number_dictionary)

# 5. multiply each number with 10 and store as a value
# {1:10,2:20,3:30.....}

# 6. {0:[0,1,2,3,4,5,6,7,8,9],1:[10,11,12,13,14,15....19],2:[20]...}

dictionary_number_range = 5
number_dictionary_problem_6 = {}

for outer_loop_number in range (dictionary_number_range):
    number_dictionary_problem_6[outer_loop_number] = []

    for inner_loop_number in range(10):
        number_dictionary_problem_6[outer_loop_number] +=[inner_loop_number+(outer_loop_number*10)]

print (number_dictionary_problem_6)

# Sunil code
# number_dictionary = {}
# for number in range(5):
#     number_dictionary[number]=[]
# print (number_dictionary)

for number in range(5):
    number_dictionary[number]=[]
    number_dictionary[number] += range(number*10,number*10+10)
print (number_dictionary)

# Kiran  code 
number_dict = {}
for num in range(5):
    dict_value = []
    for i in range (10):
        # dv = num*10+i
        dict_value += [i+(num*10)]
        number_dict[num] = dict_value

print (number_dict)
