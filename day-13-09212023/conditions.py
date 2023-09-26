"""
    if <conditional_statement>:
        success block
    else:
        failure block
"""

test_variable = ['eat','cat','mat','bat']
vowel_1C = 'A'
vowel_2C = 'E'
vowel_3C = 'I'
vowel_4C = 'O'
vowel_5C = 'U'

vowel_1S = 'a'
vowel_2S = 'e'
vowel_3S = 'i'
vowel_4S = 'o'
vowel_5S = 'u'

word_index = 3
letter_index=0

# 1. TO CHECK THE GIVEN STRING VARIABLE FIRST LETTER 
# IS EITHER EQUAL TO ANY OF THE VOWELS ?
# if (test_variable[word_index][letter_index] == vowel_1C or 
#     test_variable[word_index][letter_index] == vowel_2C or 
#     test_variable[word_index][letter_index] == vowel_3C or 
#     test_variable[word_index][letter_index] == vowel_4C or
#     test_variable[word_index][letter_index] == vowel_5C or
#     test_variable[word_index][letter_index] == vowel_1S or 
#     test_variable[word_index][letter_index] == vowel_2S or 
#     test_variable[word_index][letter_index] == vowel_3S or 
#     test_variable[word_index][letter_index] == vowel_4S or
#     test_variable[word_index][letter_index] == vowel_5S 
#     ):
#     print ("Yes, word starts with a vowel")
# else:
#     print ("No it doesnt")

vowels_C = 'AEIOU'
vowels_S = 'aeiou'

test_variable = 'EAT'

if (test_variable[0] not in vowels_C and 
    test_variable[0] not in vowels_S 
):
     print ("Yes Word starts with consonant")
else:
    print ("No it starts with vowel")

"""
    Success - Yes Word starts with consonant
    Failure - No it starts with vowel

"""

if (test_variable[0] in vowels_C):
    print ("Word starts with Capital vowel")
elif(test_variable[0] in vowels_S):
    print ("Word starts with small case vowel")
else:
    print ("No it doesnt")

# a = 40
# 10 to 20 range 
# 20 to 30 range 

test_number = 20
if (test_number >=10 and test_number<=20):
    print ('In 10 to 20 range')
elif (test_number >20 and test_number<=30):
    print ('In 20 to 30 range')
elif (test_number >30 and test_number<=40):
    print ('In 30 to 40 range')
elif (test_number >40 and test_number<=50):
    print ('In 40 to 50 range')
else:
    print ("Number out of range")