# iterative statements
# definite loops - limited with some range 
# indefinite loops 

# while 0:
#     print ("Hello")

# name_variable = "PYTHON"
# # print (name_variable)
# # for character in name_variable:
# #     print (character)

# number_variable = "0123456789"
# for number in number_variable:
#     print ("iteration - ",number)

alphabet_variable = "abcdefghijklmn"
# for character in alphabet_variable:
#     print (character)

# print (character)

# list_variable = [1,2,3,4,5,6,7]
# for element in list_variable:
#     print (element)

list_variable_2 = ['a',1,1.2,[1,2,3,4,5],{1:'a',2:'b'}]
for element in list_variable_2:
    print (element)

list_variable_3 = ['Hello','world']
for list_element in list_variable_3:
    print (list_element)
    for character in list_element:
        print (character)

print ("Hello world") # for five times

# startpoint, endpoint, stepvalue
range(0,10,1)

# shout hello world for five times

for i in range(0,5):
    print (i,"Sale ended at 10000$")

a = [1,2,3,4,5,6,7]
for i in range(0,len(a)):
    print ("List element at index ",i,"is",a[i])

for j in range(-1,-8,-2):
    print ("List element at index ",j,"is",a[j])


# ----> (+)
#   -4  -3  -2  -1 0 1 2
# < ------ (-)