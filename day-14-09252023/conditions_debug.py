# write a control flow program to see if the given list has 'a'
list_variable = [1,2,3,4,5,'a','b']

"Yes, its there"
"No, its not"

# string_variable = 'hello'
# 'h' is in string_variable

# if 'c' in list_variable:
#     print ("Yes, its there") # success block of your condition
# else:
#     print("No, its not")    # failure/else block of your condition 

test_number = 15
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

print ("end of the control flow")