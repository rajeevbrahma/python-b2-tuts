"""
    Valid way of defining variables

"""

# variables also called as identifiers


"""
    We can’t use special symbols like !,#,@,%,$ etc in our Identifier.
    Identifier can be of any length.

"""


numberofbanks = 2                   # writing two words as single name as variable name
bank_name = "X Associates"          # using underscore to connect to words as variable name

_card_cvv_number = 1238             # we can underscore before variable name and is suggested
                                    # for private variables only    
nameOnTheCard = "Father of xYz"     # this is camel case way of defining variables and suggested 
                                    # function names of class names
HOMEADDRESS = "xstreet"             # suggested for constant names
account1 = 182938492734             # can use numbers at the end of a word as a variable name

amount_1 = amount_2 = 12.3                 # same value to multiple variables

account_1_name,account_2_name = "x","y"    # multiple values to multiple variables
atm_pin_1 = 1234
atm_pin_2 = 2345

"""
    Invalid way of defining variables

"""


1account = "x"                 # cannot use number at the begining of word for a variable name
bank-name = "X Associates"     # cannot use "-" to connect two words as this will be considered
                               # value being associated to an arithmetic expression which is not allowed  
bank name = "X Associates"     # space cannot be used for variable names

# never use keyword as a variable name