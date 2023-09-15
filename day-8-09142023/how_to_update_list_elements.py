""" How to update list elements with out using methods"""

a = [1,2,3,4]
a[2] = 5
print (a)

a[:2] = 1  # mention about the TypeError

a[:2] = 'word' # since it is an iterable it will work

['a','b','c',[1,2,3,4],[True,5.6]]
#  0   1   2      3          4
a[1:4:1]
# ----------> 1, 4-1

a[4:1:-1]
# <------------4, 1+1

a[3:0:-1]
# <----------- 3, 0+1


# methods


