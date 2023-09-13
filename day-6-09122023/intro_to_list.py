"""
Lists are ordered.
Lists can contain any arbitrary objects.
List elements can be accessed by index.
Lists can be nested to arbitrary depth.
Lists are mutable / modified 
    you can use list methods to modify your list
    you can use operators (+) to modify your list
Lists are dynamic.

"""




fridge = []

eggs_tray = ['egg 1',"egg 2"]
veg_tray = [2.250,10.34]
Dairy_tray = None
Beverages_tray = [['pepsi',2],['coke',3]]
Fruits_tray = ['apple','banana']

# anand = ['X', 123.1, True, 1234]


bank_info = [
                [                              # Anand
                    ['X', 123.1, True, 1234], # Credit info
                    ['Z', 324.2, False, 8923] # Debit info
                ], 
                ['Y', 234.2, False, 4984]     # Kiran Debit info
            ]

[[['X', 123.1, True, 1234],['Z', 324.2, False, 8923]],['Y', 234.2, False, 4984]]
#   |    |       |     |     |     |      |     |       |     |      |      |
#   0    1       2     3     0     1      2     3       0     1      2      3  - Anands & Kirans individual elements in the list
#           |                          |
#           0                          1                                       - 0  - Anands Credit and Debit info, 
#                       |                                       |
#                       0                                       1              - bank_info -  0 - Anand & 1 - Kiran info            



details = []

# details[0][0] = ['Name',23]
# details[1] = ['Name 2',24]
details = [['Name',23],['Name 2',24]]
#             |     |      |      |
#             0     1      0      1
        #       |             |
#               0             1

details[0][1][2] = 'M'
details[0][1][3] = 56

details = [[None,[None,None,'M',56]]]
#                   |   |    |  |
#                   0   1    2  3       - positive indexing
#                  -4  -3   -2 -1
#                   
#           |           |
#           0           1    
#           -2          -1              - negative indexing
#                  |
#                  0

# iterable things in python
# slicing
