""" List Methods """
example_list = ["Python", "is", "very", "easy", "to", "learn"]
example_list_2 = ["But", "you", "have", "to", "practice", "every", "day"]

# example_list += ["and"]

# example_list.append(1)
# example_list.append("and")
print (example_list)
# example_list.append(["this","is","a","sub list"])
print (example_list[-1][0])
print (example_list[2])
print (example_list[0])
print (example_list[1])


# example_list += example_list_2
example_list.extend(example_list_2)

print (example_list)


list_with_repetitive_elements = ['a','b','a','a','c','b',"PYTHON",[1,2,1,2,3,4,5],[3,4],[1,2]]

print (list_with_repetitive_elements.index("a"))
print (list_with_repetitive_elements.index("a",1))
print (list_with_repetitive_elements.index("a",3))
# here 1 is the start index from where you want to start looking for the given list element
# here 2 is the end index till where you want to look for the given list element

print ("Count method ",list_with_repetitive_elements.count([3,4]))

print ("Count method result - ",list_with_repetitive_elements[7].count(2))

print ("lower method result - ",list_with_repetitive_elements[-4].lower())


print ("before insert  - ",list_with_repetitive_elements[0])
list_with_repetitive_elements.insert(0,1)
print ("insert method result - ",list_with_repetitive_elements)
print ("after insert  - ",list_with_repetitive_elements[0])

print ("length of the list",len(list_with_repetitive_elements))

print ("before insert  - ",list_with_repetitive_elements[10:])
list_with_repetitive_elements.insert(13,"Check")
print ("insert method result - ",list_with_repetitive_elements)
print ("after insert  - ",list_with_repetitive_elements[10:])

# using insert you can add an element at a desired index position
#scenario -
# if we are trying to access an index position which is greater than the length of the list
# by default it considers it as the next index position number of that list

list_with_repetitive_elements.remove('Check')
print ("Remove method ",list_with_repetitive_elements)

list_with_repetitive_elements.remove(1)
print ("Remove method ",list_with_repetitive_elements)

list_with_repetitive_elements.pop() # by default your index here is -1
print ("Pop method with default index ",list_with_repetitive_elements)

list_with_repetitive_elements.pop(1)
print ("Pop method with index ",list_with_repetitive_elements)

number_list = [1,2,3,42,3,4,5,6,78]
print ("Before sorting ",number_list)
number_list.sort()
print ("Sorted list",number_list)

number_list = [1,2,3,42,3,4,5,6,78]
number_list.sort(reverse=True)
print ("Sorted list descending order",number_list)

number_list.clear()
print (number_list)




number_list = [1,2,3,42,3,4,5,6,78]

number_list_2 = number_list
print ("Copying contents of list ",number_list_2)

number_list_2.append(45)
print (number_list_2)
print (number_list)

# [1, 2, 3, 42, 3, 4, 5, 6, 78, 45]
# [1, 2, 3, 42, 3, 4, 5, 6, 78, 45]

number_list_3 = number_list.copy()
print ("Copying contents of list using copy method",number_list_3)

number_list_3.append(46)
print (number_list_3)
print (number_list)

# [1, 2, 3, 42, 3, 4, 5, 6, 78, 45, 46]
# [1, 2, 3, 42, 3, 4, 5, 6, 78, 45]



# print (id(number_list),id(number_list_2),id(number_list_3))



# print (example_list[0:3])
# print (example_list[0:3:2])

# print (example_list + example_list_2)

# print (example_list * 3)

# print (len(example_list))

# print (example_list.index("very"))
# print (example_list.count("very"))

# example_list.append("and")
# print (example_list)

# example_list.insert(3,"super")
# print (example_list)

# example_list.remove("super")
# print (example_list)

# example_list.pop()
# print (example_list)

# example_list.pop(3)
# print (example_list)

# example_list.reverse()
# print (example_list)

# example_list.sort()
# print (example_list)

# example_list.sort(reverse=True)
# print (example_list)

# example_list.clear()
# print (example_list)

# example_list = ["Python", "is", "very", "easy", "to", "learn"]
# example_list_2 = ["But", "you", "have", "to", "practice", "every", "day"]

# example_list.extend(example_list_2)
# print (example_list)

# example_list_3 = example_list.copy()
# print (example_list_3)

# example_list_3.clear()
# print (example_list_3)

# example_list_3 = example_list
# print (example_list_3)

# example_list_3.clear()
# print (example_list_3)


# excercise on list methods
# 1. Create a list of 5 elements
# 2. Add 2 more elements to the list
# 3. Remove the last element from the list
# 4. Remove the first element from the list
# 5. Remove element with index 3
# 6. Remove the element with value "Python"
# 7. Print the length of the list
# 8. Print the index of the element with value "Python"
# 9. Print the count of the element with value "Python"
# 10. Print the list in reverse order
# 11. Sort the list
# 12. Sort the list in reverse order
# 13. Clear the list
# 14. Copy the list to another list
# 15. Clear the copied list
# 16. Copy the list to another list using "="
# 17. Clear the copied list
# 18. Extend the list with another list
# 19. Print the list
# 20. Print the copied list
# 21. Print the list using a for loop
# 22. Print the list using a while loop
# 23. Print the list using list comprehension

# #1. Create a list of 5 elements
# list1 = [1,2,3,4,5]
# print (list1)

# #2. Add 2 more elements to the list
# list1.append(6)
# list1.append(7)
# print (list1)

# #3. Remove the last element from the list
# list1.pop()
# print (list1)

# #4. Remove the first element from the list
# list1.pop(0)
# print (list1)

# #5. Remove element with index 3
# list1.pop(3)
# print (list1)

# #6. Remove the element with value "Python"
# list1.remove("Python")
# print (list1)

# #7. Print the length of the list
# print (len(list1))

# #8. Print the index of the element with value "Python"
# print (list1.index("Python"))

# #9. Print the count of the element with value "Python"
# print (list1.count("Python"))

# #10. Print the list in reverse order
# list1.reverse()
# print (list1)

# #11. Sort the list
# list1.sort()
# print (list1)

# #12. Sort the list in reverse order
# list1.sort(reverse=True)
# print (list1)

# #13. Clear the list
# list1.clear()

# #14. Copy the list to another list
# list2 = list1.copy()

# #15. Clear the copied list
# list2.clear()

# #16. Copy the list to another list using "="
# list2 = list1

# #17. Clear the copied list
# list2.clear()

# #18. Extend the list with another list
# list1.extend(list2)

# #19. Print the list
# print (list1)

# #20. Print the copied list
# print (list2)

# #21. Print the list using a for loop
# for i in list1:
#     print (i)

# #22. Print the list using a while loop
# i = 0
# while i < len(list1):
#     print (list1[i])
#     i += 1

# #23. Print the list using list comprehension
# print ([i for i in list1])




