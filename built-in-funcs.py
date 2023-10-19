""" Built in functions list """
print() # Displays in the standard output console
id()   # Return the memory location of the literal / variable given
type() # Return the data type of the literal / variable given
bin()  # Return the binary representation of an integer.
range() # Return a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
input() # which allows you to take inputs in runtime from the terminal
len() # would give me the length of string, list
ord( ) # returns the ascii number of an alphabet or symbol
sum( ) # returns the sum of numeric list elements
help( ) # helps you with the documentation of anything in python
open() # helps you open the files
# Examples

print (ord("a"))
print (ord("A"))
print (ord(" "))

print (sum([1,2,3,4,5,6,7,8,9,10]))
print (sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

print (help("keywords"))
print (help("for"))

print (range(10))
print (range(1,10))
print (range(1,10,2))

print (bin(10))
print (bin(100))

print (type(10))
print (type(10.0))
print (type("Python"))
print (type([1,2,3,4,5,6,7,8,9,10]))
print (type((1,2,3,4,5,6,7,8,9,10)))
print (type({1,2,3,4,5,6,7,8,9,10}))
print (type({"name":"John","age":23,"country":"UK"}))


print (id(10))
print (id(10.0))

print (len("Python"))
print (len([1,2,3,4,5,6,7,8,9,10]))

print (input("Enter your name: "))
print (input("Enter your age: "))


