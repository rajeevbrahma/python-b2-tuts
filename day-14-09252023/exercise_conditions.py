# write a program to check if two variables holding the same value are equal or not ?
a = 10
b = 10

"Yes"
"No"

if a is b:
    print ("Yes")
else:
    print ("No")

if a is not b:
    print ("No")
else:
    print ("Yes")


# write a program to check 
# b / c * d is greater than or equal to e 
# you can give your own numeric values in this example
# (b/c)*d >= e
# brackets, division, multiplication, addition, subtraction

# avinash is Graduate with 85 %
# check if avinash is eligible to write the exam if 
# it has following criteria
# 1. should pass 12th with should have 65% - Company A
# 2. should be a graduate with 90% - Company B
# 3  should be a grduate with 85% - Company C
# 4. either 12th pass with 90% or graduate with 75% - - Company D

b = 2
c = 5
d = 5
e = 5
if (b/c)*d >=e:
    print ("Result - ",(b/c)*d,"and Result greater than ",e)
else:
    print ("Result - ",(b/c)*d,"and Result less than ",e)