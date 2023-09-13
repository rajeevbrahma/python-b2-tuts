"""
    Python Memory - HEAP space 
"""


a = 1000
a = "hello"
b = 1000

"""
    Memory block 
       [190] <------ 
      1234567

     Memory block 
       [190] <------ 
      1234567

    Memory block 
       [190] <------ 
      1234567

    1234567     0       190   int
    object - refcount, value, type

    Memory block 
       [1900] <------ a
      2342323

     Memory block 
       [1900] <------ b
      2342323
    
      Memory block 
       [1900] <------ c
      2342323

    2342323     3       1900   int
    object - refcount, value, type

    garbage collector - is to check the refcount of each memory block and free the memory space

"""

# id() - built-in - gives the memory block number

"""
Theory - 

variables associated to numbers ranging from -5 to 256 will
refer to the same memory block 

but numbers >256, new memory block will get created even if we 
have the same value 

Example :
>>> a = 256
>>> b = 256
>>> id(a)
4336976104
>>> id(b)
4336976104
>>> a = -4
>>> b = -4
>>> id(a)
4336967784
>>> id(b)
4336967784
>>> b = -6
>>> a = -6
>>> id(a)
4339433584
>>> id(b)
4338991056
>>> a = 257
>>> b = 257
>>> id(a)
4339433648
>>> id(b)
4339433584


where as, you can still refer to the same memory block
if we initialize as follows

>>> a = b = 257
>>> id(a)
4338991056
>>> id(b)
4338991056

When it comes to string type literals, 
if it is declared as single word without any spaces
you can still refer to the same memory block

but if you have any space in the literal string value
then you will have different memory blocks.

>>> b = 'py'
>>> a = 'py'
>>> id(a)
4338478128
>>> id(b)
4338478128
>>> a = 'p y'
>>> b = 'p y'
>>> id(a)
4339397808
>>> id(b)
4339397744

"""





