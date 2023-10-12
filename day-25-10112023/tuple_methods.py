""" Tuple methods """

# what is a tuple?
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.


# Tuple methods
# count() - Returns the number of times a specified value occurs in a tuple
# index() - Searches the tuple for a specified value and returns the position of where it was found

# Tuple intialization
#1. Using paranthesis
example_tuple = ("John",23,"UK","John","John")

#2. Using tuple() constructor
example_tuple_2 = tuple(("John",23,"UK"))

print (example_tuple)
print (example_tuple_2)

# Accessing tuple elements
print (example_tuple[0])
print (example_tuple[1])

print (example_tuple.count("John"))
print (example_tuple.index("UK"))

