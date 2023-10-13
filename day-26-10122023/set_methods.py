""" set methods """

# what is a set?
# set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

# Set intialization
#1. Using curly braces
example_set = {"John",23,"UK"}

#2. Using set() constructor
example_set_2 = set(("John",23,"UK"))

print (example_set)
print (example_set_2)

# Set methods
# add() - Adds an element to the set
example_set.add("New Element") # adding string element
print (example_set)
example_set.add(1) # adding integer element
print (example_set)
example_set.add((1,2,3)) # adding tuple element
print (example_set)

# clear() - Removes all the elements from the set
example_set.clear()
print (example_set)

# copy() - Returns a copy of the set
example_set_3 = example_set_2.copy()
print (example_set_3)

# copy using assignment operator (=)
example_set_4 = example_set_2


# difference() - Returns a set containing the difference between two or more sets
example_set_4 = {"John",23,"UK"}
example_set_5 = {"John",23,"UK","New Element"}

example_set_6 = example_set_5.difference(example_set_4)
example_set_difference_swap = example_set_4.difference(example_set_5)

print (example_set_6)
print (example_set_difference_swap)

# room- 1 [1,2,3,4] - {4}
# room- 2 [1,2,3] - empty set

# discard() - Remove the specified item
example_set_9 = {"John",23,"UK"}
example_set_9.discard("John")
print (example_set_9)

# remove() - Removes the specified element
example_set_23 = {"John",23,"UK"}
example_set_23.remove("John")
print (example_set_23)

# pop() - Removes an element from the set
example_set_22 = {'a23','asdf','dummy',"John",23,"UK","New Element"}
example_set_22.pop()
print (example_set_22)

# intersection() - Returns a set, that is the intersection of two other sets
example_set_10 = {"John",23,"UK"}
example_set_11 = {"John",23,"UK",12.2}
example_set_12 = example_set_10.intersection(example_set_11)
print (example_set_12)

# union() - Return a set containing the union of sets
example_set_29 = {"John",23,"UK"}
example_set_30 = {"John",23,"UK","New Element"}
example_set_31 = example_set_29.union(example_set_30)
print (example_set_31)


# # update() - Update the set with the union of this set and others
example_set_32 = {"John",23,"UK"}
example_set_33 = {"New Element",12.2,(1,2,3)} # str, float, tuple
example_set_32.update(example_set_33)
print (example_set_32)


# Please go through the following methods after the class

# difference_update() - Removes the items in this set that are also included in another, specified set
example_set_7 = {"John",23,"UK"}
example_set_8 = {"John",23,"UK","New Element"}
example_set_7.difference_update(example_set_8)
print (example_set_7)


# intersection_update() - Removes the items in this set that are not present in other, specified set(s)
example_set_13 = {"John",23,"UK"}
example_set_14 = {"John",23,"UK","New Element"}
example_set_13.intersection_update(example_set_14)
print (example_set_13)

# isdisjoint() - Returns whether two sets have a intersection or not
example_set_15 = {"John",23,"UK"}
example_set_16 = {"John",23,"UK","New Element"}
print (example_set_15.isdisjoint(example_set_16))

# issubset() - Returns whether another set contains this set or not
example_set_18 = {"John",23,"UK"}
example_set_19 = {"John",23,"UK","New Element"}
print (example_set_18.issubset(example_set_19))

# issuperset() - Returns whether this set contains another set or not
example_set_20 = {"John",23,"UK"}
example_set_21 = {"John",23,"UK","New Element"}
print (example_set_20.issuperset(example_set_21))


# symmetric_difference() - Returns a set with the symmetric differences of two sets
example_set_24 = {"John",23,"UK"}
example_set_25 = {"John",23,"UK","New Element"}
example_set_26 = example_set_24.symmetric_difference(example_set_25)

# symmetric_difference_update() - inserts the symmetric differences from this set and another
example_set_27 = {"John",23,"UK"}
example_set_28 = {"John",23,"UK","New Element"}
example_set_27.symmetric_difference_update(example_set_28)
print (example_set_27)

















